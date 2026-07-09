# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:24:08 2026

@author: Chavosier
"""

from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("MOONSHOT_API_KEY_RED"),
    base_url="https://api.moonshot.cn/v1"
)

def ask_kimi(prompt, model="kimi-k2.6"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=1
    )
    return response.choices[0].message.content

# EXAMPLE
question="Na[Al(OH)4]溶于水有没有沉淀？"

answer = ask_kimi(question)
print(answer)
