import threading


class aSimpleClass:

    ''' A simple class to play with classes.
    '''

    classMethodCounter = 0
    classInstanceCounter = 0

    def __init__(self, someInfo):
        aSimpleClass.classInstanceCounter += 1
        self.someInfo = someInfo

    def aMethod(self):
        print("Doing a simple method {} {}".format(self.classInstanceCounter, self.someInfo))

    @classmethod
    def aClassMethod(cls):
        cls.classMethodCounter += 1
        print("Class method {}".format(cls.classMethodCounter))

    @staticmethod
    def aStaticMethod():
        print("Doing a statis method... woo hoo")



class doStuff(threading.Thread):

    def run(self):
        learn_sets()

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

    myList = ['a', 'b', 'c', 'g', 'f']

    print(myList)
    myList.sort()
    print(myList)

    myList2 = ['x','y','z']

    myList.extend(myList2)
    print(myList)

    # for thing in myList:
    #     print(thing)

    for indx, thing in enumerate(myList):
        print(indx, thing)

    print(', '.join(myList))

    print('b' in myList)

def learn_sets():
    s1 = {1,2,3,4,5,6,7}
    print(s1)
    s1.add(4)
    s1.add(8)
    print(s1)

    s2 = {4,8,16,32}
    print(s1.intersection(s2))
    print(s1.difference(s2))
    print(s1.union(s2))
    
def learn_dictionaries():
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


def play_with_strings():
    lst = ['something', 222]
    print(f"{lst[0]} then {lst[1]}")

if __name__ == '__main__':

    # learn_dictionaries()
    # learn_sets()
    # learn_lists()
    play_with_strings()

    # stuff = doStuff()
    # stuff.start()
    # print("Main thread doing stuff")
    # stuff.join()


    # aCls = aSimpleClass("Blah Blah")
    # aCls.aMethod()
    # aCls.aClassMethod()
    # aSimpleClass.aClassMethod()
    # aCls.aClassMethod()
    # aCls.aStaticMethod()
    # print(aSimpleClass.__dict__)
    # print(aCls.__dict__)

    print("Done!")