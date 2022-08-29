"""Parses arguments"""
import argparse
from runner import Runner


parser = argparse.ArgumentParser(
    description="Compare stock charts.",
    usage="Stock format: symbol YYYY-MM-DD YYYY-MM-DD\n\
        Example: SPY 2007-01-01 2008-08-01 SPY 2021-01-01 2022-08-01"
)
parser = argparse.ArgumentParser()
parser.add_argument("symbol_snippet", action='append', nargs='+')
args = parser.parse_args().symbol_snippet
runner = Runner()
runner.run(args)
