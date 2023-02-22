"""Test Download
"""
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from NasDownload import nas


def test_download():
    with open('credentials.json', 'r', encoding='ascii') as handle:
        creds = json.load(handle)
    with TemporaryDirectory() as tmpdir:
        nas.nas_unzip(
            network_path='smb://e4e-nas.ucsd.edu/temp/github_actions/synology-download/test.zip',
            output_path=tmpdir,
            username=creds['username'],
            password=creds['password']
        )
        test_path = Path(tmpdir, 'test.txt')
        assert test_path.is_file()
        with open(test_path, 'r', encoding='ascii') as handle:
            line = handle.readline()
            assert line.strip() == 'zZ7QTVKYq2MnSrL7MLieRsd8pz'