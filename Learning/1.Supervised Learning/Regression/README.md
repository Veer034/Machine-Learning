#### 1. Simple Linear Regression : 
This file contains implementation of linear regression model for making assumption on salary based on user's year of experience. We are using simple linear regression as we are making assumptions based on one variable year of experience.

- For performing the task, LinearRegression class used of sklearn.linear_model package.
- Data collection point after login in kaggle: https://storage.googleapis.com/kaggle-datasets/10624/14867/salary-data-simple-linear-regression.zip
Graphical Result:
 
#### 2. Multiple Linear Regression: 
This file contains implementation of multiple linear regression for making the assumption probable point of making more profit in the city for start-up. To make sure company spent money on the correct area and department, these attribute will help in making assumption of correct bussiness expenditure i.e R&D Spend, Administration	, Marketing Spend, State. Here we have multiple attributes which will impact on the company profit.
- For performing the task, LinearRegression class used of sklearn.linear_model package.
- Data collection point after login in kaggle: https://www.kaggle.com/farhanmd29/50-startups

#### 3. Polynomial Regression : 
This file contains implementation of salary assumption of individual based on position applied by the person. As with experience salary increases exponentially, polynomial algorithm has been used. Linear regression won't work in these scenario. We have set degree using method, which will create the be used by LinearRegression for prediction of accurate salary based on position.
- For performing the task, PolynomialFeatures class used of sklearn.preprocessing packages.
- Data collection point after log in  kaggle: https://www.kaggle.com/akram24/position-salaries
Graphical Result:

#### 4. Decision Tree Regression: 
This file contains implementation of salary assumption of individual as applied in polynomial regression, but using different regression model for computing the salary of the user. In decision tree we keep on dividing the data till we get the group of data belonging to particular group properly. For bigger data, sometimes we need to set threshold rule for making sure. No, more division is performed on the data.
- For performing the task, DecisionTreeRegressor class used of sklearn.tree
- Data collection point after log in  kaggle: https://www.kaggle.com/akram24/position-salaries
Graphical Result:

#### 5. Random Forest Regression:
This file contains implementation of salary assumption of individual as applied in decision tree regression model, but with multiple iteration to find out the best solution of making the assumption about salary of the user. We are setting n_estimators ,which will make sure the number of trees used for making the assumption.
- For performing the task,RandomForestRegressor class used of sklearn.ensemble
- Data collection point after log in  kaggle: https://www.kaggle.com/akram24/position-salaries
Graphical Result:
