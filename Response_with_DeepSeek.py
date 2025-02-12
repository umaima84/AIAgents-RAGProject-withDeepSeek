from groq import Groq

client = Groq(api_key="Enter Your GROQ Cloud API Key")

completion = client.chat.completions.create(
    model="deepseek-r1-distill-qwen-32b",  
    messages=[
        {"role": "system", "content": "You are an AI assistant specialized in AI Agents."},
        {"role": "user", "content": user_query}
    ],
    temperature=0.6,
    max_completion_tokens=1500, 
    top_p=0.95,
    stream=True, 
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")