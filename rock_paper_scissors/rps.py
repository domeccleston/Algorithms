#!/usr/bin/python

import sys


# Recursive structure of the problem: 

""" 
For a number n, and an array of options of length m, construct an array of length m ^ n
formed of all the possible order permutations of those options in subarrays of length n.

Options will always be ['rock', 'paper', 'scissors'] so m will have a constant value of 3.

Use a helper function generate which takes an input array and n. This input array will build
up our permutations and will be passed through multiple recursive calls to generate. When
n == 0, append our input array to the possibilities array and return this.

Call our helper function with an empty array and n.

If n is equal to 0, this is our base case. Write our input array to our possibilities array.

If n is greater than 0, loop through our possibilities and call generate once for each option,
passing in that option and our current input array of permutations. For n == 2, this will result in a call stack of 
length 13: 
          initial call to rock_paper_scissors(2)
            1 call to generate([input], 2)
              3 calls to generate([input], 1)
                9 calls to generate([input], 0)

  The order of the function calls will be as follows:

  rock_paper_scissors(2) ->
   generate([], 2) -> # n > 1, so start looping and calling generate() for each option
    generate(['rock'], 1) -> # n is still bigger than 1, so start looping again, appending each option to our current input
      generate(['rock'], ['rock'], 0) -> 
      generate(['rock'], ['paper'], 0) ->
      generate(['rock'], ['scissors'], 0) ->
    generate(['paper'], 1) -> 
      generate(['paper'], ['rock'], 0) -> 
      generate(['paper'], ['paper'], 0) ->
      generate(['paper'], ['scissors'], 0) ->
`   generate(['scissors'], 1) -> 
      generate(['scissors'], ['rock'], 0) -> 
      generate(['scissors'], ['paper'], 0) ->
      generate(['scissors'], ['scissors'], 0) ->`

"""


def rock_paper_scissors(n):
	options = ['rock', 'paper', 'scissors']
	possibilities = []

	def generate(input, n):
		if n == 0:
			possibilities.append(input)
		else:
			for i in options:
				generate(input + [i], n - 1)

	generate([], n)
	return possibilities

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')