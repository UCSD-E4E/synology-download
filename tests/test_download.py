"""Test Download
"""
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Dict

import pytest

from nas_unzip import nas


@pytest.fixture(name='creds')
def create_creds() -> Dict[str, str]:
    """Obtains the credentials

    Returns:
        Dict[str, str]: Username and password dictionary
    """
    if Path('credentials.json').is_file():
        with open('credentials.json', 'r', encoding='ascii') as handle:
            return json.load(handle)
    else:
        value = os.environ['NAS_CREDS'].splitlines()
        assert len(value) == 2
        return {
            'username': value[0],
            'password': value[1]
        }

def test_download(creds):
    """Tests downloading a file
    """
    with TemporaryDirectory() as tmpdir:
        nas.nas_unzip(
            network_path='smb://e4e-nas.ucsd.edu:6021/temp/github_actions/synology-download/test.zip',
            output_path=Path(tmpdir),
            username=creds['username'],
            password=creds['password']
        )
        test_path = Path(tmpdir, 'test.txt')
        assert test_path.is_file()
        with open(test_path, 'r', encoding='ascii') as handle:
            line = handle.readline()
            assert line.strip() == 'zZ7QTVKYq2MnSrL7MLieRsd8pz'
