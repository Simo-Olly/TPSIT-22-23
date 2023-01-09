import threading

def inc():
    global var
    for _ in range(100000):
        var = var + 1

t = []
var = 0
for i in range(100):
    t.append(threading.Thread(target = inc))

for i in range(100):
    t[i].start()

for j in range(100):
    t[j].join()

print(var)