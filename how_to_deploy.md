### docker deploy
> in the environment with python3.6.5
#### setting root
```
# root设置密码(root)
passwd root
apt-get update
apt-get install sudo
```
#### add user
```
# root用户下添加用户lin
useradd -m -s /bin/bash lin
# 把lin添加到sudo组
usermod -a -G sudo lin
# 设置lin的密码(lin@python)
passwd lin
# 切换用户
su - lin
```

#### install nginx
```
sudo apt-get install -y nginx
sudo service nginx start
```

#### install virtualenv
```
sudo apt-get install -y git
sudo apt-get install -y vim
sudo apt-get install -y virtualenv

# manage.py的目录下,使用python路径的python,安装在上一个目录的virtualenv下
virtualenv --python=python ../virtualenv

# 查看python路径
which python
~ /usr/local/bin/python

# 切换到虚拟环境
source ../virtualenv/bin/activate

# 查看python路径
which python
~ /home/lin/django_tdd/virtualenv/bin/python

# 安装django
pip install django

# 测试
python manage.py runserver

# 导出安装的包
pip freeze > requirement.txt

# 退出virtualenv
deactivate

# 安装
pip install -r requirement.txt
```
#### setting
```
# 修改nginx配置
cd /etc/nginx/sites-available/
sudo touch nginx_config.conf
vim nginx_config.conf

# 把真正的配置文件放在sites-available中，在sites-enabled中创建一个符号连接，便于切换网站的在线状态
# 创建软连接
sudo ln -s /etc/nginx/sites-available/nginx_config.conf /etc/nginx/sites-enabled/nginx_config.conf
# 查看软连接
ls -l /etc/nginx/sites-enabled/

# 删除自带的默认页面
sudo rm /etc/nginx/sites-enabled/default

# 重启nginx
sudo service nginx reload

# 利用virtualenv中的python启动django
../virtualenv/bin/python manage.py runserver
# 运行成功

# 停止
pkill -f "manage.py runserver"
```
#### gunicorn
```
# 安装gunicorn
../virtualenv/bin/pip install gunicorn

# 运行
../virtualenv/bin/gunicorn DjangoTest.wsgi:application
```
#### 配置静态文件
```
# 收集静态文件
../virtualenv/bin/python manage.py collectstatic --noinput

# 配置nginx,做静态文件服务器
sudo vim /etc/nginx/sites-available/nginx_config.conf

server {
    listen 80;
    server_name localhost;
    
    location /static {
        alias /home/lin/django_tdd/static;
    }
 
    location / {
        proxy_pass http://localhost:8000;
    }config
}

# 重启nginx
sudo service nginx reload

# 修改nginx，换用Unix套接字
server {
    listen 80;
    server_name localhost;
    
    location /static {
        alias /home/lin/django_tdd/static;
    }
 
    location / {
       proxy_set_header Host $host;
       proxy_pass http://unix:/tmp/nginx_config.socket;
    }
}

# 重启之后启动，需要添加套接字
../virtualenv/bin/gunicorn --bind unix:/tmp/nginx_config.socket DjangoTest.wsgi:application
```
#### gunicorn脚本启动
```
# /etc/init/创建文件gunicorn-django.conf
sudo touch /etc/init/gunicorn-django.conf
# 编写脚本（setting目录中的gunicorn-django.conf）,然后运行(目前运行失败，没有start命令)
sudo start gunicorn-django
```
#### 自动化部署
```
# 全局安装fabric,不使用virtualenv
sudo pip install fabric
# 编写代码
fab deploy
```