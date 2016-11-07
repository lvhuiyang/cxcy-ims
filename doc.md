# Cxcy-ims开发文档


## 数据库设计

Database: Mysql-5.7

OS: Ubuntu 16.04

### 用户账号表

table_name: accounts

+ id: int, 主键, 非空

+ account: str, 账号(登录账号凭证)

+ password: str, hash

+ username: str, 用户名，用户自己可修改

+ create_date: date, 添加该账号的日期

+ create_people: str, 添加该账号的管理员

### 竞赛项目表

table_name: projects

+ id: int, 主键, 非空

+ name: str, 非空, 竞赛项目名称

+ create_date: date, 添加该竞赛项目的日期

+ create_people: str, 添加该竞赛项目的管理员

### 竞赛获奖表

table_name: competitions

+ id: int, 主键

+ project_name: 外键 ==> projects.name

+ achievement_name: str, 成果名称

+ prize_category: str, 获奖级别, 选择

+ prize_level: str, 获奖等级, 选择

+ stu_name, 学生姓名

+ stu_phone_number, 学生手机

+ stu_number, 学号

+ stu_qq, 学生qq

+ stu_class, 专业班级

+ teacher_name, 教师姓名

+ teacher_title, 教师职称

+ prize_date, 获奖日期

+ award_department, 颁奖单位

+ sponsor, 主办方

+ comment, 备注

### 发表文论表

table_name: theses

+ id: 主键

+ school, 学院

+ stu_name, 学生姓名

+ stu_phone_number, 学生手机

+ stu_number, 学号

+ stu_qq, 学生qq

+ stu_class, 专业班级
 
+ periodical_name, 刊物名称

+ thesis_name, 论文名称

+ level, 档次

+ level_name, 位次

+ periodical_number, 刊号

+ publish_date, 发表日期

+ comment, 备注

### 项目立项表

与上表类似，不再重复，具体列名称见excel表。

### 公司注册表

与上表类似，不再重复，具体列名称见excel表。

### 其他成果表

与上表类似，不再重复，具体列名称见excel表。


## 权限

## API

