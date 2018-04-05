import os
import csv

import us


ST = [x.name.casefold() for x in us.states.STATES_AND_TERRITORIES]


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
                refugee_count = int(row[8].replace(',', ''))

                '''The  CSVs include every record twice -- once sorted
                by destination and once sorted by country of origin, with
                country and state swapping column positions. 🙄
                We get the pieces in the correct place here, and downstream
                we check for (and ignore) duplicates.
                '''

                # handle georgia, which is both a country and a state
                if row[2].casefold().strip() == 'georgia':
                    if row[5].casefold().strip() in ST:
                        country = row[2].strip()
                        state = row[5].strip()
                    else:
                        state = row[2].strip()
                        country = row[5].strip()
                else:
                    if row[2].casefold().strip() in ST:
                        state = row[2].strip()
                        country = row[5].strip()
                    else:
                        state = row[5].strip()
                        country = row[2].strip()

                yield {
                    'country': country,
                    'year': year,
                    'state': state,
                    'city': row[7].strip(),
                    'refugees': refugee_count
                }
            except (AssertionError, IndexError):
                pass


if __name__ == '__main__':
    with open('us-refugees.csv', 'w') as m:
        headers = ['country', 'year', 'state', 'city', 'refugees']
        writer = csv.DictWriter(m, fieldnames=headers)
        writer.writeheader()
        x = fetch_data('raw_data/wraps2017.csv')
        data_files = os.listdir('raw_data')
        for f in sorted(data_files):
            x = fetch_data(os.path.join('raw_data', f))

            # handle duplicates
            done = set()
            for record in x:
                if str(record) in done:
                    continue
                done.add(str(record))
                writer.writerow(record)
