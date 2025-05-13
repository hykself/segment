# 中文分词算法对比工具

本项目实现并对比多种中文分词算法，包含前向最大匹配、双向最大匹配算法，并与jieba分词结果进行对比。

## 文件结构说明

### 📂 核心算法文件
- `fmm-segment.py`  
  实现**前向最大匹配算法**(FMM)  
  功能：  
  - 从右向左最大匹配分词  
  - 对比jieba分词结果  
  - 输出结果到`output-fmm.txt`

- `bmm-segment.py`  
  实现**双向最大匹配算法**(BMM)  
  功能：  
  - 结合前向+后向匹配（优先选择词数少的方案）  
  - 单字较少的方案优先  
  - 输出结果到`output-bmm.txt`

### 🔧 辅助工具
- `convert.py`  
  词典格式转换工具  
  功能：  
  - 将JSON格式词典`word.json`转换为文本格式`word.txt`  
  - 支持自定义词典结构

### 📁 数据文件
- `word.json`  
  原始词典文件（JSON格式）
- `word.txt`  
  处理后的纯文本词典（每行一个词）
- `test.txt`  
  待分词的中文测试文本

### 📊 输出示例
- `output-fmm.txt`  
  前向匹配+Jieba对比结果
- `output-bmm.txt`  
  双向匹配+Jieba对比结果
- `output.txt`  
  历史测试结果存档
- `report-bmm.txt`
  双向匹配算法测试结果
- `report-fmm.txt`
  前向匹配算法测试结果

## 使用方法
1. 准备词典：
```bash
python convert.py
