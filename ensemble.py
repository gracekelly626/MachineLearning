decision tree 
attributes - features 
default - 默认值

step 1 
best - CHOOSE ATTRIBUTE 
一般用information gain， IG越大越好；　也有其他的标准
选中best　feature后，　自动剔除

｀｀
examples = [[None, Yes, French, Yes, F], [Some, Yes, Italian, No, F], [Full, Yes, Italian, No, T], [Full, No, Thai, No, T], [Full, No, Thai, No, F]] 
　# F/T 对应的是training set 的label, 是事先人为规定好的
Attributes = {"patrons", "hungry", "Type", "Fri/Sat"}

# how to calculate info gain - calculate entropy
# initial step: [F, F, T, T, F] - E0

# choosing the best feature - same process for every feature
# [None, …,F] - [F] - E1
# [Some, …, F] - [F] - E2
# [Full, …. , T], [Full, …., T], [Full, …. F] - [T, T, F] - E3

# Info Gain = E0 - (⅕*E1 + ⅕*E2 + ⅗* E3)

｀｀
step 2 
为每一个result建立ｓｕｂｔｒｅｅ

step 3 
if the labels are all the same in the same subset, then return the lable.

