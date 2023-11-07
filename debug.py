import torch

from models import ncsnpp as model
from configs.poisson import cifar10_ddpmpp as configs


config = configs.get_config()

checkpoint = torch.load('misc/poisson_debug.pth')

score_model = model.NCSNpp(config)
score_model.load_state_dict(checkpoint)
score_model = score_model.eval()
x = torch.ones(8, 3, 32, 32)
y = torch.tensor([1] * 8)
breakpoint()
with torch.no_grad():
  score = score_model(x, y)
