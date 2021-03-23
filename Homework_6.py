import random
import copy

class data:
    
    def __init__(self,case,x,y,z):
        
        #Case number
        self.case = case
        
        #X,Y,Z coordinates of data point
        self.x = x
        self.y = y
        self.z = z
        
        #Cluster number
        self.clust = -1
        
    def distance(self, point):
        
        #Distance between centroid and data point
        
        d_x = self.x - point.x
        d_y = self.y - point.y
        d_z = self.z - point.z
        
        dist = (d_x ** 2 ) + (d_y ** 2 ) + (d_z ** 2 )
        
        return abs(dist)
    
    def min_dist(self,dist):
        
        #Finding minimum distance among point and centroids
        
        min_d = min(dist)  
        
        for i in range(len(dist)):
            if min_d == dist[i]:
                self.clust = i
                
                
                
     
    def clust_list(self, cluster):
            
        i = self.clust
            
        cluster[i].append( self )

def new_cog(c_list):
    
    #Finding average point among each cluster
    
    num = len(c_list)
    
    X = 0
    Y = 0
    Z = 0
    
    for i in c_list:
        X += i.x
        Y += i.y
        Z += i.z
        
    return data(-1, X/num , Y/num , Z/num)

def comp_clust(clust, temp_clust):
    
    #Checking if clust and temp_clust have same elements
    
    c_case = []
    tc_case = []
    
    for x in clust:
        c_case.append(x.case)
        
    for x in temp_clust:
        tc_case.append(x.case)
        
    if len(c_case) == len(tc_case):
        
        for x in c_case:
            if x not in tc_case:
                return 1
    
        return 0
    
    else:
        return 1
    
def print_clust(clust,num):
    
    #Headings
    
    print("\n\n \t Case \t Cluster \n")
    
    #Values
    for i in range(num):
        
        for x in clust[i]:
            print("\t ",x.case," \t ",x.clust)
        
        print("\n")

run = True

k = 3    #Number of clusters

cluster = []    #Main/Final cluster
temp_cluster = []    #Temporary cluster for comparing with main cluster
 
#cluster[0], cluster[1]...., cluster[k] will be lists holding elements in the 0th, 1st..., kth cluster
for _ in range(k):
    cluster.append( [] )
    temp_cluster.append( [] )

#Entering all data points into a list
   
points = []

points.append( data( 1 , 4.40 , 4.57 , 2.29 ) )
points.append( data( 2 , 3.25 , 3.92 , 2.17 ) )
points.append( data( 3 , 3.10 , 4.25 , 2.40 ) )
points.append( data( 4 , 4.83 , 4.31 , 2.16 ) )
points.append( data( 5 , 3.63 , 3.60 , 1.67 ) )
points.append( data( 6 , 3.26 , 1.64 , 1.48 ) )
points.append( data( 7 , 4.89 , 1.33 , 1.04 ) )
points.append( data( 8 , 4.50 , 2.01 , 1.28 ) )
points.append( data( 9 , 4.99 , 2.47 , 2.60 ) )
points.append( data( 10 , 4.12 , 2.12 , 1.70 ) )
points.append( data( 11 , 2.21 , 2.51 , 4.17 ) )
points.append( data( 12 , 2.97 , 4.10 , 3.92 ) )
points.append( data( 13 , 2.40 , 2.45 , 4.46 ) )
points.append( data( 14 , 2.10 , 3.30 , 4.90 ) )
points.append( data( 15 , 1.13 , 2.05 , 3.28 ) )


dist = []
CoG = []    #Center of gravity of clusters

count = 0

while count<k:    #Randomly selecting CoGs
    
    i = random.randint(0,len(points)-1) 
    
    if points[i] not in CoG:
        CoG.append( points[i])
        count+=1
        
#Finding inital clusters        
        
for i in points:
    
    for j in CoG:
        
        dist.append( j.distance(i) )   #Finds distances between point and each centroid
        
    i.min_dist(dist)    #Find min among those distances
    i.clust_list(cluster)    #Organises data into cluster list
    dist.clear()    #Clears list of distances for next iteration


#Iterations begin
    
while run:
    
    CoG.clear()
    dist.clear()
    
    for i in range(k):
        
        CoG.append( new_cog( cluster[i] ) )    #Finding new center of gravity for cluster
        
    
    #Dividing all elements into clusters based on new CoG
    for i in points:
        
        for j in CoG:
        
            dist.append( j.distance(i) )   
        
        i.min_dist(dist)    
        i.clust_list(temp_cluster)    
        dist.clear()
    
    flag = 0
    
    for n in range(k):
    
        flag += comp_clust( cluster[n], temp_cluster[n] )    #If they are same, function returns 0

        
    if flag == 0:
        run = False
    
    #Copying new cluster elements into cluster list
    cluster = copy.deepcopy(temp_cluster)    

    #Resetting temp_cluster list for next iteration
    for i in range(k):
        temp_cluster[i].clear()
        

print_clust(cluster,k)    #Final cluster list
