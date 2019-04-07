# 20190406 性向数据分析
## 0 说明
本文件夹内的数据来自于 [废文网](https://sosad.fun) ，获取于2019-04-06，已经过脱敏处理，不含任何私密用户个人信息。本份数据内容按 [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议对外公开。

## 1 数据获取
### 1.1 使用sql语句获取书籍和性向的数据
```
select t.id, b.sexual_orientation
from threads as t, books as b
where b.id = t.book_id and t.deleted_at is null and t.public =1 and b.sexual_orientation >0
```
（选择未被删除的书籍、公开的数据、具有有效性向选择的书籍的数据）

### 1.2 使用sql语句获取收藏和性向的数据
```
select u.id as user_id, t.id as thread_id, b.sexual_orientation
from users as u, collections as c, threads as t, books as b
where u.id=c.user_id and c.collection_list_id = 0 and c.item_id = t.id and t.book_id = b.id and t.deleted_at is null and t.public = 1 and b.sexual_orientation >0
order by u.id
```
（选择普通收藏了的、未被删除的书籍、公开的数据、具有有效性向选择的书籍的数据，按用户id进行汇总）

## 2 数据汇总处理
### 2.1 采取python脚本“summarize_sexual_orientation_data.py”,将1.2获得的收藏夹数据按用户id进行聚类统计，结果输出为summarized_sexual_orientation.csv。
该数据又经剥离user_id脱敏。
### 2.2 采取python脚本“count_collection_so.py” 将2.1所得数据再次汇总统计，获得结果：
```
processed 33668 lines. // 总共处理的数据行数（数据表最上两行为说明信息）
total_user 33666 // 总共使用收藏功能收藏过书籍的用户总数
total_user_over3 14323 // 收藏书籍大于等于3本的用户共有14323人
collection_count [0, 14901, 4442, 2405, 1612, 1232, 1006, 815, 681, 556, 6016] // 收藏书籍数目分布数据
so_only [0, 26705, 373, 236, 372, 515, 25, 24] // 收藏夹内仅仅收藏了性向x的用户数分别是
so_only_over3 [0, 9176, 92, 20, 52, 0, 0, 0] // 收藏夹内仅仅收藏了性向x，且个人书籍收藏总数大于等于3本的用户数分别是
so_include [0, 31924, 1263, 1802, 2576, 3313, 565, 818] // 收藏夹内含有性向x的用户数为
so_include_over3 [0, 14019, 938, 1499, 2128, 2603, 526, 772] // 收藏夹内含有性向x，且个人收藏的书籍总数大于等于三本的用户分别是
accepted_so_count [0, 28250, 3497, 1138, 461, 196, 89, 35] // 能够接受 n种性向分类的用户有……
accepted_so_count_over3 [0, 9340, 3064, 1138, 461, 196, 89, 35] // 能够接受n种性向分类，且收藏夹内收藏的书籍总数大于等于三本的用户分别是
```
### 2.3 采取python脚本“count_thread_so.py”对1.1获得的书籍与性向关系数据进行汇总统计，结果如下：
```
processed 6450 lines.
count_so [0, 5000, 236, 413, 100, 356, 274, 70] //性向分类为x的书籍数量分别有多少本
```
### 3 性向数据数值说明
```
0: 性向未知
1: BL
2: GL
3: BG
4: GB
5: 混合性向
6: 无CP
7: 其他性向
```
