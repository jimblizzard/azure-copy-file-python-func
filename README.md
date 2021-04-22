# Overview
This is a sample Azure Function written in Python that retrieves a file from a URL and then saves it to an Azure Storage Container.

# Requirements
To run this sample locally you need
* [Python 3.X installed](https://www.python.org/downloads/release/python-383/)
* [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local)

# Functions
1. copy_downloaded_file
 * Makes an http request to retrieve a file from one storage account and 

# Download a file and upload to blob storage
copy_downloaded_file

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
3. POST a request to the local URL (with Postman or the like) with a JSON _fileName_ parameter designating the output file name you want to use and the _fileUrl_ of the source file.
```json
{
    "outputFileName": "output_readme.txt",
    "sourceFileUrl": "http://some-source/readme.txt"
}
```
4. The copied file should be in the designated Azure Storage Account in the container designated by the ContainerName environment/settings variable.

# Deploying to Azure
Ensure when deploying to Azure that you add the following App Settings in the function app:
* StorageAccountConnectionString
* OutputContainerName
* SourceStorageUrl