import plotly.figure_factory as ff
import random
import pandas as pd
import statistics

df = pd.read_csv("data110.csv")
temp = df["temp"].tolist()
#print(temp)

population_mean = statistics.mean(temp)
population_sd = statistics.stdev(temp)
print(population_mean)
print(population_sd)

data_set = []
sample_dist = []
for j in range(0,1000):
    for i in range(0,100):
        rand = temp[random.randint(0,len(temp)-1)]
        data_set.append(rand)
    data_mean = statistics.mean(data_set)
    sample_dist.append(data_mean)

sample_dist_sd = statistics.stdev(sample_dist)
sample_dist_mean = statistics.mean(sample_dist)
print("Standard deviation of sample distribution = "+str(sample_dist_sd))
print("Mean of sample distribution = "+str(sample_dist_mean))
#print(data_mean)
#print(data_sd)
fig = ff.create_distplot([temp],["Temperature Graph"],show_hist=False)
fig1 = ff.create_distplot([sample_dist],["Sample Distribution"],show_hist = False)
fig1.show()
#fig.show()


