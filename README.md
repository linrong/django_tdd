# django-test

#### 项目介绍
a project for test in django 

#### 开发记录（基于windows上的开发）
* 不使用virtualenvwrapper辅助开发
```
# 安装virtualenv
pip install virtualenv

# 在目标目录下新建虚拟环境
virtualenv django

# 在创建虚拟环境的目录下，进入虚拟环境
cd django\Scripts
activate.bat
# 此时看见目录前面有括号+django证明已经进入虚拟环境，可以进行开发

# 退出虚拟环境，同样要在django\Scripts目录下
deactivate.bat
```
* 使用virtualenvwrapper辅助开发
```
# 手动安装
pip install virtualenvwrapper-win

# 设置环境变量
环境变量中在新增WORK_HOME并且赋值路径E:\virtualenv，并需要重启生效

# 新建虚拟环境,默认安装在环境变量的目录下
mkvirtualenv django

# 删除虚拟环境
rmvirtualenv django

# 查看mkvirtualenv创建安装的所有虚拟环境
workon

# 进入虚拟环境
workon django

# 退出虚拟环境
deactivate
```
* python环境
```
# 冻结环境,安装包列表保存到文件packages.txt中,
pip freeze >packages.txt　　

# 重建环境,在生产环境安装好对应版本的软件包，不要出现版本兼容等问题
pip install -r packages.txt
```
* 安装django和selenium
```
pip install django
pip install selenium
# selenium中使用google浏览器需要下载chromedriver.exe
```
* django
```
# 创建django项目
django-admin startproject DjangoTest

# 进入DjangoTest，创建app
python manage.py startapp test1

# setting 添加app

# 数据库处理
python manage.py makemigrations
python manage.py migrate

# 运行
python manage.py runserver

# 测试单个
python manage.py test test1

# 测试全部
python manage.py test
```
