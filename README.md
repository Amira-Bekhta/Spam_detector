
# Spam Email Detector 📧

This project classifies emails as spam or not spam using the **Spam Email Dataset** from Kaggle. It employs the **Bag of Words (BoW)** model along with preprocessing steps to prepare the text data for classification using **Logistic Regression**.

## Goal 🎯
The goal of this project is to classify whether an email is spam or not. It uses the spam email dataset found on Kaggle, and the preprocessing and model evaluation are implemented using **NLTK**, **pandas**, and **scikit-learn**.

## Technologies 🛠️
- **Python**
- **pandas**
- **scikit-learn**
- **NLTK** (for text preprocessing)
- **Logistic Regression** (for classification)

## Folder Structure 📁
```
/project-root
│
├── /data                  # Dataset, raw and preprocessed
├── /models                # Saved models with X_test and y_test data
├── /notebooks             # Jupyter notebooks for preprocessing, and evaluation
├── /src                   # Source code for loading data, BoW, and training
├── requirements.txt       # Python dependencies
├── setup.py               # Setup script
└── README.md              # This README file
```

## Installation 🔧
1. Clone this repository:
   ```bash
   git clone https://github.com/Amira-Bekhta/Spam_detector 
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Install NLTK and download necessary resources:
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('punkt')
   ```

## Preprocessing 🧹
The dataset undergoes several preprocessing steps:
- Categorical variable encoding (Ham/Spam)
- Text tokenization using NLTK
- Bag of Words model implementation for feature extraction

## Model 🧠
- **Classifier**: Logistic Regression
- **Evaluation Metrics**: 
   - Accuracy Score: 0.98
   - F1 Score: 0.93

## Dataset 📊
This project uses the [Spam Email Dataset](https://www.kaggle.com/datasets/abdallahwagih/spam-emails).