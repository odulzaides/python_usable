def writeCSV(self, l):
        ''' Writes each tupple into a row in a csv file.'''

        with open('tz.csv', 'wb') as myfile:
            wr = csv.writer(myfile, delimiter=',', quoting=csv.QUOTE_ALL)
            wr.writerows(l) # writerrows writes items to row in cells. Tupples will be their
                            # own rows

