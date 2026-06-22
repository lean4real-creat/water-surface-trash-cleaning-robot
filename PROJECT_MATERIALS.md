# 项目材料索引

项目名称：基于视觉识别技术的水面垃圾自动清理机器人设计

本仓库是本科大创项目的归档与展示版本，用于集中整理代码、模型文件、样例数据、项目文档、答辩材料和演示视频。重点展示项目中的嵌入式视觉识别、执行机构控制和样机联调过程。

## 一、核心技术材料

- `src/maixpy/main.py`：整理后的统一入口，包含 K210 视觉识别和舵机联动控制。
- `src/maixpy/boot.py`：MaixPy 最小启动文件。
- `src/maixpy/motor.py`、`servo.py`、`stepper.py`、`pca9685.py`：电机、舵机和 PCA9685 PWM 控制模块。
- `models/model-11975.kmodel`：K210 可部署模型文件，用于展示 K210 模型部署流程。
- `models/training-report.json`：训练过程、验证结果和 AP 指标报告。

## 二、模型说明

当前仓库中的 `model-11975.kmodel` 与 `training-report.json` 对应的是原始项目文件夹中可确认的 8 类训练配置。项目目标是水面垃圾识别，`data/` 中保留了 bottle/bag 样例图像与 XML 标注，`src/maixpy/main.py` 中也保留了 bottle/bag 模型配置模板。

由于归档文件中没有单独识别出最终 bottle/bag 垃圾识别 `.kmodel`，本仓库不把当前模型描述为完整最终垃圾模型，而是作为大创过程材料、K210 部署流程和样机控制代码的展示。

## 三、数据与标注材料

- `data/labels.txt`：类别标签。
- `data/sample_images/`：样例图像。
- `data/annotations/`：XML 标注文件。

这些文件用于展示视觉识别模型的数据准备与标注流程。

## 四、申报与过程文档

- `docs/proposal/项目申报书——陈功力.docx`
- `docs/proposal/【基于视觉识别技术的水面垃圾自动清理机人设计】申请书.docx`
- `docs/proposal/【基于视觉识别技术的水面垃圾自动清理机器人设计】中期检查报告.doc`
- `docs/proposal/基于视觉识别技术的水面垃圾自动清理机器人设计.pdf`

这些材料用于说明项目来源、研究目标、方案设计、阶段进展和项目总结。

## 五、答辩与展示材料

- `docs/presentations/大创初期答辩.pptx`
- `docs/presentations/大创中期答辩.pptx`
- `docs/presentations/中期答辩 4.10v1.0.pptx`
- `docs/presentations/第五组-7清洁船大创结题答辩.pptx`
- `media/images/`：README 展示图与视频抽帧。
- `media/videos/视频1.mp4`
- `media/videos/bece2958655d6a1f605466fb102718a8.mp4`

这些材料用于展示项目汇报过程、原型演示和阶段性成果。

## 六、与机器人方向相关的能力

- 嵌入式视觉识别部署。
- K210/MaixPy/KPU 推理流程。
- PWM 舵机控制与 PCA9685 驱动。
- 电机/步进电机控制模块使用。
- 视觉感知与执行机构动作联动。
- 样机系统集成、调试和答辩展示。
