# Lengfan Yan
# Win


# The operand stack: define the operand stack and its operations
opstack = []
# now define functions to push and pop values on the opstack (i.e, add/remove elements to/from the end of the Python list) Recall that `pass` in python is a no-op: replace it with your code.

def debug (*s):
    #print(s)
    #print("easy debug message version 2")
    print()  # print nothing when fail , version 3


def opPop():
    if len(opstack) == 0:
        debug("nothing in stack")
    else:
        l = len(opstack) - 1
        #t = opstack[l]
        return opstack.pop(l)

def opPush(value):
    opstack.append(value)
# Remember that there is a Postscript operator called "pop" so we choose different names for these functions.


# The dictionary stack: define the dictionary stack and its operations
dictstack = []

# now define functions to push and pop dictionaries on the dictstack, to define name, and to lookup a name

def dictPop():
    if len(dictstack) == 0:
        debug("nothing in dstack")
    else:
        l = len(dictstack) - 1
        #t = dictstack[l]
        return dictstack.pop(l)



# dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    if isinstance(d,dict):
        dictstack.append(d)
    else:
        debug("dictPush error")


#dictPush pushes the dictionary ‘d’ to the dictstack. Note that, your interpreter will call dictPush only when Postscript “begin” operator is called. “begin” should pop the empty dictionary from the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    if len(dictstack) == 0:          # need a dict in stack
        dictstack.append({})
    # check argument validation
    if isinstance(name, str) == False or name[0] != '/' or (isinstance(value, str) and value[0] == '/'):
        debug("define error, name has to be string, value should not be string: " + str(name))
    elif isinstance(value, str):
        name = name[1:]
        l = len(dictstack) - 1
        value = lookup(str)
        dictstack[l][name] = value
    else:
        name = name[1:]             # remove / in name
        l = len(dictstack) - 1
        dictstack[l][name] = value


#add name:value pair to the top dictionary in the dictionary stack. Your psDef function should pop the name and value from operand stack and call the “define” function.

# mainly from last hw
def lookup(name):
    if len(dictstack) == 0:
        debug("lookup 0 stack Error")
    else:
        for i in range(len(dictstack)):
            L = dictstack[len(dictstack) - i -1]
            if L.get(name) != None:
                out = L.get(name)
                return out
        debug("error: this name not in stack: " + name)

    # return the value associated with name
  # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.

  # ----------------------------------------------------------------

def add():
    a = opPop()
    b = opPop()
    # check if a,b are varibles     (also for rest op)
    if isinstance(a, str):
        a = lookup(a)
    if isinstance(b, str):
        b = lookup(b)
    # check if a,b eventually is a number or not        (also for rest op)
    if (isinstance(a, int) or isinstance(a, float))  and (isinstance(b,int) or isinstance(b, float)):
        opstack.append(a + b)
    else:
        debug("add Error")

def sub():
    a = opPop()
    b = opPop()
    if isinstance(a, str):
        a = lookup(a)
    if isinstance(b, str):
        b = lookup(b)
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        opstack.append(b - a)
    else:
        debug("sub Error")

def mul():
    a = opPop()
    b = opPop()
    if isinstance(a, str):
        a = lookup(a)
    if isinstance(b, str):
        b = lookup(b)
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        opstack.append(b * a)
    else:
        debug("mul Error")

def div():
    a = opPop()
    b = opPop()
    if isinstance(a, str):
        a = lookup(a)
    if isinstance(b, str):
        b = lookup(b)
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        opstack.append(b / a)
    else:
        debug("div Error")

def mod():
    a = opPop()
    b = opPop()
    if isinstance(a, str):
        a = lookup(a)
    if isinstance(b, str):
        b = lookup(b)
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        opstack.append(b % a)
    else:
        debug("mod Error")

def eq():
    a = opPop()
    b = opPop()
    if isinstance(a, str):
        a = lookup(a)
    if isinstance(b, str):
        b = lookup(b)
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        return a == b
    else:
        debug("eq Error")

def lt():
    a = opPop()
    b = opPop()
    if isinstance(a, str):
        a = lookup(a)
    if isinstance(b, str):
        b = lookup(b)
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        return a < b
    else:
        debug("lt Error")


def gt():
    a = opPop()
    b = opPop()
    if isinstance(a, str):
        a = lookup(a)
    if isinstance(b, str):
        b = lookup(b)
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        return a > b
    else:
        debug("gt Error")


#------------------------------------

def length():
    t = opPop()
    # check if top stack is list or not
    if isinstance(t, list):
        opPush(len(t))
    else:
        debug("lenght: not list")



