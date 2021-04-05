def space(lines):
    letter = ["C", "*"]
    shuzi = ["1", "2", "3", "4", "+", "5"]
    shuzi2 = ["10", "20", "30", "40", "50"]
    zifu = ["CALL", "CHAR"]
    yema = ["·"+str(i)+"·" for i in range(100)]
    # print(yema)
    # print(yema[0])
    for line in lines:
        line = line.strip(" ")
        if line.split():
            # file2.write(line)
            if line[0:4] in yema or line[0:3] in yema:
                continue
            elif line[0:4] in zifu:  # 首字母是C，但需要缩进的代码
                file2.write("      " + line)
            elif line[0] in letter:
                file2.write(line)
            elif line[0:2] in shuzi2:  # 缩进三个空格，DO程序的执行范围前的数字
                file2.write("   " + line)
            elif line[0] in shuzi:  # 缩进五个空格，程序链接的标志
                file2.write("     " + line)
            else:  # 缩进六个空格，主程序前空六格
                file2.write("      " + line)
    return file2


# def del_space(lines):
#     for line in lines:
#         line = line.strip(" ")
#         if line.split():
#             file2.write(line)
#     return lines


if __name__ == '__main__':
    file = open("4-2.txt", "r", encoding="utf-8")
    file2 = open("umat4.for", "w+", encoding="utf-8")
    lines = file.readlines()
    # b = del_space(lines)
    # lines1 = b.readlines()
    a = space(lines)
    file.close()
    file2.close()
