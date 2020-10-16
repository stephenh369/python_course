import csv
from winner import Winner

winners = []

with open("oscars.csv") as csvfile:
  reader = csv.reader(csvfile, skipinitialspace=True)

  next(reader)
  for row in reader:
    current_winner = Winner(*row)
    winners.append(current_winner)

# for winner in winners:
#   print(f"{winner.name} won the Oscar for {winner.movie} in {winner.year} at age {winner.age}.")

for winner in winners:
  if winner.year > 1979 and winner.year < 1990:
    print(winner.name)

old_winner = winners[0]
for winner in winners:
  if winner.age > old_winner.age:
    old_winner = winner
print(old_winner.name, old_winner.age)
  
meryl_streeps_wins = [(winner.movie, winner.year) for winner in winners if winner.name == "Meryl Streep"]
print(meryl_streeps_wins)