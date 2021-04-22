import logging
import os
from azure.storage.blob import BlobServiceClient

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    json_body = req.get_json()
    if 'sourceFileUrl' not in json_body:
        error = 'Request JSON body did not include sourceFileUrl.'
        logging.error(error)
        return func.HttpResponse(
            error,
            status_code=400
        )

    file_url = json_body.get('sourceFileUrl')
    logging.info(f'sourceFileUrl: {file_url}')

    file_name = json_body.get('outputFileName')
    if 'outputFileName' not in json_body:
        logging.info('No output file name designated. Using source file name.')
        file_name = file_url.split('/')[-1]
        file_name = file_name.split('?')[0] # Remove any querystring params
    logging.info(f'outputFileName: {file_name}')

    blob_service_client = BlobServiceClient.from_connection_string(os.getenv('StorageConnectionString'))
    blob_client = blob_service_client.get_blob_client(os.getenv('ContainerName'), file_name)

    logging.info('Starting upload.')
    blob_client.upload_blob_from_url(file_url)
    logging.info('Finished Upload')

    return func.HttpResponse(
        "Successfully copied the file.",
        status_code=200
    )