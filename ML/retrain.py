import os
import pandas as pd
import glob
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score
import pickle

def train(cv, model, cv_file_path, model_file_path):
    data_file_path = os.path.join("Datasets", "ytData")
    all_files = glob.glob(os.path.join(data_file_path, "*.csv"))

    data = []
    for file in all_files:
        try:
            frame = pd.read_csv(file, index_col=None, header=0)
            data.append(frame)
        except Exception as e:
            print(f"Error reading {file}: {e}")

    data = pd.concat(data, axis=0, ignore_index=True)
    data = data[["CONTENT", "CLASS"]]
    data.loc[:, "CLASS"] = data["CLASS"].map({0: "Not Spam", 1: "Spam Comment"})

    comments = data["CONTENT"].values
    classifications = data["CLASS"].values

    comments_transformed = cv.fit_transform(comments)
    commentTrain, commentTest, classTrain, classTest = train_test_split(comments_transformed, classifications, test_size=0.2, random_state=6)

    model.fit(commentTrain, classTrain)
    classPred = model.predict(commentTest)

    accuracy = accuracy_score(classTest, classPred)
    print("Accuracy: ", accuracy)

    # Save CountVectorizer and BernoulliNB model
    pickle.dump(cv, open(cv_file_path, 'wb'))
    pickle.dump(model, open(model_file_path, 'wb'))
    print(f"Vectorizer and model saved as {cv_file_path} and {model_file_path} respectively.")

    return cv, model

if __name__ == "__main__":
    cv = CountVectorizer()
    model = BernoulliNB()
    cv_file = 'vectorizer.pkl'
    model_file = 'detectionModel.pkl'

    train(cv, model, cv_file, model_file)