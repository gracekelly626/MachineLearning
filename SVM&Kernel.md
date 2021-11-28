### kernel trick 
当在原始平面不容易用直线一分为二时， 使用kernel trick 把点映射到另外一个空间， 方便linear划分。 
https://www.google.com/url?sa=i&url=https%3A%2F%2Fmedium.com%2F%40divakar_239%2Fstochastic-vs-batch-gradient-descent-8820568eada1&psig=AOvVaw2EGBZhQoIJQ_x8Qd3R13H1&ust=1638184990724000&source=images&cd=vfe&ved=2ahUKEwjc3e3k-Lr0AhUNYxoKHcOfBRIQr4kDegUIARDMAQ


note: dot product 
X = (x1,x2,x3,x4)
Y = (y1,y2,y3,y4)
dot(X,Y) = x1*y1+ x2*y2+ ...+ x4*y4

map X,Y to Z,Z'
Z = (z1,z2,..,zn)
Z' = (z1', z2', ...'zn')

suppose Kernel = XXX , 通过K（X，Y） 算出dot（Z,Z') -> 只需要知道dot product 就可以解lagrange 
K(X,Y) = dot(Z,Z') 
