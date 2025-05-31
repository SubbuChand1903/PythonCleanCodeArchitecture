
import os
from src.config.infrastructure.azure.security.azure_keyvault_client import AppKeyVaultClient
from src.config.infrastructure.exceptions.security_exception import SecurityException
from dotenv import load_dotenv

# Load environment variables from .env file if they exist
load_dotenv()
 
class Settings:
    def __init__(self):
        # Set up the Key Vault client
        self.key_vault_url = os.getenv("KEY_VAULT_URL")  # Make sure this environment variable is set
        self.key_vault_client = AppKeyVaultClient(self.key_vault_url)
       
        # Fetch secrets
        self.AZURE_OPENAI_API_KEY = self.get_secret("AZURE-OPENAI-API-KEY")
        self.AZURE_OPENAI_ENDPOINT = self.get_secret("AZURE-OPENAI-ENDPOINT")
        self.AZURE_OPENAI_DEPLOYMENT_NAME = self.get_secret("AZURE-OPENAI-DEPLOYMENT-NAME")
        self.AZURE_OPENAI_API_VERSION = self.get_secret("AZURE-OPENAI-API-VERSION")
        self.AZURE_OPENAI_EMBEDDING_NAME = self.get_secret("AZURE-OPENAI-EMBEDDING-NAME")
        self.AZURE_OPENAI_EMBEDDING_API_VERSION = self.get_secret("AZURE-OPENAI-EMBEDDING-API-VERSION")
 
        self.AZURE_DOC_INTELLIGENCE_ENDPOINT = self.get_secret("AZURE-DOC-INTELLIGENCE-ENDPOINT")
        self.AZURE_DOC_INTELLIGENCE_KEY = self.get_secret("AZURE-DOC-INTELLIGENCE-KEY")
 
        self.AZURE_SEARCH_ENDPOINT = self.get_secret("AZURE-SEARCH-ENDPOINT")
        self.AZURE_SEARCH_ADMIN_KEY = self.get_secret("AZURE-SEARCH-ADMIN-KEY")
        self.AZURE_SEARCH_INDEX = self.get_secret("AZURE-SEARCH-INDEX")
 
        self.AZURE_STORAGE_CONNECTION_STRING = self.get_secret("AZURE-STORAGE-ENDPOINT")
        self.AZURE_BLOB_CONTAINER_NAME = self.get_secret("AZURE-BLOB-CONTAINER-NAME")
        self.AZURE_STORAGE_ACCOUNT_NAME = self.get_secret("AZURE-STORAGE-ACCOUNT-NAME")
        self.AZURE_BLOB_OUTPUT_CONTAINER_NAME = os.getenv("AZURE_BLOB_OUTPUT_CONTAINER_NAME")
   
    def get_secret(self, secret_name: str) -> str:
        try:
            return self.key_vault_client.get_secret(secret_name)
        except Exception as e:
            print(f"Failed to retrieve secret {secret_name}: {e}")
            return "None"
 
# Instantiate the settings
settings = Settings()