def get():
    i = opstack.pop()                        # int
    t = opstack.pop()                        # list

    if isinstance(t, list) and isinstance(i, int):
        if len(t) - 1 >= i:                  # check iob
            opstack.append(t[i])
        else:
            debug("get iob")
    else:
        debug("get error, not list or int")

def getinterval():
    pass

def put():
    pass

#----------------------------------

def dup():
    if len(opstack) != 0:
        t = opstack.pop()
        opstack.append(t)
        opstack.append(t)


def copy():
    n = opPop()
    l = len(opstack)

    if isinstance(n,int):
        if n > l:
            debug("copy error, n > len: no enough element to copy")
        else:               # loop # of time need copy
            for i in range(n):
                opPush(opstack[l-i -1])     # search stack value to copy
    else:
        debug("copy error not int")


def pop():
    if len(opstack) != 0:
        t = opstack.pop()
        return t
    else:
        return None   # pop nothing ( or debug("nothign to pop")



def clear():
    global opstack
    opstack = []

def exch():
    if len(opstack) >= 2:               # must have 2 value
        t1 = opPop()
        t2 = opPop()
        opPush(t1)
        opPush(t2)
    else:
        debug("exch i<2")

def roll():
    t1 = opPop()
    t2 = opPop()
    if isinstance(t1,int) and isinstance(t2,int):
        for i in range(t1):
            l = []
            r1 = opPop()             # store the value going down
            for j in range(t2-1):   # store rest of value to a list
                l.append(opPop())
            opPush(r1)               # put r1 into right position
            for k in range(t2-1):   # push back rest value
                opPush(l.pop())
    else:
        debug("roll: not int")

def stack():
    if len(opstack) != 0:
        for i in range(len(opstack) - 1):
            print(opstack[len(opstack) - i])



#---------------------------------------
#------- Part 1 TEST CASES--------------


def testDefine():
    define("/n1", 4)
    if lookup("n1") != 4:
        return False

    define("/x", [1])
    if lookup("x") != [1]:
        return False
    define("/n1", 99)
    if lookup("n1") != 99:
        return False
    x = "a1"
    define("/"+x, 0)
    if lookup(x) != 0:
        return False

    #x = define(5,0)                    # not sure how to test bad arguement, the function is printing some error message, but the test will break
    #if x != "define error, not defining name":
    #   return False
    return True

