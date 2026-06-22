
def Servo(servo,angle):
    servo.duty((angle+90)/180*10+2.5)
import sensor, image, lcd, time
import KPU as kpu
import gc, sys
from machine import I2C
from servo import Servos
from stepper import Steppers
i2c1 = I2C(I2C.I2C0, mode=I2C.MODE_MASTER,scl=7, sda=6)
s=Steppers(i2c1)
i2c1 = I2C(I2C.I2C0, mode=I2C.MODE_MASTER,scl=7, sda=6)
s1=Servos(i2c1)
input_size = (224, 224)
labels = ['5', '6', '7', '8', '1', '2', '3', '4']
anchors = [1.88, 2.38, 1.31, 2.11, 1.69, 2.19, 1.59, 1.94, 1.53, 1.66]

def lcd_show_except(e):
    import uio
    err_str = uio.StringIO()
    sys.print_exception(e, err_str)
    err_str = err_str.getvalue()
    img = image.Image(size=input_size)
    img.draw_string(0, 10, err_str, scale=1, color=(0xff,0x00,0x00))
    lcd.display(img)

def main(anchors, labels = None, model_addr="/sd/m.kmodel", sensor_window=input_size, lcd_rotation=0, sensor_hmirror=False, sensor_vflip=False):
    sensor.reset()
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    sensor.set_windowing(sensor_window)
    sensor.set_hmirror(sensor_hmirror)
    sensor.set_vflip(sensor_vflip)
    sensor.run(1)

    lcd.init(type=1)
    lcd.rotation(lcd_rotation)
    lcd.clear(lcd.WHITE)

    if not labels:
        with open('labels.txt','r') as f:
            exec(f.read())
    if not labels:
        print("no labels.txt")
        img = image.Image(size=(320, 240))
        img.draw_string(90, 110, "no labels.txt", color=(255, 0, 0), scale=2)
        lcd.display(img)
        return 1
    try:
        img = image.Image("startup.jpg")
        lcd.display(img)
    except Exception:
        img = image.Image(size=(320, 240))
        img.draw_string(90, 110, "loadi1ng model...", color=(255, 255, 255), scale=2)
        lcd.display(img)

    try:
        for i in range(16):
            s1.position(i,90) #i为0~15的16路输出，180表示角度180度。
        task = None
        task = kpu.load(model_addr)
        kpu.init_yolo2(task, 0.5, 0.3, 5, anchors) # threshold:[0,1], nms_value: [0, 1]
        b=0
        while(1):
            img = sensor.snapshot()
            t = time.ticks_ms()
            objects = kpu.run_yolo2(task, img)
            t = time.ticks_ms() - t
            if objects:
                for obj in objects:
                    pos = obj.rect()
                    img.draw_rectangle(pos)
                    img.draw_string(pos[0], pos[1], "%s : %.2f" %(labels[obj.classid()], obj.value()), scale=2, color=(255, 0, 0))
                    for a in range(3):
                        s1.position(a,180) #i为0~15的16路输出，180表示角度180度。
            else:
                b=b+1;
                if(b==200):##调整这个参数 就是调整灵敏度
                    for a in range(3):
                        s1.position(a,90);
                        b=0
            img.draw_string(0, 200, "t:%dms" %(t), scale=2, color=(255, 0, 0))
            lcd.display(img)

    except Exception as e:
        raise e
    finally:
        if not task is None:
                kpu.deinit(task)




if __name__ == "__main__":
    try:
        # main(anchors = anchors, labels=labels, model_addr=0x300000, lcd_rotation=0)
        main(anchors = anchors, labels=labels, model_addr="/sd/model-11975.kmodel")
    except Exception as e:
        sys.print_exception(e)
        lcd_show_except(e)
    finally:
        gc.collect()
