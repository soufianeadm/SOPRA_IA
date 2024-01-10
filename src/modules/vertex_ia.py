import vertexai
from vertexai.preview.language_models import TextGenerationModel
from google.auth.transport.requests import Request
from google.auth import exceptions
from google.auth.compute_engine import Credentials
import google.auth
import os


def main():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "fr-gcp-i2s-agence-lille-116ae9aaee72.json"

    print("GOOGLE_APPLICATION_CREDENTIALS:", os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))
    # Créez un objet de classe Credentials pour une instance GCP
    credentials, gcp_project = google.auth.default()

    # Vérifiez si les informations d'authentification sont valides

    try:
        print(gcp_project, credentials)
    except:
        print("ca a merde")


    vertexai.init(project=gcp_project, location="us-central1")
    parameters = {
        "max_output_tokens": 2048,
        "temperature": 0.9,
        "top_p": 1
    }
    print("GOOGLE_APPLICATION_CREDENTIALS:", os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))
    # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials
    model = TextGenerationModel.from_pretrained("text-bison")
    response = model.predict(
        """la on parle d os , de sysyteme d exploitation

    input: qu est ce que linux
    output: linux est un os

    input: qu est ce que windows
    output: windows est un os de microsoft

    input: qu est ce que debian avec une reponse complete
    output:
    """,
        **parameters
    )
    print(f"Response from Model: {response.text}")
    return f"Response from Model: {response.text}"