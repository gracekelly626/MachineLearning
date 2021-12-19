#### Deep Learning - try to find out the function to tell the underlying rule, can be prediction or classification 
Neural networks (inspired by bio,  并不是生物的神经网络， 只是借用比喻) Model 
F = f4(f3(f2(f1(x)))
- MLP multi layer perceptron  
 解决的问题 
- computer vision e.g. self driving 
- NLP 
- reinforcement learning e.g. AlphaGo 

#### Key Component
###### Data (pictures, voice,etc)
  - label - supervised learning
     - classification, regression, recommender system(filtering + ranking), sequence learning(translation, input/data dim is not fixed)
  - without label - unsupervised learning 
     - clustering, PCA
     - self - supervised learning NLP
###### Model 
  - CNN (convolutional neural Network) convolution(typical)
  - RNN (Recurrent Neural Network): output可以作为input再一次输入
  - Attention： focus on factors that matter 
    - volitional cue
    - non-volitional cue
###### Objective Function 
loss function -> minimise sum(||yhat - y||^2)
###### Optimization Algo
SGD, Adam - Adaptive Moment Estimation 
##### Difference from Traditional 
1. traditional: feature engineering
  - manual 
  - engineer(canny, SIFT)
2. Deep Learning: end-to-end training 
Disadvatage: data & computation power 
https://arxiv.org/pdf/1910.13796.pdf
