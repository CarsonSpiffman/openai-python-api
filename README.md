# openai-python-api
Una simple libreria de openAI escrita en Python3

##### Documentacion [ESP]

## Importar API e Inicializar clase OpenAI
```python
from api import OpenAI

API = OpenAI("API-KEY")
```
## Metodos de la API
#### Consultar completions
##### Documentacion
>https://beta.openai.com/docs/api-reference/completions
##### Parametros seteados por defecto
```python
def __init__(self, prompt: str, engine: str = "text-davinci-001", max_tokens: int = 1500,
                temperature: int = 1, top_p: int = 1, n: int = 1, 
                stream: bool = False, logprobs: object = None, stop: str = "<|endoftext|>", **kwargs) -> None:
```
##### Llamada
```python
completions = API.completions(prompt="Say this is a test")
```
##### Devuelve un diccionario
```json
{
  "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
  "object": "text_completion",
  "created": 1589478378,
  "model": "text-davinci-001",
  "choices": [
    {
      "text": "\n\nThis is a test",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ]
}
```


#### Consultar todos los engines disponibles en OpenAI
##### Referencias
>https://beta.openai.com/docs/api-reference/engines
```python
engines = API.engines()
```
##### Devuelve un diccionario
```json
{
  "data": [
    {
      "id": "engine-id-0",
      "object": "engine",
      "owner": "organization-owner",
      "ready": true
    },
    {
      "id": "engine-id-2",
      "object": "engine",
      "owner": "organization-owner",
      "ready": true
    },
    {
      "id": "engine-id-3",
      "object": "engine",
      "owner": "openai",
      "ready": false
    },
  ],
  "object": "list"
}
```

#### Consultar searches
##### Referencias
>https://beta.openai.com/docs/api-reference/searches
##### Parametros seteados por defecto
```python
def __init__(self, query: str, engine: str,  documents: list, 
             file: str = None, max_rerank: int = 200, return_metadata: bool = False, **kwargs) -> None:
```
##### Llamada
```python
search = API.search(query = "the president", engine = "text-curie-001", documents = ["White House",
                                                                                    "hospital",
                                                                                    "school"])
```
##### Devuelve un diccionario
```json
{
  "data": [
    {
      "document": 0,
      "object": "search_result",
      "score": 215.412
    },
    {
      "document": 1,
      "object": "search_result",
      "score": 40.316
    },
    {
      "document": 2,
      "object": "search_result",
      "score":  55.226
    }
  ],
  "object": "list"
}
```
#### Consultar classifications
##### Referencias
>https://beta.openai.com/docs/api-reference/classifications
##### Parametros seteados por defecto
```python
def __init__(self, query: str, search_model: str, model: str, 
                 examples: list, labels: list, file: str = None,
                 temperature: float = 0, logprobs: int = None, max_examples: int = 200,
                 return_prompt: bool = False, return_metadata: bool = False,
                 expand: list = [], **kwargs) -> None:
```
##### Llamada
```python
classification = API.classification(query = "It is a raining day :(", search_model = "ada", model = "curie", examples=[["A happy moment", "Positive"],
                                                                                                                      ["I am sad.", "Negative"],
                                                                                                                      ["I am feeling awesome", "Positive"]],
                                                                                                                      labels = ["Positive", "Negative", "Neutral"])
```
##### Devuelve un diccionario
```json
{
  "completion": "cmpl-2euN7lUVZ0d4RKbQqRV79IiiE6M1f",
  "label": "Negative",
  "model": "curie:2020-05-03",
  "object": "classification",
  "search_model": "ada",
  "selected_examples": [
    {
      "document": 1,
      "label": "Negative",
      "text": "I am sad."
    },
    {
      "document": 0,
      "label": "Positive",
      "text": "A happy moment"
    },
    {
      "document": 2,
      "label": "Positive",
      "text": "I am feeling awesome"
    }
  ]
}

```

