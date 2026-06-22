# 项目材料索引

项目名称：基于视觉识别技术的水面垃圾自动清理机器人设计

本仓库是从原始“大创”文件夹中整理出的 GitHub 展示版，目标是让评审老师或导师可以快速看到项目的技术路线、代码实现、模型材料、数据样例和答辩过程。

## 一、核心技术材料

- `src/maixpy/大创最终项目.py`：项目整合代码，包含 K210 视觉识别和执行机构控制。
- `src/maixpy/main.py`：K210 目标检测主程序。
- `src/maixpy/motor.py`、`servo.py`、`stepper.py`、`pca9685.py`：电机、舵机和 PCA9685 PWM 控制模块。
- `models/model-11975.kmodel`：K210 可部署模型。
- `models/training-report.json`：训练过程、验证结果和 AP 指标报告。

## 二、数据与标注材料

- `data/labels.txt`：类别标签。
- `data/sample_images/`：样例图像。
- `data/annotations/`：XML 标注文件。

这些文件用于展示视觉识别模型的数据准备与训练流程。

## 三、申报与过程文档

- `docs/proposal/项目申报书——陈功力.docx`
- `docs/proposal/【基于视觉识别技术的水面垃圾自动清理机人设计】申请书.docx`
- `docs/proposal/【基于视觉识别技术的水面垃圾自动清理机器人设计】中期检查报告.doc`
- `docs/proposal/基于视觉识别技术的水面垃圾自动清理机器人设计.pdf`

这些材料用于说明项目来源、研究目标、方案设计、阶段进展和项目总结。

## 四、答辩与展示材料

- `docs/presentations/大创初期答辩.pptx`
- `docs/presentations/大创中期答辩.pptx`
- `docs/presentations/中期答辩 4.10v1.0.pptx`
- `docs/presentations/第五组-7清洁船大创结题答辩.pptx`
- `media/videos/视频1.mp4`
- `media/videos/bece2958655d6a1f605466fb102718a8.mp4`

这些材料用于展示项目汇报过程、原型演示和阶段性成果。

## 五、未公开材料说明

原始文件夹中还包含个人简历、第三方开发包、驱动程序、无关软件和超大压缩包。为了保护隐私、避免版权问题并符合 GitHub 文件大小限制，这些内容未放入公开仓库。具体说明见 `archive-notes/original-materials.md`。
