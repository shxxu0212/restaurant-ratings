"""Restaurant rating lister."""

# restaurants_data = open('scores.txt')
restaurants = {}

with open('scores.txt') as restaurant_data:
    for line in restaurant_data:
        restaurant, rating = line.rstrip().split(":")
        restaurants[restaurant] = rating

# lambda statement = sort by rating
# sorted_rs = sorted(restaurants.items(), key=lambda tup: tup[1])

def print_sorted_restaurants(restaurant_data):
    for restaurant, rating in sorted(restaurant_data.items()):
        print restaurant, "is rated at", str(rating) + "."


def add_restaurant():
    restaurant = raw_input(("Which respectable nutrient insertion factory would"
                            " you like to judge? ")).title()
    while True:
        rating = int(raw_input("What is your standard good sir/madame? "))
        if 1 > rating or rating > 5:
            print "Oops, rating out of range!"
            continue
        else:
            break

    restaurants[restaurant] = rating

while True:
    desire = raw_input("What would you like to do?\n"
                       "a: See all ratings (alphabetical by restaurant)\n"
                       "b: Add new restaurant\n"
                       "c: Quit\n"
                       ">")

    if desire.lower() == 'a':
        print_sorted_restaurants(restaurants)
    elif desire.lower() == 'b':
        add_restaurant()
    elif desire.lower() == 'c':
        quit()
