# Write code for algorithm 4 below
# 4. Write a function that calculates the value of 'a' to the power of 'b'.

def aMulb(a,b):
  if b < 1:
    print("invalid input")
  elif b == 1:
    return a
  else:
    return a * aMulb(a,b-1)
    
print(aMulb(2,4)) 