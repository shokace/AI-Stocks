import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB

def load_model_and_vectorizer(model_file_path, vectorizer_file_path):

    # Load the trained model and vectorizer from the specified file paths
    with open(vectorizer_file_path, 'rb') as vec_file:
        vectorizer = pickle.load(vec_file)

    with open(model_file_path, 'rb') as model_file:
        model = pickle.load(model_file)


    return model, vectorizer

def classify_comment(comment, model, vectorizer):
    
    # Transform the comment using the loaded vectorizer
    comment_transformed = vectorizer.transform([comment])

    # Predict the class of the comment using the loaded model
    prediction = model.predict(comment_transformed)
    return prediction[0]



if __name__ == "__main__":

    # File paths for the saved model and vectorizer
    model_file = 'detectionModel.pkl'
    vectorizer_file = 'vectorizer.pkl'

    # Load the model and vectorizer
    model, vectorizer = load_model_and_vectorizer(model_file, vectorizer_file)

    # Sample comment to classify
    sample_comment = "This is a great video, thanks for sharing!"

    # Classify the comment
    prediction = classify_comment(sample_comment, model, vectorizer)

    # Print the classification result
    print(f"The comment '{sample_comment}' is classified as: {prediction}")

