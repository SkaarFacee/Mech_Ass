import shapely
from shapely import geometry

print "Enter the number of sides"
n=input()
x=[]
y=[]
for i in range(0,n):
    print "Enter x and y coordinates of vertex "+str(i+1)+" with reference to origin"
    x.append(input())
    y.append(input())

p=[]
for i in range(0,n):
    p.append(geometry.Point(x[i],y[i]))

pointList=[]
for i in range(0,n):
    pointList.append(p[i])
pointList.append(p[0])

poly = geometry.Polygon([[p.x, p.y] for p in pointList])
centroid = list(poly.centroid.coords)
print "The centroid is "
for x in centroid:
    print x
