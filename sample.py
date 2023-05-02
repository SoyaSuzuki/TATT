import torch

CUDA_VISIBLE_DEVICES=1

print(torch.cuda.current_device())
print(torch.cuda.device_count())
print(torch.cuda.get_device_capability())