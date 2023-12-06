import glob
import tomllib
import pandas as pd
from pathlib import Path
from models import MetaData


def file_reader():
    def read_txt(metadata, file):
        try:
            df = pd.read_fwf(file, names=list(metadata.keys()), widths=list(metadata.values()), header=None, encoding='latin-1')[1:-1]
        except Exception as error:
            raise Exception(f'Error reading file: {file}. \n Error: {error}')
            
        return df
    
    dfs = list()
    
    files = glob.glob('historical_quotes' + "/*")
    
    data = tomllib.loads(Path("metadata.toml").read_text(encoding='utf 8'))
    metadata = MetaData(data)
    
    dfs = list(map(lambda file: read_txt(metadata.metadata, file), files))
    
    return dfs