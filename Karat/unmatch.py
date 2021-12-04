badge_records = [
["Martha",   "exit"],
["Paul",     "enter"],
 ["Martha",   "enter"],
["Martha",   "exit"],
 ["Jennifer", "enter"],
["Paul",     "enter"],
 ["Curtis",   "enter"],
 ["Paul",     "exit"],
["Martha",   "enter"],
 ["Martha",   "exit"],
["Jennifer", "exit"],
 ]

def unmatch(arr):
    enter = set()
    wrongenter = set()
    wrongexit = set()
    for name, record in arr:
        if record == "enter":
            if name not in enter:
                enter.add(name)
            else:
                wrongenter.add(name)
        if record == "exit":
            if name not in enter:
                wrongexit.add(name)
            else:
                enter.remove(name)
    for name in enter:
        wrongenter.add(name)
    return list(wrongenter), list(wrongexit)
print(unmatch(badge_records))

def timedifference(time1, time2):
    h1 = int(time1[:2])
    m1 = int(time1[2:])
    h2 = int(time2[:2])
    m2 = int(time2[2:])
    return abs(h1 * 60 + m1 - h2*60 - m2)
def withinhour(inputs):
    lastvisited = {}
    output = {}
    inputs.sort(key = lambda x: int(x[1]))
    print(inputs)
    for name, time in inputs:
        if name not in lastvisited:
            lastvisited[name] = time
        else:
            lasttime = lastvisited[name]
            if timedifference(time, lasttime) < 60:
                if name not in output:
                    output[name] = set()
                output[name].add(lasttime)
                output[name].add(time)
    for o in output:
        output[o] = list(output[o])
    return output
arr =  [['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']] 
print(withinhour(arr))
    