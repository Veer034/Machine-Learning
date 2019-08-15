1.CustomClassifier : This file contains custom classifier using sklearn test dataset and scipy methods to find the distance between points. This custom class can predicts the simplest problem in machine learning via predicting the point belongs to which group via shortest distance between other points available in the graphs.

For doing this custom class written CustomPredictKNNAlorithm:
	This class creates 3 methods for solving the problem
	fit(self,x_train,y_train): This method used to store the train data and train result.
	predict(self,x_test): This method is used to predict the result.
	closest(self,row): This method contains the custom code to calculate the nearest point to the passed 	   
					   test value. This method returns the result.

2.NumberClassifier : This file contains custom classifier using MNSIT data to identify the number passed in as input. tensor-flow basic learning algorithm(LinearClassifier) used for learning from data provided in MNSIT.	
