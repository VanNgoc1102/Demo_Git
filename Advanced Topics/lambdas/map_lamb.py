# Python code to illustrate
# map() with lambda()
# to get double of a list.

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
even = lambda x: x*2
final_list = list(map(even, li))

print(final_list)
# [5, 7, 97, 77, 23, 73, 61]

animals = ['dog', 'cat', 'parrot', 'rabbit']
 
# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal: animal.upper(), animals))
 
print(uppered_animals)

# ['DOG', 'CAT', 'PARROT', 'RABBIT']