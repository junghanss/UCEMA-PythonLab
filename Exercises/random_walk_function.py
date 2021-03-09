import matplotlib.pyplot as plt 
from random import choice

#plt.rc('figure',figsize=(12,6))
#plt.xlim(0,1.0)
#plt.ylim(0,50)
#plt.title('Random Walk')
#plt.xlabel('Number of steps')
#plt.ylabel('Distance from origin')

def rand_walk(step_num):
    walk = []
    step_choice= choice([-1,1])
    walk.append(step_choice)
    for i in range(1, step_num):
        step_choice_2= choice([-1,1])
        next_step=walk[i-1] + step_choice_2
        walk.append(next_step)
    return walk

random_w=rand_walk(100)
print(random_w)

def plot_walk(walk):
    x=list(range(1,len(walk)+1))

    plt.plot(x,walk)
    plt.xlabel("Number of steps")
    plt.ylabel("Distance from origin")
    plt.title("Random Walk")
    plt.show()

plot_walk(rand_walk(1000))