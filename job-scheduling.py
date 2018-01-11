
# weighted Job scheduling problem

 
import sys



L=[]
#---------------------------Read File and store in List---------------------
with open (sys.argv[1]) as f:
        for line in f:
                if not line.isspace():
                        mlist = [int(x) for x in line.split()]
                        L.append(mlist)

#----------------------------------------------------------------------------
#print L

#function to check if the job has conflict with its previous job
def check_conflict(G,i):
        j=i-1
        while(j>=0):
                if (G[j][1] <= G[i][0]):   #check if the finish time of previous job is less than start time of the current jon

                        return j        #if yes return the job because it has no conflict
                j-=1
        return -1


#main function that does the job scheduling based on whether conflicts exists or not
def schedule(L):
        # make all elements of array as 0
        Array = [0] * len(L)
        n=len(L)
        # sort the array based on end time
        L.sort(key = lambda x : x[1])

        #print L[0][2]
        #sorted_jobs = [x for _,x in sorted(zip(E,W))]

        Array[0]=L[0][2] #First element in Array must be weight of first sorted job

        for c in xrange(n):
                #check if job has conflicts
                z=check_conflict(L,c)
                if (z != -1):
                        #if no conflicts then add to existing weight
                        L[c][2]+= Array[z]
                #get the max of accumulated weight or the weight of previous job
                Array[c] = max (L[c][2], Array[c-1])
        #return the last element of array
        return Array[n-1]

#----------------------------------------------------------------------------------------------
#print L

A=schedule(L)
print("The maximum weight possible is ",A)
