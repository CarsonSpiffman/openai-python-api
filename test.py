from api import OpenAI
import json

API = OpenAI("API_KEY")

query_ejemplo = "#Python\n Hacer una funcion usando Threading. \n"

completions = API.completions(prompt = query_ejemplo, engine= "code-davinci-001", max_tokens = 300)

print(json.loads(completions)["choices"][0]["text"])