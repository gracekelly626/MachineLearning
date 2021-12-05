一个解决问题的方法 - iterative method to optimise loss function/cost function/objective function的方法之一， 经常运用在deep learning 数据量比较大的时候用

https://www.google.com/url?sa=i&url=https%3A%2F%2Fmedium.com%2F%40divakar_239%2Fstochastic-vs-batch-gradient-descent-8820568eada1&psig=AOvVaw2EGBZhQoIJQ_x8Qd3R13H1&ust=1638184990724000&source=images&cd=vfe&ved=2ahUKEwjc3e3k-Lr0AhUNYxoKHcOfBRIQr4kDegUIARDMAQ

- SVM - 通过lagrange 直接出来一个解
- SGD - 一步一步走（数据量大） 

stochastic gradient descent 
normally， 100 samples 要算100次, 取average
while， stochastic gradient descent RANDOMLY select training sample to calculate gradient. no need to calculate all. 

optimazation 
- 求方程 得到一个确切的解
- 数值逼近，e.g.SGD
