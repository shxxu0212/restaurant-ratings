"""Restaurant rating lister."""

restaurants_f = open('scores.txt')
restaurants = {}
for line in restaurants_f:
    restaurant_name, rating = line.rstrip().split(":")
    restaurants[restaurant_name] = rating

sorted_rs = sorted(restaurants.items())

for restaurant, rating in sorted_rs:
    print restaurant, "is rated at", rating + "."
