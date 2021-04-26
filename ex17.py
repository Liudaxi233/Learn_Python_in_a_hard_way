from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")


in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)} ")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file =open(to_file,'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()#怀疑不会保存 但是并未在vs code里发现
# 确认 内容会写入到 to_file 的内存数据中，但仍未写入硬盘
'''
那么为什么在 精简练习、极限精简练习 中不需要关闭呢？
我的理解：
关键点在于没有使用变量，也就是没有个打开的文件起名字。
这个时候，任何操作是一次性的，我们没办法在写入了一些东西后再说“喂，就你，你再写入这些内容”，python 不知道这句‘喂’说的是哪一个内存堆栈中的数据。
所有没有其名的代码都是一次性的，不会保存在内存中，针对 open 来说，python 就自动关闭它了 
'''
in_file.close()