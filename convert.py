import json

# 读取JSON文件（假设是对象数组结构）
with open('word.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  # 这里读取的是包含字典的列表

# 转换为仅保留word的词典
with open('word.txt', 'w', encoding='utf-8') as f:
    for entry in data:    # 遍历数组中的每个字典
        word = entry["word"]
        f.write(f"{word}\n")  # 只写入词语本身
