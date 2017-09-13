# U.S. refugee data

This repository stores and processes city-level data from [WrapsNet](http://www.wrapsnet.org/) for refugees who have resettled in the United States.

## Data coverage
The `rawdata` directory contains annual CSV files downloaded from the Wrapsnet tool for years 2002-2016.

## If the data are online already ... what's the point?
The WrapsNet tool is clunky and prone to crshing. Plus, chunking the data in years introduces a useful organizing principle.

## Combining the data into one file
Run `parse.py` to pull the data into a clean, combined CSV ('us-refugees.csv').