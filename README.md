# Overview
This is a sample Azure Function written in Python that retrieves a file from a URL and then saves it to an Azure Storage Container.

# Requirements
To run this sample locally you need
* [Python 3.X installed](https://www.python.org/downloads/release/python-383/)
* [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local)

To run the sample:
1. Create a _local.settings.json_ file with the following settings (ensure the source container has anonymous read access)
```json
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "StorageAccountConnectionString": "(output_storage_account_connection_string)",
    "OutputContainerName": "(output_container_name)",
    "SourceStorageUrl": "(source_file_storage_url)"
  }
}
```
2. Run _func start_ in the directory
3. POST a request to the local URL (with Postman or the like) with a JSON _fileName_ parameter designating the path and file name of the file to copy. This will be appended to the SourceStorageUrl app setting to create the full URL for file retrieval.
```json
{
    "fileName": "readme.txt"
}
```
4. The copied file should be in the designated Azure Storage Account 

# Deploying to Azure
Ensure when deploying to Azure that you add the following App Settings in the function app:
* StorageAccountConnectionString
* OutputContainerName
* SourceStorageUrl