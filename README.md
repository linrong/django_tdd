# django-test

#### 项目介绍
a project for test in django 

#### 开发记录（基于windows上的开发）
* 安装virtualenv
```
pip install virtualenv
```
* 以下为没有设置环境变量时，在目标目录下新建虚拟环境
```
virtualenv django
```
* 在创建虚拟环境的目录下，进入虚拟环境
```
# 将在此目录下进行虚拟化
cd django\Scripts
activate.bat
# 此时看见目录前面有括号+django证明已经进入虚拟环境，可以进行开发
```
* 退出虚拟环境
```
# 同样要在django\Scripts目录下
deactivate.bat
```
* 使用virtualenvwrapper辅助开发
```
# 一般安装virtualenv时也默认安装了，如果没有安装手动安装
pip install virtualenvwrapper-win
# 设置环境变量
环境变量中在新增WORK_HOME并且赋值路径~django\Scripts
# 新建虚拟环境,默认安装在环境变量的目录下
mkvirtualenv django
# 查看mkvirtualenv创建安装的所有虚拟环境
workon
# 进入虚拟环境
workon django
# 退出虚拟环境
deactivate
```