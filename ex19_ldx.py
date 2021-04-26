def in_ten_ways(a, b):
    print(f"you got {a} pens")
    print(f"and {b} books")
    print("end")

def compare(first, second):
    if (a9 == new_6a & b9 == new_6b):
        print(f"your input {first} and {second} are correct")
    if (a9 != new_6a):
        print(f"your input {first} is incorrect")
    if (b9 != new_6b):
        print(f"your input {second} is incorrect")


print("just assign the numbers")   #1
in_ten_ways(1,2)


print(" in sprint")    #2
number_a = 3
number_b = 4

in_ten_ways(number_a, number_b)


print("do a caulate in sprint")  #3
in_ten_ways(5+5, 6+6)


print("do a caulate with number_a and number_b") #4
in_ten_ways(number_a+1, number_b+2)


print("do a switch") #5
backup_a = number_a
number_a = number_b
number_b = backup_a
in_ten_ways(number_a, number_b)


print("plz input 2 numbers") #6
print("plz input new a ")
new_6a = int(input())
print("plz input new b ")
new_6b = int(input())
in_ten_ways(new_6a,new_6b)


print("plus 1 with 6a and 6b") #7   
in_ten_ways(new_6a + 1, new_6b + 1)


print("guess input") #8
print("you answers: ")
print("input a u guess")
a8 =int(input()) 
print("input b u guess")
b8 = int(input()) 
if( a8 == new_6a):
    print("a is correct")
else:
    print("a is incorrect")
if (b8 == new_6b):
    print("b is correct")
else:
    print("b is incorrect")


print("guess input") #9
print("you answers: ")
print("input a u guess")
a9 =int(input()) 
print("input b u guess")
b9 = int(input())

compare(a9, b9)




