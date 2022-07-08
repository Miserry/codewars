n = int(input())
##fb = []
##for z in range(1, n+1):
##    if z % 15 == 0:
##        fb.append("FizzBuzz")
##    elif z % 3 == 0:
##        fb.append("Fizz")
##    elif z % 5 == 0:
##        fb.append("Buzz")
##    else:
##        fb.append(str(z))
##print(fb)

print([ "Fizz"*(z%3 == 0) + "Buzz"*(z%5 == 0) or str(z) for z in range(1,n+1)])
