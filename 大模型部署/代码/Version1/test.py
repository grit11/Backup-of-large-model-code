import requests
import json
import time

def test_text_chat(prompt: str, max_tokens: int = 512, temperature: float = 0.7):
    """
    测试模型的纯文本对话能力
    :param prompt: 用户输入的文本提示
    :param max_tokens: 最大生成 tokens 数
    :param temperature: 生成随机性（0-1，值越低越确定）
    """
    # 模型服务地址（默认端口8000，与启动脚本一致）
    url = "http://localhost:8000/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    
    # 构造请求数据
    payload = {
        "model": "Qwen2.5-VL-72B-Instruct",  # 与启动时的模型名称一致
        "messages": [
            {"role": "system", "content": "你是一个高效的AI助手，擅长清晰、准确地回答各类问题。"},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stream": False  # 非流式返回，直接获取完整结果
    }
    
    try:
        # 发送请求并计时
        start_time = time.time()
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=60)
        end_time = time.time()
        
        # 解析响应
        if response.status_code == 200:
            result = response.json()
            if "choices" in result and len(result["choices"]) > 0:
                answer = result["choices"][0]["message"]["content"]
                print(f"用户输入: {prompt}\n")
                print(f"模型回复 ({end_time - start_time:.2f}秒):\n{answer}\n")
                print("-" * 80)
            else:
                print("模型未返回有效结果:", result)
        else:
            print(f"请求失败 (状态码: {response.status_code}):", response.text)
    
    except requests.exceptions.RequestException as e:
        print(f"请求出错: {str(e)}")
    except json.JSONDecodeError:
        print("响应格式错误，无法解析为JSON")

if __name__ == "__main__":
    print("===== Qwen2.5-VL-72B-Instruct 纯文本测试 =====")
    
    # 测试用例：涵盖不同类型的问题
    test_cases = [
        "解释一下什么是机器学习，并举例说明其在日常生活中的应用。",
        "用三句话概括量子计算的核心原理及其潜在影响。",
        "写一段关于秋天的散文，要求语言优美且有画面感。",
        "已知一个三角形的两边长分别为3和4，夹角为90度，求第三边长和面积。"
    ]
    
    # 依次运行测试用例
    for i, prompt in enumerate(test_cases, 1):
        print(f"测试用例 {i}/{len(test_cases)}:")
        test_text_chat(prompt)
        time.sleep(1)  # 避免请求过于密集
