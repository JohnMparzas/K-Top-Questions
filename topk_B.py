# giannis mparzas 2765
import sys
import math
import time
import heapq

time0=time.time()
k=int(sys.argv[1])#input("dwse to k: "))#int(sys.argv[1]) 
male_f=open('males_sorted','r',encoding='utf-8') 
female_f=open('females_sorted','r',encoding='utf-8') 
male_dict={}#hash for male 
#female_dict={}#hash for female 
#female_max=0#max value of female
#male_max=0 #max value of male
##female_cur=0 #current value of female
#male_cur=0 #current value of male

heap=[] #the heap!

def isValid(age,status):# true if the line is Valid
     if(age>=18 and (status[0:8].strip() != "Married")):
          return True
     
     return False

male_line=male_f.readline()

while(male_line): #read all male file and add all valid lines in male_dict

     array_line=male_line.split(",")
     id_ = int(array_line[0])
     age = int(array_line[1])
     status = array_line[8]
     weight = float(array_line[25])

     if(isValid(age,status)):
          
          if( age in male_dict.keys() ):#add line in dict if is valid

               male_dict[age].append( (id_,weight) )
          else:
               male_dict[age]=[ (id_,weight) ]

     male_line=male_f.readline()



female_line=female_f.readline()

while(female_line): #read line by line the female file and

     array_line=female_line.split(",")
     id_ = int(array_line[0])
     age = int(array_line[1])
     status = array_line[8]
     weight = float(array_line[25])

     if(isValid(age,status)):
          
          if( age in male_dict.keys() ):

               for man in male_dict[age]:# do pairs
                    
                    if(len(heap)<k):
                         
                         heapq.heappush(heap,( man[1] + weight ,man[0], id_ ) )
                                        
                    elif(heap[0][0] <= man[1] + weight) : 

                         heapq.heapreplace(heap, (man[1] + weight, man[0], id_ ) )
                    
                         
                         
                

     female_line=female_f.readline()



for i in range(k):

     heapq._heapify_max(heap)# move top pair in position 0
     top_i=heapq.heappop(heap)#take it
     print(str(i+1),". pair: ",top_i[1],",",top_i[2]," score: ",round(top_i[0],2))

time1=time.time()
time_B=time1-time0
print("-----------------------------------------------------")
print("execute time: ",time_B,"sec\n")


