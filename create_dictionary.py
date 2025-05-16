import jieba
import jieba.analyse

def generate_vocab(input_path, output_path):
    # 读取原始文本
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 使用jieba进行精确模式分词
    words = jieba.lcut(text)

    # 提取TF-IDF权重最高的前30%词语
    keywords = jieba.analyse.extract_tags(text, topK=int(len(words)*0.3))

    # 合并结果并去重
    vocab = sorted(set(words + keywords), key=lambda x: (len(x), x))

    # 写入文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(vocab))

if __name__ == "__main__":
    generate_vocab('test.txt', 'word1.txt')
    print("基于jieba的词典已生成：word1.txt")
