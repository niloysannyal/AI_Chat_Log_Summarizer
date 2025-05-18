# utils.py
import re
from collections import Counter, defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

STOPWORDS = set(stopwords.words('english'))


def parse_chat_log(text):
    messages = defaultdict(list)
    lines = text.strip().split("\n")
    for line in lines:
        if line.startswith("User:"):
            messages["User"].append(line[5:].strip())
        elif line.startswith("AI:"):
            messages["AI"].append(line[3:].strip())
    return messages


def get_statistics(messages):
    total = sum(len(msgs) for msgs in messages.values())
    return {
        "total_messages": total,
        "user_messages": len(messages["User"]),
        "ai_messages": len(messages["AI"])
    }


def extract_keywords(messages):
    all_text = " ".join(messages["User"] + messages["AI"])
    words = re.findall(r'\b\w+\b', all_text.lower())
    filtered_words = [w for w in words if w not in STOPWORDS]
    counter = Counter(filtered_words)
    return [word for word, _ in counter.most_common(5)]


def generate_summary(stats, keywords):
    summary = (
        f"Summary:\n"
        f"- Total exchanges: {stats['total_messages']}\n"
        f"- User messages: {stats['user_messages']}, AI messages: {stats['ai_messages']}\n"
        f"- Most common keywords: {', '.join(keywords)}"
    )
    return summary
