"""Retrieves the data"""
from stock_snippet import StockSnippet


class DataRetriever:
    """Retrieves the historical stock prices"""

    def retrieve_data(self, *args: StockSnippet):
        """Retrieves the historical stock prices"""
        for stock_snippet in args[0]:
            print(stock_snippet.symbol)
