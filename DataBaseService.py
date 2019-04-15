from pymysql import connect,IntegrityError
from datetime import datetime

class DataBaseService:

    def __init__(self):
        # real host, user,password were replaced
        self.connection = connect(host='host',user='user',password='password',db='db')
        self.cursor = self.connection.cursor()

    def save_log(self,ip,request,response):
        log_time = datetime.now()

        self.cursor.execute('INSERT INTO Log (ip,requestType,response,time)'
                            ' VALUES ("{}",{},{},"{}")'.format(ip,request,response,log_time.strftime("%Y-%m-%d %H:%M:%S")))

        self.connection.commit()

    def __del__(self):
        self.connection.close()
