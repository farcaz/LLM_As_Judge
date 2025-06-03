import os
import requests

API_URL = "https://router.huggingface.co/hf-inference/models/meta-llama/Llama-3.1-8B-Instruct/v1/chat/completions"

def judge_response(user_prompt, chatbot_response, model="meta-llama/Llama-3.1-8B-Instruct"):
    hf_token = os.getenv("HUGGINGFACE_TOKEN")
    if not hf_token:
        raise ValueError("HUGGINGFACE_TOKEN not set in environment variables.")

    judge_prompt = (
        f"User asked: {user_prompt}\n"
        f"Chatbot replied: {chatbot_response}\n"
        "Please evaluate the chatbot's response for correctness, helpfulness, and completeness. "
        "Give a short justification and a score from 1 to 10."
    )

    headers = {
        "Authorization": f"Bearer {hf_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "messages": [
            {
                "role": "user",
                "content": judge_prompt
            }
        ],
        "model": model
    }

    response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    result = response.json()
    return result["choices"][0]["message"]["content"]