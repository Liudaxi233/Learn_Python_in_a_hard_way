people = 30
cars = 40
trucks = 15


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide")


if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks")
else:
    print("We still can't decide.")


if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")


if cars > people or trucks < cars: #多个elif触发为真，用第一个
    print("test one")
elif cars > people or trucks> cars:
    print("test two")
elif cars < people or trucks < cars:
    print("Three")
elif cars < people or trucks > cars:
    print("four")
else:
    print("five")