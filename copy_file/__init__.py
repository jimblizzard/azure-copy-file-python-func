import logging
import requests
import os

import azure.functions as func


def main(req: func.HttpRequest, outputblob: func.Out[func.InputStream]) -> func.HttpResponse:
    json_body = req.get_json()
    if 'fileName' not in json_body:
        return func.HttpResponse(
            "Request JSON body did not include fileName.",
            status_code=400
        )

    response = requests.get(get_url(json_body['fileName']))

    if response.status_code >= 300:
        logging.error("Source file error", response.raise_for_status())
        return func.HttpResponse(
            "Error occured with the source file.",
            status_code=500
        )

    outputblob.set(response.content)

    return func.HttpResponse(
        "Successfully copied the file.",
        status_code=200
    )

def get_url(fileName):
    url = os.environ['SourceStorageUrl']
    
    if not url.endswith('/'):
        url += '/'

    url += fileName
    return url