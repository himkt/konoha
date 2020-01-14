from typing import Optional

import logging


RED = "\033[1;31m"
RST = "\033[0;0m"


logger = logging.getLogger(__name__)


class Resource:
    NBYTES = 6
    TINY_TOKENIZER_DIR = '/tmp/konoha'

    def __init__(self, path: Optional[str]):

        if path is None:
            self._path = None
            self._raw_path = None

        elif path.startswith('s3://'):
            self._path = self.download_from_s3(path)
            self._raw_path = path

        else:
            self._path = path
            self._raw_path = path

    def download_from_s3(self, path: str) -> str:

        try:
            import boto3
            import re
            import os.path
            import secrets
        except ImportError:
            msg = 'Please install boto3:'
            msg += f' {RED}`pip install boto3`{RST}'
            msg += f' or {RED}`pip install konoha[remote]{RST}'
            raise ImportError(msg)

        prefix = secrets.token_hex(self.NBYTES)
        resource_dir = os.path.join(self.TINY_TOKENIZER_DIR, prefix)
        os.makedirs(resource_dir, exist_ok=True)

        re_result = re.search(r's3://(.*?)/(.+)', path)
        if re_result is None:
            raise ValueError(f'Cannot find bucket name or prefix from {path}')

        bucket_name = re_result.group(1)
        prefix = re_result.group(2)

        resource = boto3.resource('s3')
        bucket = resource.Bucket(bucket_name)

        for obj in bucket.objects.filter(Prefix=prefix):
            _prefix = obj.key.replace(prefix, '')
            if _prefix.startswith('/'):
                _prefix = _prefix[1:]

            if _prefix == '':
                download_path = os.path.join(resource_dir, os.path.basename(obj.key))
                logger.info(f'Downloading {obj.key}')
                bucket.download_file(obj.key, download_path)
                logging.info(f'Downloaded to {download_path}')
                return download_path
            else:
                download_path = os.path.join(resource_dir, _prefix)
                dir_name = os.path.dirname(download_path)
                if not os.path.exists(dir_name):
                    os.makedirs(dir_name, exist_ok=True)

            logger.info(f'Downloading {obj.key}')
            bucket.download_file(obj.key, download_path)

        logging.info(f'Downloaded to {resource_dir}')
        return resource_dir

    @property
    def path(self):
        return self._path


if __name__ == '__main__':
    r = Resource("/tmp/main")
    print(r.path)
