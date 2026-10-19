import ollama

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Hello from PyCharm! Are we ready for model evaluation?',
  },
])

print(response['message']['content'])