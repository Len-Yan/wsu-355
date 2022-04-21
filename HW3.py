

# 1
def busStops(b):
    ans = {}
    for bus in b:
        stopl = b.get(bus, None)
        for stop in stopl:
            if ans.get(stop, None) == None:
                ans[stop] = [bus]
            else:
                stopl2 = ans[stop]
                stopl2.append(bus)
                stopl2.sort()
    return ans



# 2a)
def addDict(d):
    a = {}
    for x in d:
        for c in d.get(x):              # loop and find date information
            if a.get(c) == None:        # add hour infor to new dict
                a[c] = d.get(x).get(c)
            else:
                a[c] += d.get(x).get(c)
    #print(a)
    return a

# 2b
def addDictN(L):                        # same idea to part a
    a = {}
    for week in L:
        t = addDict(week)
        for c in t:
            if a.get(c) == None:
                a[c] = t.get(c)
            else:
                a[c] += t.get(c)
    return a



# 3a
def searchDicts(L,k):
    L.reverse()             # reverse it for backorder

    for l in L:
        if l.get(k) != None:
            out = l.get(k)
            L.reverse()     # reverse L back to original List
            return out
    L.reverse()             # reverse L back to original List
    return None

# 3b
def searchDicts2(L2, k):
    return search(L2,k, len(L2)-1)

def search(L2, k, i):
    if L2[i][1].get(k) != None:
        #print(L2[i][1].get(k))     #show return value
        return L2[i][1].get(k)
    else:
        index = L2[i][0]
        if i == 0 and index == 0:   # find where to end search
            return None
        return search(L2, k, index)



# 4
def subsets(L):
    l = len(L)
    ans = []

    for i in range(0, (1 << l)):
        subset = []
        for j in range(0, l):
            if ((i & (1 << j)) > 0):
                subset.append(L[j])     #new subset to list
                ans.append(subset)
    t = set(map(tuple, ans))
    ans = list(map(list, t))
    ans.sort(key=len)
    ans.insert(0,[])
    return ans



# 5
def numPaths(m, n):
    if m == 0 or n == 0:            #check if input has path
        return 0
    return pathmath(m+n-2)/(pathmath(m-1) * pathmath(n-1))


def pathmath(x):
    a = 1;
    for i in range(0,x):
        a *= a*i
    return a

def path(m,n, cm, cn):
    if(m == cm or n == cn):         # found path if current_m,n #  reach m,n
        return 1
    return path(m,n,cm +1, cn) + path(m,n,cm, cn+1) # add path



# 6a
class iterPrimes():
    def __init__(self):
        self.current = 2

    def __next__(self):
        result = self.current
        self.trace = result
        self.current = self.findp()
        return result

    def traceback(self):        # only for part b
        for x in range(self.current-1, (int)(self.current / 2), -1):
            for y in range(2, x):
                if x % y == 0:
                    break
            else:
                self.current = x
                return
        return None

    def __iter__(self):
        return self

    def findp(self):
        for x in range(self.current +1, self.current * 2):
            for y in range(2,x):
                if x % y ==0:
                    break
            else:
                return x
        return None

# 6b
def numbersToSum(iNumbers, sum):
    #s = iNumbers
    l = []
    mysum = 0

    while(True):
        t = iNumbers.__next__()
        if mysum + t < sum:
            l.append(t)
            mysum += t
        else:               # traceback last number for next call
            iNumbers.traceback()
            break
    return l



#====================================================================

# 1
def testbusStops():
    buses = {
        "Lentil": ["Chinook", "Orchard", "Valley", "Emerald", "Providence", "Stadium", "Main", "Arbor", "Sunnyside",
                   "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"],
        "Wheat": ["Chinook", "Orchard", "Valley", "Maple", "Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop",
                  "Walmart", "PorchLight", "Campus"],
        "Silver": ["TransferStation", "PorchLight", "Stadium", "Bishop", "Walmart", "Shopco", "RockeyWay"],
        "Blue": ["TransferStation", "State", "Larry", "TerreView", "Grand", "TacoBell", "Chinook", "Library"],
        "Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside", "Crestview", "CityHall", "Stadium", "Colorado"]
    }
    returns = {'Chinook': ['Blue', 'Lentil', 'Wheat'], 'Orchard': ['Lentil',
    'Wheat'], 'Valley': ['Lentil', 'Wheat'], 'Emerald': ['Lentil'],
    'Providence': ['Lentil'], 'Stadium': ['Gray', 'Lentil', 'Silver'],
    'Main': ['Gray', 'Lentil'], 'Arbor': ['Lentil'], 'Sunnyside': ['Gray',
    'Lentil'], 'Fountain': ['Lentil'], 'Crestview': ['Gray', 'Lentil'],
    'Wheatland': ['Lentil'], 'Walmart': ['Lentil', 'Silver', 'Wheat'],
    'Bishop': ['Lentil', 'Silver', 'Wheat'], 'Derby': ['Lentil'], 'Dilke':
    ['Lentil'], 'Maple': ['Wheat'], 'Aspen': ['Wheat'], 'TerreView':
    ['Blue', 'Wheat'], 'Clay': ['Wheat'], 'Dismores': ['Wheat'], 'Martin':
    ['Wheat'], 'PorchLight': ['Silver', 'Wheat'], 'Campus': ['Wheat'],
    'TransferStation': ['Blue', 'Gray', 'Silver'], 'Shopco': ['Silver'],
    'RockeyWay': ['Silver'], 'State': ['Blue'], 'Larry': ['Blue'], 'Grand':
    ['Blue'], 'TacoBell': ['Blue'], 'Library': ['Blue'], 'Wawawai':
    ['Gray'], 'CityHall': ['Gray'], 'Colorado': ['Gray']}

    if busStops(buses) != returns:
        return False
    return True


