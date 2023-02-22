'''Wrapper around the synology API for help with NAS access
'''
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Optional
from urllib.parse import urlparse

from synology_api import filestation


def nas_unzip(
        network_path: str,
        output_path: Path,
        *,
        username: Optional[str] = None,
        password: Optional[str] = None) -> None:
    """Downloads the file located at network_path to output_path

    Args:
        network_path (str): Network path of zip file
        output_path (Path): Local path to unzip to
        username (Optional[str], optional): Username for server. Defaults to None.
        password (Optional[str], optional): Password for server. Defaults to None.
    """
    url_parts = urlparse(network_path)

    file_station = filestation.FileStation(
        ip_address=url_parts.hostname,
        port=url_parts.port or 5001,
        username=username,
        password=password,
        secure=True,
        cert_verify=False,
        otp_code=None
    )

    with TemporaryDirectory() as tmpdir:
        tmp_file = Path(tmpdir, 'tmp.zip')
        file_station.get_file(
            path=url_parts.path,
            mode='download',
            dest_path=tmp_file.as_posix()
        )
        with open(tmp_file, 'rb') as handle:
            with zipfile.ZipFile(handle, 'r') as zip_handle:
                zip_handle.extractall(path=output_path.as_posix())
