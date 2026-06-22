# Models

This folder contains the K210 model artifact and training metadata.

- `model-11975.kmodel`: deployable model for K210/MaixPy KPU inference.
- `training-report.json`: exported training report, including anchors, validation metrics, AP values, and representative prediction results.

The model is loaded in MaixPy with:

```python
task = kpu.load("/sd/model-11975.kmodel")
kpu.init_yolo2(task, 0.5, 0.3, 5, anchors)
```
