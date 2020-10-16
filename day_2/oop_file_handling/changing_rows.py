import csv
from winner import Winner

winners = []
with open("oscars.csv") as csvfile:
  reader = csv.reader(csvfile, skipinitialspace=True)

  next(reader)
  for row in reader:
    winners.append(Winner(*row))

with open("oscars.csv", "w", newline="") as csvfile:
  writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

  writer.writerow(["Index", "Year", "Age", "Name", "Movie"])

  for winner in winners:
    winner.age -= 1
    writer.writerow(winner.values_as_list())
