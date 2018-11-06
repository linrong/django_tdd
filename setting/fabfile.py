from fabric.contrib.files import append,exists,sed
from fabric.api import env,local,run
import random

# 代码仓库
REPO_URL ='https://github.com/linrong1994/django_tdd.git'

def deploy():
    # env.user指的是登陆服务器用户名，env.host是命令行中指定的服务器地址
    repo_folder='/home/%s' % (env.user)
    code_folder=repo_folder+'/code'
    _create_directory_structure_if_necessary(repo_folder)
    _get_latest_code(code_folder)
    _update_settings(code_folder,'sat-tech.cn')
    _upadte_virtualenv(code_folder)
    _update_static_files(code_folder)
    _update_database(code_folder)


# 创建目录文件夹
def _create_directory_structure_if_necessary(repo_folder):
    for subfolder in ('code','document'):
        # 使用fabric函数run执行shell
        run('mkdir -p %s/%s' %(repo_folder,subfolder))

# 拉取代码 
def _get_latest_code(code_folder):
    # 拉取更新
    if exists(code_folder+'/.git'):
        run('cd %s && git fetch'%(code_folder,))
    # 克隆
    else:
        run('git clone %s %s'% (REPO_URL,code_folder))
    # 利用fabric的local函数捕获git log的输出，获取提交的哈希值
    current_commit=local("git log -n 1 --format=%H",captrue=True)
    run('cd %s && git reset --hard %s'%(code_folder,current_commit))

def _update_settings(code_folder,site_name):
    settings_path=code_folder+'/django_tdd/DjangoTest/settings.py'
    sed(settings_path,"DEBUG = True","DEBUG=False")
    sed(settings_path,
        'ALLOWED_HOSTS=.+$',
        'ALLOWED_HOSTS=["%s"]'%(site_name)
    )
    secret_key_file=code_folder+'/django_tdd/DjangoTest/secret_key.py'
    if not exists(secret_key_file):
        chars='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-='
        key=''.join(random.SystemRandom().choice(chars) for _ in range(50) )
        append(secret_key_file,"SECRET_KEY='%s'"%(key,))
    append(settings_path,'\nfrom .secret_key import SECRET_KEY')

def _upadte_virtualenv(code_folder):
    virtualenv_folder =code_folder+'/django_tdd/virtualenv'
    if not exists(virtualenv_folder+'/bin/pip'):
        run('virtualenv --python=python %s'%(virtualenv_folder,))
    run('%s/bin/pip install -r %s/requirement.txt'%(virtualenv_folder,code_folder+'/django_tdd/DjangoTest'))

def _update_static_files(code_folder):
    run('cd %s && django_tdd/virtualenv/bin/python manage.py collectstatic --noinput'%(code_folder,))

def _update_database(code_folder):
    run('cd %s && django_tdd/virtualenv/bin/python manage.py migrate --noinput'%(code_folder,))
