"""Runs processes"""
from stock_snippet import StockSnippet
from data_retriever import DataRetriever


class Runner():
    """Runs processes"""

    def run(self, *args):
        """Runs processes"""
        args = args[0][0]
        stock_snippets = []
        print(args)
        for i in range(0, len(args), 3):
            print(i)
            print(args[i:i+3])
            stock_snippets.append(StockSnippet(*args[i:i+3], None))
        data_retriever = DataRetriever()
        stock_snippets = data_retriever.retrieve_data(stock_snippets) # Get historical stock prices.
