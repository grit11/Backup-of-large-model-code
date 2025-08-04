import os
from modelscope import snapshot_download

# 设置国内镜像源
os.environ["MODEL_SCOPE_REPO_MIRROR"] = "https://mirror.modelscope.cn"

# 下载模型（自动从国内镜像加速）
model_dir = snapshot_download('Qwen/Qwen2.5-VL-72B-Instruct', cache_dir='./')
