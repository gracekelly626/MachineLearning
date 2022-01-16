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
no. of parameters won't change as input; operate piece by piece using the same kernel
![image](https://user-images.githubusercontent.com/90355504/149656632-71e15154-5717-403e-b457-3a7a7d8c5edd.png)

strikde - 移动步伐

padding - in order to remain the size of output as the same as input, add extra layer to input
 ![image](https://user-images.githubusercontent.com/90355504/149657008-900b55da-1aca-49ed-8e6a-67f27032f892.png)


CNN - can learn the kernel's parameters from the data

Translation Invariance - in images, it implies that all patches of an image will be treated in the same manner

Locality - only a small nerghborhood of pixels will be used to compute the corresponding hidden representations 

convolutional layers typically require fewer parameters that fully-connected layers 

Pooling layers provide an approach to down sampling feature maps by summarizing the presence of features in patches of the feature map. Two common pooling methods are average pooling and max pooling that summarize the average presence of a feature and the most activated presence of a feature respectively.

feature map 
![image](https://user-images.githubusercontent.com/90355504/149657927-44c9929f-acb6-4a84-9f67-61efc9849ff6.png)

https://www.google.com/url?sa=i&url=https%3A%2F%2Fireneli.eu%2F2016%2F02%2F03%2Fdeep-learning-05-talk-about-convolutional-neural-network%25EF%25BC%2588cnn%25EF%25BC%2589%2F&psig=AOvVaw1cdQrDSywfmN0jC1oXV16t&ust=1642418109732000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCOjambSStvUCFQAAAAAdAAAAABAf
