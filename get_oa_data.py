# encoding: utf-8
import pymssql
import pymssql._mssql as _mssql
import decimal
import uuid

_mssql.__version__
decimal.__version__


class GetOaDta:
    def __init__(self):
        self.conn = pymssql.connect(host='192.168.0.66',
                                    user='sa',
                                    password='123.com',
                                    database='a8v56',
                                    charset='utf8')
        print('链接OA数据库')

    def get_worker_bonus(self, year, month):
        print(year)
        print(month)
        sql = "SELECT c.field0004 AS '工号',a.field0190 AS '岗位类型', a.field0049 AS '工龄' , c.field0064 AS '加班天数' ,c.field0046 AS '年度',c.field0047 AS '月份',c.field0048 AS '应出勤天数' ,c.field0049 AS '实际出勤天数', c.field0070 AS '事假合计天数', c.field0071 AS '病假合计天数',c.field0050 AS '旷工天数',c.field0129 AS '换算工资天数',c.field0130 AS '剩余调休天数' , a.field0001 AS '姓名',a.field0236 AS '加班工资金额',a.field0235 AS '加班工资类型' FROM formmain_1950 AS c LEFT JOIN formmain_1726 AS a ON c.field0004 = a.field0189 WHERE c.field0129 is NOT NULL AND c.field0129!='.00' AND a.field0236 is NOT NULL AND c.field0046 = %d AND c.field0047=%d"
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, (year, month))
            re = cursor.fetchall()
            cursor.close()
            self.conn.close()
            return re
        except ValueError:
            return '失败！'

    def get_money(self, year, month):
        sql = "SELECT c.field0004 AS '工号',a.field0190 AS '岗位类型', a.field0049 AS '工龄' , c.field0064 AS '加班天数' ,c.field0046 AS '年度',c.field0047 AS '月份',c.field0048 AS '应出勤天数' ,c.field0049 AS '实际出勤天数', c.field0070 AS '事假合计天数', c.field0071 AS '病假合计天数',c.field0050 AS '旷工天数',c.field0129 AS '换算工资天数',c.field0130 AS '剩余调休天数' FROM formmain_1950 AS c LEFT JOIN formmain_1726 AS a ON c.field0004 = a.field0189 WHERE c.field0129 is NOT NULL AND c.field0129!='.00'AND c.field0046 = %d AND c.field0047=%d"
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, (year, month))
            re = cursor.fetchall()
            cursor.close()
            self.conn.close()
            return re
        except ValueError:
            return '失败！'

    def get_user_data(self, year, month):
        print(year)
        print(month)
        sql = "SELECT c.field0004 AS '工号',a.field0190 AS '岗位类型', a.field0049 AS '工龄' , c.field0064 AS '加班天数' ,c.field0046 AS '年度',c.field0047 AS '月份',c.field0048 AS '应出勤天数' ,c.field0049 AS '实际出勤天数', c.field0070 AS '事假合计天数', c.field0071 AS '病假合计天数',c.field0050 AS '旷工天数',c.field0129 AS '换算工资天数',c.field0130 AS '剩余调休天数' , a.field0001 AS '姓名',a.field0236 AS '加班工资金额',a.field0235 AS '加班工资类型' FROM formmain_1950 AS c LEFT JOIN formmain_1726 AS a ON c.field0004 = a.field0189 WHERE  c.field0046 = %d AND c.field0047=%d"
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, (year, month))
            re = cursor.fetchall()
            cursor.close()
            self.conn.close()
            return re
        except ValueError:
            return '失败！'
