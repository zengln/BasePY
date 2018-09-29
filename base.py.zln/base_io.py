# -*-coding:utf-8 -*-

# 读文件(默认读取 UTF-8 编码的文本文件)
f = open('D:\\tmpz\\ssologin.txt', 'r')
print(f.read())
f.close()

# 由于文件读写可能出现异常, 导致后续的 close 操作不会被调用
try:
    f = open('D:\\tmpz\\ssologin.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 除了上述方法外, python 中引入了 with 语句自动调用 close
with open('D:\\tmpz\\ssologin.txt', 'r') as f:
    print(f.read())

# 读取二进制文件(图片和视频等)
# f = open("D:\\tmpz\\test.jpg", 'rb')
# f.close()

# 读取 gbk 编码的文本文件
f = open('D:\\tmpz\\ssologin.txt', 'r', encoding='gbk')
f.read()
f.close()

# 遇到编码不规范的文件, 会出现 UnicodeDecodeError 错误, 因为在文本文件中可能夹杂了一些非法编码的字符
# open 函数接收一个 errors 参数, 表示如果遇到编码错误后如何处理, 最简单的方式是直接忽略
f = open('D:\\tmpz\\ssologin.txt', 'r', encoding='gbk', errors='ignore')
f.close()

# 写文件
f = open('D:\\tmpz\\ssologin.txt', 'w')
f.write('test')
f.close()

# 写二进制文件
f = open('D:\\tmpz\\ssologin.txt', 'wb')
f.close()

# 写入特定编码的文件
f = open('D:\\tmpz\\ssologin.txt', 'w', encoding='gbk')
f.write('test')
f.close()

# 以 w 模式写入文件时, 文件存在则会直接覆盖, 若想要追加到文件末尾, 可以传入 a 以追加模式写入
f = open('D:\\tmpz\\ssologin.txt', 'a')
f.write('test')
f.close()
