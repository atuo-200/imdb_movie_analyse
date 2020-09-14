# -*- coding: UTF-8 –*- 
import pandas as pd

#读取csv时，第一列作为行名
data = pd.read_csv("./file_tackle.csv",index_col=0)
data.dropna(inplace=True)


#评分数据分段
data["grade_cut"] = pd.cut(data["grade"],[0,2,4,6,8,10])

#统计各评分区间的电影数目（绘图数据1）
grade_cut_num = data["grade_cut"].value_counts()
grade_cut_num = grade_cut_num.sort_index(axis=0)
#index数据类型转换为字符串类型
grade_cut_num.index = grade_cut_num.index.astype(str)
grade_cut_num.to_json("./plot_grade_cut.json")

#不同地区的电影数目（绘图数据2）
state_num = data["country"].value_counts()
state_num.to_json("./plot_state_num.json")


def wordcount(words_list):
    count_dict = {}
    # 如果字典里有该单词则加1，否则添加入字典
    for str in words_list:
        if str in count_dict.keys():
            count_dict[str] = count_dict[str] + 1
        else:
            count_dict[str] = 1
    #按照词频从高到低排列
    count_list=sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
    return count_list

#不同类型的电影数目
genre_list = "/".join(list(data["genre"])).split("/")
genre_num = wordcount(genre_list)
#不同类型的电影数目（绘图数据3）
genre_num_df = pd.Series(dict(genre_num))
genre_num_df.to_json("./plot_genre_num.json")

#不同年份电影的数量（绘图数据4）
years_num = data["up_date"].value_counts()
print(years_num)
years_num.to_json("./plot_years_num.json")

#计算评分平均值
grade_average = data["grade"].mean()

#导演参与电影的部数（绘图数据5）

director_list = list(data[data["grade"] > grade_average]["director"])
director_num = wordcount(director_list)
director_num_df = pd.Series(dict(director_num))
print(director_num_df)
director_num_df.to_json("./plot_director_num.json")

#演员参与电影的部数（绘图数据6 ）
actors_list = "/".join(list(data[data["grade"] > grade_average]["actors"])).split(",")
actors_num = wordcount(actors_list)
actors_num_df = pd.Series(dict(actors_num))
actors_num_df.to_json("./plot_actors_num.json")