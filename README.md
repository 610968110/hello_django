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

## 6、mysql单条件查询

|函数名	|功能	|返回值	|说明|
|---|---|---|---|
|get	|返回表中满足条件的一条且只能有一条数据。|	返回值是一个模型类对象。|	参数中写查询条件。<br>1)如果查到多条数据，则抛异常MultipleObjectsReturned。<br>2)查询不到数据，则抛异常：DoesNotExist。|
|all	|返回模型类对应表格中的所有数据。|	返回值是QuerySet类型|	查询集|
|filter	|返回满足条件的数据。|	返回值是QuerySet类型	|参数写查询条件。|
|exclude	|返回不满足条件的数据。|	返回值是QuerySet类型	|参数写查询条件。|
|order_by	|对查询结果进行排序。|	返回值是QuerySet类型	|参数中写根据哪些字段进行排序。|


### 6.1 get示例：
例：查询图书id为3的图书信息。
### all方法示例：
例：查询图书所有信息。
### 6.1 filter方法示例：
#### 6.2.1 条件格式：
	模型类属性名__条件名=值
查询图书评论量为34的图书的信息：       
- a)判等 条件名:exact。
例：查询编号为1的图书。        
BookInfo.objects.get(id=1)      
- b)模糊查询
例：查询书名包含'传'的图书。contains     
BookInfo.objects.filter(btitle__contains='传')       
例：查询书名以'部'结尾的图书 endswith 开头:startswith      
BookInfo.objects.filter(btitle__endswith='部')       
- c)空查询 isnull
例：查询书名不为空的图书。isnull         
select * from booktest_bookinfo where btitle is not null;       
BookInfo.objects.filter(btitle__isnull=False)       
- d)范围查询 in
例：查询id为1或3或5的图书。        
select * from booktest_bookinfo where id in (1,3,5);        
BookInfo.objects.filter(id__in = [1,3,5])       
- e)比较查询 gt(greate than) lt(less  than) gte(equal) 大于等于  lte 小于等于        
例：查询id大于3的图书。       
Select * from booktest_bookinfo where id>3;     
BookInfo.objects.filter(id__gt=3)       
- f)日期查询
例：查询1980年发表的图书。     
BookInfo.objects.filter(bpub_date__year=1980)       
例：查询1980年1月1日后发表的图书。        
from datetime import date       
BookInfo.objects.filter(bpub_date__gt=date(1980,1,1)) 
      
### 6.3 exclude方法示例：
例：查询id不为3的图书信息。     
BookInfo.objects.exclude(id=3)   
   
### 6.4 order_by方法示例：
作用：进行查询结果进行排序。      
例：查询所有图书的信息，按照id从小到大进行排序。       
BookInfo.objects.all().order_by('id')       
例：查询所有图书的信息，按照id从大到小进行排序。       
BookInfo.objects.all().order_by('-id')      
例：把id大于3的图书信息按阅读量从大到小排序显示。      
BookInfo.objects.filter(id__gt=3).order_by('-bread')        

## 7、mysql多属性比较查询和多条件查询
### 7.1 F对象
作用：用于类属性之间的比较。      
使用之前需要先导入：      
from django.db.models import F 
     
例：查询图书阅读量大于评论量图书信息。     
BookInfo.objects.filter(bread__gt=F('bcomment'))        
例：查询图书阅读量大于2倍评论量图书信息。       
BookInfo.objects.filter(bread__gt=F('bcomment')*2)      

### 7.2 Q对象
作用：用于查询时条件之间的逻辑关系。not and or，可以对Q对象进行&|~操作。     
使用之前需要先导入：      
from django.db.models import Q      

例：查询id大于3且阅读量大于30的图书的信息。        
BookInfo.objects.filter(id__gt=3, bread__gt=30)
BookInfo.objects.filter(Q(id__gt=3)&Q(bread__gt=30))        
例：查询id大于3或者阅读量大于30的图书的信息。       
BookInfo.objects.filter(Q(id__gt=3)|Q(bread__gt=30))        
例：查询id不等于3图书的信息。        
BookInfo.objects.filter(~Q(id=3))


