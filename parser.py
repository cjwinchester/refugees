import os
import csv

import us


def fetch_data(data_file):
    '''Parse data from a WRAPS csv into something sensical'''

    state_names = [x.name.casefold() for x in us.states.STATES_AND_TERRITORIES]

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

                # some records are ~randomly~ in the wrong order

                # handle georgia, which is both a country and a state
                if row[2].casefold().strip() == 'georgia':
                    if row[5].casefold().strip() in state_names:
                        country = row[2].strip()
                        state = row[5].strip()
                    else:
                        state = row[2].strip()
                        country = row[5].strip()
                else:
                    if row[2].casefold().strip() in state_names:
                        state = row[2]
                        country = row[5]
                    else:
                        state = row[5]
                        country = row[2]

                yield {
                    'country': country,
                    'year': year,
                    'state': state,
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
