#!/usr/bin/python

import argparse

def find_max_profit(prices):
	min_index = 0
  # we cannot buy and sell the same stock, so default max profit is the second item - the first item
	max_profit = (prices[1] - prices[0])
	for i in range(len(prices)):
		# check for a new minimum buy price, excluding the last as we cannot buy the last item
		if prices[i] < prices[min_index] and i != len(prices) - 1:
			min_index = i
		# check that each buy/sell represents and increase in profit, and that we are not buying and selling the same stock
		if prices[i] - prices[min_index] > max_profit and i != min_index:
			max_profit = prices[i] - prices[min_index]
	return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))