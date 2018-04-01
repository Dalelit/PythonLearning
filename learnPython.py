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

def args_test_decorator(func):
    def wrap(*args):
        print(args)
        if args[0] != 1:
            print("First arg needs to be of value 1")
            return None
        else:
            print("First arg is 1")
            return func(*args)
    return wrap

@args_test_decorator
def args_test_func(num):
    print('We can assume the arg has been check to be 1')
    return num + num

def learn_decorators():
    print(f'--> {args_test_func(0)}')
    print(f'--> {args_test_func(1)}')
    print(f'--> {args_test_func(2)}')

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

def learn_args(*args, **kwargs):
    print(args)
    print(kwargs)

def play_with_args():
    learn_args()
    learn_args(1)
    learn_args(2,'asd', bob='jane')
    learn_args(bill='will')

    lst = ['asd',23,2.3]
    dic = {'name':'bob', 'age':34}
    learn_args(*lst, **dic)
    
def a_generator(lst_of_nums):
    for n in lst_of_nums:
        yield n+1

def play_with_generators():
    a_list = [1,2,3,4,5,6]

    for a in a_generator(a_list):
        print(a)

    a_gen = (n*n for n in a_list)
    for b in a_gen:
        print(b)

def learn_list_comprehension():
    a_list = [1,2,3,4,5,6,7,8,9,10,11,12]

    a_new_list = [n*n for n in a_list]
    print(a_new_list)

    print([n for n in a_list if n%2 == 0])

    def numTest(num, divi):
        return num % divi == 0

    print([n for n in a_list if numTest(n,3)])

    print([(a,b) for a in 'qwerty' for b in range(3,6)])

    another_list = ['a','b','c','d']
    a_dic = {name: val for val, name in zip(a_list, another_list) if val != 2}
    print(a_dic)
    
    # set example
    print({n for n in [1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1]})

if __name__ == '__main__':

    # learn_dictionaries()
    # learn_sets()
    # learn_lists()
    # play_with_strings()
    # play_with_args()
    # play_with_generators()
    # learn_list_comprehension()
    learn_decorators()

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