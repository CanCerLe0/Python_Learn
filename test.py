#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基础 Python 示例代码
"""


def greet(name: str) -> str:
    """返回问候语"""
    return f"你好, {name}!"


def main():
    """主函数"""
    # 变量
    name = "Python 学习者"

    # 输出
    print(greet(name))

    # 列表操作
    fruits = ["苹果", "香蕉", "橙子"]
    print(f"\n水果列表: {fruits}")

    # 循环
    print("\n遍历水果:")
    for i, fruit in enumerate(fruits, 1):
        print(f"  {i}. {fruit}")

    # 字典
    student = {
        "姓名": "小明",
        "年龄": 20,
        "成绩": [85, 92, 78]
    }
    print(f"\n学生信息: {student}")

    # 条件判断
    avg_score = sum(student["成绩"]) / len(student["成绩"])
    print(f"平均成绩: {avg_score:.1f}")

    if avg_score >= 90:
        print("评价: 优秀")
    elif avg_score >= 80:
        print("评价: 良好")
    else:
        print("评价: 需要加油")


if __name__ == "__main__":
    main()
