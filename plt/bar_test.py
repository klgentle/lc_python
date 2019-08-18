from matplotlib import pyplot as plt

num_list = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
length = range(len(num_list))
plt.bar(length,num_list)
plt.show()
