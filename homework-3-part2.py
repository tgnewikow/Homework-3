#Tara Gnewikow
#6/5/2025
#Homework 3, Part 2

#PART TWO: Lists

#Make a list called "countries" 
#It should contain seven different countries and NOT be in alphabetical order
countries = ['United States', 'Canada', 'Mexico', 'China', 'Germany', 'France', 'Brazil']

#Using a for loop, print each element of the list
for country in countries:
    print(country)

#Sort the list permanently
countries.sort()
print(countries)

#Display the first element of the list
print(countries[0])

#Display the second-to-last element of the list
print(countries[-2])

#Delete one of the countries from the list using its name
countries.remove('United States')
print(countries)

#Using a for loop, print each country's name in all caps
for country in countries:
    print(country.upper())

#PART TWO: Dictionaries

#Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude' 
#Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees
tree = {
    'name':'Witch Tree',
    'species': 'Eastern White Cedar',
    'age':300,
    'location_name': 'Cook County, Minnesota',
    'latitude': 47.5730,
    'longitude': 9.3830
}

#Print the sentence "{name} is a {years} year old tree that is in {location_name}"
print(f'{tree['name']} is a {tree['age']} year old tree that is in {tree['location_name']}')

#The coordinates of New York City are 40.7128° N, 74.0059° W 
#Check to see if the tree is south of NYC
#Print "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"
nyc_lat = 40.7128

if tree['latitude'] < nyc_lat:
    print(f'The tree {tree['name']} in {tree['location_name']} is south of NYC')
elif tree['latitude'] > nyc_lat:
    print(f'The tree {tree['name']} in {tree['location_name']} is north of NYC')

#Ask the user how old they are 
# If they are older than the tree, display "you are {XXX} years older than {name}" 
# If they are younger than the tree, display "{name} was {XXX} years old when you were born"

user_age = input('How old are you?')
user_age = int(user_age)

if user_age > tree['age']:
    print(f'you are {user_age - tree['age']} years older than {tree['name']}')
elif tree['age'] > user_age:
    print(f'{tree['name']} was {tree['age'] - user_age} years old when you were born')

#PART TWO: Lists of dictionaries

#Make a list of dictionaries of five places across the world: (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago
#Each dictionary should include each city's name and latitude/longitude

places = [
    {'name': 'Moscow', 'latitude': 55.75582600, 'longitude': 37.61729990},
    {'name': 'Tehran', 'latitude': 35.72484160, 'longitude': 51.38165300},
    {'name': 'Falkland Islands', 'latitude': -51.796253, 'longitude': -59.523613},
    {'name': 'Seoul', 'latitude':37.56600000, 'longitude': 126.97840000},
    {'name': 'Santiago', 'latitude': -33.45694000, 'longitude': -70.64827000}
]

#Loop through the list, printing each city's name and whether it is above or below the equator 
# When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone"
for place in places:
    if place['latitude'] > 0:
        print(f'{place['name']} is above the equator.')
    elif place['latitude'] < 0:
        print(f'{place['name']} is below the equator. The {places[2]['name']} are a biogeographical part of the mild Antarctic zone')

#Loop through the list, printing whether each city is north of south of your tree

for place in places:
    if place['latitude'] > tree['latitude']:
        print(f'{place['name']} is north of {tree['name']}')
    elif place['latitude'] < tree['latitude']:
        print(f'{place['name']} is south of {tree['name']}')