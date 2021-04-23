# Overview
This is a sample Azure Function written in Python that retrieves a file from a URL and then saves it to an Azure Storage Container.

# Requirements
To run this sample locally you need
* [Python 3.X installed](https://www.python.org/downloads/release/python-383/)
* [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local)

# Functions
1. copy_downloaded_file
    + Makes an http request to retrieve a file from a URL using a standard web request and then streams the blob to an output binding pointing to an Azure Storage Container.
2. copy_streamed_file
    + Invokes the Azure Storage API to retrieve a file from a specified URL and stream it directly into an Azure Storage Container. This is a blocking operation in the function invocation instance until the transfer is complete.

# Running Locally

To run the sample:
1. Create a _local.settings.json_ file with the following settings (ensure the source container has anonymous read access)
```json
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "StorageConnectionString": "(output_storage_account_connection_string)",
    "ContainerName": "(output_container_name)"
  }
}
```
2. Run _func start_ in the directory
3. POST a request to the local URL of the specific function you want to invoke (with Postman or the like) with the following payload:
 * outputFileName: The desired file name of the uploaded blob in Azure Storage.
 * sourceFileUrl: The url of the source blob.
```json
{
    "outputFileName": "output_readme.txt",
    "sourceFileUrl": "http://some-source/readme.txt"
}
```

# Deploying to Azure
Ensure when deploying to Azure that you add the following App Settings in the function app:
* StorageConnectionString
* ContainerName