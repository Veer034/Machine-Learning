1.CustomClassifier : This file contains custom classifier using sklearn test dataset and scipy methods to find the distance between points. This custom class can predicts the simplest problem in machine learning via predicting the point belongs to which group via shortest distance between other points available in the graphs.

For doing this custom class written CustomPredictKNNAlorithm:
	This class creates 3 methods for solving the problem
	fit(self,x_train,y_train): This method used to store the train data and train result.
	predict(self,x_test): This method is used to predict the result.
	closest(self,row): This method contains the custom code to calculate the nearest point to the passed 	   
					   test value. This method returns the result.

2.NumberClassifier : This file contains custom classifier using MNSIT data to identify the number passed in as input. tensor-flow basic learning algorithm(LinearClassifier) used for learning from data provided in MNSIT.	

3.DecisionTreeClassifier : This file contains code to identify the the type of tree based on passed combination of input values. This Classifier makes a tree structure based on the passed data. Tree structure keep on getting created till the leaf node reached, where no further node can be created. Based on that result will be calculated for the passed test input data. 

4.Reinforcement learning : It refers to goal-oriented algorithms, which learn how to attain a complex objective (goal) or maximize along a particular dimension over many steps; for example, maximize the points won in a game over many moves.

4.1 Q-Learning:
	This contains the implementation of the Q learning algorithm implementation. Also used matplotlib library to show the UI for 2D Games. In given code can be customised based on the passed argument. A map is created for the 2DGame, in which all the possible movement of item along with reward points. As the game starts , system will make random steps. But, as the game progress system will start taking decision based on the reward points for each action. 


				   
				   