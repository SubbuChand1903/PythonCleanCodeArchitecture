from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

class AppKeyVaultClient:
    def __init__(self, vault_url, client_id, client_secret, tenant_id):
        self.vault_url = vault_url
        self.credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
        self.client = SecretClient(vault_url=self.vault_url, credential=self.credential)
        # print(self.credential,self.client)

    def get_secret(self, secret_name):
        try:
            secret = self.client.get_secret(secret_name)
            # print(secret.value)
            return secret.value
        except Exception as e:
            print(f"Error fetching secret '{secret_name}' from Azure Key Vault: {str(e)}")
            return None