#### Consultar answers
##### Referencias
>https://beta.openai.com/docs/api-reference/answers
##### Parametros seteados por defecto
```python
def __init__(self, question: str, documents: list, search_model: str,
                 model: str, examples_context: str, examples: list,
                 max_tokens: int = 1500, stop: list = ["\n", "<|endoftext|>"], file: str = None,
                 temperature: float = 0, n: int = 1, return_metadata: bool = False,
                 return_prompt: bool = False, expand: list = [], **kwargs) -> None:
```
##### Llamada
```python
answer = API.answer(question = "which puppy is happy?",
                    documents = ["Puppy A is happy.", 
                                 "Puppy B is sad."],
                    search_model = "ada",
                    model = "curie",
                    examples_context = "In 2017, U.S. life expectancy was 78.6 years.",
                    examples = [["What is human life expectancy in the United States?",
                                 "78 years."]],
                    max_tokens = 5,
                    stop = ["\n", "<|endoftext|>"])
```
##### Devuelve un diccionario
```json
{
  "answers": [
    "puppy A."
  ],
  "completion": "cmpl-2euVa1kmKUuLpSX600M41125Mo9NI",
  "model": "curie:2020-05-03",
  "object": "answer",
  "search_model": "ada",
  "selected_documents": [
    {
      "document": 0,
      "text": "Puppy A is happy. "
    },
    {
      "document": 1,
      "text": "Puppy B is sad. "
    }
  ]
}
```
#### Consultar files, listar files
##### Referencias
>https://beta.openai.com/docs/api-reference/files/list
##### Parametros seteados por defecto
```
Ninguno
```
##### Llamada
```python
list_files = API.list_files()
```
##### Devuelve un diccionario
```json
{
  "data": [
    {
      "id": "file-ccdDZrC3iZVNiQVeEA6Z66wf",
      "object": "file",
      "bytes": 175,
      "created_at": 1613677385,
      "filename": "train.jsonl",
      "purpose": "search"
    },
    {
      "id": "file-XjGxS3KTG0uNmNOK362iJua3",
      "object": "file",
      "bytes": 140,
      "created_at": 1613779121,
      "filename": "puppy.jsonl",
      "purpose": "search"
    }
  ],
  "object": "list"
}
```
#### Consultar files, subir files
##### Referencias
>https://beta.openai.com/docs/api-reference/files/upload
##### Parametros seteados por defecto
```python
def __init__(self, file: str, purpose: str, **kwargs) -> None:
```
##### Llamada
```python
archivo_ejemplo = json.load(open('filw.json'), "r"))

upload_files = API.upload_files(file = archivo_ejemplo, purpose = "Ejemplo/Example")
```
##### Devuelve un diccionario
```json
{
  "id": "file-XjGxS3KTG0uNmNOK362iJua3",
  "object": "file",
  "bytes": 140,
  "created_at": 1613779121,
  "filename": "puppy.jsonl",
  "purpose": "answers"
}
```
#### Consultar files, borrar files
##### Referencias
>https://beta.openai.com/docs/api-reference/files/delete
##### Parametros seteados por defecto
```
Ninguno
```
##### Llamada
```python
delete_file = API.delete_files(file_id = "file-XjGxS3KTG0uNmNOK362iJua3")
```
##### Devuelve un diccionario
```json
{
  "id": "file-XjGxS3KTG0uNmNOK362iJua3",
  "object": "file",
  "deleted": true
}
```
#### Consultar fine-tunes, crear fine-tune
##### Referencias
>https://beta.openai.com/docs/api-reference/fine-tunes/create
##### Parametros seteados por defecto
```python
def __init__(self, training_file: str, validation_file: str = '', model: str = "curie",
                 n_epochs: int = 4, batch_size: int = 256, learning_rate_multiplier: float = 0.1,
                 prompt_loss_weight: float = 0.1, compute_classification_metrics: bool = False, classification_n_classes: int = 0,
                 classification_positive_class: str = '', classification_betas: list = [], **kwargs) -> None:
```
##### Llamada
```python
create_fine_tune = API.create_fine_tune(training_file = "file-XGinujblHPwGLSztz8cPS8XY")
```
##### Devuelve un diccionario
```json
{
  "id": "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
  "object": "fine-tune",
  "model": "curie",
  "created_at": 1614807352,
  "events": [
    {
      "object": "fine-tune-event",
      "created_at": 1614807352,
      "level": "info",
      "message": "Job enqueued. Waiting for jobs ahead to complete. Queue number: 0."
    }
  ],
  "fine_tuned_model": null,
  "hyperparams": {
    "batch_size": 4,
    "learning_rate_multiplier": 0.1,
    "n_epochs": 4,
    "prompt_loss_weight": 0.1,
  },
  "organization_id": "org-...",
  "result_files": [],
  "status": "pending",
  "validation_files": [],
  "training_files": [
    {
      "id": "file-XGinujblHPwGLSztz8cPS8XY",
      "object": "file",
      "bytes": 1547276,
      "created_at": 1610062281,
      "filename": "my-data-train.jsonl",
      "purpose": "fine-tune-train"
    }
  ],
  "updated_at": 1614807352,
}
```
#### Consultar files, subir files
##### Referencias
>https://beta.openai.com/docs/api-reference/files/upload
##### Parametros seteados por defecto

