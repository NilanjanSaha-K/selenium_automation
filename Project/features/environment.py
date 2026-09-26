from config.settings import Config
from core.api_client import APIClient

def before_all(context):
    context.api = APIClient(Config.BASE_URL)
    context.test_data = {}