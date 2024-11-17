# accept csv, use polars to do some bi return it.
from fastapi import UploadFile
import polars as pl


def parse_csv(file: UploadFile) -> pl.DataFrame:
    """
    parses a binary uploadFile into polars dataframe and renames the columns.
    """
    #TODO: implement
    pass
    
