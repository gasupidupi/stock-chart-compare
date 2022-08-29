"""Stores information about a stock"""
from dataclasses import dataclass
from datetime import date
import numpy as np

@dataclass
class StockSnippet:
    """Stores information about a stock"""
    symbol: str
    start_date: date
    end_date: date
    data: np.ndarray
