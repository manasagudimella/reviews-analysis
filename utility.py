import json
from pathlib import Path
import pandas as pd

def get_jsondata(data_path: str = "test_response.json") -> json:
    with open(data_path, "r") as f:
        data = json.load(f)
    return data