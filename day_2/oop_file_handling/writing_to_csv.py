import csv
from winner import Winner

with open("oscars.csv") as csvfile:
  reader = csv.reader(csvfile, skipinitialspace=True)
  index = sum(1 for row in reader)

with open("oscars.csv", "a") as csvfile:
  writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
  winner = Winner(index, 2020, 50, "Renée Zelweger", "Judy")
  writer.writerow(winner.values_as_list())