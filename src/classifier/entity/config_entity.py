from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=False)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path