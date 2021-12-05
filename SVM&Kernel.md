SVM - solve classification problem 
want to draw a straight line with the view putting in the **widest** street that seperates the positive samples from the negative samples. 
![image](https://user-images.githubusercontent.com/90355504/144755453-3277dcea-808d-457e-b0b2-c1a70d8dbc02.png)

decision boundary - a vecotr w constraint with any length, perpendicular to the median line of the street; also have some unknown points, and have a vector u that points to it -> project to the vecotr u down on to one that is perpendicular to the street to figure out the unkown is on the irght or left side of the street. THE FURTHER, THE RIGHT

### Developments for SVM 
- DECISION RULE: dot(w,u) + b >= 0 , then +
- SUPPORT VECOTR: yi(xi*w + b) -1 = 0 for xi in gutter 
- WIDTH OF THE STREET: dot((x+ - x-), w/||w||) = 2/||w|| (want the width as wide as possible)
- ![image](https://user-images.githubusercontent.com/90355504/144757571-2cb23b16-7b53-4e38-9878-c51af81ba218.png)

### Detailed Explaination 
- dot(w, u) >= c (a constant) 
- WTLG dot(w,u) + b >= 0 , then + (DECISION RULE) 
- dot(w,x+) + b >= 1 & dot(w,x-) + b <= -1 (considering both sides of the line)
- introducing a new varible, yi s.t yi = 1 for sample + ; yi +-1 for sample -
- therefore, the decision rule is equivalent to yi(xi*w + b) -1 >= 0 
- yi(xi*w + b) -1 = 0 ** for xi in gutter - support vector
- WIDTH OF THE STREET: dot((x+ - x-), w/|w|) = 2/|w| from equation ** 
- maximise 2/|w| -> equivalent to maximise 1/|w| -> equivalently minimise |w| -> equivalently minimise 1/2|w|^2
- by LAGRANGE multipliers, L = 1/2|W|^2 - SUM(alpha i(yi(dot(w,xi) + b) -1) ; find the derivatives and set to 0 (differetiate vector is equal to differentiate a scaler) 
- w is equal to the linear sum of some vectors in the sample w = sum(alpha i* yi*xi) 


reference: https://www.youtube.com/watch?v=_PwhiWxHK8o

### kernel trick - don't need to find Z,Z' explicitly, juts know its dot product
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

Guess mapping F, F(x) = z, difficult ;(

K(X, X’) = dot(Z, Z’)  -> guess K -> (‘rbf’, ….., ….)
Implicit 
         Suppose Kernel = exp(−(X − X’)^2)
         exp(-X^2 + 2*X*X’ - X’^2)
= exp(-X^2)*exp(-X’^2)*exp(2*X*X’)
= exp(-X^2)*exp(-X’^2)*Sum(2^k * (X^k) * (X’^k)/ k!)
= 2^k/k! * Sum( exp(-X^2)*(X^k) * exp(-X’^2)*(X’^k) )

Where k = 0, …., infinity


Z = (exp(-X^2)*(X^0),   …..  , exp(-X^2)*(X^k))

### kernel approxiamtion - map Z,Z', will know its explicit value
