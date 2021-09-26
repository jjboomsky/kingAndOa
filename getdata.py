# encoding: utf-8
import pymssql
import pymssql._mssql as _mssql
import decimal
import uuid

_mssql.__version__
decimal.__version__

# 获取26金蝶数据库得数据
class Getdata:

    def __init__(self):
        print("链接26数据库")

    def get_data(self, year, month):
        conn = pymssql.connect(host='192.168.0.26',
                               user='sa',
                               password='123.com',
                               database='AIS20210908080054',
                               charset='utf8')
        sql = "SELECT  FPerMemoryCode,FEmpID,FYear,FPeriod,FPA15,FPA16,FPA17,FPA18,FPA19,FPA22 FROM t_PANewData LEFT JOIN t_PA_Personal ON t_PANewData.FEmpID = t_PA_Personal.FItemID WHERE  t_PA_Personal.FPerMemoryCode!='' AND FYear=%d AND FPeriod = %d"
        cursor = conn.cursor()
        cursor.execute(sql, (year, month))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    def get_data2(self, year, month):
        conn = pymssql.connect(host='192.168.0.26',
                               user='sa',
                               password='123.com',
                               database='AIS20210908080122',
                               charset='utf8')
        sql = "SELECT  FPerMemoryCode,FEmpID,FYear,FPeriod,FPA15,FPA16,FPA17,FPA18,FPA19,FPA22 FROM t_PANewData LEFT JOIN t_PA_Personal ON t_PANewData.FEmpID = t_PA_Personal.FItemID WHERE  t_PA_Personal.FPerMemoryCode!='' AND FYear=%d AND FPeriod = %d"
        cursor = conn.cursor()
        cursor.execute(sql, (year, month))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    def get_data3(self, year, month):
        conn = pymssql.connect(host='192.168.0.26',
                               user='sa',
                               password='123.com',
                               database='AIS20210908080155',
                               charset='utf8')
        sql = "SELECT  FPerMemoryCode,FEmpID,FYear,FPeriod,FPA15,FPA16,FPA17,FPA18,FPA19,FPA22 FROM t_PANewData LEFT JOIN t_PA_Personal ON t_PANewData.FEmpID = t_PA_Personal.FItemID WHERE  t_PA_Personal.FPerMemoryCode!='' AND FYear=%d AND FPeriod = %d"
        cursor = conn.cursor()
        cursor.execute(sql, (year, month))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    def get_data4(self, year, month):
        conn = pymssql.connect(host='192.168.0.26',
                               user='sa',
                               password='123.com',
                               database='AIS20210908080214',
                               charset='utf8')
        sql = "SELECT  FPerMemoryCode,FEmpID,FYear,FPeriod,FPA15,FPA16,FPA17,FPA18,FPA19,FPA22 FROM t_PANewData LEFT JOIN t_PA_Personal ON t_PANewData.FEmpID = t_PA_Personal.FItemID WHERE  t_PA_Personal.FPerMemoryCode!='' AND FYear=%d AND FPeriod = %d"
        cursor = conn.cursor()
        cursor.execute(sql, (year, month))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results

    def set_money(self, re):
        conn = pymssql.connect(host='192.168.0.26',
                               user='sa',
                               password='123.com',
                               database='AIS20210908080054',
                               charset='utf8')
        sql = "UPDATE t_PANewData SET FPA1053 = %d  WHERE FEmpID = %d AND FYear = %d AND FPeriod = %d"
        cursor = conn.cursor()
        try:
            cursor.executemany(sql, re)
            conn.commit()
            cursor.close()
            conn.close()
            return 1
        except ValueError:
            return 0
    def set_money2(self, re):
        conn = pymssql.connect(host='192.168.0.26',
                               user='sa',
                               password='123.com',
                               database='AIS20210908080122',
                               charset='utf8')
        sql = "UPDATE t_PANewData SET FPA1052 = %d  WHERE FEmpID = %d AND FYear = %d AND FPeriod = %d"
        cursor = conn.cursor()
        try:
            cursor.executemany(sql, re)
            conn.commit()
            cursor.close()
            conn.close()
            return 1
        except ValueError:
            return 0
    def set_money3(self, re):
        conn = pymssql.connect(host='192.168.0.26',
                               user='sa',
                               password='123.com',
                               database='AIS20210908080155',
                               charset='utf8')
        sql = "UPDATE t_PANewData SET FPA1052 = %d  WHERE FEmpID = %d AND FYear = %d AND FPeriod = %d"
        cursor = conn.cursor()
        try:
            cursor.executemany(sql, re)
            conn.commit()
            cursor.close()
            conn.close()
            return 1
        except ValueError:
            return 0
    def set_money4(self, re):
        conn = pymssql.connect(host='192.168.0.26',
                               user='sa',
                               password='123.com',
                               database='AIS20210908080214',
                               charset='utf8')
        sql = "UPDATE t_PANewData SET FPA1052 = %d  WHERE FEmpID = %d AND FYear = %d AND FPeriod = %d"
        cursor = conn.cursor()
        try:
            cursor.executemany(sql, re)
            conn.commit()
            cursor.close()
            conn.close()
            return 1
        except ValueError:
            return 0

