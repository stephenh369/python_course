beatles = [
    {"name": "John Lennon", "birth_year": 1940, "death_year": 1980, "instrument": "piano"},
    {"name": "Paul McCartney", "birth_year": 1942, "death_year": None, "instrument": "bass"},
    {"name": "George Harrison", "birth_year": 1943, "death_year": 2001, "instrument": "guitar"},
    {"name": "Ringo Starr", "birth_year": 1940, "death_year": None, "instrument": "drums"}
]

# beatles[0]["instrument"] = "guitar"
# print(beatles)

def band_member_names(band):
    for member in band:
        print(member["name"])

# band_member_names(beatles)

def band_members_alive(band):
    for member in band:
        if member["death_year"] == None:
            print(member)

# band_members_alive(beatles)

names_of_members = [print(member["name"]) for member in beatles]
members_alive = [print(member) for member in beatles if member["death_year"] == None]