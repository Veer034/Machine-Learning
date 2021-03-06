import random
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from scipy.spatial import distance

def euc(a,b):
	return distance.euclidean(a,b)
	
class CustomPredictKNNAlorithm():
	def fit(self,x_train,y_train):
		self.x_train=x_train
		self.y_train=y_train
		
	def predict(self,x_test):
		predictions =[]
		for row in x_test:
			label= self.closest(row)
			predictions.append(label)
		return predictions
		
	# Custom Method for choosing the nearest suitable point	
	def closest(self,row):
		best_dist = euc(row,x_train[0])
		best_index = 0
		for i in range(1,len(x_train)):
			dist =euc(row,x_train[i])
			if dist<best_dist:
				best_dist=dist
				best_index=i
		return self.y_train[best_index]
		
iris= datasets.load_iris()
x= iris.data
y= iris.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.5)

# Library for learning from input data and predict the output
#from sklearn.neighbors import KNeighborsClassifier
#my_classifier = KNeighborsClassifier()

my_classifier = CustomPredictKNNAlorithm()
my_classifier.fit(x_train,y_train)

predictions = my_classifier.predict(x_test)

# accuracy_score method used to calculate the result in form of correct prediction done by method.
print(accuracy_score(y_test,predictions))
