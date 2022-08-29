"""Retrieves the data"""
import yfinance as yf
from stock import Stock


class DataRetriever:
    """Retrieves the historical stock prices"""

    def retrieve_data(self, *args: Stock):
        """Retrieves the historical stock prices"""
        for stock in args[0]:
            stock.dataframe = yf.download(
                                stock.symbol,
                                start=stock.start_date,
                                end=stock.end_date
                            ).drop(["Open","High","Low","Adj Close","Volume"], axis=1).reset_index(
                            ).drop("Date", axis=1)
        return args[0]
