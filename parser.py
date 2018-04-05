import os
import csv


def fetch_data(data_file):
    '''Parse data from a WRAPS csv into something sensical'''

    with open(data_file, 'r') as d:
        reader = csv.reader(d)

        # skip header jank
        next(reader)
        next(reader)
        next(reader)
        next(reader)

        for row in reader:
            try:
                assert(row[0].startswith('From'))
                year = row[3].split(' ')[1]
                yield {
                    'country': row[5],
                    'year': year,
                    'state': row[2],
                    'city': row[7],
                    'refugees': row[8]
                }
            except (AssertionError, IndexError):
                pass


if __name__ == '__main__':
    with open('us-refugees.csv', 'w') as m:
        headers = ['country', 'year', 'state', 'city', 'refugees']
        writer = csv.DictWriter(m, fieldnames=headers)
        writer.writeheader()
        data_files = sorted(os.listdir('raw_data'))
        for f in data_files:
            x = fetch_data(os.path.join('raw_data', f))
            for record in x:
                writer.writerow(record)
