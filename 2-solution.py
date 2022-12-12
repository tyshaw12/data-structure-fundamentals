
# FIRST SOLUTION
# First set definition
first_set = {1,2,3,4,5,6,7}

# Second set definition
second_set = {5,6,7,8,9,10}

# DO NOT MODIFY CODE ABOVE THIS LINE

# Write your code below

second_set.remove(5)
second_set.remove(6)
second_set.remove(7)


# Printing intersection
print(first_set.intersection(second_set))





# SECOND SOLUTION
# First set definition
first_set = {1,2,3,4,5,6,7}

# Second set definition
second_set = {5,6,7,8,9,10}

# DO NOT MODIFY CODE ABOVE THIS LINE

# Write your code below

second_set.add(1)
second_set.add(2)
second_set.add(3)
second_set.add(4)



# Printing intersection
print(first_set.difference(second_set))