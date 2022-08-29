"""Generates the chart"""
import pandas as pd
import matplotlib.pyplot as plt


class Charter():
    """Generates the chart"""

    def chart(self, stocks):
        """Generates the chart"""
        plt.style.use("dark_background")
        plt.title("charts compared")
        colors = ["red","orange","yellow","green","blue","purple"]
        for stock in stocks:
            plt.plot(stock.dataframe, color=colors.pop(), label=stock.symbol)
        plt.legend(loc="upper right")
        plt.xlabel("time")
        plt.ylabel("price")
        plt.tight_layout()
        plt.savefig("output.png")
