
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from imblearn.under_sampling import RandomUnderSampler
from scipy import stats
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.cluster import KMeans
import warnings
#filter to ignore any sklearn convergance warnings
warnings.filterwarnings("ignore")





#used dropna to get rid of any empty rows on both datasets
df1 = pd.read_csv("loan.csv")
df1 = df1.dropna()

df2 = pd.read_csv("laptop.csv")
df2 = df2.dropna()

def Task1():
    #use datetime to convert age columns to date object and subtract the days to get age in days
    df1["s_age"] = pd.to_datetime(df1["DoB"], dayfirst=True)
    df1["r_age"] = pd.to_datetime(df1["DoR"], dayfirst=True)
    df1["age"] = (df1["r_age"] - df1["s_age"]).dt.days
    #use labelencoder to convert education values to numeric so it can be used with the classifier
    l_encoder = preprocessing.LabelEncoder()
    df1["education"] = l_encoder.fit_transform(df1["education"])
    #both targets for training and testing and the datas used to predict
    target_a = df1[:]["loan"]
    target_b = df1[:]["y"]
    data = df1[:][["balance","education","age"]]
    #use traintestsplit to create the training and test sets and use stratify to ensure no bias 
    data_train,data_test,targeta_train,targeta_test = train_test_split(data,target_a,test_size=0.2,stratify=target_a)
    clfa = tree.DecisionTreeClassifier() #tree classifier for prediction
    clfa.fit(data_train,targeta_train)
    print("Loan prediction: ")
    print(clfa.predict(data_test)) # using predict()
    print("Loan prediction accuracy: ")
    print(accuracy_score(targeta_test, clfa.predict(data_test))) # printing out accuracy score
    # same as above except the target is "y"
    data_train_b, data_test_b,targetb_train,targetb_test = train_test_split(data,target_b,test_size=0.2,stratify=target_a)
    clfb = tree.DecisionTreeClassifier()
    clfb.fit(data_train_b,targetb_train)
    print("Y prediction: ")
    print(clfb.predict(data_test_b))
    print("Y prediction accuracy: ")
    print(accuracy_score(targetb_test, clfb.predict(data_test_b)))
Task1()    


def Task2():
    #datetime again but to get year difference
    df1["s_age"] = pd.to_datetime(df1["DoB"], dayfirst=True)
    df1["r_age"] = pd.to_datetime(df1["DoR"], dayfirst=True)
    df1["age"] = (df1["r_age"].dt.year - df1["s_age"].dt.year)
    l_encoder = preprocessing.LabelEncoder()
    df1["education"] = l_encoder.fit_transform(df1["education"])
    
    target = df1[:]["y"]
    data = df1[:][["balance","education","age"]]
    #useing imbalanced learn libary for its randomundersampler to balance the input
    rus = RandomUnderSampler(sampling_strategy=1)
    bal_data,bal_target = rus.fit_resample(data,target)
    
    data_train,data_test,target_train,target_test = train_test_split(bal_data,bal_target,test_size=0.33,stratify=bal_target)
    # apeening the 5 supervised models to be used
    models = []
    accuracy = []
    model_name = []
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('DTC', tree.DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC()))
    models.append(('RFS',RandomForestClassifier()))
    #for loop to make a predicition using each model
    for name, model in models:
        model.fit(data_train,target_train)
        pred = model.predict(data_test)
        accuracy.append(accuracy_score(target_test,pred))
        model_name.append(name)
        print(pred)
        print(name, "Accuracy:" ,accuracy_score(target_test,pred))
        #using a bar chart to visualize the accuracy of each model
    colors = ["red","green","blue","orange", "purple"]
    plt.bar(model_name,accuracy, color=colors)
    plt.title("Comparing Accuracy Between Multiple Classification Models")
    plt.xlabel("Model")
    plt.ylabel("Accuracy")
    plt.show()
Task2()


def Task3():
    #using interquartile range to detect and exclude outliers from the dataset
    q1 = df1["duration"].quantile(0.25)
    q3 = df1["duration"].quantile(0.75)
    iqr = q3-q1
    threshold = 3
    outlier = (df1["duration"] < q1 - threshold * iqr) | (df1["duration"] > q3 + threshold * iqr)
    df = df1[~outlier]
    
    l_encoder = preprocessing.LabelEncoder()
    df["education"] = l_encoder.fit_transform(df["education"])
    df["job"] = l_encoder.fit_transform(df["job"])
    df["marital"] = l_encoder.fit_transform(df["marital"])
    
    target = df[:]["y"]
    data = df[:][["education","job","marital"]]
    
    data_train,data_test,target_train,target_test = train_test_split(data,target,test_size=0.33,stratify=target)
    clfa = tree.DecisionTreeClassifier()
    clfa.fit(data_train,target_train)
    print("Y preiction")
    print(clfa.predict(data_test))
    print(accuracy_score(target_test, clfa.predict(data_test)))
Task3()


def Task4():
    
    l_encoder = preprocessing.LabelEncoder()
    df2["CPU_Type"] = l_encoder.fit_transform(df2["CPU_Type"])
    df2["Memory"] = l_encoder.fit_transform(df2["Memory"])
    target = df2[:]["Price"]
    data = df2[:][["CPU_Frequency","RAM","Memory","CPU_Type"]]
   
    data_train,data_test,target_train,target_test = train_test_split(data,target,test_size=0.33)
    rf = RandomForestRegressor(n_estimators=100) # using random forest to predict the price
    rf.fit(data_train,target_train)
    print(rf.predict(data_test))
    # using sklearn metrics to calculate error score and r2 score
    mae_test = mean_absolute_error(target_test, rf.predict(data_test))
    mse_test = mean_squared_error(target_test, rf.predict(data_test))
    r2_test = r2_score(target_test, rf.predict(data_test))
    print(f"Mean Absolute Error (MAE): {mae_test}")
    print(f"Mean Squared Error (MSE): {mse_test}")
    print(f"R² Score: {r2_test}")
   #same as above but for the training data
    mae_train = mean_absolute_error(target_train, rf.predict(data_train))
    mse_train = mean_squared_error(target_train, rf.predict(data_train))
    r2_train = r2_score(target_train, rf.predict(data_train))
    print(f"Mean Absolute Error (MAE) for training data: {mae_train}")
    print(f"Mean Squared Error (MSE): {mse_train}")
    print(f"R² Score: {r2_train}")
    #getting correlation of each data column and graphing the one withthe most correalation
    freq_corr = df2["Price"].corr(df2["CPU_Frequency"])
    ram_corr = df2["Price"].corr(df2["RAM"])
    mem_corr = df2["Price"].corr(df2["Memory"])
    cputype_corr = df2["Price"].corr(df2["CPU_Type"])
    print(freq_corr,ram_corr,mem_corr,cputype_corr)
    
    plt.scatter(df2["RAM"], df2["Price"], color='blue')
    plt.title("Correlation between Price (EUR) and RAM (GB)")
    plt.xlabel("RAM (GB)")
    plt.ylabel("Price (EUR)")
    plt.grid(True)
    plt.show()
    
Task4()


def Task5():
    q1 = df2["Price"].quantile(0.25)
    q3 = df2["Price"].quantile(0.75)
    iqr = q3-q1
    threshold = 3
    outlier = (df2["Price"] < q1 - threshold * iqr) | (df2["Price"] > q3 + threshold * iqr)
    df = df2[~outlier]
    
    l_encoder = preprocessing.LabelEncoder()
    df["CPU_Type"] = l_encoder.fit_transform(df["CPU_Type"])
    df["Memory"] = l_encoder.fit_transform(df["Memory"])
    #using pd.cut() to create a new column that assings the price calues to new labels based on the bin values specified so it can be used in a classifier algorithm
    df = df.assign(cost=pd.cut(df["Price"], bins=[0,300,1000,1000000], labels=["Budget", "Mid_range","High end"]))

    target = df[:]["cost"]
    data = df[:][["CPU_Frequency","RAM","Memory","CPU_Type"]]
    
    data_train,data_test,target_train,target_test = train_test_split(data,target,test_size=0.33,stratify=target)
    clfa = tree.DecisionTreeClassifier()
    clfa.fit(data_train,target_train)
    print(clfa.predict(data_test))
    print(accuracy_score(target_test, clfa.predict(data_test)))
Task5()


def Task6():
    #creating a dataframe of the 2 input data columns then using fillna. to fill empty rows with the mean value
    flt = df2[["Inches","RAM"]]
    flt = flt.fillna(flt.mean())
    min_max = preprocessing.MinMaxScaler()
    flt = min_max.fit_transform(flt)
    #using a for loop to run the kmeans unsepervised algorithm on 8 clusters as specified i the range then appending the inertia to the list
    inertia_value = []
    cluster = range(1,9)
    for i in cluster:
        kmeans = KMeans(n_clusters=i, random_state=0).fit(flt)
        inertia_value.append(kmeans.inertia_)
        #plotting an elbow curve of the data obtained from kmeans
    plt.plot(cluster,inertia_value, marker="o")
    plt.title("K-Means Cluster Elobow Curve")
    plt.xlabel("# of Clusters")
    plt.ylabel("Inertia")
    plt.grid(True)
    plt.show()
Task6()
