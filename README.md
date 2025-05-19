# 🤖 AI Chat Log Summarizer 💬

A Python-based tool that analyzes AI chat logs saved in plain `.txt` files. It parses dialogues between the user and AI, extracts key insights, and generates summaries with useful statistics and keywords.

---

## 🎯 Project Objective

This project aims to:  
- Automatically process multiple `.txt` chat log files  
- Extract and display basic statistics (e.g., total exchanges, number of user/AI messages)  
- Identify the most common keywords used in the conversations  
- Generate human-readable summaries  

Useful for analyzing AI conversation behavior, reviewing chatbot interactions, or organizing large chat logs.

---

## 📁 Project Structure
~~~
AI_Chat_Log_Summarizer/ 
│
├──chat_logs          # Sample chat logs
│  ├── chat1.txt
│  └── chat2.txt
├── main.py           # Entry point to process all .txt logs 
├── utils.py          # Core logic: parsing, statistics, keyword extraction 
└── README.md         # Project documentation
~~~


## 🛠️ Requirements

- Python 3.6 or higher  
- nltk  
- scikit-learn  

Install dependencies with:

```bash
pip install nltk scikit-learn

```

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/niloysannyal/AI_Chat_Log_Summarizer.git
```
### 2. Navigate to the project folder

```
cd AI_Chat_Log_Summarizer
```

### 4. Run the script

python main.py

All .txt files in the current folder will be processed, and summaries will be printed to the terminal.

---
## 💡 Testing

### Sample Inputs: 
**chat1.txt**
```
User: Hello! 
AI: Hi! How can I assist you today? 
User: Can you explain what machine learning is? 
AI: Certainly! Machine learning is a field of AI that allows systems to learn from data.
```

**chat2.txt**
```
User: Hi, can you tell me about Python? 
AI: Sure! Python is a popular programming language known for its readability. 
User: What can I use it for? 
AI: You can use Python for web development, data analysis, AI, and more.
```

### Sample Output:
```
Processing: ./chat2.txt
Summary:
- Total exchanges: 4
- User messages: 2, AI messages: 2
- Most common keywords: python, use, hi, tell, sure

--------------------------------------------------



Processing: ./chat1.txt
Summary:
- Total exchanges: 4
- User messages: 2, AI messages: 2
- Most common keywords: machine, learning, hello, explain, hi

--------------------------------------------------


[Program finished]
```
