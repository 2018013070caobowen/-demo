 ##!E/Python first-homework
"""
Author: 计普 曹博雯 2018013070
Purpose: Generate random data set.
Created: 28/4/2020
"""
import random
from collections.abc import Iterable


def dataSampling(datatype, datarange, num,strlen = 8):

    '''
    :Description: Generate a given condition randon data set
    :param datatype:The type of random，it must be a built-in type，
    :param dataRange: The range of random array,it must be a iterable data set
    :param num: The length of random array
    :param strlen: A dataset for str type, describes the length of the string
    :return:Random data set constructed
    '''

    try:
        result = set()
        # 以下代码用于检验错误，抛出异常
        if datatype is not int and datatype is not float and datatype is not str: # 当datatype非可处理类型时抛出异常
            raise Exception("datatype is not a built-in type")
        if not isinstance(datarange, Iterable): # 当datarange非可迭代类型时抛出异常
            raise Exception("datarange is not a Iterable")
        if type(num)!=int: # 当num非整型时抛出异常
            raise Exception("num is not int")
        elif(num>10000): # 当num太大时抛出异常
            raise Exception("num is out of processable range")
        if type(strlen)!=int: # 当strlen非整型时抛出异常
            raise Exception("strlen is not int")
        # 以上代码用于检验错误，抛出异常

        if datatype is int:
            it = iter(datarange)
            result = random.sample(range(next(it), next(it)), num) # 使用此方法生成的随机数据集不会产生重复
        elif datatype is float:
            for index in range(0,num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype is str:
            for index in range(0,num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen)) # for _ in range(6) 6表示长度
                result.add(item)

    except Exception as e:
        print("ERROR:", e)
    else:
        return result
    finally:
        print("dataSampling 异常处理调用完成")


def dataScreening(data, *args): # *args
    """
    :param data: Data set waiting to be screening
    :param args:Screening way 只支持类型筛选以及当类型为int时还可以增加一个int型数据，进行求余筛选
    :return:Already screening dataset
    """
    try:
        if not isinstance(data, Iterable): # 当data非可迭代时抛出异常
            raise Exception("dataset is not a Iterable")
        result = set()
        for index in args:
            result = set()
            if index is "int":
                for item in data:
                    if isinstance(item, int):
                        result.add(item)
            elif index is "float":
                for item in data:
                    if isinstance(item, float):
                        result.add(item)
            elif index is "str":
                for item in data:
                    if isinstance(item, str):
                        result.add(item)
            elif isinstance(index, int):
                for item in data:
                    if isinstance(item,int) and item % index == 0:
                        result.add(item)
            else:
                raise Exception("args must be int or str or float or a number") # 当args非可处理形式时抛出异常
            data = result
    except Exception as e:
        print("ERROR:", e)
    else:
        return result
    finally:
        print("dataScreening 异常处理调用完成")


def apply():
    print("#======此处用于验证dataSampling的异常处理======#")
    # result = dataSampling(int, 0, 10) # 此例为检验datarange非迭代的时候是否会抛出异常
    # result = dataSampling(int, (0,10), 10, 'a') # 此例为检验strlen非整型的时候是否会抛出异常
    # result = dataSampling('a', (0,10), 10) # 此例为检验datatype非内置类型的时候是否会抛出异常
    # result = dataSampling(int, (0,10), 'a') # 此例为检验num非整形的时候是否会抛出异常
    # result = dataSampling(str,string.ascii_letters+string.digits+string.punctuation,10) # 此为正确样例生成字符串数据集
    # result = dataSampling(float, (0, 10), 10) # 此为正确样例生成整型数据集
    result = dataSampling(int, (0,10), 10) # 此为正确样例生成整型数据集
    print("   输出dataSampling调用结果",result)

    print("#======此处用于验证dataScreening的异常处理======#")
    result = dataSampling(int, (0, 20), 20)
    result.append("abc") # 增加一个字符用于下面字符串的筛选
    print("待筛选的数据集是:",result)
    # result = dataScreening(0, "int", 1, 2) # 此例为检验datarange非迭代的时候是否会抛出异常
    # result = dataScreening(result, "int", "a") # 此例为检验args非可处理类型的时候是否会抛出异常
    # result = dataScreening(result, "str")
    result = dataScreening(result, "int", 5, 2) # 此例为正确的，输出结果应在result中筛选出整型数据，并且每一个数都级可以被5整除，又可以被2整除
    print("输出dataScreening调用结果", result)

apply()