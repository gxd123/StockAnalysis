import MySQLdb

class DataStore:
	strInsertYahooData='insert into YahooData(%s, %s, %s, %s, %s)
	def __init__(self)
		self.conn =MySQLdb.connect( host = 'localhost', port = 3306, user = 'root', passwd = '19891338', db = 'test' ) 
		self.cur==conn.cursor()
	
	def addYahooData(data)
		cur.execute(strInsertYahooData, 
		(data.code, 
		data.date, 
		data.open, 
		data.high, 
		data.low, 
		data.close,
		data.volume,
		data.adjClose))
		
	def done(self)
		self.cur.close()
		self.conn.commit()
		self.conn.close()

	
