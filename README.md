# Water Surface Trash Cleaning Robot

本科大创项目材料整理仓库：基于视觉识别技术的水面垃圾自动清理机器人设计。

This repository collects the source code, trained K210 model, sample dataset, project documents, presentation files, and demo videos for an undergraduate innovation project on an autonomous water-surface trash cleaning robot.

## 中文简介

本项目面向水面漂浮垃圾自动清理场景，设计了一个结合嵌入式视觉识别与执行机构控制的小型清洁机器人方案。项目使用 K210 边缘 AI 开发板进行目标检测，将识别到的垃圾目标与舵机/电机控制联动，实现从视觉感知到机械执行的闭环原型。

仓库内容经过公开展示整理，适合作为申博/科研经历材料查看：

- 项目代码：K210 MaixPy 推理、舵机、电机和 PCA9685 控制程序。
- 模型材料：可部署 `.kmodel` 模型与训练评估报告。
- 数据材料：样例图片、类别标签和 XML 标注文件。
- 项目文档：申报书、中期检查、项目 PDF、初期/中期/结题答辩 PPT。
- 演示材料：项目运行视频。

更多中文材料索引见 `PROJECT_MATERIALS.md`。

## Project Overview

The project focuses on a small robotic platform for detecting and collecting floating trash on water. The vision module uses a Kendryte K210 board running MaixPy, with a YOLO-style object detection model converted to `.kmodel`. The control side drives servos and motors through an I2C PCA9685 controller to trigger collection actions after object detection.

Main goals:

- Detect common floating trash targets such as bottles and bags.
- Run inference on embedded hardware with MaixPy/KPU.
- Link perception results to actuator control for automatic cleanup.
- Package the project as reproducible research and application material for graduate application review.

## Repository Structure

```text
.
├── src/maixpy/              # MaixPy source code for K210 vision and actuator control
├── models/                  # K210 model and training report
├── data/                    # Sample images, labels, and XML annotations
├── docs/proposal/           # Proposal, midterm report, and project PDF
├── docs/presentations/      # Defense and progress presentation slides
├── media/videos/            # Project demo videos
├── media/images/            # Reserved for selected result images
├── hardware/                # Reserved for hardware notes and diagrams
└── archive-notes/           # Notes about excluded local materials
```

## Technical Stack

- Embedded vision: Kendryte K210, MaixPy, KPU
- Model type: YOLO2-style object detection model
- Input size: `224 x 224`
- Hardware control: PCA9685 PWM driver, servos, motors, I2C
- Project language: MicroPython / MaixPy Python

## Code Entry Points

- `src/maixpy/大创最终项目.py`: integrated detection and actuator-control script.
- `src/maixpy/main.py`: generated K210 detection script.
- `src/maixpy/motor.py`, `servo.py`, `stepper.py`, `pca9685.py`: actuator and PWM driver modules.
- `src/maixpy/boot.py`, `setup.py`: board setup/support scripts.

The final project script initializes the camera and LCD, loads the `.kmodel`, performs object detection, draws detection results, and drives servos when trash is detected.

## Model And Dataset

Model artifacts:

- `models/model-11975.kmodel`: K210 deployable model.
- `models/training-report.json`: training/evaluation report exported from the model workflow.

Dataset sample:

- `data/labels.txt`: dataset labels.
- `data/sample_images/`: sample training/validation images.
- `data/annotations/`: XML detection annotations.

The training report records the model configuration, anchors, loss curve, validation accuracy, AP values, and representative prediction results.

## Hardware Deployment

Typical deployment steps:

1. Copy files from `src/maixpy/` and `models/model-11975.kmodel` to the K210 board or TF card.
2. Adjust the model path in the main script if needed, for example `/sd/model-11975.kmodel`.
3. Connect the PCA9685 board through I2C pins used in the script.
4. Connect servos or motors to the expected PCA9685 output channels.
5. Power on the board and run the MaixPy script.

Hardware parameters such as I2C pins, servo channels, and detection thresholds should be checked against the actual robot wiring before running.

## Project Materials

Project documents and presentation materials are kept in `docs/`:

- Project proposal and midterm materials in `docs/proposal/`
- Initial, midterm, and final defense slides in `docs/presentations/`

Demo videos are kept in `media/videos/`.

## Notes For Reviewers

This repository is a curated public-facing version of the original project folder. Personal resume files, unrelated software packages, third-party development kits, executable tools, and oversized compressed archives were excluded from the GitHub version. See `archive-notes/original-materials.md` for details.

## License

Project code and self-created materials are shared for academic review and portfolio demonstration. Third-party materials remain owned by their original authors and are not redistributed here.
