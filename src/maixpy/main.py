# MaixPy/K210 unified entry point for project deployment.
# Copy this file, the driver modules, and the selected .kmodel to the TF card.
import gc
import sys
import time

import image
import KPU as kpu
import lcd
import sensor
from machine import I2C

from servo import Servos


INPUT_SIZE = (224, 224)
MODEL_ADDR = "/sd/model-11975.kmodel"

# The checked-in model-11975.kmodel matches models/training-report.json.
MODEL_LABELS = ["5", "6", "7", "8", "1", "2", "3", "4"]
MODEL_ANCHORS = [1.88, 2.38, 1.31, 2.11, 1.69, 2.19, 1.59, 1.94, 1.53, 1.66]

# Template for the trash model used by the final project script. Use this only
# when the matching bottle/bag .kmodel is available on the TF card.
TRASH_LABELS = ["bottle", "bag"]
TRASH_ANCHORS = [5.0, 5.0, 5.87, 4.69, 6.2, 5.66, 5.5, 5.44, 5.83, 6.53]

YOLO_THRESHOLD = 0.5
YOLO_NMS = 0.3
YOLO_ANCHOR_NUM = 5

SERVO_ENABLED = True
SERVO_I2C_ID = I2C.I2C0
SERVO_SCL_PIN = 7
SERVO_SDA_PIN = 6
SERVO_CHANNELS = (0, 1, 2)
SERVO_IDLE_ANGLE = 90
SERVO_ACTIVE_ANGLE = 180
RESET_AFTER_MISSING_FRAMES = 200


def lcd_show_exception(err):
    import uio
    err_str = uio.StringIO()
    sys.print_exception(err, err_str)
    img = image.Image(size=INPUT_SIZE)
    img.draw_string(0, 10, err_str.getvalue(), scale=1, color=(255, 0, 0))
    lcd.display(img)


def show_loading():
    try:
        img = image.Image("startup.jpg")
    except Exception:
        img = image.Image(size=(320, 240))
        img.draw_string(80, 110, "loading model...", color=(255, 255, 255), scale=2)
    lcd.display(img)


def init_camera(sensor_window=INPUT_SIZE, lcd_rotation=0, hmirror=False, vflip=False):
    sensor.reset()
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    sensor.set_windowing(sensor_window)
    sensor.set_hmirror(hmirror)
    sensor.set_vflip(vflip)
    sensor.run(1)

    lcd.init(type=1)
    lcd.rotation(lcd_rotation)
    lcd.clear(lcd.WHITE)


def init_servos():
    if not SERVO_ENABLED:
        return None

    try:
        i2c = I2C(SERVO_I2C_ID, mode=I2C.MODE_MASTER, scl=SERVO_SCL_PIN, sda=SERVO_SDA_PIN)
        servos = Servos(i2c)
        set_servo_angle(servos, SERVO_IDLE_ANGLE)
        return servos
    except Exception as err:
        print("servo init failed, detection-only mode")
        sys.print_exception(err)
        return None


def set_servo_angle(servos, angle):
    if servos is None:
        return

    for channel in SERVO_CHANNELS:
        servos.position(channel, angle)


def label_name(labels, class_id):
    if 0 <= class_id < len(labels):
        return labels[class_id]
    return "class_%d" % class_id


def draw_detections(img, objects, labels):
    for obj in objects:
        pos = obj.rect()
        name = label_name(labels, obj.classid())
        img.draw_rectangle(pos)
        img.draw_string(pos[0], pos[1], "%s : %.2f" % (name, obj.value()),
                        scale=2, color=(255, 0, 0))


def run(model_addr=MODEL_ADDR, labels=MODEL_LABELS, anchors=MODEL_ANCHORS):
    init_camera()
    show_loading()

    servos = init_servos()
    task = None
    missing_frames = 0

    try:
        task = kpu.load(model_addr)
        kpu.init_yolo2(task, YOLO_THRESHOLD, YOLO_NMS, YOLO_ANCHOR_NUM, anchors)

        while True:
            img = sensor.snapshot()
            start = time.ticks_ms()
            objects = kpu.run_yolo2(task, img)
            elapsed = time.ticks_ms() - start

            if objects:
                missing_frames = 0
                draw_detections(img, objects, labels)
                set_servo_angle(servos, SERVO_ACTIVE_ANGLE)
            else:
                missing_frames += 1
                if missing_frames >= RESET_AFTER_MISSING_FRAMES:
                    set_servo_angle(servos, SERVO_IDLE_ANGLE)
                    missing_frames = 0

            img.draw_string(0, 200, "t:%dms" % elapsed, scale=2, color=(255, 0, 0))
            lcd.display(img)
    finally:
        if task is not None:
            kpu.deinit(task)


if __name__ == "__main__":
    try:
        run()
    except Exception as err:
        sys.print_exception(err)
        lcd_show_exception(err)
    finally:
        gc.collect()
