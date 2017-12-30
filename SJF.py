# main function
# short job first with order given
f1=open("SJF.txt","r")
duration=[]
copy=[]
process=[]
arrival=[]
order=[]
total=0
totalval=[]
f1.readline()
for l in f1:
     vals = [int(x) for x in l.split()]
     duration.append(vals[1])
     copy.append(vals[1])
     process.append(vals[0])
     order.append(vals[2])
     arrival.append(vals[3])
duration.sort()
print "GANTT CHART : "
for val in duration:
    total += int(val)
    totalval.append(total)
    for val2 in range(len(copy)):
        if (val==copy[val2]):
            print 'p'+str(process[val2]),
print
for val in totalval:
    print val,
print
print "Total Time : ",
print total
f1.close()