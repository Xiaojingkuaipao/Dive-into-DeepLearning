import matplotlib.pyplot as plt
import torch
from d2l import torch as d2l
from torch.utils import data
from torch import nn


def load_array(X, y, batch_size, is_train=True):
    dataset = data.TensorDataset(X, y)
    return data.DataLoader(dataset, batch_size, is_train)


true_w = torch.normal(0, 0.01, (2, 1))
true_b = torch.zeros(1)

features, labels = d2l.synthetic_data(true_w, true_b, 1000)

batch_size = 10
data_iter = load_array(features, labels, batch_size)

# 定义模型
net = nn.Sequential(nn.Linear(2, 1))

# 初始化参数
net[0].weight.data.normal_(0, 10)
net[0].bias.data.fill_(100)

# 定义损失函数
loss = torch.nn.MSELoss()

# 定义优化器
trainer = torch.optim.SGD(net.parameters(), lr=0.03)

# 开始训练
num_epochs = 15
losses = []

for epoch in range(num_epochs):
    for X, y in data_iter:
        l = loss(net(X), y)
        # 先把之前的梯度清零，因为torch默认累计梯度
        trainer.zero_grad()
        l.backward()
        trainer.step()
    l = loss(net(features), labels)
    losses.append(l.detach().to("cpu").numpy())
    print(f"epoch:{epoch + 1}'s loss :{l}")

plt.plot(list(range(1, num_epochs + 1)), losses)
plt.show()