#!/usr/bin/python

import sys

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