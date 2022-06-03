# giannis mparzas 2765
import sys
import math
import time
import heapq

time0=time.time()
k=int(input("dwse to k: "))
male_f=open('males_sorted','r',encoding='utf-8') 
female_f=open('females_sorted','r',encoding='utf-8') 
male_dict={}
female_dict={}
female_max=0
male_max=0
female_cur=0
male_cur=0
heap=[]

l_m=0
l_f=0



     
      
def nextValid(sex):
     global l_m,l_f,first_malee,first_femalee
     
     if(sex==1):
               
          new_line=male_f.readline()
          array_line=new_line.split(",")
          age=int(array_line[1])
          status=array_line[8]
          id_=int(array_line[0])
          weight=float(array_line[25])
          
          while( not isValid(age,status) ):#
          
               l_m+=1
               if(not new_line):
                    return -1
               
               
               
               new_line=male_f.readline()
               array_line=new_line.split(",")
               age=int(array_line[1])
               status=array_line[8]
               #except:
                   # print(array_line," exception!")
                   # print(new_line," !",l_m)
              
             
          
          id_=int(array_line[0])
          weight=float(array_line[25])
          return [id_,age,weight]
          '''
          if(first_male==1):
               first_male=0
               male_max=weight
               print(" max Valid line male ",id_," ",male_max," ",age," ",status,"in line ",l_m)'''
          
     elif(sex==-1):
         
          new_line=female_f.readline()
          array_line=new_line.split(",")
          age=int(array_line[1])
          status=array_line[8]
          id_=int(array_line[0])
          weight=float(array_line[25])
          
          while( not isValid(age,status) ):#
            
          
               if(not new_line):
                    return -1
               l_f=1
               new_line=female_f.readline()
               array_line=new_line.split(",")
               age=int(array_line[1])
               status=array_line[8]
               
          
          id_=int(array_line[0])
          weight=float(array_line[25])
          return [id_,age,weight]
          
    

          

def isValid(age,status):
     if(age>=18 and (status[0:8].strip() != "Married")):
          return True
     
     return False

def  top_k_A():
     global female_cur,male_cur
     
     turn=1
     heapq.heapify(heap)
     
     ##########max male
     max_male_line=nextValid(1)
     
     
     id_1=max_male_line[0]
     age_1=max_male_line[1]
     weight_m=max_male_line[2]
     
     male_max=max_male_line[2]
     male_cur=male_max
     #print("max male id ",id_1,"weight ",weight_m,"age ",age_1)
     male_dict[age_1]=[ ( id_1,weight_m ) ]

     #########max female
     max_female_line=nextValid(-1)
     
     id_2=max_female_line[0]
     age_2=max_female_line[1]
     weight_f=max_female_line[2]
     #print("max female id ",id_2,"weight ",weight_f,"age ",age_2)
     female_max=max_female_line[2]
     female_cur=female_max
     
     female_dict[age_2]=[ ( id_2,weight_f ) ]

     T= male_max + female_max
     
     if (age_2 in male_dict.keys() ) :
          print(-(weight_m + weight_f), id_1, id_2)
          heapq.heappush(heap, (-(weight_m + weight_f), id_1, id_2))
        
     if(len(heap) > 0 and -heap[0][0] >= T) :
        
        yield heapq.heappop(heap) 


     
     while(1):
          
          if(turn==1): #male turn==1
               
               male_line=nextValid(turn)
               
               if(male_line!=-1):
                    id_=male_line[0]
                    age=male_line[1]
                    weight=male_line[2]
                    
                    if( age in male_dict.keys() ):
                    
                         male_dict[age].append( (id_,weight) )
                    else:
                         male_dict[age]=[ (id_,weight ) ]
                    
                    male_cur=male_line[2]
                    
                    if( age in female_dict.keys() ):
                    
                         femaleInAge=female_dict[age]
                    
                         for person in femaleInAge :
                             
                              total_sum_weight =-1*(person[1]+male_cur)
                              maleid=id_
                              femaleid=person[0]
                              heapq.heappush(heap,(total_sum_weight,maleid,femaleid ) )
                         
          else:# female turn==-1
               
               female_line=nextValid(turn)
               
               if(female_line!=-1):
                    
                    id_=female_line[0]
                    age=female_line[1]
                    weight=female_line[2]
                    
                    if( age in female_dict.keys() ):
                         female_dict[age].append( (id_,weight) )
                    else:
                         female_dict[age]=[ ( id_,weight ) ]
                    
                    female_cur=female_line[2]
               
                    if( age in male_dict.keys() ):
                         
                         maleInAge=male_dict[age]
                    
                         for person in maleInAge:
                              total_sum_weight=-1*(person[1]+female_cur)
                              femaleid=id_
                              maleid=person[0]
                              heapq.heappush(heap,(total_sum_weight,maleid,femaleid) )
               
          turn=turn*(-1) #change turn
          T=max( male_max+female_cur,female_max+male_cur)
         
               
          if(len(heap)>0 and (heap[0][0])*(-1)>=T):
          
               yield heapq.heappop(heap)
               
          
          
     


gen=top_k_A()
print("--------------------k Results------------------------")
for i in range(k):
     result=next(gen)
     total_weight=float(result[0])*(-1)
     print(i+1,"pair: ",result[1],",",result[2],"score: ",round(total_weight,2))
     
time1=time.time()
time_A=time1-time0
print("-----------------------------------------------------")
print("execute time: ",time_A,"sec\n")
#m_l=male_f.readline()
#f_l=female_f.readline()
