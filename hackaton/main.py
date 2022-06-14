"""
The mean, standard error and “worst” or largest (mean of the three largest values) of these features were computed for each image, resulting in 30 features. For instance, field 3 is Mean Radius, field 13 is Radius SE, field 23 is Worst Radius.
"""
import wget
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

"""
Download data from the UCI Machine Learning Repository
link = 'https://ftp.cs.wisc.edu/math-prog/cpo-dataset/machine-learn/cancer/WDBC/WDBC.dat'
wget.download(link)
"""

df = pd.read_table("WDBC.dat", sep=",", header=None)
df.columns = ["id","diagnosis","radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"]

df['diagnisis_int'] = np.where(
    df['diagnosis'] == 'M', 1, 0
    )
X = df.iloc[:,2:32].values
Y = df.iloc[:,32].values
print(X.shape)
# check the distribution of the data
n_bins = 20
for col in df.columns[1:32]:
    plt.hist(df[col], bins=n_bins, alpha=0.5, label=col)
    plt.legend(loc='upper right')
    plt.title("Histogram of %s" % col)
#    plt.show()

# show missing values
# print('Null values: ', df.isnull().sum())
# print('Is NOT a number: ', df.isna().sum())

# convert categorical data into numbers
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)


# split data to create training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

# transforming your data so that it fits within a specific scale
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Using Logistic Regression Algorithm to the Training Set
from sklearn.linear_model import LogisticRegression
classifier_reg = LogisticRegression(random_state = 0)
classifier_reg.fit(X_train, Y_train)

# Using KNeighborsClassifier Method of neighbors class to use Nearest Neighbor algorithm
from sklearn.neighbors import KNeighborsClassifier
classifier_nei = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier_nei.fit(X_train, Y_train)

# Using SVC method of svm class to use Support Vector Machine Algorithm
from sklearn.svm import SVC
classifier_svc_linear = SVC(kernel = 'linear', random_state = 0)
classifier_svc_linear.fit(X_train, Y_train)

# Using SVC method of svm class to use Kernel SVM Algorithm
from sklearn.svm import SVC
classifier_svc_rbf = SVC(kernel = 'rbf', random_state = 0)
classifier_svc_rbf.fit(X_train, Y_train)

# Using GaussianNB method of naïve_bayes class to use Naïve Bayes Algorithm
from sklearn.naive_bayes import GaussianNB
classifier_gau = GaussianNB()
classifier_gau.fit(X_train, Y_train)

# Using DecisionTreeClassifier of tree class to use Decision Tree Algorithm
from sklearn.tree import DecisionTreeClassifier
classifier_tre = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier_tre.fit(X_train, Y_train)

# Using RandomForestClassifier method of ensemble class to use Random Forest Classification algorithm
from sklearn.ensemble import RandomForestClassifier
classifier_for = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier_for.fit(X_train, Y_train)


# predict test and set results
Y_pred = classifier_for.predict(X_test)
print('accuracy ForestClassifier: ', np.mean(Y_pred == Y_test))
print('score ForestClassifier: ', classifier_for.score(X_test, Y_test))

# tabulating the number of mis-classifications
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
print(cm)