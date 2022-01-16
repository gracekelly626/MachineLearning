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

- Neural Network Basics, BP 
- Image Classificaiton: CNN
- Machine Translation: RNN, embedding
- Machine Translation: Transformer(attention)


784 个小圆圈

- perceptron/single neuron
- : forward propagation
![image](https://user-images.githubusercontent.com/90355504/148845104-9ae8f385-6e74-4ba2-bd89-d3ad9bfef8d0.png)
![image](https://user-images.githubusercontent.com/90355504/148846150-d0a2e862-8a30-4db0-af8b-e8728ddf7e2c.png)

- xi: input; 
- wi: corresponding weight; 
- w0: bias term to allow shift the activation function left or right
- common activation function: sigmoid, hyperbolic tangent, ReLU
the purpose of activation function is to introduce non-linearities into the network. 

#### CNN
convolution: can do soem changes to our input
parameters won't change as input; operate piece by piece using the same kernel


strikde - 移动步伐

padding - in order to remain the size of output as the same as input, add extra layer to input
 
![image](https://user-images.githubusercontent.com/90355504/149656632-71e15154-5717-403e-b457-3a7a7d8c5edd.png)
