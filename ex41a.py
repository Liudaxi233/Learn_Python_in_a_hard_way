import random  # 随机产生浮点数/整数/字符串等
from urllib.request import urlopen  # urlopen 打开网址
import sys

WORD_URL = "http://learnpythonthehardway.org/words.txt"
Words = []
# 他们想要翻译短语吗？
if len(sys.argv) == 2 and sys.argv[1] == "english":       # '''判断argv参数是否是2个且第二个参数是english，如果是则为真，不是则为假'''
    Phrase_first = True
else:
    Phrase_first = False


# 加载网站的文字
for word in urlopen(WORD_URL).readlines():                #'''打开网址，读取网址的所有行，每一行为一个元素，以列表的形式保存，读取列表中的所有元素（也就是单词）'''
    Words.append(str(word.strip(), encoding="utf-8"))     # '''去除单词的首尾空格或换行符，以utf-8编码，以字符串的类型添加到列表追加给Words里面'''


Phrases = {                                               #Phrase →字典类型
    "class %%%(%%%):":                                     #"""创建一个叫%%%的类，并继承%%%。"""
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(slef,***)":        #"""类%%%有一个__init__方法，该方法有self和***两个参数。"""
        "class %%% has-a __init__that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self,@@@)":
        "class %%% hass-a function  *** that takes self and @@@ params.",  #"""类%%%有一个叫***的函数，该函数有self和@@@两个参数。"""
    "***==%%%%()":
        "Set *** to an instance of class %%%。",
    "***.***(@@@)":
        "From *** get the *** function,call it with params self,@@@.",
    "***.***='***'":
        "From *** get the *** attribute and set it to '***."
}


def convert(section, phrase):
    class_names = [w.capitalize() for w in                      #capitalize()将字符串的第一个字母变成大写,其他字母变小写
                   random.sample(Words, section.count("%%%"))]  # '''先统计snippet中‘%%%’出现的次数n，再随机返回WORDS中n个元素'''
    other_names = random.sample(Words, section.count("***"))
    print("1#-----------------------\n class_names and others names")
    print(class_names)
    print(other_names)
    results = []
    param_names = []



    for i in range(0, section.count("@@@")):
        param_count = random.randint(1, 3)               #random.randint()随机生一个整数int类型，可以指定这个整数的范围，同样有上限和下限值
        param_names.append('-'.join(random.sample(Words, param_count)))    #.join()将序列中的元素以指定的字符连接生成一个新的字符串。
        print("2#-----------------------\n param_names and param_count")
        print(param_count)
        print(param_names)
    # 用下划线连接随机的WORDS单词追加给param_names
    for sentence in section, phrase:
        result = sentence[:]
        print("2.0#-----------------------\n")
        print(result)#python中复制列表的方法


        for word in class_names:
            result = result.replace("%%%", word, 1)   # replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
            print("2.1#-----------------------\n")
            print(word)
            print(result)

        for word in other_names:
            result = result.replace("***", word, 1)
            print("2.2#-----------------------\n")
            print(word)
            print(result)

            # 假冒参数列表
        for word in param_names:
            result = result.replace("@@@", word, 1)
            print("2.3#-----------------------\n")
            print(word)
            print(result)

        results.append(result)

    return results
    print(result)


# 执行到ctrl-D

try:
    while True:
        sections = list(Phrases.keys())    #`Python 字典(D`ictionary) keys() 函数以列表返回一个字典所有的键
        random.shuffle(sections)            #random.shuffle()如果你想将一个序列中的元素，随机打乱的话可以用这个函数方法

        for section in sections:
            phrase = Phrases[section]
            question, answer = convert(section, phrase)
            if Phrase_first:
                question, answer = answer, question

                print("3#-----------------------\n section,phrase,question")
                print(section)
                print(phrase)
                print(question)

                input(">")
                print(f'Answer:{answer}\n\n')
except EOFError:   """#eof 是end of file的缩写,“eof” 表示到文件末尾了，所以eoferror表示它发现了一个不期望的文件尾。"""
print("\nBye")
