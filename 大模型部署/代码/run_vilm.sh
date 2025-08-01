#!/bin/bash

# ===== 手动初始化conda环境（确保conda命令可用） =====
source /root/miniconda3/etc/profile.d/conda.sh

# ===== 激活Qwen2环境（需提前创建好，包含vllm、flash-attention等依赖） =====
conda activate Qwen2_env

# ===== 启动vLLM OpenAI API服务 =====
# 参数说明：
# --model                 : 指定模型权重文件路径
# --host                  : 监听主机地址（0.0.0.0允许外部访问）
# --port                  : API服务端口
# --tensor-parallel-size  : 使用的GPU卡数（建议与物理GPU数量一致）
# --gpu-memory-utilization: 每块GPU分配的显存利用率上限（0.0~1.0，防止OOM）
# --swap-space            : 启用交换空间（单位GB），提升超大模型推理的容错能力
# --max-model-len         : 最大支持的token序列长度
# --trust-remote-code     : 信任模型自带的自定义代码（如Qwen系列需开启）
# --disable-log-requests  : 关闭API请求详细日志（减少日志压力）
# --served-model-name     : 显式指定OpenAI API返回的模型名称（避免与默认冲突）

python -m vllm.entrypoints.openai.api_server \
    --model /root/autodl-tmp/Qwen/Qwen2.5-VL-72B-Instruct \
    --host 0.0.0.0 \
    --port 8000 \
    --tensor-parallel-size 4 \
    --gpu-memory-utilization 0.85 \
    --swap-space 32 \
    --max-model-len 4096 \
    --trust-remote-code \
    --disable-log-requests \
    --served-model-name Qwen2.5-VL-72B-Instruct  # 显式指定模型名称，API调用需使用该名

# ===== END =====

