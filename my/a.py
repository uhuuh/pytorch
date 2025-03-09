import torch
from torch.profiler import profile, record_function, ProfilerActivity

model = models.resnet18()
inputs = torch.randn(5, 3, 224, 224)

with profile(activities=[ProfilerActivity.CPU], record_shapes=True) as prof:
    with record_function("model_inference"):
        img = torch.rand(1, 3, 224, 224)
        conv = torch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=5)
        out = conv(img)

print(prof.key_averages().table(sort_by="cpu_time_total", row_limit=10))