## Ejemplos de uso
```python
from api import OpenAI

API = OpenAI("API_KEY")

query_ejemplo = "#Python\n Hacer una funcion para sumar enteros llamada sumarEnteros y usarla con un ejemplo. \n"

completions = API.completions(prompt = query_ejemplo, engine= "code-davinci-001", max_tokens = 150)

print(completions)
```
## Respuesta
```json
{"id": "cmpl-ID", "object": "text_completion", "created": 1641651411, "model": "code-davinci:001", "choices": [{"text": "\n\ndef sumarEnteros(a,b):\nif isinstance(a and b, int):\n   return a+b\n    else:\n        return(\"error\")\n\nprint(\"sumarEnteros(3,3): \",sumarEnteros(3,3))\nprint(\"sumarEnteros(22,67): \",sumarEnteros(22,67))\nprint(\"sumarEnteros(22,67,\",sumarEnteros(\"orru\",\"alte\"))\n    \n    \n\n\n#%%%\n#%%", "index": 0, "logprobs": null, "finish_reason": "stop"}]}
```

## Imprimir respuesta
```python
from api import OpenAI
import json

API = OpenAI("sess-1mD0uh9uzgvfIytcnzhsGzoFVuY1ycwC5Mm9SmvF")

query_ejemplo = "#Python\n Hacer una funcion usando Threading. \n"

completions = API.completions(prompt = query_ejemplo, engine= "code-davinci-001", max_tokens = 300)

print(json.loads(completions)["choices"][0]["text"])
```
## Respuesta (identado automatico cualquier lenguaje)
```
 Que al recibir una lista de 10 palabras, crear 10 hilos, y cada hilo, imprimir las palabras pero
cada uno, debe esperar un segundo en hacerlo.

from threading import Thread
from time import sleep
from random import randint

# se ejecuta en hilo1
def imprime(listaIngresada):
    print("Se imprime en hilo demonio")
    for i in listaIngresada:
        #hace una pausa de un segundo antes de continuar
        sleep(1)
        print("({})".format(i))
    print("*Fin de la lista*")


sleep(randint(1,5))
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#De aqui se crea un nuevo hilo, queue es un thread
#en este caso el demonio

hilo = Thread(target=imprime, args=(lista,))
#el demonio es un tipo de thread, ejecuta en paralelo
#con el codigo principal
hilo.daemon = True
#se inicia el
```
## Como obtener la ApiKey
>https://beta.openai.com/account/api-keys

###### Cualquier duda o consulta preguntame mi discord es `Carson#9752`, algunos metodos no los inclui.
