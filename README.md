## 1、创建项目
django-admin startproject 项目名



## 2、迁移
python manage.py makemigrations

python manage.py migrate



## 3、可视化
python manage.py createsuperuser

去setting.py里修改  LANGUAGE_CODE = 'zh-hans'  TIME_ZONE = 'Asia/Shanghai' 

去admin.py里注册要显示models


## 4、mysql
请看代码


## 5、模型字段类型

|类型|描述|
|---|---|
|AutoField | 自动增长的IntegerField，通常不用指定，不指定时Django会自动创建属性名为id的自动增长属性。|
|BooleanField|布尔字段，值为True或False。|
|NullBooleanField|支持Null、True、False三种值。|
|CharField(max_length=最大长度)|	字符串。参数max_length表示最大字符个数|。
|TextField|	大文本字段，一般超过4000个字符时使用。|
|IntegerField	|整数|
|DecimalField(max_digits=None, decimal_places=None)	| 十进制浮点数。参数max_digits表示总位。参数decimal_places表示小数位数。|
|FloatField|	浮点数。参数同上|
|DateTimeField|日期时间，参数同DateField。|
|TimeField|	时间，参数同DateField。|
|FileField	|上传文件字段。|
|ImageField	|继承于FileField，对上传的内容进行校验，确保是有效的图片。|
|DateField：([auto_now=False, auto_now_add=False])|	日期:<br>1)参数auto_now表示每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为false。<br>2) 参数auto_now_add表示当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为false。<br>3)参数auto_now_add和auto_now是相互排斥的，组合将会发生错误。|


## 5、模型选项
|选项名  |描述|
|---|---|
|default	|默认值。设置默认值。|
|primary_key	|若为True，则该字段会成为模型的主键字段，默认值是False，一般作为AutoField的选项使用。|
|unique	|如果为True, 这个字段在表中必须有唯一值，默认值是False。|
|db_index	|若值为True, 则在表中会为此字段创建索引，默认值是False。|
|db_column|	字段的名称，如果未指定，则使用属性的名称。|
|null|	如果为True，表示允许为空，默认值是False。|
|blank|	如果为True，则该字段允许为空白，默认值是False。|

