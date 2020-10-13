import requests
import os
from pprint import pprint


key = os.environ.get('FOOD_KEY')

url = 'https://api.spoonacular.com/recipes/complexSearch'


def main():
    recipe = get_recipe()
    recipe_query = get_recipe_query(recipe)
    recipe_info = get_recipe_info(recipe_query)
    print(f'The recipe you saved: {recipe_info}')


def get_recipe():
    recipe_search = ''.strip()
    while len(recipe_search) == 0 or not recipe_search.isalpha():
        recipe_search = input('Search for a recipe: ')
    return recipe_search


def get_recipe_query(recipe):
    try:
        query = {'query': recipe, 'addRecipeInformation': 'true', 'maxCalories': '800', 'minFat': '1', 'minProtein': '10', 'number': '2', 'apiKey': key}
        # data = requests.get(url, params=query).json()
        response = requests.get(url, params=query).json()
        data = response['results']
        pprint(data)
        return data
    except Exception as e:
        print('Error with your query. ')

def get_recipe_info(recipe_data):


    try:
        results = recipe_data['nutrition']['spoonacularSourceUrl']
        return results
    except KeyError:
        print('This data is not in the format expected')
        return 'Unknown'


    # recipe_list = []

    # save_a_recipe = input('Type in the recipe name that you want to save. '))
    # for i in recipe_data:
    #     save_data = (i['title': save_a_recipe],i['spoonacularSourceUrl'])
    # if save_a_recipe == 0:
    #     print('Please enter a valid id. ')
    # else:
    #     recipe_list.append(save_data)
    # return recipe_list

    # recipe_list.append(save_a_recipe)

if __name__ == "__main__":
    main()

# def recipe_api(recipe_id, recipe_name, url, calories):
#     key = os.environ.get('FOOD_KEY')

#     recipe = input('Search for a recipe: ')

#     params = {'query': recipe, 'addRecipeInformation': 'true', 'maxCalories': '800', 'minFat': '1', 'minProtein': '10', 'number': '1', 'apiKey': key }
#     url = 'https://api.spoonacular.com/recipes/complexSearch'
#     recipe_data = requests.get(url, params=params).json()
#     pprint(recipe_data) # Not required - developer data verification only.
#     return recipe_data


# def drink_api(drink_name, calories):
#     key = os.environ.get('DRINK_KEY') # TODO get actual key
    
#     drinks = input('Search for a drink: ')

#     params = {'query': drinks, 'addRecipeInformation': 'true', 'maxCalories': '800', 'minFat': '1', 'minProtein': '10', 'number': '1', 'apiKey': key }
#     url = 'https://api.spoonacular.com/recipes/complexSearch'
#     drink_data = requests.get(url, params=params).json()
#     pprint(drink_data) # Not required - developer data verification only.
#     return drink_data