django-admin startproject 项目名

迁移
python manage.py makemigrations
python manage.py migrate

可视化
python manage.py createsuperuser
去setting.py里修改  LANGUAGE_CODE = 'zh-hans'  TIME_ZONE = 'Asia/Shanghai' 
去admin.py里注册要显示models


