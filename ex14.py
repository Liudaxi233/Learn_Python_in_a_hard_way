from sys import argv

script, user_name, first, second = argv
prompt = '>'
flash = '0.0'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me{user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.   
You live in {lives}.  Not sure where that is.   
And you have a {computer} computer.  Nice.
""")
print(f"""
It's a test, the {first} test and the {second} test.
""")

first = input(flash)
print("****") #并未执行此行

#在终端输入python user_name
#注意 只输出了一次0.0