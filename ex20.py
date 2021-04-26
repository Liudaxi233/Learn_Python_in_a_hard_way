from sys import argv

script, input_file = argv

def print_all(f): # 读取文件
    print(f.read())

def rewind(f): # move back to the start of file
    f.seek(0)

def print_a_line(line_count, f): #a print function
    print(line_count, f.readline()) # print the no. of line and text

current_file = open(input_file) # open the file

print("First let's print the whole file:\n")

print_all(current_file)   #print thr whole text

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line =1
print(f"it's first time {current_line}")
print_a_line(current_line, current_file)
print(f"it's 2 time {current_line}")
current_line +=1
print(f"it's 3 time {current_line}")
print_a_line(current_line, current_file)
print(f"it's 4 time {current_line}")
current_line +=1
print(f"it's 5 time {current_line}")
print_a_line(current_line, current_file)
print(f"it's 6 time {current_line}")
# try study drills 4     2.16.2021