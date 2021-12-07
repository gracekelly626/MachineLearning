### Ensemble Methods
- bagging
- boosting
Ensemble technique can be applied to many ML models, not just for tree/forest. classification 
https://www.edureka.co/blog/boosting-machine-learning/
https://web.stanford.edu/~hastie/Papers/samme.pdf


#### Boosting - making a strong classifier H by combining several weak classifers h by letting them vote
assume a binary classifer h produces [-1,1]. e.g 1 for true and -1 for false

error ranges from 0 to 1. 

weaker learner - little bit better than fliping a coin

x is sample H(x) = sign(h1(x)+h2(x)+h3(x))


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
