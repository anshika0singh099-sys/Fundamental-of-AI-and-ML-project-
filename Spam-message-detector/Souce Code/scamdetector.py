# Scam Message Detector
 
#Using libraries panda,re,string

import pandas as pd
import re
import string

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


#  Loading the dataset

print("Loading dataset...")

data = pd.read_csv(r"C:\Users\anshi\OneDrive\Desktop\aiml\spam.csv", encoding='latin-1')
# Convert labels into numbers (ham = 0, scam/spam = 1)
data['label'] = data['label'].map({'ham': 0, 'spam': 1})


# Step 2: Cleaning  the text

def clean_message(text):
    text = text.lower()  # make lowercase
    text = re.sub(r'\d+', '', text)  # remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    return text

print("Cleaning messages...")
data['message'] = data['message'].apply(clean_message)


# Prepare training and testing data

X = data['message']
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


 # Converting text into numbers (TF-IDF)

vectorizer = TfidfVectorizer(stop_words='english')

X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)


#  Train the model

print("Training the model...")
model = MultinomialNB()
model.fit(X_train_vectors, y_train)


# Checking accuracy

predictions = model.predict(X_test_vectors)
accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy: {accuracy:.2f}")


#  Testing with input

print("\nScam Detector is ready!")
print("Type a message and I will tell you if it's a scam.\n")

while True:
    user_input = input("Enter message (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    cleaned_input = clean_message(user_input)
    vector_input = vectorizer.transform([cleaned_input])

    result = model.predict(vector_input)

    if result[0] == 1:
        print("⚠️ This looks like a SCAM message!\n")
    else:
        print("✅ This seems safe.\n")
        