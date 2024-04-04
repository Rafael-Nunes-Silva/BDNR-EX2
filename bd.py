from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class BD:
    def __init__(self):
        uri = "URL_CONEXAO_BD"
        
        client = MongoClient(uri, server_api=ServerApi('1'))
        try:
            client.admin.command('ping')
            # print("Conectado com sucesso.")
        except:
            print("A conexão falhou.")
            return

        self.bd = client["BDNR-ML-EX1"]
    
    def usuario_collection(self):
        return self.bd["Usuario"]
    
    def produto_collection(self):
        return self.bd["Produto"]
    
    def vendedor_collection(self):
        return self.bd["Vendedor"]
    
    def compra_collection(self):
        return self.bd["Compra"]