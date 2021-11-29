num = [1,2,3,4,5,6,7,8,9,10]
print( "Original list:",num)
num = [x for x in num if x%2!=0]
print("List after removing even numbers:",num)
