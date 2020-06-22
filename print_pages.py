import sys

#calculating double pages
#returns array of tuples which consist of pair of pages
def calculateDouble(a, b):
    p = []
    for x in range(a, b, 4):
        p.append((x, x + 1))
        if x + 4 == stop:
            p.append((x + 4, None))
    
    return p

#calculating single pages
#returns array of pages
def calculateSingle(a, b):
    p = []
    for x in range(a, b, 2):
        p.append(x)
        if x + 2 == stop:
            p.append(x + 2)
    
    return p

#checking parameters correctness
def checkParams():
    params = len(sys.argv)
    correct = True
    
    if params == 3:
        print("no mode specified!")
        correct = False
    elif params >= 1 and params < 3:
        print("no range specified!")
        correct = False
    elif params == 4:
        s = int(sys.argv[3])
        if s != 1 and s != 2:
            print("incorrect mode! you need to choose single page mode - 1, or double page - 2")
            correct = False
    
    if correct is False:
        sys.exit(0)

#displaying results, both directions        
def display(even, odd, switch):
    print("\nonwards:")

    if switch == 1:
        for p in even:
            print(p, end=', ')

        print("\n\nbackwards:")
        for t in reversed(odd):
            print(t, end=', ')
        
    elif switch == 2:
        for p in even:
            for t in p:
                print(t, end=', ')

        print("\n\nbackwards:")
        for p in reversed(odd):
            for t in p:
                print(t, end=', ')
    
    print("\n")

checkParams()

start = int(sys.argv[1])
stop = int(sys.argv[2])
switch = int(sys.argv[3]) 
even = []
odd = []

if switch == 1:
    even = calculateSingle(start, stop)
    odd = calculateSingle(start + 1, stop)
        
elif switch == 2:
    even = calculateDouble(start, stop)
    odd = calculateDouble(start + 2, stop)
    
display(even, odd, switch)