"""Parses arguments"""
import argparse
from runner import Runner


parser = argparse.ArgumentParser(
    description="Compare stock charts.",
    usage="There is no limit to stoks you want to compare.\n\
        Format of a single stock: symbol YYYY-MM-DD YYYY-MM-DD\n\
        Example: AAPL 2019-10-10 2019-10-15 GOOGL 2018-01-01 2018-01-05"
)
parser = argparse.ArgumentParser()
parser.add_argument("symbol_snippet", action='append', nargs='+')
args = parser.parse_args().symbol_snippet
runner = Runner()
runner.run(args)
