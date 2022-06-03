import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
k=[1, 2, 5, 10, 20, 50, 100]
time_A=[ 0.0009, 0.0040, 0.0149,0.0529,0.1960, 0.735, 1.9433]

male_lines=[44,134,437,1145,2656,6030,10139]
female_lines=[44,134,437,1145,2656,6030,10139]
time_B=[ 6.222, 6.931, 7.070,6.720,6.118, 6.604, 7.0828]
df=pd.DataFrame({"k":k,"time_A":time_A,"time_B":time_B,"male_lines":male_lines,"female_lines":female_lines})

#sns.lineplot(x= 'k', y='time_A',data = df,marker='o')

df.plot(x = 'k', y = ['male_lines','female_lines'],marker='o', linestyle='--');
plt.xlabel(k)
plt.show()
df.plot(x = 'k', y = ['male_lines','female_lines'],marker='o', linestyle='--');
plt.xlabel(k)

plt.show()


plt.plot(k,time_A , marker='o', linestyle='--', color='r', 
label='Square') 
plt.xlabel('x')
plt.ylabel('y') 
plt.title('compare')
plt.legend() 
plt.show()
