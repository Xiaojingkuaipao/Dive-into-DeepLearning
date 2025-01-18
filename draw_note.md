# 绘图笔记

## matplotlib散点图绘制

```python
import matplotlib.pyplot as plt

plt.scatter(x, y, s=None, c=None, alpha=None, marker=None, cmap=None)
```

### 参数

- **x**: x轴数据（一个数组或列表）。
- **y**: y轴数据（一个数组或列表）。
- **s**: 点的大小（可选）。如果是标量，所有点的大小相同；如果是数组，每个点有不同的大小。
- **c**: 点的颜色（可选）。可以是标量、数组或颜色名称。
- **alpha**: 点的透明度（可选），范围为 `[0, 1]`，`0` 表示完全透明，`1` 表示完全不透明。
- **marker**: 点的形状（可选）。例如 `'o'` 表示圆形，`'x'` 表示叉号等。
- **cmap**: 如果 `c` 为数组，`cmap` 设定了颜色映射表（可选）。