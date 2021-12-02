import csv
import os


class csvReader:
    def __init__(self, address) -> None:
        self.address = address
        self.data = []

    def read(self, delimiter=",") -> None:
        with open(self.address) as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            self.fields = next(reader)
            for row in reader:
                self.data.append(row)

    def write(self, address, delimiter=",") -> None:
        with open(address, "a+") as csvfile:
            writer = csv.writer(csvfile,
                                delimiter=delimiter,
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
            for row in self.data:
                writer.writerow(row)

    def writeRows(self, address, rows, delimiter=",") -> None:
        with open(address, "a+") as csvfile:
            writer = csv.writer(csvfile,
                                delimiter=delimiter,
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
            writer.writerows(rows)

    def readDict(self, delimiter=",") -> None:
        with open(self.address) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=delimiter)
            self.fields = reader.fieldnames
            for row in reader:
                self.data.append(row)

    def writeDictRow(self, address, delimiter=",") -> None:
        with open(address, "w") as csvfile:
            writer = csv.DictWriter(csvfile,
                                    delimiter=delimiter,
                                    quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL,
                                    fieldnames=self.data[0].keys())
            for row in self.data:
                writer.writerow(row)

    def writeDictRows(self, address, rows, delimiter=",") -> None:
        with open(address, "w") as csvfile:
            writer = csv.DictWriter(csvfile,
                                    delimiter=delimiter,
                                    quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL,
                                    fieldnames=rows[0].keys())
            writer.writerows(rows)

    def getData(self) -> list:
        return self.data
