import jieba
import re
import json
from collections import Counter

cut_words = ""

for line in open('./comments.json',encoding='utf-8'):
    line.strip('\n')
    line = re.sub("[A-Za-z0-9\“\”\，\。\：]", "", line)#去除特殊字母符号
    seg_list=jieba.cut(line) #默认精确模式
    cut_words += (" ".join(seg_list))
words = cut_words.split()
print(words)

c = Counter()
print(c)
for i in words:
    if len(i)>1 and i != '\r\n':
        c[i] += 1

comments = []
for k,v in c.most_common(200):
    comment = {}
    comment["name"] = k
    comment["value"] = v
    comments.append(comment)
    print(comment)
with open('wordCount.json', 'a', encoding='utf-8') as f:
    f.write(json.dumps(comments, indent=2, ensure_ascii=False))