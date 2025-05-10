import jieba

def load_dict():
    # 读取词典并获取最大词长
    with open('word.txt', 'r', encoding='utf-8') as f:
        word_dict = {line.strip() for line in f}
    max_len = max(len(word) for word in word_dict)
    return word_dict, max_len

def forward_max_match(text, word_dict, max_len):
    result = []
    index = 0
    text_length = len(text)
    
    while index < text_length:
        # 动态调整窗口大小
        window_size = min(max_len, text_length - index)
        while window_size > 0:
            candidate = text[index:index+window_size]
            if candidate in word_dict or window_size == 1:
                result.append(candidate)
                index += window_size
                break
            window_size -= 1
    return result

def compare_with_jieba(text, word_dict, max_len):
    # 前向最大匹配结果
    fmm_result = forward_max_match(text, word_dict, max_len)
    
    # 加载自定义词典（可选）
    jieba.load_userdict('word.txt')
    jieba_result = list(jieba.cut(text))
    
    # 结果输出到文件
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write("前向最大匹配结果: " + '/ '.join(fmm_result) + "\n")
        f.write("\nJieba分词结果: " + '/ '.join(jieba_result))

if __name__ == "__main__":
    # 读取测试文件
    with open('test.txt', 'r', encoding='utf-8') as f:
        text = f.read().strip()
    
    word_dict, max_len = load_dict()
    compare_with_jieba(text, word_dict, max_len)
