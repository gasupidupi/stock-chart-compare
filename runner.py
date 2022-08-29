"""Runs processes"""
from charter import Charter
from stock import Stock
from data_retriever import DataRetriever


class Runner():
    """Runs processes"""

    def run(self, *args):
        """Runs processes"""
        args = args[0][0]
        stock_snippets = []
        for i in range(0, len(args), 3):
            stock_snippets.append(Stock(*args[i:i+3], None))
        data_retriever = DataRetriever()
        stocks = data_retriever.retrieve_data(stock_snippets)
        charter = Charter()
        charter.chart(stocks)
