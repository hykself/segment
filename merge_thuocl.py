import glob
import os

def merge_thuocl_files(input_dir, output_file="words.txt"):
    # 获取所有以THUOCL开头的txt文件
    thuocl_files = glob.glob(os.path.join(input_dir, "THUOCL*.txt"))

    # 用于存储所有提取的词语
    unique_words = set()

    for file_path in thuocl_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # 分割每行的词语和词频
                word = line.strip().split('\t')[0]
                unique_words.add(word)

    # 写入输出文件（按字母顺序排序）
    with open(os.path.join(input_dir, output_file), 'w', encoding='utf-8') as f:
        for word in sorted(unique_words):
            f.write(f"{word}\n")

if __name__ == "__main__":
    target_dir = r"F:\study\three\NLP\superjieba"
    merge_thuocl_files(target_dir)
    print(f"合并完成！生成文件路径：{os.path.join(target_dir, 'words.txt')}")

