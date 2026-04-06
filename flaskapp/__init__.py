import azure.functions as func
from ..main import main as flask_main


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return flask_main(req, context)
