# Hardware Notes

This project used a K210/MaixPy vision module with a PCA9685-based PWM control board for actuator output.

## Main Modules

- K210 development board running MaixPy/KPU.
- Camera and LCD module for image capture and visual debugging.
- PCA9685 PWM driver board.
- Servo channels for collection/action mechanisms.
- DC motor or stepper modules for prototype motion, depending on test setup.

## Default Script Parameters

The current `src/maixpy/main.py` uses:

- I2C bus: `I2C.I2C0`
- SCL pin: `7`
- SDA pin: `6`
- Servo channels: `0`, `1`, `2`
- Idle servo angle: `90`
- Active servo angle: `180`

These parameters should be adjusted to match the actual wiring before running on hardware.

## Deployment Checklist

- Confirm the K210 firmware and MaixPy version.
- Copy `main.py`, `boot.py`, and required driver modules to the board or TF card.
- Copy the selected `.kmodel` to the path configured by `MODEL_ADDR`.
- Verify I2C wiring and PCA9685 address.
- Test servo motion separately before enabling detection-triggered actions.
