# def next_bigger_2(n):
      """可能和方法1的思路一致"""
#     n=str(n)[::-1]
#     try:
#         i=min(i+1 for i in range(len(n[:-1])) if n[i]>n[i+1])  # 判断n中的每一个元素是否存在前一个大于后一个,并找出最小的下标
#
#         j=n[:i].index(min([a for a in n[:i] if a>n[i]]))
#         return int(n[i+1::][::-1]+n[j]+''.join(sorted(n[j+1:i+1]+n[:j])))
#     except:
#         return -1

# result=next_bigger_2('13800')
# print(result)



def is_bigger(a,b):
    return True if a>b else False

#loop the str num as inverted and exchange the a,b if bigger
def run(num):
    """
    1.从末尾向前进行比较,如果后一个数大于前一个数,将后一个数放在前一个数的位置,
    2.根据j确定head和tail,针对tail 进行排序
    3.最后重置num值
    eg.
    从n个位开始依次和n+1(十位)，n+2(百位)，n+3(千位)，n+4(万位)...进行比较
    如果发现有大的数字，把n插入到n+1那里，同时把原来的n挪走，得到一个新的数字，放入我们的新列表
    over and over again
    
    :param num:
    :return:
    """
    contain=[]
    num_str=list(str(num))
    # 从末尾开始比较
    for i in range (1, len(num_str)+1):
        for j in range(i+1, len (num_str)+1):

            if is_bigger(num_str[-i],num_str[-j]):  # 如果后一个数大于前一个数
                num_str.insert(-j,num_str[-i])  # 将后一个数放在前一个数的位置

                head=num_str[:-j]
                tail=num_str[-j:]
                tail.pop()

                num_str=head+sorted(tail,reverse=False)
                new_num=int(''.join(num_str))
                contain.append(new_num)  # 保存下一个较大数
                #reset the num
                num_str=list(str(num))
                break  # 针对某个i 下的所有j的情况, 找到一个就跳出当前循环,继续下一个i循环

    return contain

def next_bigger(n) :
    return min(run(n)) if run(n) else -1  # 如果返回结果集为空,直接-1

result=next_bigger('138100')
print(result)




