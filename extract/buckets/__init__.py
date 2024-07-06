import json
import logging
from typing import Any

from google.cloud.storage import Client


def get(bucket_name: str, key: str) -> Any:
    try:
        bucket = Client().get_bucket(bucket_name)
        blob = bucket.get_blob(key).download_as_bytes()
        data = json.loads(blob)
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
