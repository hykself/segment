import time

import jieba

def forward_max_match(text, word_dict, max_len):
    result = []
    index = 0
    while index < len(text):
        for size in range(min(max_len, len(text) - index), 0, -1):
            word = text[index:index+size]
            if word in word_dict or size == 1:
                result.append(word)
                index += size
                break
    return result

def backward_max_match(text, word_dict, max_len):
    result = []
    index = len(text)
    while index > 0:
        size = min(max_len, index)
        for i in range(size, 0, -1):
            word = text[index-i:index]
            if word in word_dict or i == 1:
                result.append(word)
                index -= i
                break
    return result[::-1]

def bidirectional_max_match(text, word_dict, max_len):
    forward = forward_max_match(text, word_dict, max_len)
    backward = backward_max_match(text, word_dict, max_len)
    
    if len(forward) != len(backward):
        return forward if len(forward) < len(backward) else backward
    else:
        f_single = sum(1 for w in forward if len(w) == 1)
        b_single = sum(1 for w in backward if len(w) == 1)
        return forward if f_single < b_single else backward

# 在 compare_with_jieba 函数中添加评估逻辑
def compare_with_jieba(text, word_dict, max_len):
    start_time = time.time()
    bmm_result = bidirectional_max_match(text, word_dict, max_len)
    bmm_time = time.time() - start_time

    jieba.load_userdict('word.txt')
    jieba_result = list(jieba.cut(text))
    
    # 双向匹配特有评估指标
    evaluation = {
        '分词数量': len(bmm_result),
        '单字词数量': sum(1 for w in bmm_result if len(w) == 1),
        '处理时间(ms)': round(bmm_time * 1000, 2),
        '与Jieba重合度': len(set(bmm_result) & set(jieba_result)) / len(jieba_result),
        '算法选择统计': {
            '前向选择次数': sum(1 for w in bmm_result if w in forward_max_match(text, word_dict, max_len)),
            '后向选择次数': sum(1 for w in bmm_result if w in backward_max_match(text, word_dict, max_len))
        }
    }


    with open('report-bmm.txt', 'w', encoding='utf-8') as f:
        f.write("【双向匹配评估报告】\n")
        [f.write(f"{k}: {v}\n") for k, v in evaluation.items()]
    with open('output-bmm.txt', 'w', encoding='utf-8') as f:
        f.write("双向最大匹配结果: " + '/ '.join(bmm_result) + "\n")
        f.write("Jieba分词结果: " + '/ '.join(jieba_result))

if __name__ == "__main__":
    # 加载词典
    word_dict = set()
    with open('word.txt', 'r', encoding='utf-8') as f:
        word_dict.update(line.strip() for line in f)
    
    # 读取训练文本
    with open('test.txt', 'r', encoding='utf-8') as f:
        text = f.read().strip()
    
    max_len = max(len(word) for word in word_dict)
    compare_with_jieba(text, word_dict, max_len)
