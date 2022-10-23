def lucky_number(name):
  number = len(name) * 9
  a = "Hello " + name + ". Your lucky number is " + str(number)
  return a
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
