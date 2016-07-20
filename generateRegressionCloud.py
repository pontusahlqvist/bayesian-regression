import matplotlib.pyplot as plt
import numpy as np

numPoints = 50
numLines = 10
noiseMagnitude = 0.1
w0 = 1
w1 = 0.5
xmin = 0
xmax = 2
ymin = 0
ymax = 2
x = [xmin + np.random.rand()*(xmax-xmin) for i in range(numPoints)]
y = [w0 + w1*xi + noiseMagnitude*np.random.rand() for xi in x]

plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)

for ind,(xi,yi) in enumerate(zip(x,y)):
	plt.scatter(xi, yi, s=10, c='r', alpha=0.5)
	theta_rand = np.random.rand()
	for i in range(numLines):
		theta = theta_rand + np.pi*i/(numLines)
		slope = np.tan(theta)
		plt.plot([xmin,xmax],[yi + slope*(xmin - xi),yi + slope*(xmax - xi)], c='b')
		

plt.savefig('regression_%d_%d.jpg'%(numPoints,numLines))
plt.show()

