import torch
shape = (1,10,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)
eps = 1e-6
mean = torch.mean(rand_tensor)
var = torch.var(rand_tensor)
layer_norm = torch.nn.LayerNorm(len(rand_tensor))
layer_norm(rand_tensor)

print(rand_tensor)
print(layer_norm)
print(f"mean: {mean}")
print(f"variance: {var}")

layernorm_tensor = ones_tensor * rand_tensor - mean / (var + eps) + zeros_tensor
print(layernorm_tensor)
