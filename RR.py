class Process:
    arrival=0
    duration=0
    name=""
    def __init__(self,arrival=0,duration=0,name=""): #constructor
        self.arrival=arrival
        self.name=name
        self.duration=duration
    def show(self):
        print self.name

    def ASort(self,array):
        for x in array:
            for y in range(len(array)-1):
                if (array[y].arrival>array[y+1].arrival):
                    temp=array[y]
                    array[y]=array[y+1]
                    array[y+1]=temp

#main
f= open("rr.txt","r")
arr=[]
ready=[]
quantum=f.readline()
quantum=int(quantum)
temp=Process()
rqueue1=[]
rqueue2=[]
f.readline()
time=0
processes=0
enqueue=0
completed=[]
for x in f:
    val=[ int(val) for val in x.split()]
    arr.append(Process(val[1],val[2],'p'+str(val[0])))
    processes+=1
temp.ASort(arr)
i=0
rqueue.append(arr[i])
time+=arr[i].arrival
enqueue+=1
while rqueue!=[]:
    time+=quantum
    if enqueue!=processes and i<processes:
        for z in range(i+1,len(arr)):
            if (arr[z].arrival<=time):
                rqueue.append(arr[z])
                enqueue+1
    rqueue[i].duration-=quantum
    if rqueue[i].duration<=0:
        completed.append(rqueue[i])
    else:
        rqueue.append(rqueue[i])
    i+=1
time+=quantum
f.close()