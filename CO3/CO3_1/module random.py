import random
mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))        #Returns a random element from the given sequence

print(random.choices(mylist, k=2)) 

print(random.sample(mylist, k=2))   #Return a list that contains any 2 of the items from a list:

random.shuffle(mylist)

print(mylist)                   #Takes a sequence and returns the sequence in a random order

print(random.randrange(3, 9))      #Return a number between 3 and 9: