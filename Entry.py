__author__ = 'Janne'


class Entry:
    def __init__(self, rank, authors, title):
        self.rank = rank,
        self.authors = authors,
        self.title = title

    def showEntry(self):
        print("Entry number: " + str(self.rank))
        print("Title: " + self.title)
        print("Authors: " + str(self.authors))

    def getEntryDataForCSV(self, delimiter):
        return str(self.rank).strip("()\',") + delimiter + self.title.replace(",", "") + delimiter + str(self.authors).strip("()\',").replace(".", "").replace(",", "")