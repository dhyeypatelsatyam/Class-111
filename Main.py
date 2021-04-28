import csv 
import pandas as pd     
import plotly.figure_factory as ff
import random 
import statistics
import plotly.graph_objects as go

df=pd.read_csv("studentMarks.csv") 
data=df["Math_score"].tolist()

Mean=statistics.mean(data)
Stdev=statistics.stdev(data)
#fig=ff.create_distplot([data],["Math Score"],show_hist=False)
#fig.show()

#print(Mean,stdev)

#This is Z sample test

def random_set_of_mean(counter):
    data_set=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        data_set.append(value)
    
    Mean=statistics.mean(data_set)
    return Mean    #pass the number of time you want the mean of the datapoints as a para meter in range()


Mean_list=[]
for i in range(0,1000):
    set_of_mean=random_set_of_mean(100)
    Mean_list.append(set_of_mean)

mean=statistics.mean(Mean_list)
stdev=statistics.stdev(Mean_list)


print(mean,stdev)

fig=ff.create_distplot([Mean_list],["Student_score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="Mean"))
fig.show()