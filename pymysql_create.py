import pymysql,time

def connect_db():
	try:
		ljdb = pymysql.connect(host='127.0.0.1',
								port=3306,
								user='gumo',
								password='12345',
								db='lianjia_ershoufang',
								charset='utf8'
								)
		
		lj_cur = ljdb.cursor()
		print('数据库连接成功！')
		return ljdb,lj_cur
	except:
		print('连接数据库失败！')
		return None
	
def close_db(ljdb):
	
	ljdb.close()
	print('关闭数据库')	

def create_table(lj_cur):
	
	try:
		sql_create = '''create table chengdu_20190315 (houselink varchar(255),houseID varchar(255),housename varchar(255),time_build varchar(255),totalprice varchar(255),
						unitprice varchar(255),community varchar(255),district varchar(255),block varchar(255),road varchar(255),supplement varchar(255),
						type_house varchar(255),area_gross varchar(255),area_real varchar(255),orientation varchar(255),decoration varchar(255),own_time varchar(255),
						floor varchar(255),layout varchar(255),type_building varchar(255),material varchar(255),elevator_num varchar(255),
						time_listing varchar(255),time_deal varchar(255),time_limit varchar(255),property varchar(255),usage_yt varchar(255),
						own varchar(255),pledge varchar(255),upload varchar(255)
				)ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
				'''

		lj_cur.execute(sql_create)
		
		print('创建数据库表格成功！')
	
	except:
		print('创建数据库表格失败！')

def drop_table(lj_cur):
	
	try:
		lj_cur.execute('drop table chengdu_20190315')
		print('删除表格成功！')
	except:
		print('删除表格失败！')

	
if __name__ =='__main__':

	ljdb,lj_cur= connect_db()
	
	create_table(lj_cur)
	#drop_table(lj_cur)
	
	close_db(ljdb)
