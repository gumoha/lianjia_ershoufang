# scrapy-lianjia_ershoufang-v190105

配置：Anaconda3，scrapy-1.5,python-3.6,mysql-8.0。

描述： 
1、获取lianjia二手房数据（基本信息+交易信息），spider获取的数量与网站动态所示数量基本无差别； 

2、提交requests随机暂停N秒，更换User_Agent；关闭cookies；

3、自动生成按日期命名的log日志文件（json格式），方便查询错误；

4、数据获取后同步写入至自动生成按日期命名的json文件，以及异步写入mysql数据库； 

