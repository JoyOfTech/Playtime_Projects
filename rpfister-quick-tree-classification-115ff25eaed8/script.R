#EDIT THIS TO YOUR WORKING DIRECTORY
setwd("C:/source/titanic/quick-tree-classification")

#import dataset - EDIT THIS FILENAME
data <- read.csv("train.csv")

#split the last 400 rows off into their own dataset;
#set the training data to the remaining rows
numberOfTrainingDataRows <- 400
train <- head(data, n = numberOfTrainingDataRows)
test <- tail(data, n = nrow(data) - numberOfTrainingDataRows)

#import tree classification library
library(rpart)

#Classification tree equation: EDIT THIS EQUATION
#  The first variable is the taget to classify for; the others are parameters
#  to consider for use in the tree.
fit <- rpart(
  Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked, method="class",
             data=train)

#Plot the classification tree - you can show this to your business users
#   or programmers to implement
library(rpart.plot)
prp(fit, faclen=0)

#Add predictions to the test data
test$Prediction <- predict(fit, test, type="class")

#Compare the prediction against the true value - CHANGE "Survived"
#   to whatever your target variable is named
test$RightOrWrong <- test$Prediction == test$Survived

#Baseline if we just marked everything as false - CHANGE "Survived"
prop.table(table(test$Survived))

table(test$RightOrWrong) #How many we got right vs. wrong
prop.table(table(test$RightOrWrong)) #Proportion we got right vs. wrong