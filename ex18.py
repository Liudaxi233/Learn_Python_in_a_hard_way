def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1},arg2: {arg2}" )
# *args is pointless
def print_two_again(arg1,arg2):
    print(f"arg1: {arg1},arg2: {arg2}" )
#print_two_again 比 print_two 好
def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing!")

print_two("zed", "shaw")    
print_two_again("Zed","Shaw")    
print_one("First!")    
print_none()