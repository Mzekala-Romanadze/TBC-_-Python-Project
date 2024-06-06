# This program reads recipes from recipes.json and markets from markets.json files.
# The program asks the user which dish the user is going to cook
# and prints the markets the user should visit to buy the ingredients for the chosen dish.
# The program chooses as few markets as possible for the user
# to save time. If it is impossible to find all ingredients,
# the program prints that the dish can not be cooked in this city.

import json


def open_json_files(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"The {file_name} file does not exist.")
        exit()


def find_market(user_choice, recipes, markets):
    if user_choice not in recipes:
        print(f"The recipe for {user_choice} is not available. Try to cook another dish.")
    else:
        print(f"The chosen dish: {user_choice}")
        needed_ingredients = recipes[user_choice]["ingredients"]
        print(f"Needed ingredients: {needed_ingredients}")

        available_markets = {}
        available_ingredients = []
        for market, products in markets.items():
            available_products = set(needed_ingredients) & set(products)
            temp_ingredient_list = []
            for ingredient in available_products:
                available_ingredients.append(ingredient)
                temp_ingredient_list.append(ingredient)

            available_ingredients = list(set(available_ingredients))
            available_markets[market] = temp_ingredient_list

        # print(f"Markets and available ingredients: {available_markets}")
        print(f"All available ingredients: {available_ingredients}")  # without duplicating of the ingredients

        if len(available_ingredients) != len(needed_ingredients):
            missing_ingredient = set(needed_ingredients) - set(available_ingredients)
            print(f"The {user_choice} can not be cooked. Because the {missing_ingredient} "
                  f"is/are not available in any market in the city.")
            # print(f"But, the user can buy the rest ingredients for {user_choice} in the following markets:")
            # for market, ingredients in available_markets.items():
            #     print(f"=> {market}: {', '.join(ingredients)}")
            # best_choice = optimize_time(available_markets)
            # print(f"The user should buy ingredients in the {best_choice} markets to optimize time.")
        else:
            print(f"All ingredients of {user_choice} are available in the following markets: ")
            for market, ingredients in available_markets.items():
                print(f"=> {market}: {', '.join(ingredients)}")
            best_choice = optimize_time(available_markets)
            print(f"The user should buy ingredients in the {best_choice} markets to optimize time.")


def optimize_time(available_markets):
    ingredient_to_markets = {}

    for market, ingredients in available_markets.items():
        for ingredient in ingredients:
            if ingredient not in ingredient_to_markets:
                ingredient_to_markets[ingredient] = set()
            ingredient_to_markets[ingredient].add(market)

    all_ingredients = set(ingredient_to_markets.keys())
    selected_markets = set()

    while all_ingredients:
        best_market = None
        ingredients_covered_by_best = set()
        for market, ingredients in available_markets.items():
            uncovered_ingredients = set(ingredients) & all_ingredients
            if len(uncovered_ingredients) > len(ingredients_covered_by_best):
                best_market = market
                ingredients_covered_by_best = uncovered_ingredients

        selected_markets.add(best_market)
        all_ingredients -= ingredients_covered_by_best

    return selected_markets


def main():
    recipes = open_json_files("recipes.json")
    markets = open_json_files("markets.json")

    available_dishes = []
    for dish in recipes:
        available_dishes.append(dish)
    print(f"Ready to cook? Pick a tasty dish: {available_dishes}")

    user_choice = input("What are you going to cook? ")

    find_market(user_choice, recipes, markets)


if __name__ == "__main__":
    main()
