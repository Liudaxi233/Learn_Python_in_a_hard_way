from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())

#为什么我们两次打开文件都没有错误？
#Python不会限制您多次打开文件，有时这是必要的。