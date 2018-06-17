"""Given starting and ending positions of segments on a line, the task is to take the union of
all given line segments and find the length covered by the line segments"""

segments = [(2,5),(4,8),(9,12)]  # a hardcoded example but can easily be altered for more points

def beginandend(segments):
    startpoints = []
    endpoints = []
    for i in range(len(segments)):
        startpoints.append(segments[i][0])
        endpoints.append(segments[i][1])
    return startpoints,endpoints

y = beginandend(segments)

newendpoints = [x+1 for x in y[1]] # adding 1 to end points cause we want the endpoints to be included and the range function does not include th eend point so this slight modification

ranges = zip(y[0],newendpoints)

r1 = range(ranges[0][0],ranges[0][1])
r2 = range(ranges[1][0],ranges[1][1])
r3 = range(ranges[2][0],ranges[2][1])

Unionr1r2 = list(set(r1).union(r2))
Unions = [min(Unionr1r2),max(Unionr1r2)]

def getsegmentlength(Union,r3):
    if min(r3)-max(Unions)== 1:
        return max(Unions)- min(Unions) + max(r3)-min(r3)
    else:
        print("There has to be a continuum")

print(getsegmentlength(Unions,r3))
