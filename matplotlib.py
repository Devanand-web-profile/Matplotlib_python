

import matplotlib.pyplot as plt

x1=[12,34,5,23,24]
plt.xlabel("--------rate---------")
x2=[34,65,76,79,45]
'''
plt.plot(x,y,color="magenta")   # dashed , dotted 
plt.grid(True,color="green")
plt.show()

'''
'''
#plt.plot(x,y,'ro')  # ro = r= color[red] , o = circle[shape ] 
plt.plot(x,y,'gs')   # gs = g=green , s= square
plt.grid(True,color="green")
plt.show()
'''

size=[150,60,20,250,160]
plt.scatter(x1,x2,color=["red","yellow","purple","green","magenta"],sizes=size) 
plt.grid(True,color="green")
plt.plot(x1,x2,color="cyan")
plt.show()

