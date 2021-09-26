# encoding: utf-8
import pymssql
import pymssql._mssql as _mssql
import decimal
import uuid

_mssql.__version__
decimal.__version__


# 中间数据库92
class Indata:
    re_data = {}
    conn = None

    def __init__(self):
        self.conn = pymssql.connect(host='192.168.0.92',
                                    user='sa',
                                    password='123.com',
                                    database='report',
                                    charset='utf8')
        print('开始插入')

    def get_report(self, re):
        sql = "INSERT INTO report_data(FPerMemoryCode,FEmpID,FYear,FPeriod,FPA15,FPA16,FPA17,FPA18,FPA19,FPA22) VALUES(%s,%d,%d,%d,%d,%d,%d,%d,%d,%d)"
        cursor = self.conn.cursor()
        try:
            cursor.executemany(sql, re)
            self.conn.commit()
            cursor.close()
            self.conn.close()
            return 'k3取数成功！'
        except ValueError:
            return 'k3取数失败！'

    def set_worker_money(self, re):
        sql = "UPDATE report_data SET FPA1053 = %d WHERE FPerMemoryCode=%s AND FYear = %d AND FPeriod = %d"
        cursor = self.conn.cursor()
        try:
            cursor.executemany(sql, re)
            self.conn.commit()
            cursor.close()
            self.conn.close()
            return 1
        except ValueError:
            return 0

    def set_worker_data(self, re):
        sql = "UPDATE report_data SET name = %s , PFA_type = %s WHERE FPerMemoryCode=%s AND FYear = %d AND FPeriod = %d"
        cursor = self.conn.cursor()
        try:
            cursor.executemany(sql, re)
            self.conn.commit()
            cursor.close()
            self.conn.close()
            return '成功！'
        except ValueError:
            return '失败！'

    def get_data(self):
        sql = "SELECT * FROM report_data WHERE FPA1053 IS NOT NULL AND FPA1053!='.00'"
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            self.conn.close()
            return results
        except ValueError:
            return []

    # 查看是否存在月份的数据
    def select_flag(self, year, month):
        sql = "SELECT * FROM report_data WHERE FYear = %s AND FPeriod = %s"
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, (year, month))
            results = cursor.fetchone()
            cursor.close()
            return results
        except ValueError:
            return []
