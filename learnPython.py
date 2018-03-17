import threading

class doStuff(threading.Thread):

    def run(self):
        learn_sets_and_dictionaries()

def my_first_decorator(func):
    def wrap():
        print("calling " + str(func))
        func()
        print("called func")
    return wrap

@my_first_decorator
def learn_lists():

    l1 = [1,2,3,4]
    print(l1)

    l2 = list(range(5,10))
    print(l2)
    l3 = [x**2 for x in l2]
    print(l3)
    l4 = list(map(lambda x: x+1, l3))
    print(l4)

def learn_sets_and_dictionaries():
    s1 = {1,2,3,4,5,6,7}
    print(s1)
    s1.add(4)
    s1.add(8)
    print(s1)

    d1 = dict(dale=1, dana=2, lynn=3, abby=4)
    print(d1)
    d2 = {'a':3, 'b':7, 'c':4}
    print(d2)
    print(d2['c'])

    for k,v in d1.items():
        # print(("key {}, value {}").format(k,v))
        print(k,v)

    print("-"*20)

    print(dict(zip(d1,d2)))

    print("-"*20)
    for i,k in enumerate(d2):
        print(("index {}, value {}").format(i,v))

def abbys_first_function():
    print("Hello world. Abby and Dale are the best!")

if __name__ == '__main__':
    # learn_sets_and_dictionaries()
    # learn_lists()

    # stuff = doStuff()
    # stuff.start()
    # print("Main thread doing stuff")
    # stuff.join()

    for i in range(0,8):
        abbys_first_function()

    