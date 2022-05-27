# def add(n1,n2):
# 	print(n1+n2)

# num1 = 10
# num2 = input('Please provide a number : ')

# try:
# 	# want to attenpt this code
# 	# may have an error
# 	# add(num1,num2)

# 	result = add(10,20)

# except:
# 	print("Hey it looks like you aren't adding correctly!")

# else:					  		# only execute if there is no error
# 	print("Add went well!")
# 	print(result)

# finally: 						# always execute 
# 	print("I always run")

#############################################

# try:
# 	f = open('testfile','r')
# 	f.write("Write a test line")

# except TypeError:
# 	print("There is a type error!")

# except OSError:
# 	print("Hey you have an OS error!")

# except:
# 	print("All other exception")

# finally: 						# always execute 
# 	print("I always run")

####################################################

def ask_for_int():

	while True:
		try:
			result = int(input("Please provide number : "))
		except:
			print("Whoops! That is not a number")
			continue
		else:
			print("Yes thank you")
			break
		finally:
			print("End of try/except/finally")
			print("I will always run at the end!")

ask_for_int()