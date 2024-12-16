"""
Print total words

Top 20 Words and it's count
"""
from collections import Counter
import re

WordCount = {}

LinesWithoutNewline = []
with open("shakespeare.txt", "r", encoding="utf-8") as f:
    filecontent = f.read()
    words = re.findall(r"[0-9a-zA-Z'-]+", filecontent)
    words = [word.upper() for word in words]
    print(f'Total words {len(words)}')
    
    
    CountWords = Counter(words)
    for count in CountWords.most_common(20):
        print(f'{count[0]} - {count[1]}')
        

