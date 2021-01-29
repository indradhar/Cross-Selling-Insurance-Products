# Cross-Selling-Insurance-Products
Cross Selling Insurance Products using machine learning algorithms

Your client is an Insurance company that has provided Health Insurance to its customers for many years. Now they need your help in building a model to predict whether the policyholders (customers) from past years will also be interested in Vehicle Insurance provided by the company.

For example, you may pay a premium of Rs. 5000 each year for a health insurance cover of Rs. 200,000/- so that if, God forbid, you fall ill and need to be hospitalised in that year, the insurance provider company will bear the cost of hospitalisation etc. for upto Rs. 200,000. Now if you are wondering as to how the company bears such a high hospitalisation cost when it charges a premium of only Rs. 5000/-, that is where the concept of probabilities comes in picture. For example, like you, there may be 100 customers who would be paying a premium of Rs. 5000 every year, but only a few of them (say 2-3) would get hospitalised that year and not everyone. This way everyone shares the risk of everyone else.

Just like medical insurance, there is vehicle insurance where every year customer needs to pay a premium of a certain amount to insurance provider company so that in case of unfortunate accident by the vehicle, the insurance provider company will provide compensation (called ‘sum assured’) to the customer.

Building a model to predict whether a customer would be interested in Vehicle Insurance is extremely helpful for the company because it can then accordingly plan its communication strategy to reach out to those customers and optimise its business model and revenue, without annoying all customers including those unlikely to buy car insurance.

In order to predict, whether the customer would be interested in Vehicle insurance, you have the following information:

Id: Unique ID for the customer
Gender:Gender of the customer
Age: Age of the customer
Driving_License: 0 : Customer does not have DL, 1 : Customer already has DL
Region_Code: Unique code for the region of the customer
Previously_Insured: 1 : Customer already has Vehicle Insurance, 0 : Customer doesn't have Vehicle Insurance
Vehicle_Age: Age of the Vehicle
Vehicle_Damage: 1 : Customer got his/her vehicle damaged in the past. 0 : Customer didn't get his/her vehicle damaged in the past.
Annual_Premium: The amount customer needs to pay as premium in the year
PolicySalesChannel: Anonymized Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc.
Vintage: Number of Days, Customer has been associated with the company
Response: 1: Customer is interested, 0: Customer is not interested in buying car insurance
Using the data provided:

Undertake Exploratory Data Analysis to identify patterns in the data to discover insights that could help you build better models 
Build models using the standard classification algorithms that you have studied during the course i.e. logistic regression, k-nearest neighbour, naive Bayes, decision trees, support vector machines, random forest and gradient boosted decision trees 
Noting the skew in the distribution, study methods for addressing the skew using over or under-sampling and SMOTE and apply them to the problem 
Use methods discussed in class for hyperparameter tuning of the models 
Using area under ROC curve to select the best performing model 
Deploy the model as a FLASK API 
