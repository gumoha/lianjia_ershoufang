# scrapy-lianjia_ershoufang-v190105

配置：Anaconda3，scrapy-1.5,python-3.6,mysql-8.0。

描述： 1、获取lianjia二手房数据（基本信息+交易信息），spider获取的数量与网站动态所示数量基本无差别； 2、数据获取后同步写入至json文件，以及异步写入mysql数据库； 3、提交requests随机暂停N秒，更换User_Agent；关闭cookies；
