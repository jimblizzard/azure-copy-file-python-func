import logging
import requests
import os

import azure.functions as func


def main(req: func.HttpRequest, outputblob: func.Out[func.InputStream]) -> func.HttpResponse:
    json_body = req.get_json()
    if 'outputFileName' not in json_body:
        error = 'Request JSON body did not include outputFileName.'
        logging.error(error)
        return func.HttpResponse(
            error,
            status_code=400
        )
    if 'sourceFileUrl' not in json_body:
        error = 'Request JSON body did not include sourceFileUrl.'
        logging.error(error)
        return func.HttpResponse(
            error,
            status_code=400
        )

    response = requests.get(json_body['sourceFileUrl'])

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