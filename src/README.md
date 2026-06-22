# Source Code

The source code targets MaixPy on K210 hardware.

Important files:

- `maixpy/大创最终项目.py`: integrated object detection and servo-control workflow.
- `maixpy/main.py`: model inference script generated from the K210 model workflow.
- `maixpy/motor.py`, `maixpy/servo.py`, `maixpy/stepper.py`, `maixpy/pca9685.py`: motor and servo control helpers.

Before running on hardware, verify:

- K210 firmware/MaixPy version.
- Model file path on the TF card.
- I2C pins and PCA9685 address.
- Servo/motor channel mapping.
