import os
import csv


def fetch_data(data_file):
    with open(data_file, 'r') as d:
        reader = csv.reader(d)

        for row in reader:

            try:
                if row[0].startswith('From'):

                    year = row[3].split(' ')[1]

                    yield {
                        'country': row[2],
                        'year': year,
                        'state': row[5],
                        'city': row[7],
                        'refugees': row[8]
                    }
            except:
                pass


def doit():

    with open('us-refugees.csv', 'w') as m:

        headers = ['country', 'year', 'state', 'city', 'refugees']

        writer = csv.DictWriter(m, fieldnames=headers)

        writer.writeheader()

        data_files = os.listdir('rawdata')

        for f in data_files:

            x = fetch_data(os.path.join('rawdata', f))

            for thing in x:
                writer.writerow(thing)


if __name__ == '__main__':
    doit()
