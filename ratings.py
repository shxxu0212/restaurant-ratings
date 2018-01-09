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
        print restaurant, "is rated at", rating + "."

restaurant = raw_input("which respectable nutrient insertion factory would\
                             you like to judge? ")
rating = raw_input("what is your standard good sir/madame? ")

restaurants[restaurant] = rating
print_sorted_restaurants(restaurants)