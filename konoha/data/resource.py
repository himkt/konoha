from typing import Optional

import logging
import os.path
import re
import secrets


RED = "\033[1;31m"
RST = "\033[0;0m"


logger = logging.getLogger(__name__)


class Resource:
    NBYTES = 6
    KONOHA_DIR = "/tmp/konoha"

    def __init__(self, path: Optional[str]) -> None:
        if path is None:
            self._path = None
            self._raw_path = None

        elif path.startswith("s3://"):
            self._path = self.download_from_s3(path)
            self._raw_path = path

        else:
            self._path = path
            self._raw_path = path

    def download_from_s3(self, path: str) -> str:
        """
        Download file(s) from Amazon S3.

        """
        try:
            import boto3
        except ImportError:
            msg = "Please install boto3:"
            msg += f" {RED}`pip install boto3`{RST}"
            msg += f" or {RED}`pip install konoha[remote]{RST}"
            raise ImportError(msg)

        prefix = secrets.token_hex(self.NBYTES)
        resource_dir = os.path.join(self.KONOHA_DIR, prefix)
        os.makedirs(resource_dir, exist_ok=True)

        re_result = re.search(r"s3://(.*?)/(.+)", path)
        if re_result is None:
            raise ValueError(f"Cannot find bucket name or prefix from {path}")

        bucket_name = re_result.group(1)
        prefix = re_result.group(2)

        resource = boto3.resource("s3")
        bucket = resource.Bucket(bucket_name)

        for obj in bucket.objects.filter(Prefix=prefix):
            data_dir = os.path.join(resource_dir, os.path.dirname(prefix))
            os.makedirs(data_dir, exist_ok=True)

            logger.info(f"Downloading {obj.key}")
            download_path = os.path.join(resource_dir, obj.key)
            bucket.download_file(obj.key, download_path)
            logging.info(f"Downloaded to {download_path}")

        dest_dir = os.path.join(resource_dir, prefix)
        logging.info(f"Downloaded to {dest_dir}")
        return dest_dir

    @property
    def path(self) -> Optional[str]:
        return self._path


if __name__ == "__main__":
    r = Resource("/tmp/main")
    print(r.path)
