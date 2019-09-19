# Soal 2 - SPLTV (Sistem Persamaan Linear Tiga Variabel)
#persamaan linear 3 variabel:
#x  - 2y +  z =  6
#3x +  y - 2z =  4
#7x - 6y -  z = 10
# 1. menentukan nilai x, y, z
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d 
import matplotlib.tri as mtri

a = np.array([[1,-2,1],[3,1,-2],[7,-6,-1]])
b = np.array([6,4,10])
X = round(np.linalg.solve(a,b)[0])
Y = round(np.linalg.solve(a,b)[1])
Z = round(np.linalg.solve(a,b)[2])
print('Nilai x:',X)
print('Nilai y:',Y)
print('Nilai z:',Z)

# 2. plotting masing-masing persamaan dalam bentuk 3D
#x -2y + z = 6
X = 6 #ketika y dan z 0 maka x = 6
Y = -3 #ketika x dan z 0 maka -2y = 6
Z = 6 #ketika x dan y 0 maka z = 6

x = np.array([X,0,0])
y = np.array([0,Y,0])
z = np.array([0,0,Z])

triang = mtri.Triangulation(x, y)
fig = plt.figure(figsize = (9,6))
ax = fig.add_subplot(1,3,1, projection='3d')
ax.plot_trisurf(triang, z, color = 'red',alpha=0.5)
ax.scatter(x,y,z, marker='.', s=15, color = 'blue')
ax.set_xlabel('Nilai X')
ax.set_ylabel('Nilai Y')
ax.set_zlabel('Nilai Z')
plt.title('x -2y + z = 6')


#3x + y - 2z = 4
X = 3/4 #ketika y dan z 0 maka 3x = 4
Y = 4 #ketika x dan z 0 maka y = 4
Z = -2 #ketika -2z = 4 maka -2z = 4

x = np.array([X,0,0])
y = np.array([0,Y,0])
z = np.array([0,0,Z])

triang = mtri.Triangulation(x, y)
ax = fig.add_subplot(1,3,2, projection='3d')
ax.plot_trisurf(triang, z,color = 'yellow',alpha = 0.5)
ax.scatter(x,y,z, marker='.', s=15, color = 'red')
# ax.view_init(elev=60, azim=-45)
ax.set_xlabel('Nilai X')
ax.set_ylabel('Nilai Y')
ax.set_zlabel('Nilai Z')
plt.title('3x + y - 2z = 4')

#7x - 6y - z = 10
X = 10/7 #ketika y dan z 0 maka 7x = 10
Y = -10/6 #ketika x dan z 0 maka -6y = 10
Z = -10 #ketika -2z = 4 maka -z = 10

x = np.array([X,0,0])
y = np.array([0,Y,0])
z = np.array([0,0,Z])

triang = mtri.Triangulation(x, y)
ax = fig.add_subplot(1,3,3, projection='3d')
ax.plot_trisurf(triang, z,color='blue',alpha=0.5)
ax.scatter(x,y,z, marker='.', s=5, color = 'green')
# ax.view_init(elev=60, azim=-45)
ax.set_xlabel('Nilai X')
ax.set_ylabel('Nilai Y')
ax.set_zlabel('Nilai Z')
plt.title('7x - 6y - z = 10')
plt.show()
