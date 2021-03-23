class data:
    
    def __init__(self,value1,value2,true_output):
        
        #Boolean Input Values
        self.x1 = value1
        self.x2 = value2
        
        #Weights
        self.w1 = 0.7
        self.w2 = 0.8
        self.w3  =-0.2
        
        #Change in Weights
        self.dw1 = 0.0
        self.dw2 = 0.0
        self.dw3 = 0.0
        
        #True and resultant outputs
        self.t = true_output
        self.o = -1
        
        #Learning rate
        self.a = 0.1
        
    def print_row(self):
        
        #Print row of table 
        
        print("\n",end="    ")
        print(self.x1, end="    ")
        print(self.x2, end="    ")
        print(self.t, end="    ")
        print(self.o, end="    ")
        print(round(self.dw1,1), end="    ")
        print(round(self.w1,1), end="    ")
        print(round(self.dw2,1), end="    ")
        print(round(self.w2,1), end="    ")
        print(round(self.dw3,1), end="    ")
        print(round(self.w3,1))
        
    def check_TO(self):
        
        #Checking if output equals expected output
        
        if self.t == self.o:
            return 0
        else:
            return 1
     
    def fix_w(di,df):
        
        #Changing weight of next input
        di.w1 += di.dw1
        di.w2 += di.dw2
        di.w3 += di.dw3
        
        df.w1 = di.w1
        df.w2 = di.w2
        df.w3 = di.w3
        
    def cal_dw(self):
        
        #Calculating values of dw's
        self.dw1 = self.a * self.x1 * (self.t - self.o)
        self.dw2 = self.a * self.x2 * (self.t - self.o)
        self.dw3 = self.a * 1 * (self.t - self.o)
        
    def check_thresh(self):
        
        thresh  = (self.x1 * self.w1) + (self.x2 * self.w2) + (self.w3)
        
        if thresh >=0:
            self.o = 1
        else:
            self.o = 0
        
#Printing Table Headers
print("\n"*2)
print("\n",end="    ")
print("x1", end="   ")
print("x2", end="   ")
print("T", end="    ")
print("O", end="    ")
print("dw1", end="    ")
print("w1", end="     ")
print("dw2", end="    ")
print("w2", end="     ")
print("dw3", end="     ")
print("w3")

        
    
run = 1        

#Boolean Input/Output for AND
d1 = data(0,0,0)
d2 = data(0,1,0)
d3 = data(1,0,0)
d4 = data(1,1,1)

print("\n", end="    ")
print(" "*27, end="")
print(d1.w1, end="")
print(" "*11, end="")
print(d1.w2, end="")
print(" "*11, end="")
print(d1.w3)

while run:

    flag = 0
    
    i_flag = 0
    
    # [Check d1] --------------------------------
    
    d1.check_thresh()    #Calculating output by checking if threshold is met
    
    flag = d1.check_TO()    #Returns 1 if T not equal to O
    i_flag += flag    #i_flag stays 0 if all four cases are successful
    
    d1.cal_dw()    #Calculated dw values
    data.fix_w(d1, d2)    #Adjusts weights if needed
        
    d1.print_row()    #Prints row
        
    # [Check d2] ---------------------------------------
        
    d2.check_thresh() 
        
    flag = d2.check_TO()
    i_flag += flag
    
    d2.cal_dw()    
    data.fix_w(d2, d3)
            
    d2.print_row()
            
    # [Check d3] ---------------------------------------
            
    d3.check_thresh() 
            
    flag = d3.check_TO()
    i_flag += flag
    
    d3.cal_dw()       
    data.fix_w(d3, d4)
                
    d3.print_row()
                
    # [Check d4] ----------------------------------------
                
    d4.check_thresh() 
                
    flag = d4.check_TO()
    i_flag += flag
    
    d4.cal_dw()            
    data.fix_w(d4, d1)
                    
    d4.print_row()
    
    # End of iteration checks ------------------------------
                    
    if i_flag == 0:
        run = 0
                   
    i_flag = 0
    
    #print("-----",end="")
                        
                        
print("\n")
    
        
        
        
        

