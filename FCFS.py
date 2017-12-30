f=open("FCFS.txt","r")
f.readline()
process=[]
duration=[]
copy=[]
order=[]
arrival=[]
total=0
totaltime=[]
index=0
for val in f :
    value=[int(x) for x in val.split()]
    process.append((value[0]))
    duration.append(value[1])
    order.append(value[2])
    arrival.append(value[3])
    copy.append(value[3])
arrival.sort()
print ("GANTT CHART : ")
for x in arrival:
    for y in range(len(copy)):
        if (x==copy[y]):
            index=y
    total+=duration[index]
    totaltime.append(total)
    print 'p'+str(process[index]),
print
for x in totaltime:
    print x,
print
print "Total Time : "+str(total)
f.close()