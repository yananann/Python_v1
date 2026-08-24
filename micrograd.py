import random

# ====================== 第一部分：Value 标量自动微分引擎（计算图核心） ======================
class Value:
    """
    存储单个标量数值，同时记录梯度、计算关系，实现反向传播自动求导
    对标 PyTorch 的 Tensor 标量版本
    """
    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data          # 数值本身
        self.grad = 0.0           # 梯度 dLoss/d当前值，初始0
        self._backward = lambda: None  # 反向传播函数，每个运算符自定义
        self._prev = set(_children)    # 生成该值的父节点（计算图上游）
        self._op = _op            # 生成该值的运算符，用于可视化
        self.label = label        # 节点标签，方便调试

    def __repr__(self):
        # 打印对象时的输出文本
        return f"Value(data={self.data}, grad={self.grad})"

    # 加法重载 a + b
    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')

        # 定义加法反向传播：y = a + b → dy/da = 1, dy/db = 1
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward
        return out

    # 乘法重载 a * b
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')

        # 乘法反向传播：y = a*b → dy/da = b, dy/db = a
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out

    # 负数 -a
    def __neg__(self):
        return self * -1

    # 减法 a - b
    def __sub__(self, other):
        return self + (-other)

    # 右乘兼容 2 * Value(3)
    def __rmul__(self, other):
        return self * other

    # ReLU 激活函数：max(0, x)，神经网络非线性核心
    def relu(self):
        out = Value(0 if self.data < 0 else self.data, (self,), 'ReLU')
        # ReLU反向：大于0梯度传递，小于0梯度截断
        def _backward():
            self.grad += (1 if out.data > 0 else 0) * out.grad
        out._backward = _backward
        return out

    # 反向传播入口：拓扑排序，从输出节点逐层计算梯度
    def backward(self):
        # 1. 拓扑排序，保证父节点先算梯度
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        # 2. 输出梯度初始化为1（dLoss/dLoss = 1）
        self.grad = 1.0
        # 3. 逆序执行每个节点的反向函数
        for node in reversed(topo):
            node._backward()

# ====================== 第二部分：神经网络模块（图片中全部代码在这里） ======================
class Module:
    """
    神经网络基类，对标 PyTorch nn.Module
    规定两个核心接口：parameters() 获取所有参数、zero_grad() 清空梯度
    """
    def zero_grad(self):
        """清空所有参数的梯度，训练每轮前必须调用"""
        for p in self.parameters():
            p.grad = 0

    def parameters(self):
        """获取当前模块下全部可训练参数（权重、偏置），子类必须重写"""
        return []

# 图片里核心：单个神经元 Neuron
class Neuron(Module):
    def __init__(self, nin, nonlin=True):
        """
        初始化单个神经元
        :param nin: 输入特征维度（输入有多少个数字）
        :param nonlin: 是否启用ReLU非线性激活；False则为纯线性神经元
        """
        # 随机初始化权重，范围 [-1, 1]，每个输入对应一个权重
        self.w = [Value(random.uniform(-1, 1)) for _ in range(nin)]
        # 偏置项，初始值0
        self.b = Value(0)
        # 标记是否开启非线性激活
        self.nonlin = nonlin

    def __call__(self, x):
        """
        前向传播计算：接收输入x，输出神经元结果
        调用方式：neuron(x) 等价于 neuron.__call__(x)
        公式：y = ReLU( sum(w_i * x_i) + b )  / y = sum(w_i * x_i) + b
        """
        # 加权求和：所有w*x相加，再加上偏置b
        act = sum((wi * xi for wi, xi in zip(self.w, x)), self.b)
        # 根据nonlin判断是否使用ReLU激活
        return act.relu() if self.nonlin else act

    def parameters(self):
        """返回该神经元所有可训练参数：权重列表 + 偏置"""
        return self.w + [self.b]

    def __repr__(self):
        """打印神经元信息，区分线性/ReLU神经元"""
        return f"{'ReLU' if self.nonlin else 'Linear'}Neuron({len(self.w)})"

# 图片下半部分：神经网络层 Layer（一层包含多个Neuron）
class Layer(Module):
    def __init__(self, nin, nout, **kwargs):
        """
        初始化一层神经网络
        :param nin: 输入维度，传给层内每一个神经元
        :param nout: 该层输出神经元数量（输出维度）
        :param kwargs: 透传给Neuron的参数（如nonlin=False关闭激活）
        """
        # 创建 nout 个神经元，组成一层
        self.neurons = [Neuron(nin, **kwargs) for _ in range(nout)]

    def __call__(self, x):
        """层前向传播：输入x过每一个神经元，收集所有输出"""
        outs = [n(x) for n in self.neurons]
        # 只有1个输出时直接返回标量，否则返回列表
        return outs[0] if len(outs) == 1 else outs

    def parameters(self):
        """递归收集层内所有神经元的全部参数"""
        return [p for neuron in self.neurons for p in neuron.parameters()]

    def __repr__(self):
        return f"Layer of [{', '.join(str(n) for n in self.neurons)}]"

# 拓展：多层感知器 MLP（多层网络，Layer堆叠）
class MLP(Module):
    def __init__(self, nin, nouts):
        """
        搭建完整多层神经网络
        :param nin: 输入层维度
        :param nouts: 列表，每层输出维度，如 [4,4,1] 代表2隐藏层+1输出层
        """
        sz = [nin] + nouts
        # 构建所有层，最后一层关闭ReLU（回归任务常用）
        self.layers = [Layer(sz[i], sz[i+1], nonlin=i != len(nouts)-1) for i in range(len(nouts))]

    def __call__(self, x):
        # 数据逐层向前传递
        for layer in self.layers:
            x = layer(x)
        return x

    def parameters(self):
        """收集整个网络全部参数"""
        return [p for layer in self.layers for p in layer.parameters()]

    def __repr__(self):
        return f"MLP of [{', '.join(str(layer) for layer in self.layers)}]"

# ====================== 测试示例 ======================
if __name__ == "__main__":
    # 1. 测试单个神经元（图片核心代码）
    n = Neuron(nin=3)
    print("神经元结构：", n)
    input_x = [2.0, -1.0, 0.5]
    out = n(input_x)
    print("神经元输出：", out)
    print("神经元参数：", n.parameters())

    # 2. 测试单层Layer
    layer = Layer(nin=3, nout=2)
    print("\n单层网络：", layer)
    print("单层输出：", layer(input_x))

    # 3. 测试完整3层MLP
    net = MLP(nin=3, nouts=[4, 4, 1])
    print("\n完整神经网络：", net)
    print("网络总参数数量：", len(net.parameters()))