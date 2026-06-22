# Source Code

The source code targets MaixPy on K210 hardware.

Important files:

- `maixpy/main.py`: unified object detection and servo-control entry point.
- `maixpy/boot.py`: minimal MaixPy boot file; `main.py` is the project entry point.
- `maixpy/motor.py`, `maixpy/servo.py`, `maixpy/stepper.py`, `maixpy/pca9685.py`: motor, servo, stepper, and PWM control helpers.

Before running on hardware, verify:

- K210 firmware/MaixPy version.
- Model file path on the TF card.
- I2C pins and PCA9685 address.
- Servo/motor channel mapping.
- Model labels and anchors.

Note: the checked-in `model-11975.kmodel` matches the 8-class model in `models/training-report.json`. The bottle/bag configuration in `main.py` is kept as a template for the trash-specific model because a separate final bottle/bag `.kmodel` was not identifiable in the archived local files.