# 2
def testaddDict():
    d = {'Mon':{'355':2,'451':1,'360':2},'Tue':{'451':2,'360':3}, 'Thu':{'355':3,'451':2,'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1,'451':3,'360':1}}
    d1 = {'Tue':{'360':0},'Wed':{'355':0},'Fri':{'360':0, '355':0}}
    d2 = {}
    if addDict(d) != {'355': 8, '360': 9, '451': 8}:
        return False
    if addDict(d1) !=  {'360': 0, '355': 0}:
        return False
    if addDict(d2) !=  {}:
        return False
    return True

def testaddDictN():
    d = [{'Mon':{'355':2,'360':2},'Tue':{'451':2,'360':3},'Thu':{'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1}},
{'Tue':{'360':2},'Wed':{'355':2},'Fri':{'360':3, '355':1}},
{'Mon':{'360':5},'Wed':{'451':4},'Thu':{'355':3},'Fri':{'360':6}, 'Sun':{'355':5}}]
    d2 = [{'Tue':{'360':0},'Wed':{'355':0},'Fri':{'360':0, '355':0}},
    {'Mon': {'360': 24}, 'Wed': {'451': 1}, 'Thu': {'355': 3}, 'Sun': {'360': 5}}]
    d3 = [{'Mon':{},'Sun':{}}]
    if addDictN(d) != {'355': 16, '360': 24, '451': 6}:
        return False
    if addDictN(d2) !=  {'360': 29, '355': 3, '451': 1}:
        return False
    if addDictN(d3) !=  {}:
        return False
    return True


# 3
def testsearchDicts():
    L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
    L2 = [{}]
    L3 = [{'1': 0, '/': 5}]
    if searchDicts(L1,"x") != 2:
        return False
    if searchDicts(L1,"z") != "found":
        return False
    if searchDicts(L1,"t") != None:
        return False
    if searchDicts(L2,"x") != None:
        return False
    if searchDicts(L3,"/") != 5:
        return False
    return True


def testsearchDicts2():
    L1 = [(0,{"x":0,"y":True,"z":"zero"}),
(0,{"x":1}),
(1,{"y":False}),
(1,{"x":3, "z":"three"}),
(2,{})]
    L2 = [(0,{})]
    L3 = [(0,{}),(1,{'x': 4}),(1,{}),(2,{}),(3,{3:0}),(3,{3:"?"})]
    if searchDicts2(L1, "x") != 1:
        return False
    if searchDicts2(L1, "z") != "zero":
        return False
    if searchDicts2(L1, "t") != None:
        return False
    if searchDicts2(L2, "x") != None:
        return False
    if searchDicts2(L3, 3) != '?':
        return False
    return True


# 4
def testsubsets():
    s1 = [1,2]

    if subsets([1,2,3]) != [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]:
        return False
    if subsets([(1,"one"),(2,"two")]) != [[], [(1, "one")], [(2, "two")], [(1, "one"), (2, "two")]]:
        return False
    if subsets([]) != [[]]:
        return False
    if subsets(s1) != [[],[1],[2],[1,2]]:
        return False
    if subsets([9]) != [[],[9]]:
        return False
    return True


# 5
def testnumPaths():
    if numPaths(2,2) != 2:
        return False
    if numPaths(3,3) != 6:
        return False
    if numPaths(4,5) != 35:
        return False
    if numPaths(1,2) != 1:
        return False
    if numPaths(4,3) != 10:
        return False
    if numPaths(5,0) != 0:
        return False
    return True


import sys as sys


# 6
def testiterPrimes():
    s = iterPrimes()
    if s.__next__() != 2:
        return False
    if s.__next__() != 3:
        return False
    if s.__next__() != 5:
        return False
    return True


def testnumbersToSum():
    s = iterPrimes()
    if numbersToSum(s, 58) != [2, 3, 5, 7, 11, 13]:
        return False
    if numbersToSum(s, 100) != [17, 19, 23, 29]:
        return False
    if numbersToSum(s, 50) != [31]:
        return False
    if numbersToSum(s, 100) != [37, 41]:
        return False
    if numbersToSum(s, 11) != []:
        return False
    return True



# =====================================
# =====================================

if __name__ == '__main__':
    passedMsg = "%s passed"
    failedMsg = "%s failed"
    l = [testbusStops, testaddDict(),testaddDictN(),testsearchDicts(),testsearchDicts2(),testsubsets(),
         testnumPaths(),testiterPrimes(),testnumbersToSum()]
    l2 = ['testaddDict ','testaddDictN ','testcharCount ','testcharCount2 ','testlookupVal ','testlookupVal2 ','testfunRun ',
         'testnumPaths ','testiterSquares ','testnumbersToSum ','teststreamSquares ','testevenStream ']
    i = 0
    for f in l:

        if f:
            print ( passedMsg % l2[i] )
        else:
            print ( failedMsg % l2[i] )
        i += 1

