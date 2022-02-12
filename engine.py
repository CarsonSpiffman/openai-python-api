import requests

class Engines():
    def __init__(self) -> None:
        self.PETICIONES = Peticiones(None, None)
    
    def req(self, headers: dict) -> dict:
        return(self.PETICIONES.peticionEngines(headers))
    
class RetrieveEngines():
    def __init__(self, engine_id: str, **kwargs) -> None:
        kwargs["engine_id"] = engine_id
        
        self.parametros = kwargs
        self.PETICIONES = Peticiones(kwargs["engine_id"], self.parametros)
        
    def req(self, headers: dict) -> dict:
        return(self.PETICIONES.peticionesRetrieveEngines(headers))

class Completions():
    def __init__(self, prompt: str, engine: str = "text-davinci-001", max_tokens: int = 1500,
                temperature: int = 1, top_p: int = 1, n: int = 1, 
                stream: bool = False, logprobs: object = None, stop: str = "<|endoftext|>", **kwargs) -> dict:
        
        kwargs["prompt"] = prompt
        kwargs["max_tokens"] = max_tokens
        kwargs["temperature"] = temperature
        kwargs["top_p"] = top_p
        kwargs["n"] = n
        kwargs["stream"] = stream
        kwargs["logprobs"] = logprobs
        kwargs["stop"] = stop 

        self.engine = engine
        self.parametros = kwargs
        self.PETICIONES = Peticiones(self.engine, self.parametros)
        
    def req(self, headers: dict) -> dict:
        return(self.PETICIONES.peticionCompletions(headers))

class Search():
    def __init__(self, query: str, engine: str,  documents: list, 
                 file: str = None, max_rerank: int = 200, return_metadata: bool = False, **kwargs) -> None:
        kwargs["query"] = query
        kwargs["engine"] = engine
        kwargs["documents"] = documents
        kwargs["file"] = file
        kwargs["max_rerank"] = max_rerank
        kwargs["return_metadata"] = return_metadata
        
        self.parametros = kwargs
        self.PETICIONES = Peticiones(engine, self.parametros)
    
    def req(self, headers: dict) -> dict:
        return(self.PETICIONES.peticionSearch(headers))

class Classification():
    def __init__(self, query: str, search_model: str, model: str, 
                 examples: list, labels: list, file: str = None,
                 temperature: float = 0, logprobs: int = None, max_examples: int = 200,
                 return_prompt: bool = False, return_metadata: bool = False,
                 expand: list = [], **kwargs) -> None:
        
        kwargs["query"] = query
        kwargs["search_model"] = search_model
        kwargs["model"] = model
        kwargs["examples"] = examples
        kwargs["labels"] = labels
        kwargs["file"] = file
        kwargs["temperature"] = temperature
        kwargs["logprobs"] = logprobs
        kwargs["max_examples"] = max_examples
        kwargs["return_prompt"] = return_prompt
        kwargs["return_metadata"] = return_metadata
        kwargs["expand"] = expand
        
        self.parametros = kwargs
        self.PETICIONES = Peticiones(None, self.parametros)
        
    def req(self, headers: dict) -> dict:
        return(self.PETICIONES.peticionClassification(headers))

class Answer():
    def __init__(self, question: str, documents: list, search_model: str,
                 model: str, examples_context: str, examples: list,
                 max_tokens: int = 1500, stop: list = ["\n", "<|endoftext|>"], file: str = None,
                 temperature: float = 0, n: int = 1, return_metadata: bool = False,
                 return_prompt: bool = False, expand: list = [], **kwargs) -> None:
        kwargs["question"] = question
        kwargs["documents"] = documents
        kwargs["search_model"] = search_model
        kwargs["model"] = model
        kwargs["examples_context"] = examples_context
        kwargs["max_tokens"] = max_tokens
        kwargs["stop"] = stop
        kwargs["file"] = file
        kwargs["temperature"] = temperature
        kwargs["n"] = n
        kwargs["return_metadata"] = return_metadata
        kwargs["return_prompt"] = return_prompt
        kwargs["expand"] = expand
        
        self.parametros = kwargs
        self.PETICIONES = Peticiones(None, self.parametros)
        
    def req(self, headers: dict) -> dict:
        return(self.PETICIONES.peticionAnswer(headers))
        
class DeleteFile():
    def __init__(self, file_id: str, **kwargs) -> None:
        kwargs["file_id"] = file_id
        
        self.parametros = kwargs
        self.PETICIONES = Peticiones(None, self.parametros)
        
    def req(self, headers: dict) -> dict:
        return(self.PETICIONES.peticionDeleteFile(headers))
    
