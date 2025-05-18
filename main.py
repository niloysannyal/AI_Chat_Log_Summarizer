# main.py
import os
from utils import parse_chat_log, get_statistics, extract_keywords, generate_summary


def process_file(file_path):
    print(f"Processing: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    messages = parse_chat_log(content)
    stats = get_statistics(messages)
    keywords = extract_keywords(messages)
    summary = generate_summary(stats, keywords)

    print(summary)
    print("\n" + "-"*50 + "\n")


def main():
    folder_path = "chat_logs"
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            process_file(os.path.join(folder_path, filename))


if __name__ == "__main__":
    main()
