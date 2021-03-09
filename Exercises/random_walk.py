import matplotlib.pyplot as plt
from random import choice

plt.rc('figure',figsize=(12,6))
#plt.xlim(0,1.0)
#plt.ylim(0,50)
plt.title('Random Walk')
plt.xlabel('Number of steps')
plt.ylabel('Distance from origin')

step_option= [-1,1]
step_choice= choice(step_option)
step_choice

walk=[]
walk.append(step_choice)
for step in range(1,1000):
    next_step=walk[step-1] + choice(step_option)
    walk.append(next_step)
print(walk)

plt.plot(walk)
plt.show()

