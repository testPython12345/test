counter = 0
def f():
    global counter 
    counter += 10
    print(counter)
f()
f()