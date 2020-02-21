#!/usr/bin/python

import math

def recipe_batches(recipe: dict, ingredients: dict) -> int:
	''' Calculate how many of a given recipe can be formed from some ingredients. '''
	min = math.inf
	for k, v in recipe.items():
		try:
			possible_batches = ingredients[k] // recipe[k]
		# if we are missing an ingredient, we can't make the recipe
		except KeyError:
			return 0
		if possible_batches < min:
			min = possible_batches
	return min


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))