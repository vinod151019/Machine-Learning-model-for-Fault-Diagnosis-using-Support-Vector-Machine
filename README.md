# Machine-Learning-model-for-Fault-Diagnosis-using-Support-Vector-Machine
It's a machine learning model for fault diagnosis of gearbox using support vector machine for vibration data at differnt speeds (500 rpm,750 rpm,1000 rpm) for four gears.
From raw vibration data we acquired eight features of each column (i.e mean, sum, minimum, maximum, std, variance, kurtosis, skewness) using python pre defined functions.
Out 8 features we selected best 6 fixtures using decision tree.
Then we standardize the data using standard scaler.
we have created SVM model and dump into pickel file.
So the input data will be in the form .csv file having six features, this data should be standardize then only you should give data to the model.
Then this model has been deployed in heroku platform.
