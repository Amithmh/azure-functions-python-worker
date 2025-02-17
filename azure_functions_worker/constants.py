# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import sys

# Capabilities
RAW_HTTP_BODY_BYTES = "RawHttpBodyBytes"
TYPED_DATA_COLLECTION = "TypedDataCollection"
RPC_HTTP_BODY_ONLY = "RpcHttpBodyOnly"
RPC_HTTP_TRIGGER_METADATA_REMOVED = "RpcHttpTriggerMetadataRemoved"
WORKER_STATUS = "WorkerStatus"
SHARED_MEMORY_DATA_TRANSFER = "SharedMemoryDataTransfer"
FUNCTION_DATA_CACHE = "FunctionDataCache"

# Debug Flags
PYAZURE_WEBHOST_DEBUG = "PYAZURE_WEBHOST_DEBUG"

# E2E Integration Flags and Configurations
PYAZURE_INTEGRATION_TEST = "PYAZURE_INTEGRATION_TEST"
PYAZURE_WORKER_DIR = "PYAZURE_WORKER_DIR"

# Platform Environment Variables
AZURE_WEBJOBS_SCRIPT_ROOT = "AzureWebJobsScriptRoot"
CONTAINER_NAME = "CONTAINER_NAME"

# Python Specific Feature Flags and App Settings
PYTHON_ROLLBACK_CWD_PATH = "PYTHON_ROLLBACK_CWD_PATH"
PYTHON_THREADPOOL_THREAD_COUNT = "PYTHON_THREADPOOL_THREAD_COUNT"
PYTHON_ISOLATE_WORKER_DEPENDENCIES = "PYTHON_ISOLATE_WORKER_DEPENDENCIES"
PYTHON_ENABLE_WORKER_EXTENSIONS = "PYTHON_ENABLE_WORKER_EXTENSIONS"
FUNCTIONS_WORKER_SHARED_MEMORY_DATA_TRANSFER_ENABLED = \
    "FUNCTIONS_WORKER_SHARED_MEMORY_DATA_TRANSFER_ENABLED"
"""
Comma-separated list of directories where shared memory maps can be created for
data transfer between host and worker.
"""
UNIX_SHARED_MEMORY_DIRECTORIES = "FUNCTIONS_UNIX_SHARED_MEMORY_DIRECTORIES"

# Setting Defaults
PYTHON_THREADPOOL_THREAD_COUNT_DEFAULT = 1
PYTHON_THREADPOOL_THREAD_COUNT_MIN = 1
PYTHON_THREADPOOL_THREAD_COUNT_MAX = sys.maxsize
PYTHON_THREADPOOL_THREAD_COUNT_MAX_37 = 32

PYTHON_ISOLATE_WORKER_DEPENDENCIES_DEFAULT = False
PYTHON_ISOLATE_WORKER_DEPENDENCIES_DEFAULT_39 = False
PYTHON_ENABLE_WORKER_EXTENSIONS_DEFAULT = False
PYTHON_ENABLE_WORKER_EXTENSIONS_DEFAULT_39 = True

# External Site URLs
MODULE_NOT_FOUND_TS_URL = "https://aka.ms/functions-modulenotfound"
