import csv

def parseCSV(year, filename, delim):
    with open(filename, "rb") as ref:
        f = open("refugees-" + year + "-processed.txt", "wb")
        reader = csv.reader(ref, delimiter=delim)
        state = country = city = ''
        for row in reader:
            if row[0] != "":
                state = row[0]
            if row[1] != "":
                country = row[1]
            if row[2] != "":
                city = row[2]
            if row[0] == "" and row[1] == "":
                number = str(int(float(row[3])))
                f.write("|".join([year, city, state, country, number]) + "\n")
        f.close()