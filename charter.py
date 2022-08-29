"""Generates the chart"""
import matplotlib.pyplot as plt


class Charter():
    """Generates the chart"""

    def chart(self, stocks):
        """Generates the chart"""
        plt.style.use("dark_background")
        plt.title("charts compared")
        colors = ["red","orange","yellow","green","blue","purple"]
        for stock in stocks:
            dtf = stock.dataframe
            normalized_dtf = (dtf-dtf.min())/(dtf.max()-dtf.min())
            plt.plot(normalized_dtf, color=colors.pop(), label=stock.symbol)
        plt.legend(loc="upper right")
        plt.xlabel("time (days)")
        plt.ylabel("price (normalized)")
        plt.tight_layout()
        plt.savefig("output.png")
