### Ensemble Methods
- bagging
- boosting
Ensemble technique can be applied to many ML models, not just for tree/forest. classification 

https://www.edureka.co/blog/boosting-machine-learning/

https://web.stanford.edu/~hastie/Papers/samme.pdf


#### Boosting - making a strong classifier H by combining several weak classifers h by letting them vote
- start with wieght that sample wi = 1/N (N is teh no. of sample)
- pick ht s.t minimise the error at time t 
- pick weight alpha at time t 
- calculate the wi at time t+1 
- ![image](https://user-images.githubusercontent.com/90355504/145109020-c8e515c6-dd5b-486f-8a8a-ca11a990bcf9.png)
- (y is just a function with value plus 1 or minus 1 depending on the output ought to be plus 1 or minus 1, flip the sign for the wrong answer; Z is normaliser to make new wieghts add up to one)
- ![image](https://user-images.githubusercontent.com/90355504/145114571-eb5abab4-dece-4437-930f-9886b7c587cc.png)
- sum(wi) for wrong is equal to the error rate; while sum(wi) for right is equal to (1-err)
- ![image](https://user-images.githubusercontent.com/90355504/145112632-3e11998b-0e0a-40fe-bf7d-d208b7ff42bf.png)
converge to zero 
assume a binary classifer h produces [-1,1]. e.g 1 for true and -1 for false

error ranges from 0 to 1. 

weaker learner - little bit better than fliping a coin

x is sample H(x) = sign(h1(x)+h2(x)+h3(x))
- use the data ubdisturbed to produce h1
- data exaggeration of h1 error to produce h2
- data exaggeration of h2 != h1 to produce h 3 




通过weak　learner建一个strong　learner：　F

#### Random Forest - bagging
is a type of bagging 
F -> Random Forest 
h -> Decision Tree

random forest ->(sample with replacement 同一颗树可以用很多次) -  10 trees -> majority voting

#### Adaboost
1. equally weighted 
2. compute alpha - err 越大，　alpha越大　－> 之前做的不好会有更大的weight
3. 之前的tree还是保留，　打补丁

#### Gradient Boosting 
F -> gradient boosting tree; h -> decision tree
x : [x1,x2,x3...] feature Y: y (label/ground true)
Loss Function L = (F(x) - y ) ^2
train weak learner for pseudo-residuals
https://en.wikipedia.org/wiki/Gradient_boosting
