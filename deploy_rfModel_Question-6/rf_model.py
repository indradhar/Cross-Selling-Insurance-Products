from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

from imblearn.over_sampling import SMOTE
import pickle
df = pd.read_csv(r"Insurance cross sell.csv")
df.drop('id',axis=1,inplace=True)
gender=pd.get_dummies(df['Gender'],drop_first=True)
vehicle_age=pd.get_dummies(df['Vehicle_Age'],drop_first=True)
vehicle_damage=pd.get_dummies(df['Vehicle_Damage'],drop_first=True)
df= pd.concat([df,gender,vehicle_age,vehicle_damage],axis=1)
df.drop(['Gender','Vehicle_Age','Vehicle_Damage',],axis=1,inplace=True)
X= df.drop('Response',axis=1)
Y= df['Response']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=42)

sm = SMOTE(random_state=2)
X_train_res, Y_train_res = sm.fit_sample(X_train, Y_train.ravel())

classifier = RandomForestClassifier()

classifier.fit(X_train_res, Y_train_res)


# Saving model to disk
pickle.dump(classifier, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
result = model.score(X_test,Y_test)
if(result>0.5):
  result = 1
else:
  result=0
print(result)