# torch 学习笔记

## 1. torch.permute

用于 **重新排列张量维度** 的操作。它可以按照用户指定的顺序，改变张量的维度排列方式。

### **1. 基本功能**

`torch.permute` 会根据输入的维度顺序返回一个新的张量，但不改变原始张量的内容和形状，只是调整维度的顺序。

**语法**：

```python
tensor.permute(*dims)
```

- **`dims`**：一个整数元组或多个整数，表示新的维度排列顺序。每个整数是原始维度的索引，必须包含张量的所有维度索引。

### **2. 特点**

- 返回的是一个 **视图**（view），并不会复制原始数据。
- 维度的数量保持不变，只有顺序发生变化。

### **3. 示例**

```python
import torch

# 原始张量 (2, 3, 4)
x = torch.randn(2, 3, 4)

# 调整维度顺序为 (1, 0, 2)
y = x.permute(1, 0, 2)

print(x.shape)  # 输出: torch.Size([2, 3, 4])
print(y.shape)  # 输出: torch.Size([3, 2, 4])
```

**解释**：

- 原始张量的维度是 

  ```
  (2, 3, 4)
  ```

  ，其中：

  - `dim=0` 表示大小为 2。
  - `dim=1` 表示大小为 3。
  - `dim=2` 表示大小为 4。

- ```
  x.permute(1, 0, 2)
  ```

   表示交换维度顺序：

  - 原来的 `dim=1`（大小为 3）变成新的 `dim=0`。
  - 原来的 `dim=0`（大小为 2）变成新的 `dim=1`。
  - `dim=2` 保持不变。

------

### **4. 与 `torch.transpose` 的区别**

- `torch.permute`：
  - 可以重新排列多个维度的顺序。
  - 更灵活。
- `torch.transpose`：
  - 只能交换两个指定的维度。
  - 用法更简单，适用于简单的两维交换。

**示例**：

```python
x = torch.randn(2, 3, 4)

# permute：调整到 (2, 4, 3)
y1 = x.permute(0, 2, 1)

# transpose：交换 dim=1 和 dim=2
y2 = x.transpose(1, 2)

print(y1.shape)  # torch.Size([2, 4, 3])
print(y2.shape)  # torch.Size([2, 4, 3])
```

## torch.norm

求2范数用的API



## torch.normal

- 生成正态分布的随机数，API见下面

```python
import torch
torch.normal(mean, std, size)
```

- 基本用法就是

```python
torch.normal(0, 1, (3,4))
```

> 这个用法就是说生成了一个3*4大小的均值为0，标准差为1的tensor



## torch.climp

- 用于将张量中的元素限制在指定的范围内。将输入张量中的每个元素调整到 `[min, max]` 区间内

- ```python
  torch.clamp(input, min=None, max=None, *, out=None) → Tensor
  ```



## torch.cat

- 用于`Tensor`的拼接， dim用于指定维度，等于几就在哪个维度上进行拼接

- ```py
  torch.cat(tensors, dim=0, *, out=None) → Tensor
  ```
