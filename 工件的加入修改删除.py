def write():
    with open('data.txt', 'a', encoding='utf-8') as f:  # 使用with语句自动管理文件关闭
        while True:  # 创建一个无限循环 
            name = input("请输入你的工件名字：")
            try:
                price = float(input("该工件的价格："))  # 转换为浮点数
            except ValueError:
                print("价格需要是一个数字，请重新输入。")
                price = float(input("该工件的价格："))

            f.write(f" {name}： {price} ")  # 写入文件，并添加换行符
            # 询问用户是否继续输入
            continue_input = input('是否还要继续增加，是则按1，不是则按其他数字：')
            if continue_input != '1':
                break  # 如果用户不输入1，则退出循环

def change():#修改文件的
        name=input("你想要修改的器件：")
        price=float(input('你想要的数值：'))
        gongjian_dict[name]=price
        print('successful')
        if int(input("你是否还需要修改，继续修改则输入1，否在按其他"))==1:
             change()

def delete():#删除
    name=input('你需要删除的工件名称：')
# 检查键是否存在于字典中，如果存在则删除
    if name in gongjian_dict:
        del gongjian_dict[name]
        print(f"已删除工件：{name}")
    else:
        print(f"工件：{name} 不存在。")
    if int(input("你是否还需要删除，继续修改则输入1，否在按其他"))==1:
             delete()
# 创建一个空字典来存储工件名称和对应的数量
gongjian_dict = {}

key=input('你是否需要增加工件，增加请输入1，不需要输入其他:')
if key=='1':
     write()

f = open('data.txt', 'r', encoding='utf-8')
a = f.read()
f.close()  # 记得关闭文件
# 使用split()方法按空格分割字符串
b = a.replace("：","").split()
print(b)


for i in range(0, len(b), 2):  # 步长为2，假设每两个元素是一对工件名称和数量
    name = b[i]  # 工件名称
    try:
        quantity = float(b[i+1])  # 尝试转换数量为整数
        gongjian_dict[name] = quantity  # 将工件名称和数量存储到字典中
    except ValueError:
        # 如果转换失败，打印错误信息并跳过这个元素
        print(f"无法将 '{b[i+1]}' 转换为整数，跳过这个元素。")

for name, quantity in gongjian_dict.items():
    print(f'{name}:{quantity}')
key=input('你是否需要删除原有工件，修改请输入1，不需要输入其他:')
if key=='1':
     delete()
key=input('你是否需要修改原有工件价格，修改请输入1，不需要输入其他:')
if key=='1':
     change()
f = open('data.txt', 'w', encoding='utf-8')
for name, quantity in gongjian_dict.items():
     f.write(f"{name}： {quantity} ")
     print(name,quantity)
f.close()
