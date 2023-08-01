### 运行环境

pip install qbittorrent-api

### qb批量编辑tracker

使用前先编辑qb_tr_change_tracker.py文件内连接信息和参数

#### 参数

old_tracker：旧的tracker关键字

new_tracker：替换的新trakcer



### qb批量删除旧文件

使用前先编辑qb_tr_delete.py文件内连接信息和参数

#### 参数

categories：qb分类列表

days：未活动天数，默认60天

file_size：文件大小，默认小于50G