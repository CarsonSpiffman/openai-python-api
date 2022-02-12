from utils import headers
import engine

class OpenAI():
    def __init__(self, apiKey: str) -> None:
        self.TOKEN = apiKey
        self.HEADS = headers.heads(apiKey)
        self.ENGINE = engine

    def completions(self, **kwargs: dict) -> dict:
        return(self.ENGINE.Completions(**kwargs).req(self.HEADS[0]))
    
    def engines(self) -> dict:
        return(self.ENGINE.Engines().req(self.HEADS[0]))
    
    # def retrieve_engine(self, **kwargs: dict) -> dict:
    #     return(self.ENGINE.RetrieveEngines(**kwargs).req(self.HEADS[0]))

    def search(self, **kwargs: tuple) -> dict:
        return(self.ENGINE.Search(**kwargs).req(self.HEADS[0]))
    
    def classification(self, **kwargs: tuple) -> dict:
        return(self.ENGINE.Classification(**kwargs).req(self.HEADS[0]))
        
    def answer(self, **kwargs: tuple) -> dict:
        return(self.ENGINE.Answer(**kwargs).req(self.HEADS[0]))
        
    def delete_files(self, **kwargs: tuple) -> dict:
        return(self.ENGINE.DeleteFile(**kwargs).req(self.HEADS[0]))

    def list_files(self) -> dict:
        return(self.ENGINE.GetFiles().req(self.HEADS[0]))
    
    def upload_files(self, **kwargs: tuple) -> dict:
        return(self.ENGINE.UploadFiles(**kwargs).req(self.HEADS[1]))
    
    def retrieve_files(self, **kwargs: tuple) -> dict:
        return(self.ENGINE.RetrieveFiles(**kwargs).req(self.HEADS[0]))
    
    def retrieve_file_content(self, **kwargs: tuple) -> dict:
        return(self.ENGINE.RetrieveFileContent(**kwargs).req(self.HEADS[0]))
    
    def create_fine_tune(self, **kwargs: tuple) -> dict:
        return(self.ENGINE.CreateFineTune(**kwargs).req(self.HEADS[0]))