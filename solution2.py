# Write code for algorithm 2 below
# Write a function that prints the natural numbers from 1 to n.

#def natural_numbers(x,i):
	#your code here
#natural_numbers(3)
#output: 1 2 3

def natural_numbers(x,i=1):
	#base case
  if i > x:
    return
  #recursive case
  else:
    print(i)
    natural_numbers(x,i+1)
natural_numbers(5)
