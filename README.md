# Fundamental-of-AI-and-ML-project-
## Scam Message Detector (Machine Learning Project)

##  About the Project

This project is a simple **Scam Message Detector** built using basic concepts of Machine Learning and Natural Language Processing (NLP).

In daily life, we receive many messages. Some of them are normal (safe), while others are spam or scam messages that try to trick us. These messages may say things like “you won a prize” or “click this link urgently”.

So, I created this project to **automatically detect whether a message is safe or scam** using a machine learning model.


# Steps followed in this project:

Load the dataset from a CSV file
Clean the text (remove punctuation, numbers, etc.)
Convert text into numbers using TF-IDF
Train the model using Naive Bayes algorithm
Test the model and check accuracy


##  How It Works

The system learns from a dataset of messages that are already labeled as:

* **Ham (Safe message)**
* **Spam (Scam message)**

Steps followed in this project:

1. Load the dataset from a CSV file
2. Clean the text (remove punctuation, numbers, etc.)
3. Convert text into numbers using **TF-IDF**
4. Train the model using **Naive Bayes algorithm**
5. Test the model and check accuracy
6. Take user input and predict result



##  Features

* Detects spam/scam messages
* Simple and beginner-friendly code
* Takes user input in real time
* Shows prediction instantly
* Easy to understand and modify



## Project Structure

scam-message-detector/
│── data/
│   └── spam.csv
│── src/
│   └── main.py
│── report/
│   └── project-report.pdf
│── README.md


##  Requirements

You need Python installed. Then install required libraries:


pip install pandas scikit-learn


##  How to Run the Project



3. Run the Python file:

```
python src/main.py
```

4. Enter any message and check result
   Type `exit` to stop the program

##  Example

```
Enter message: You won a free prize click now
Output: ⚠️ This looks like a SCAM message!

Enter message: Let's meet tomorrow
Output: ✅ This seems safe.
```

## 🔹 Technologies And libraries used 

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Naive Bayes Algorithm


##  What I Learned

* Basics of Machine Learning
* How to clean and process text data
* How to convert text into numbers
* How classification models work
* How to build a real-life useful project


##  Future Improvements

* Use bigger dataset for better accuracy
* Add GUI (Graphical Interface)
* Convert into web or mobile app
* Support multiple languages
  

## 🔹 Conclusion

This project shows how machine learning can be used to detect scam messages in real life. By using simple techniques like text processing and Naive Bayes, the system can identify whether a message is safe or not. It helped me understand basic AI concepts and how they can be applied to solve real-world problems.



