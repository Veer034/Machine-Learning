1. Custom Classifier : This file contains custom classifier using sklearn test dataset and scipy methods to find the distance between points. This custom class can predicts the simplest problem in machine learning via predicting the point belongs to which group via shortest distance between other points available in the graphs.

For doing this custom class written CustomPredictKNNAlorithm:
	This class creates 3 methods for solving the problem
	fit(self,x_train,y_train): This method used to store the train data and train result.
	predict(self,x_test): This method is used to predict the result.
	closest(self,row): This method contains the custom code to calculate the nearest point to the passed 	   
					   test value. This method returns the result.

2. Number Classifier : This file contains custom classifier using MNSIT data to identify the number passed in as input. tensor-flow basic learning algorithm(LinearClassifier) used for learning from data provided in MNSIT.	

3. Logistic Regression :  This file contains classifier that will be used to classify whether the person will buy car or not, this data will be used by car manufacturing company for focusing on customer with higher expectation of buying car. 
            For performing the task,LogisticRegression class used of sklearn.linear_model
            Data collection point after log in  kaggle: https://www.kaggle.com/rakeshrau/social-network-ads
            Test Graphical Result:

4. K-Nearest Neighbors : This file contains classifier for performing classification with nearest neighbor algorithm. In this algorithm when ever decision need to be made about new point. Nearest point will be considered for classification of new point. "K" points will be considered for making the classification of the new point. K values should always have odd number for proper use of the classifier.
            For performing the task,KNeighborsClassifier class used of sklearn.neighbors
            Data collection point after log in  kaggle: https://www.kaggle.com/rakeshrau/social-network-ads
            Test Graphical Result:
            
5. Support Vector Classification : This file contains classifier for performing same as Logistic Regression, but this classifier use SVM algorithm for setting correct classification.In SVC() constructor kernel value passed as "linear". In this we create a line between the two points(support vector) with maximum distance 
            For performing the task,SVC class used of sklearn.svm
            Data collection point after log in  kaggle: https://www.kaggle.com/rakeshrau/social-network-ads
            Test Graphical Result:

6. Kernel Support Vector Classification : This file contains classifier for performing classification using SVM algorithm for setting correct classification.In SVC() constructor kernel value passed as "rbf". This algorithm change the dimesion of data for dividing the data into two classes. for more details can look into this site :https://towardsdatascience.com/understanding-support-vector-machine-part-2-kernel-trick-mercers-theorem-e1e6848c6c4d
            For performing the task,SVC class used of sklearn.svm
            Data collection point after log in  kaggle: https://www.kaggle.com/rakeshrau/social-network-ads
            Test Graphical Result:

7. Naive Bayes : This file contains classifier for performing classification based on naive bayes algorithm. In this we try to find out probability of happening an event A, given that B has already happened.Formula of relative probability: P(A|B) = P(B|A)P(A)/P(B) .For more details  https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c
             For performing the task,GaussianNB class used of sklearn.naive_bayes
            Data collection point after log in  kaggle: https://www.kaggle.com/rakeshrau/social-network-ads
            Test Graphical Result:
            
8. Decision Tree Classification: This file contains implementation based on decision tree algorithm. We keep on dividing the data till we get the group of data belonging to particular group properly. For bigger data, sometimes we need to set threshold rule for making sure. No, more division is performed on the data.
            For performing the task, DecisionTreeClassifier class used of sklearn.tree
            Data collection point after log in  kaggle: https://www.kaggle.com/akram24/position-salaries
            Test Grabhical Result:
            
5. Random Forest Classification: This file contains implementation of sales team assumption of possible customer for sales of car just like decision tree regression model, but with multiple iteration to find out the best solution of making the assumption about possibility of purchase. We are setting n_estimators ,which will make sure the number of trees used for making the assumption.
            For performing the task,RandomForestClassifier class used of sklearn.ensemble
            Data collection point after log in  kaggle: https://www.kaggle.com/akram24/position-salaries
            Test Graphical Result:
