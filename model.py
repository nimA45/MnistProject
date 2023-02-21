import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def model(file): 
    train = pd.read_csv(file)
    test = pd.read_csv("fashion-mnist_test.csv")
    train_label = train["label"]
    train.drop("label", axis = 1 , inplace=True)
    test_label = test["label"]
    test.drop("label", axis = 1 , inplace=True)


    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(train, train_label)

    y_pred = clf.predict(test)
    acc = accuracy_score(test_label, y_pred)
    print("Accuracy on validation set: {:.2f}%".format(acc * 100))
    fichier =  open(file + "_accuracy.txt", "a")
    fichier.write(str(acc))

    import joblib

    # Save the model to disk
    filename ='trained_model.joblib'
    joblib.dump(clf, filename)
import sys
 
def file(i):
    print (i)
 
if __name__ == '__main__':
    print ('sys.argv:'), sys.argv
    if len(sys.argv) > 1:
        file = (sys.argv[1])
        model(file)
   
    else:
        file('No such file')