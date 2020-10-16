breakfast = ["eggs", "bacon", "beans", "toast"]
print(len(breakfast[:2]))

lucky_numbers = [3, 6, 9, 12, 27]
print(sum(lucky_numbers))

stops = ["Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket"]

stops.append("Edinburgh Waverley")
print(stops)

stops.insert(0, "Queen Street",)
print(stops)

print(stops.index("Croy"))

stops.insert(stops.index("Falkirk High") + 1, "Polmont")
print(stops)

stops.remove("Haymarket")
print(stops)

stops.clear()
print(stops)



