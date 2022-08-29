"""Stores information about a stock"""
from dataclasses import dataclass
from datetime import date
import pandas as pd

@dataclass
class Stock:
    """Stores information about a stock"""
    symbol: str
    start_date: date
    end_date: date
    dataframe: pd.DataFrame