## 8、mysql的聚合函数 
作用：对查询结果进行聚合操作。     
sum count avg max min       

### 8.1 aggregate：调用这个函数来使用聚合。 返回值是一个字典
使用前需先导入聚合类：         
from django.db.models import Sum,Count,Max,Min,Avg      

例：查询所有图书的数目。        
BookInfo.objects.all().aggregate(Count('id'))       
{'id__count': 5}        

例：查询所有图书阅读量的总和。     
BookInfo.objects.aggregate(Sum('bread'))        
{'bread__sum': 126}     

### 8.2 count函数 返回值是一个数字
作用：统计满足条件数据的数目。   
  
例：统计所有图书的数目。        
BookInfo.objects.all().count()      
BookInfo.objects.count()        

例：统计id大于3的所有图书的数目。      
BookInfo.objects.filter(id__gt=3).count()       

## 9、mysql查询集
all, filter, exclude, order_by调用这些函数会产生一个查询集，QuerySet类对象可以继续调用上面的所有函数。      

### 9.1 查询集特性
1）	惰性查询：只有在实际使用查询集中的数据的时候才会发生对数据库的真正查询。        
2）	缓存：当使用的是同一个查询集时，第一次使用的时候会发生实际数据库的查询，然后把结果缓存起来，之后再使用这个查询集时，使用的是缓存中的结果。       

### 9.2 限制查询集
可以对一个查询集进行取下标或者切片操作来限制查询集的结果。       
对一个查询集进行切片操作会产生一个新的查询集，下标不允许为负数。        
取出查询集第一条数据的两种方式:    
    
|方式|说明|
|---|---|
|b[0]|	如果b[0]不存在，会抛出IndexError异常|
|b[0:1].get()	|如果b[0:1].get()不存在，会抛出DoesNotExist异常。|

exists:判断一个查询集中是否有数据。True False


## 10、模型关系

### 10.1 一对多关系
例：图书类-英雄类       
models.ForeignKey() 定义在多的类中。        

### 10.2 多对多关系
例：新闻类-新闻类型类 体育新闻 国际新闻       
models.ManyToManyField() 定义在哪个类中都可以。        

### 10.3 一对一关系
例：员工基本信息类-员工详细信息类. 员工工号     
models.OneToOneField 定义在哪个类中都可以。     


## 11、mysql关联查询（一对多）

### 11.1 查询和对象关联的数据
在一对多关系中，一对应的类我们把它叫做一类，多对应的那个类我们把它叫做多类，我们把多类中定义的建立关联的类属性叫做关联属性。      

例：查询id为1的图书关联的英雄的信息。        
	b=BookInfo.objects.get(id=1)        
	b.heroinfo_set.all()        
通过模型类查询：        
	HeroInfo.objects.filter(hbook__id=1)        
	
例：查询id为1的英雄关联的图书信息。     
	h = HeroInfo.objects.get(id=1)      
	h.hbook     
通过模型类查询：        
	BookInfo.objects.filter(heroinfo__id=1)     

### 11.2 通过模型类实现关联查询

通过多类的条件查询一类的数据：     
	一类名.objects.filter(多类名小写__多类属性名__条件名)       
通过一类的条件查询多类的数据：     
	多类名.objects.filter(关联属性__一类属性名__条件名)  

例：查询图书信息，要求图书关联的英雄的描述包含'八'。     
BookInfo.objects.filter(heroinfo__hcomment__contains='八')       

例：查询图书信息，要求图书中的英雄的id大于3.        
BookInfo.objects.filter(heroinfo__id__gt=3)     

例：查询书名为“天龙八部”的所有英雄。
HeroInfo.objects.filter(hbook__btitle='天龙八部')    
   
      
