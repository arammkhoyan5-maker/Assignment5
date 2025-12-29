# super_confusing_code.py

def doStuff(x):
    t = 0
    # Off-by-one error here:
    for j in range(len(x) + 1):    
        t = t + x[j]              
    return t / len(x)             


def g():
    a = []                        
    for n in range(5):
        q = input("Give number: ") 
        a.append(float(q))        
    return a


def run():
    z = g()                        
    r = doStuff(z)                
    print("Here:", r)


run()