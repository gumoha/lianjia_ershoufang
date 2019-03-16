import json
import pymysql

def connect_db():
	try:
		ljdb = pymysql.connect(host='127.0.0.1',
								port=3306,
								user='banquan',
								password='12345',
								db='lianjia_ershoufang')
		
		lj_cur = ljdb.cursor()
		print('数据库连接成功！')
		return ljdb,lj_cur
	except:
		print('连接数据库失败！')
		return None
	
def close_db(ljdb):
	
	ljdb.close()
	print('关闭数据库')

def jsondata_insert(ljdb,lj_cur):
	with open (r'F:\Scrapy\lianjia_ershoufang\ershoufang_json',encoding='utf-8') as f:
		i = 0
		while True:
			i +=1
			print('正在载入第%s行……'%i)
			try:
				lines = f.readline()
				data_text = json.loads(lines)
				
				
				
			except Exception as e:
				ljdb.rollback()
				print('写入数据库错误：',e)
				break
			

	
if __name__ =='__main__':

	ljdb,lj_cur= connect_db()
	
	#create_table(lj_cur)
	#drop_table(lj_cur)
	
	
	
	close_db(ljdb)
