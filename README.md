# Machine-Learning

Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for themselves.

### Types of Machine Learning
Machine learning is sub-categorized to three types:

####  Supervised learning :
Supervised learning is the Data mining task of inferring a function from labelled training data. The training data consist of a set of training examples. In supervised learning, each example is a pair consisting of an input object (typically a vector) and a desired output value (also called the supervisory signal)

	Classification:
		1. Logistic Regression: 
			Logistic regression is a predictive analysis. Logistic regression is used to 
			describe data and to explain the relationship between one dependent binary 
			variable and one or more nominal, ordinal, interval or ratio-level independent 
			variables.

		2. KNN:
			K nearest neighbours is a simple algorithm that stores all available cases and 
			classifies new cases based on a similarity measure (e.g., distance 
			functions). KNN has been used in statistical estimation and pattern 
			recognition already in the beginning of 1970s as a non-parametric technique.

		3. Support Vector Machine(SVM):
			Support Vector Machine (SVM) is primarily a classier method that performs 
			classification tasks by constructing hyperplanes in a multidimensional space 
			that separates cases of different class labels. SVM supports both regression 
			and classification tasks and can handle multiple continuous and categorical 
			variables.

		4. Naive Bayes:
			It is a classification technique based on Bayes Theorem with an assumption of 
			independence among predictors. In simple terms, a Naive Bayes classifier 
			assumes that the presence of a particular feature in a class is unrelated to 
			the presence of any other feature.

		5. Decision Tree:
			Decision tree uses the tree representation to solve the problem in which each 
			leaf node corresponds to a class label and attributes are represented on the
			internal node of the tree.

		6. Random Forest :
			Random forests  are an ensemble learning method for classification, tasks 	
			that operates by constructing a multitude of decision trees at training time  
			and outputting the class that is the mode of the classes or mean prediction 
			of the individual trees


	Regression:
		1. Linear Regression:
			Linear Regression is a machine learning algorithm based on supervised 
			learning. It performs a regression task. Regression models a target prediction 
			value based on independent variables. It is mostly used for finding out the 
			relationship between variables and forecasting.

		2. Multiple Linear Regression:
			Multiple linear regression (MLR), also known simply as multiple regression, is a 
			statistical technique that uses several explanatory variables to predict the 
			outcome of a response variable. The goal of multiple linear regression (MLR) 
			is to model the linear relationship between the explanatory (independent) 
			variables and response (dependent) variable.

		3. Polynomial Regression:
			Polynomial Regression is a form of linear regression in which the relationship 
			between the independent variable x and dependent variable y is modeled as 
			an nth degree polynomial. Polynomial regression fits a nonlinear relationship 
			between the value of x and the corresponding conditional mean of y, denoted 
			E(y |x)

		4. Decision Tree Regression and Random Forest
			Concept same as Classifier, only difference is result set will produce proper
			data. It will not consider only group classsifier as output

------------

####  Unsupervised Learning:
The model learns through observation and finds structures in the data. Once the model is given a dataset, it automatically finds patterns and relationships in the dataset by creating clusters in it. What it cannot do is add labels to the cluster, like it cannot say this a group of apples or mangoes, but it will separate all the apples from mangoes.

Suppose we presented images of apples, bananas and mangoes to the model, so what it does, based on some patterns and relationships it creates clusters and divides the dataset into those clusters. Now if a new data is fed to the model, it adds it to one of the created clusters.

		1. Hierarchical clustering:
			Hierarchical clustering, also known as hierarchical cluster analysis, is an 
			algorithm that groups similar objects into groups called clusters.The endpoint 
			is a set of clusters, where each cluster is distinct from each other cluster, and 
			the objects within each cluster are broadly similar to each other.

		2. K-means:
			K-means clustering is a method of vector quantisation, originally from signal
			processing, that is popular for cluster analysis in data mining. k-means 
			clustering aims to partition n observations into k clusters in which each 
			observation belongs to the cluster with the nearest mean, serving as a 
			prototype of the cluster.


------------


####  Reinforcement Learning:
Reinforcement learning is an area of Machine Learning. Reinforcement. It is about taking suitable action to maximize reward in a particular situation. It is employed by various software and machines to find the best possible behavior or path it should take in a specific situation. Reinforcement learning differs from the supervised learning in a way that in supervised learning the training data has the answer key with it so the model is trained with the correct answer itself whereas in reinforcement learning, there is no answer but the reinforcement agent decides what to do to perform the given task. In the absence of training dataset, it is bound to learn from its experience.

		- Markov Decision Processes:
			A Markov Decision Processes (MDP) is a discrete time stochastic control 
			process. MDP is the best approach we have so far to model the complex 
			environment of an AI agent. Every problem that the agent aims to solve can 
			be considered as a sequence of states S1, S2, S3, … Sn (A state may be for 
			example a Go/chess board configuration). The agent takes actions and moves 
			from one state to an other. In the following you will learn the mathematics 
			that determine which action the agent must take in any given situation.

		- Bellman Equation Markov Reward Processes:
			It writes the "value" of a decision problem at a certain point in time in terms of 
			the payoff from some initial choices and the "value" of the remaining decision 
			problem that results from those initial choices.

		- Temporal Difference: 
			Temporal difference (TD) learning is an approach to learning how to predict a
			quantity that depends on future values of a given signal.The name TD derives
			from its use of changes, or differences, in predictions over successive time
			steps to drive the learning process.

		1. State-Action-Reward-State-Action (SARSA) – On Policy:
			The Sarsa algorithm is an On-Policy algorithm for TD-Learning. The major 
			difference between it and Q-Learning, is that the maximum reward for the 
			next state is not necessarily used for updating the Q-values. Instead, a new 
			action, and therefore reward, is selected using the same policy that 
			determined the original action.The name SARSA actually comes from the fact 
			that the updates are done using the quintuple Q (s, a, r, s', a').

		2. Q-Learning – Off Policy:
			Q-learning is a reinforcement learning technique used in machine learning. 
			The goal of Q-learning is to learn a policy, which tells an agent what action to 
			take under what circumstances. It does not require a model of the 
			environment and can handle problems with stochastic transitions and 
			rewards, without requiring adaptations.