class GetFiles():
    def __init__(self) -> None:
        self.PETICIONES = Peticiones(None, None)
    
    def req(self, headers: dict) -> dict:
        return(self.PETICIONES.peticionGetFiles(headers))
    
class UploadFiles():
    def __init__(self, file: str, purpose: str, **kwargs) -> None:
        kwargs["file"] = file
        kwargs["purpose"] = purpose
        
        self.parametros = kwargs
        self.PETICIONES = Peticiones(None, self.parametros)
    
    def req(self, headers: dict) -> dict:
        return(self.PETICIONES.peticionUploadFiles(headers))

class RetrieveFiles():
    def __init__(self, file_id: str, **kwargs) -> None:
        kwargs["file_id"] = file_id
        
        self.parametros = file_id
        self.PETICIONES = Peticiones(None, self.parametros)
    
    def req(self, headers:dict) -> dict:
        return(self.PETICIONES.peticionRetrieveFiles(headers))
    
class RetrieveFileContent():
    def __init__(self, file_id: str, **kwargs) -> None:
        kwargs["file_id"] = file_id
        
        self.parametros = file_id
        self.PETICIONES = Peticiones(None, self.parametros)

    def req(self, headers:dict) -> dict:
        return(self.PETICIONES.peticionRetrieveFileContent(headers))

class CreateFineTune():
    def __init__(self, training_file: str, validation_file: str = '', model: str = "curie",
                 n_epochs: int = 4, batch_size: int = 256, learning_rate_multiplier: float = 0.1,
                 prompt_loss_weight: float = 0.1, compute_classification_metrics: bool = False, classification_n_classes: int = 0,
                 classification_positive_class: str = '', classification_betas: list = [], **kwargs) -> None:
        kwargs["training_file"] = training_file
        kwargs["validation_file"] = validation_file
        kwargs["model"] = model
        kwargs["n_epochs"] = n_epochs
        kwargs["batch_size"] = batch_size
        kwargs["learning_rate_multiplier"] = learning_rate_multiplier
        kwargs["prompt_loss_weight"] = prompt_loss_weight
        kwargs["compute_classification_metrics"] = compute_classification_metrics
        kwargs["classification_n_classes"] = classification_n_classes
        kwargs["classification_positive_class"] = classification_positive_class
        kwargs["classification_betas"] = classification_betas
        
        self.parametros = kwargs
        self.PETICIONES = Peticiones(None, self.parametros)
    
    def req(self, headers: dict) -> dict:
        return(self.PETICIONES.peticionCreateFineTune(headers))
 
class Peticiones:
    def __init__(self, engine: str, parametros: dict) -> None:
        self.API = "https://api.openai.com/v1/"
        self.ENGINE = engine
        self.PARAMS = parametros
            
    def reqAndy(self, api_url: str, metodo: str, headers: dict) -> dict:
        return(requests.request(metodo, api_url, json=self.PARAMS, headers=headers).text)
        
    def peticionCompletions(self, headers: dict) -> dict:
        return(self.reqAndy(f"{self.API}engines/{self.ENGINE}/completions", "POST", headers))
        
    def peticionEngines(self, headers: dict) -> dict:
        return(self.reqAndy(f"{self.API}engines", "GET", headers))
    
    def peticionesRetrieveEngines(self, headers: dict) -> dict:
        return(self.reqAndy(f"{self.API}engines/{self.ENGINE}", "GET", headers))
    
    def peticionSearch(self, headers: dict) -> dict:
        return(self.reqAndy(f"{self.API}engines/{self.ENGINE}/search", "POST", headers))
    
    def peticionClassification(self, headers: dict) -> dict:
        return(self.reqAndy(f"{self.API}classifications", "POST", headers))
    
    def peticionAnswer(self, headers: dict) -> dict:
        return(self.reqAndy(f"{self.API}answers", "POST", headers))
    
    def peticionDeleteFile(self, headers: dict) -> dict:
        return(self.reqAndy(f"{self.API}files/{self.PARAMS['file_id']}", "DELETE", headers))
    
    def peticionGetFiles(self, headers: dict) -> dict:
        return(self.reqAndy(f"{self.API}files", "GET", headers))
    
    def peticionUploadFiles(self, headers: dict) -> dict:
        return(self.reqAndy(f"{self.API}files", "POST", headers))
    
    def peticionRetrieveFiles(self, headers: dict) -> dict:
        return(self.reqAndy(f"{self.API}files/{self.PARAMS}", "GET", headers))
    
    def peticionRetrieveFileContent(self, headers: dict) -> dict:
        return(self.reqAndy(f"{self.API}files/{self.PARAMS}/content", "GET", headers))
    
    def peticionCreateFineTune(self, headers: dict) -> dict:
        return(self.reqAndy(f"{self.API}fine-tunes", "POST", headers))