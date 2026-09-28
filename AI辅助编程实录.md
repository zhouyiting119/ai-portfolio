# AI辅助编程实录

## 1.任务与提示词
需求：读取data文件夹里的生词表csv文件，筛选HSK4级别的词汇，统计各个词性的分布，按照词性分组，输出整理后的生词清单保存到练习.txt。读取、文件路径统一使用weekpath工具库。

## 2.AI初版代码
```python
import csv

def load_words():
    path = "生词表.csv"
    word_list = []
    with open(path,"r",encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            word_list.append(row)
    return word_list

if __name__ == "__main__":
    words = load_words()
    hsk4 = [w for w in words if w["等级"] == "4"]
    print(hsk4)
3.我的修改点（4条）
1.文件读取路径：接入weekpath.data_path()，统一项目路径管理。硬编码本地文件路径，换电脑运行就会找不到data目录，容易出现文件不存在报错。
2.CSV表头字段修正：把代码里面的键名"等级"改成csv实际表头"HSK等级"，字典键名和表格表头不一致，运行会出现KeyError。
3.文件编码统一修改为utf‑8，Windows系统读写文本文件很容易出现中文乱码，必须显式指定编码参数。
4.新增词性分组逻辑，用字典自动归类不同词性的生词，格式化排版输出造句练习题，补齐脚本导出练习文档的完整功能。

4.最终版和初版差异说明
AI最初生成的代码只实现了最简单的读取文件+筛选功能。路径写死、表头名称错误，没有统计词性、导出习题文本的逻辑。
我对照项目规范，引入weekpath工具处理文件路径，修正表头bug，补充词性统计、习题生成、文件写入整套流程，脚本最终可以直接生成可用的课堂练习txt文档。