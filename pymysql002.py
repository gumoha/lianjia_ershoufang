#写入数据库
class MysqlPipeline(object):

    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod #重写类方法
    def from_settings(cls,settings):

        adbparams = dict(
            host = settings['MYSQL_HOST'],
            port = settings['MYSQL_PORT'],
            user = settings['MYSQL_USER'],
            password = settings['MYSQL_PASSWD'],
            db = settings['MYSQL_DBNAME'],
            charset='utf8',
            use_unicode=True,
            cursorclass = pymysql.cursors.DictCursor, #指定cursor类型

        )

        dbpool = adbapi.ConnectionPool("pymysql",**adbparams)

        return cls(dbpool) # 相当于dbpool付给了这个类，self可以调用


    def process_item(self,item,spider):
        query = self.dbpool.runInteraction(self.sql_insert,item)# 调用插入的方法

        query.addErrback(self.handle_error)# 调用异常处理方法

        return item

    #写入数据库语句
    def sql_insert(self,cursor,item):
        insert_sql = '''
                            insert into test01 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    '''

        item_values = (
            item['houselink'],item['houseID'],item['housename'],item['time_build'],item['totalprice'],item['unitprice'],item['community'], \
            item['district'],item['block'],item['road'],item['supplement'], \
            item['type_house'],item['area_gross'],item['area_real'],item['orientation'],item['decoration'],item['own_time'],item['floor'], \
            item['layout'],item['type_building'],item['material'],item['elevator_num'], \
            item['time_listing'],item['time_deal'],item['time_limit'],item['property'],item['usage_yt'], \
            item['own'],item['pledge'],item['upload']
        )

        cursor.execute(insert_sql,item_values)

    #错误处理
    def handle_error(self,failure):
        if failure:
            print(failure)