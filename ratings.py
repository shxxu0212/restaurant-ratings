"""Restaurant rating lister."""
import random
# restaurants_data = open('scores.txt')

# def new_rating():
#     while True:
#         rating = int(raw_input("What is your standard good sir/madame? "))
#         if 1 > rating or rating > 5:
#             print "Oops, rating out of range!"
#         else:
#             break
#     return rating
    

def load_restaurants(file_name):
    """populates restaurants dictionary"""
    restaurants = {}

    with open(file_name) as restaurant_data:
        for line in restaurant_data:
            restaurant, rating = line.rstrip().split(":")
            restaurants[restaurant] = rating

    return restaurants

# lambda statement = sort by rating
# sorted_rs = sorted(restaurants.items(), key=lambda tup: tup[1])


def print_sorted_restaurants(restaurant_data):
    """ print sorted restaurants, like the name suggests """
    for restaurant, rating in sorted(restaurant_data.items()):
        print restaurant, "is rated at", str(rating) + "."


def add_restaurant(restaurants):
    """ add new restaurant and rating """
    restaurant = raw_input(("Which respectable nutrient insertion factory would"
                            " you like to judge? ")).title()
    while True:
        rating = int(raw_input("What is your standard good sir/madame? "))
        if 1 > rating or rating > 5:
            print "Oops, rating out of range!"
        else:
            break
    restaurants[restaurant] = rating


def edit_random_restaurant(restaurants):
    """ edit random restaurant's rating """
    random_restaurant = random.choice(restaurants.keys())
    print "{} is currently rated at {}".format(random_restaurant,
                                               restaurants[random_restaurant])
    new_rating = int(raw_input("New rating: "))
    restaurants[random_restaurant] = new_rating
    print "{}'s rating has been updated to {}.".format(random_restaurant,
                                                       new_rating)

def edit_restaurant(restaurants):
    """ update a chosen restaurant's rating """
    restaurant = raw_input(("Which respectable nutrient insertion factory would"
                            " you like to judge? ")).title()
    print "{} is currently rated at {}".format(restaurant,
                                               restaurants[restaurant])
    new_rating = int(raw_input("New rating: "))
    restaurants[restaurant] = new_rating()
    print "{}'s rating has been updated to {}.".format(restaurant,
                                                       new_rating)


def run_interface():
    """main program"""
    restaurants = load_restaurants('scores.txt')
    while True:
        desire = raw_input("\nWhat would you like to do?\n"
                           "a: See all ratings (alphabetical by restaurant)\n"
                           "b: Add new restaurant\n"
                           "c: Update random restaurant's rating\n"
                           "d: Update a restaurant's rating\n"
                           "q: Quit\n"
                           "> ")
        desire = desire.lower()

        if desire == 'a':
            print_sorted_restaurants(restaurants)
        elif desire == 'b':
            add_restaurant(restaurants)
        elif desire == 'c':
            edit_random_restaurant(restaurants)
        elif desire == 'd':
            edit_restaurant(restaurants)
        elif desire == 'q':
            return

run_interface()
