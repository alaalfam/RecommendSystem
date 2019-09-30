import csv


class CSVtoDictConverter:
    def open(self, filename):
        dictionary = dict()
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for entry in reader:
                username = entry[0]
                artist = entry[1]
                rating = entry[2]
                if username in dictionary:
                    dictionary[username][artist] = rating
                else:
                    dictionary[username] = {artist: rating}

        return dictionary