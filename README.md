# scrapy-lianjia_ershoufang-v190105

配置：Anaconda3，scrapy-1.5,python-3.6,mysql-8.0。

描述： 
1、尽可能获取lianjia二手房的大部分房源数据（包含基本信息+交易信息），网站动态所示数量为六万左右，spider最后获取数量相比无较大出入；

2、基本防ban措施：提交requests间隙，设置随机暂停若干秒；随机更换User_Agent；关闭cookies；

3、自动生成按运行时间命名的log日志文件（json格式），以供spider停止后查询错误；

4、数据获取后同步写入至自动生成按运行时间命名的json文件，以及Twisted异步写入mysql数据库； 
