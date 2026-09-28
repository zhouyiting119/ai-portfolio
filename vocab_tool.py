# W3 生词表 CSV -> 自动生成练习题
# 运行：python vocab_tool.py
import os
import csv
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import weekpath  # noqa: E402  统一解析 data/ 路径，换目录也不会找不到文件

DATA = weekpath.data_path("生词表.csv")


def load_words(path=DATA):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def filter_by_level(words, level="4"):
    return [w for w in words if str(w["HSK等级"]) == str(level)]


def count_by_pos(words):
    d = {}
    for w in words:
        d[w["词性"]] = d.get(w["词性"], 0) + 1
    return d


def gen_exercises(words, out=None):
    # 产物统一落到代码包根目录：否则"从哪个目录运行"决定了文件落在哪，
    # 与 README 的"任意目录运行"承诺冲突，且散落的产物 .gitignore 拦不住。
    out = out or weekpath.root_path("练习.txt")
    with open(out, "w", encoding="utf-8") as f:
        # =========作业2新增：按HSK等级分组输出============
        level_set = sorted({item["HSK等级"] for item in words})
        for lv in level_set:
            group = [x for x in words if x["HSK等级"] == lv]
            f.write(f"----------HSK{lv} 练习题----------\n")
            for w in group:
                f.write("用“%s”造一个句子。（%s）\n" % (w["词汇"], w["词性"]))


if __name__ == "__main__":
    words = load_words()
    # 作业1改动示例：集合推导式，新语法写法
    all_level = {w["HSK等级"] for w in words}
    print(f"本文件包含全部HSK等级：{sorted(all_level)}")
    
    lv4 = filter_by_level(words, "4")
    print("总词汇 %d 个，其中 HSK4 词汇 %d 个，词性分布：%s"
          % (len(words), len(lv4), count_by_pos(lv4)))
    out = weekpath.root_path("练习.txt")
    gen_exercises(words, out)   # 这里传入全部词汇，脚本自动分组
    print("已生成：%s" % out)