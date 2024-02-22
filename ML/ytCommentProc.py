import os
import pandas as pd
import glob

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score


def train(cv, model):
    data_file_path = os.path.join("Datasets", "ytData")
    all_files = glob.glob(os.path.join(data_file_path, "*.csv"))

    data = []
    for file in all_files:
        frame = pd.read_csv(file, index_col=None, header=0)
        data.append(frame)
        
    data = pd.concat(data, axis=0, ignore_index=True)


    data = data[["CONTENT", "CLASS"]]
    data.loc[:, "CLASS"] = data["CLASS"].map({0: "Not Spam", 1: "Spam Comment"})
    data.head()


    comment = data["CONTENT"].values
    classification = data["CLASS"].values

    
    comment = cv.fit_transform(comment)

    commentTrain, commentTest, classTrain, classTest = train_test_split(comment, classification, test_size=0.2, random_state=6)

    
    model.fit(commentTrain, classTrain)
    classPred = model.predict(commentTest)

    accuracy = accuracy_score(classTest, classPred)
    print("Accuracy: ", accuracy)
    
    return cv, model

if __name__ == "__main__":

    cv = CountVectorizer()
    model = BernoulliNB()


    train(cv, model)
    sample = "hey, add me on kik, i'll send you all kinds of stuff ;) @kimmi1443"
    vectorized_sample = cv.transform([sample])
    classPred = model.predict(vectorized_sample)
    print(classPred)
