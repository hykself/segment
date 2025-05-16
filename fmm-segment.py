import time

import jieba

def load_dict():
    # 读取词典并获取最大词长
    with open('word1.txt', 'r', encoding='utf-8') as f:
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

# 在 compare_with_jieba 函数中添加评估逻辑
def compare_with_jieba(text, word_dict, max_len):
    # 添加计时功能
    start_time = time.time()
    fmm_result = forward_max_match(text, word_dict, max_len)
    fmm_time = time.time() - start_time

    jieba.load_userdict('word.txt')
    jieba_result = list(jieba.cut(text))
    
    # 评估指标计算
    evaluation = {
        '分词数量': len(fmm_result),
        '单字词数量': sum(1 for w in fmm_result if len(w) == 1),
        '处理时间(ms)': round(fmm_time * 1000, 2),
        '与Jieba重合度': len(set(fmm_result) & set(jieba_result)) / len(jieba_result)
    }

    with open('output-fmm.txt', 'w', encoding='utf-8') as f:
        f.write("前向最大匹配结果: " + '/ '.join(fmm_result) + "\n")

    # 生成评估报告
    with open('report-fmm.txt', 'w', encoding='utf-8') as f:
        f.write("【前向匹配评估报告】\n")
        [f.write(f"{k}: {v}\n") for k, v in evaluation.items()]
        f.write("\nJieba分词结果: " + '/ '.join(jieba_result))

if __name__ == "__main__":
    # 读取测试文件
    with open('test.txt', 'r', encoding='utf-8') as f:
        text = f.read().strip()
    
    word_dict, max_len = load_dict()
    compare_with_jieba(text, word_dict, max_len)
