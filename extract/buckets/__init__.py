import json
import logging
import os
from typing import Any

from google.cloud.storage import Client


def get(bucket_name: str, key: str) -> Any:
    try:
        file_path = f"./data/{str.replace(key, "/", "_")}"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                    return json.load(file)
        bucket = Client().get_bucket(bucket_name)
        blob = bucket.get_blob(key).download_as_bytes()
        data = json.loads(blob)
        with open(file_path, "w") as fp:
            json.dump(data, fp)
        return data
    except Exception as ex:
        logging.error(f"getting {key}: {ex}", exc_info=True)
        return None


def list_files(bucket_name: str, prefix: str) -> Any:
    try:
        return Client().list_blobs(bucket_name, prefix=prefix)
    except Exception as ex:
        logging.error(f"getting {bucket_name}: {ex}", exc_info=True)
        return None
