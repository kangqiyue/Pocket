```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
```


```python
# Define model
class TheModelClass(nn.Module):
    def __init__(self):
        super(TheModelClass, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Initialize model
model = TheModelClass()

# Initialize optimizer
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

```


```python
# Print model's state_dict
print("Model's state_dict:")
for param_tensor in model.state_dict():
    print(param_tensor, "\t", model.state_dict()[param_tensor].size())

```

    Model's state_dict:
    conv1.weight 	 torch.Size([6, 3, 5, 5])
    conv1.bias 	 torch.Size([6])
    conv2.weight 	 torch.Size([16, 6, 5, 5])
    conv2.bias 	 torch.Size([16])
    fc1.weight 	 torch.Size([120, 400])
    fc1.bias 	 torch.Size([120])
    fc2.weight 	 torch.Size([84, 120])
    fc2.bias 	 torch.Size([84])
    fc3.weight 	 torch.Size([10, 84])
    fc3.bias 	 torch.Size([10])
    


```python
# Print optimizer's state_dict
print("Optimizer's state_dict:")
for var_name in optimizer.state_dict():
    print(var_name, "\t", optimizer.state_dict()[var_name])
```

    Optimizer's state_dict:
    state 	 {}
    param_groups 	 [{'lr': 0.001, 'momentum': 0.9, 'dampening': 0, 'weight_decay': 0, 'nesterov': False, 'params': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}]
    


```python
type(model.state_dict())
```




    collections.OrderedDict




```python
type(model.parameters())
```




    generator




```python
for k in model.parameters():
    print(k.shape)
```

    torch.Size([6, 3, 5, 5])
    torch.Size([6])
    torch.Size([16, 6, 5, 5])
    torch.Size([16])
    torch.Size([120, 400])
    torch.Size([120])
    torch.Size([84, 120])
    torch.Size([84])
    torch.Size([10, 84])
    torch.Size([10])
    


```python
for k in model.state_dict():
    print(k)
```

    conv1.weight
    conv1.bias
    conv2.weight
    conv2.bias
    fc1.weight
    fc1.bias
    fc2.weight
    fc2.bias
    fc3.weight
    fc3.bias
    


```python
for k,v in model.state_dict().items():
    print(f"key: {k}; v: {v.shape}")
```

    key: conv1.weight; v: torch.Size([6, 3, 5, 5])
    key: conv1.bias; v: torch.Size([6])
    key: conv2.weight; v: torch.Size([16, 6, 5, 5])
    key: conv2.bias; v: torch.Size([16])
    key: fc1.weight; v: torch.Size([120, 400])
    key: fc1.bias; v: torch.Size([120])
    key: fc2.weight; v: torch.Size([84, 120])
    key: fc2.bias; v: torch.Size([84])
    key: fc3.weight; v: torch.Size([10, 84])
    key: fc3.bias; v: torch.Size([10])
    


```python

```
