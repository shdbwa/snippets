#from https://www.w3schools.com/python/python_for_loops.asp

# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  
# Loop through the letters in the word "banana":
for x in "banana":
print(x)


# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Loop through a set of code a specified number of times    
for x in range(6):
  print(x)    

# Idem, where "x" as starting value, "y" the end, and "z" the increment/step size
for x in range(x, y, z):
  print(x)
  
  
# Print all numbers from 0 to 5, and print a message when the loop has ended (if not stopped by a break statement ) stopped by a break statement:  
for x in range(6):
  print(x)
else:
  print("Finally finished!")  

  
# Parallel
# create a process pool that uses all cpus
with multiprocessing.Pool() as pool:
	# prepare arguments for reach call to target function
	items = [(1,2), (3,4), (5,6)]
	# call the function for each item in parallel with multiple arguments
	for result in pool.starmap(task, items):
		print(result)
    
    
