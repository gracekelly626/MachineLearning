### Linear Regression - continuous output; linear model; predict the trend
choose the line that minimise the error function, i.e loss function 

X: features of apartments xi = [no of bedrooms = 2,area = 100, age = 10, no. of transaction = 3, facing = 1] (有很多个

![image](https://user-images.githubusercontent.com/90355504/144762286-d72dcc55-12f1-4796-93df-cff189ecc8dc.png)
![image](https://user-images.githubusercontent.com/90355504/144762300-2869edb1-23f2-42cc-a009-27a34726fae9.png)

RSS = ![image](https://user-images.githubusercontent.com/90355504/144762452-a318892e-efee-4da2-9b9c-fd20b5248f93.png)
 ### for least square
![image](https://user-images.githubusercontent.com/90355504/144762257-12eecd84-03ee-4f5b-af99-f21c131d9eea.png)

solve overfitting problem -> reduce variance at the cost of introducing some bias -> Regularisation 
![image](https://user-images.githubusercontent.com/90355504/144763306-72e220f5-4f14-46b9-8d75-37918159da7f.png)

### Lasso Regression - L1 regularisation lamda  是个经验值， 调整曲线的平滑度 hyper parameter -> zeros weights -> feature selection 
more likely 找到尖角 -》 parameter 更容易为0
![image](https://user-images.githubusercontent.com/90355504/144762518-f8535303-9e02-4bd1-ae38-aa89b746fabd.png)
### Ridge Regression - L2 regularisation -> small weights -> smooth curve 
![image](https://user-images.githubusercontent.com/90355504/144762785-a55b088f-6de7-443a-942c-1697225d30a0.png)
### Elastic Net 
![image](https://user-images.githubusercontent.com/90355504/144763074-2a3761df-3c43-4af6-ace6-e4368a6fcbca.png)


