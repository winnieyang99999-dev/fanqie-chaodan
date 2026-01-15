# -*- coding: utf-8 -*-
# 番茄炒蛋示例代码

def make_dish():
    ingredients = ["番茄", "鸡蛋", "盐", "糖", "油"]
    steps = [
        "番茄切块，鸡蛋打散。",
        "热锅凉油，倒入鸡蛋液翻炒成型后盛出。",
        "再次热锅，加油，放入番茄翻炒至出汁。",
        "倒入炒好的鸡蛋，加入盐和少许糖调味，翻炒均匀即可。"
    ]
    print("番茄炒蛋的做法：")
    for step in steps:
        print(step)

if __name__ == "__main__":
    make_dish()
