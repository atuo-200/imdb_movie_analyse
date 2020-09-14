# -*- coding:utf-8 -*-
import pandas as pd
data = pd.read_csv("./file.csv")

# 数据预处理阶段
# 1.去重
data.drop_duplicates(inplace=True)

# 2.去空值
#查看空值情况
null1 = data.isnull().sum(axis=0)
null2 = data.isnull().sum(axis=1)
data.dropna(inplace=True)


#3.去除评分为0的电影数据（未上映电影）
data = data.loc[data["grade"] != 0]

#4.去除类型、演员、关键词字段的字符串的空白字符（空格、换行符、制表符）
data["genre"] = data["genre"].str.replace("\\s*","")
data["actors"] = data["actors"].str.replace("\\s*","")
data["keywords"] = data["keywords"].str.replace("\\s*","")

#5.把片长、上映年份字段转换为正常数据格式，时长单位为分钟
data["length"] = data["length"].str[0:-2]
data["up_date"] = data["up_date"].str[1:-1]

#6.中国香港，中国台湾，中国大陆统称为中国
data["country"].replace(["中国大陆","中国香港","中国台湾"],"中国",inplace = True)

#保存预处理后的数据
data.to_csv("./file_tackle.csv")