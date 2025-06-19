#Tara Gnewikow
#6/4/2025
#Homework 3, Part 1

#PART ONE: Lists

numbers = [22, 90, 0, -10, 3, 22, 48]

#Display the number of elements in the list
print(len(numbers))

#Display the 4th element of this list
print(numbers[3])

#Display the sum of the 2nd and 4th element of the list
print(numbers[1] + numbers[3])

#Display the 2nd-largest value in the list
sorted = sorted(numbers)
print(sorted[-2])

#Display the last element of the original unsorted list
print(numbers[-1])

#Display the sum of all of the numbers divided by two
print(sum(numbers)/2)

#Print whether the median or the mean of the numbers is higher
mean = sum(numbers)/len(numbers)
median = sorted[3]
if mean > median:
    print(mean)
elif median > mean:
    print(median)

#PART ONE: Dictionaries

movie = {
    'title':'Fantastic Mr. Fox',
    'year':2009,
    'director':'Wes Anderson',
    'budget':40_000_000,
    'revenue':58_091_644
    }

#Define a dictionary called movie that works with the following code
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

#Print if the movie was a bad, great or okay investment
if movie['budget'] > movie['revenue']:
    print('That was a bad investment') 
elif movie['revenue'] > movie['budget'] * 5:
    print('That was a great investment')
else:
    print('That was an okay investment')

#Make 1 dictionary that describes the population of the boroughs of NYC
pop = {
    'Manhattan': 1_600_000,
    'Brooklyn': 2_600_000,
    'Bronx': 1_400_000,
    'Queens': 2_300_000,
    'Staten Island': 470_000
}

#Display the population of Brooklyn
print(pop['Brooklyn'])

#Display the combined population of all five boroughs
nyc_pop = pop['Manhattan'] + pop['Brooklyn'] + pop['Bronx'] + pop['Queens'] + pop['Staten Island']
print(nyc_pop)

#Display what percent of NYC's population lives in Manhattan
print(round(pop['Manhattan']/nyc_pop * 100, 2))