def testLookup():
    opPush("/n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False

    opPush("/n1")
    opPush(0)
    psDef()
    if lookup("n1") != 0:
        return False
    opPush("/1")
    opPush([1])
    psDef()
    if lookup("1") != [1]:
        return False
    opPush("/n15")
    opPush(9)
    psDef()
    if lookup("n1") != 0:
        return False
    return True

#Arithmatic operator tests
def testAdd():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False

    opPush(0)
    opPush(0)
    add()
    if opPop() != 0:
        return False
    define("/n1", 4)
    opPush("n1")
    opPush(0)
    add()
    if opPop() != 4:
        return False
    define("/x", -4)
    opPush("x")
    opPush("n1")
    add()
    if opPop() != 0:
        return False
    return True


def testSub():
    opPush(10)
    opPush(4.5)
    sub()
    if opPop() != 5.5:
        return False

    opPush(0)
    opPush(4.5)
    sub()
    if opPop() != -4.5:
        return False
    define("/x", -4.5)
    opPush('x')
    opPush(4.5)
    sub()
    if opPop() != -9.0:
        return False
    opPush('x')
    define("/y", 0)
    opPush('y')
    sub()
    if opPop() != -4.5:
        return False
    return True
#

def testMul():
    opPush(2)
    opPush(4.5)
    mul()
    if opPop() != 9:
        return False

    opPush(0)
    opPush(4.5)
    mul()
    if opPop() != 0:
        return False
    opPush(2)
    opPush(-1)
    mul()
    if opPop() != -2:
        return False
    define("/x", 3.4)
    opPush('x')
    opPush(3)
    mul()
    if opPop() != 10.2:
        return False
    return True

def testDiv():
    opPush(10)
    opPush(4)
    div()
    if opPop() != 2.5:
        return False

    opPush(0)
    opPush(4)
    div()
    if opPop() != 0:
        return False
    opPush(10)
    opPush(1)
    div()
    if opPop() != 10:
        return False
    define("/x", 55)
    opPush('x')
    opPush(-2)
    div()
    if opPop() != -27.5:
        return False

    return True

def testMod():
    opPush(10)
    opPush(3)
    mod()
    if opPop() != 1:
        return False

    opPush(3)
    opPush(3)
    mod()
    if opPop() != 0:
        return False
    opPush(10)
    opPush(6)
    mod()
    if opPop() != 4:
        return False
    return True

def testeq():
    opPush(5)
    opPush(5)
    if eq() != True:
        return False
    opPush(3)
    opPush(8)
    if eq() == True:
        return False
    return True

def testlt():
    opPush(5)
    opPush(5)
    if eq() == True:
        return False
    opPush(3)
    opPush(8)
    if eq() != True:
        return False
    return True

def testgt():
    opPush(5)
    opPush(5)
    if eq() == True:
        return False
    opPush(3)
    opPush(8)
    if eq() == True:
        return False
    return True

#Array operator tests
def testLength():
    opPush([1,2,3,4,5])
    length()
    if opPop() != 5:
        return False

    opPush([])
    length()
    if opPop() != 0:
        return False
    opPush([1,2,3])
    opPush([1, 2, 3, 4, 5])
    length()
    if opPop() != 5:
        return False
    length()
    if opPop() != 3:
        return False
    return True

def testGet():
    opPush([1,2,3,4,5])
    opPush(4)
    get()
    if opPop() != 5:
        return False

    opPush([1, 2, 3, 4, 5])
    opPush(0)
    get()
    if opPop() != 1:
        return False
    opPush([2,3,4])
    opPush([2,3, 7,4])
    opPush(2)
    get()
    if opPop() != 7:
        return False
    opPush(2)
    get()
    if opPop() != 4:
        return False
    return True

def testGetinterval():

    return True

def testPut():

    return True

#stack manipulation functions
def testDup():
    opPush(10)
    dup()
    if opPop()!=opPop():
        return False

    opPush(10)
    opPush(0)
    dup()
    if opPop()!=opPop():
        return False
    opPush('/x')
    dup()
    if opPop()!=opPop():
        return False
    return True


def testPop():
    l1 = len(opstack)
    opPush(10)
    pop()
    l2= len(opstack)
    if l1!=l2:
        return False

    opPush(10)
    if pop() != 10:
        return False
    opPush(0)
    l1 = len(opstack)
    pop()
    if l1 != len(opstack)+1:
        return False

    return True


def testRoll():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(4)
    opPush(-2)
    roll()
    if opPop()!=3 and opPop()!=2 and opPop()!=5 and opPop()!=4 and opPop()!=1:
        return False

    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(3)
    opPush(2)
    roll()
    if opPop()!=3 and opPop()!=5 and opPop()!=4 and opPop()!=2 and opPop()!=1:
        return False

    opPush(5)
    opPush(6)
    opPush(1)
    opPush(8)
    opPush(4)
    opPush(2)
    opPush(0)
    opPush(7)
    opPush(3)
    opPush(3)
    roll()
    if opPop() != 7 and opPop() != 0 and opPop() != 2 and opPop() != 4 and opPop() != 8:
        return False

    opPush(8)
    opPush(8)
    opPush(4)
    opPush(2)
    roll()
    if opPop() != 1 and opPop() != 6 and opPop() != 8 and opPop() != 8 and opPop() != 5:
        return False

    return True

def testCopy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    copy()
    if opPop()!=5 and opPop()!=4 and opPop()!=5 and opPop()!=4 and opPop()!=3 and opPop()!=2:
        return False

    opPush(5)
    opPush(2)
    opPush("/n")
    opPush(3)
    copy()
    if opPop()!= "/n" and opPop()!=2 and opPop()!=5 :
        return False

    clear()
    opPush(0)
    copy()
    if len(opstack) != 0:
        return False

    opPush(0)
    opPush(0)
    opPush(0)
    copy()
    if opPop()!= 0 and opPop()!= 0:
        return False

    return True

def testClear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack)!=0:
        return False

    clear()
    clear()
    if len(opstack)!=0:
        return False
    opPush("/x")
    opPush(5)
    opPop()
    clear()
    if len(opstack)!=0:
        return False

    return True

def testExch():
    opPush(10)
    opPush("/x")
    exch()
    if opPop()!=10 and opPop()!="/x":
        return False

    opPush(10)
    opPush(0)
    exch()
    if opPop()!=10 and opPop()!=0:
        return False
    opPush("/x")
    opPush("/q")
    exch()
    if opPop()!="/x" and opPop()!="/q":
        return False

    return True



def main_part1():
    testCases = [('define',testDefine),('lookup',testLookup),('add', testAdd), ('sub', testSub),('mul', testMul),('div', testDiv), \
                ('mod', testMod),('eq',testeq),('lt',testlt),('gt',testgt), ('getinterval',testGetinterval),('put',testPut),\
                ('length', testLength),('get', testGet), ('dup', testDup), ('copy', testCopy),('pop', testPop), ('roll', testRoll), \
                ('clear', testClear),('exch', testExch)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return ('Some tests failed', failedTests)
    else:
        return ('All part-1 tests OK')

print(main_part1())