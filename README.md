# Synology NAS Downloader
This package provides a way to easily download and unzip a `.zip` file into the specified directory.

# Example Usage
```
from pathlib import Path

from nas_unzip.nas import nas_unzip

nas_unzip(
    network_path='smb://example.com/share/path/file.zip',
    output_path=Path('.'),
    username='username',
    password='password'
)
```

For the above example, if `file.zip` contained the following structure:
```
file.zip
  > folderA
    - file1
    - file2
  - file3
```

Then we would have the resulting structure:
```
.
> folderA
  - file1
  - file2
- file3
```

## Developers
This package should be developed using VS Code.
1. Clone this repository
2. Open `synology-download.code-workspace` with VS Code.
3. Create a python virtual environment for this project (we suggest `venv`, so do `python3 -m venv .venv` and select that environment for this project)
4. Install poetry (`python -m pip install poetry`)
5. Install this package using `poetry` (`python -m poetry install`)
6. Configure your test parameters
    1. Create `${workspaceFolder}/credentials.json`
    2. Put the following information into `${workspaceFolder}/credentials.json`:
    ```
    {
        "username": "username",
        "password": "password",
    }
    ```