# U.S. refugee data

This repository stores and processes city-level data from [WrapsNet](http://www.wrapsnet.org/) on refugees who have resettled in the United States.

## Data coverage
The `raw_data` directory contains annual CSV files downloaded from the Wrapsnet tool for years 2002-2017.

## If the data's online already ... what's the point?
The WrapsNet tool is clunky and prone to crashing. Plus, chunking the data in years introduces a useful organizing principle.

## Combining the data into one file
Run `parse.py` to pull the data into one clean, combined CSV (`us-refugees.csv`).

## Known issues
Just for fun, sometimes the WRAPSnet CSVs switch the state and country column values. This script uses the [`us`](https://pypi.python.org/pypi/us) package to check whether a column value is a U.S. state or territory and handle it accordingly, with a special case for Georgia, which, turns out, is both a state and a country.