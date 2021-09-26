from decimal import Decimal

import xlwt
import xlrd
import get_oa_data
import getdata
import indata


class ServerMain:

    def __init__(self):
        print("主服务")

    def get_report(self, year, month):
        b = indata.Indata()
        select_one = b.select_flag(year, month)
        msg = '数据已经存在！'
        if select_one is None:
            a = getdata.Getdata()
            re1 = a.get_data(year, month)
            re2 = a.get_data2(year, month)
            re3 = a.get_data3(year, month)
            re4 = a.get_data4(year, month)
            re = re1 + re2 + re3 + re4
            print(re)
            msg = b.get_report(re)
        return msg

    # 这个月发的工资是上个月的奖金
    def get_worker_mooney(self, year, month):
        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet("Sheet1")
        worksheet.write(0, 0, '年份')
        worksheet.write(0, 1, '月份')
        worksheet.write(0, 2, '工号')
        worksheet.write(0, 3, '姓名')
        worksheet.write(0, 4, '加班转工资天数')
        worksheet.write(0, 5, '加班工资')
        int_year = int(year)
        int_month = int(month) - 1
        if int_month <= 0:
            int_year = int_year - 1
            int_month = 12
        a = get_oa_data.GetOaDta()
        re = a.get_worker_bonus(int_year, int_month)
        print(re)
        for i, x in enumerate(re):
            worksheet.write(i + 1, 0, year)
            worksheet.write(i + 1, 1, month)
            worksheet.write(i + 1, 2, x[0])
            worksheet.write(i + 1, 3, x[13])
            worksheet.write(i + 1, 4, x[11])
            worksheet.write(i + 1, 5, (x[11] * x[14]).quantize(Decimal('0.0')))
        try:
            workbook.save("数据.xls")
            return 1
        except ValueError:
            return 0


    # 回写到金蝶的奖金中，1053
    def set_king_mooney(self, year, month):
        b = indata.Indata()
        re = b.get_data()
        print(re)
        r_list = []
        for x in re:
            one_data = (x[10], x[1], year, month)
            r_list.append(one_data)
        print(r_list)
        king = getdata.Getdata()
        flg1 = king.set_money(r_list)
        flg2 = king.set_money2(r_list)
        flg3 = king.set_money3(r_list)
        flg4 = king.set_money4(r_list)
        if flg1 == 1 and flg2 == 1 and flg3 == 1 and flg4 == 1:
            msg = '金蝶写入加班工资成功！'
        else:
            msg = '金蝶写入加班工资失败！'
        return msg

    def set_user_name(self, year, month):
        int_year = int(year)
        int_month = int(month) - 1
        if int_month <= 0:
            int_year = int_year - 1
            int_month = 12
        a = get_oa_data.GetOaDta()
        re = a.get_user_data(int_year, int_month)
        r_list = []
        for x in re:
            one_data = (x[13], x[15], x[0], year, month)
            r_list.append(one_data)
        b = indata.Indata()
        msg = b.set_worker_data(r_list)
        return msg

    # excel写回oa数据库
    def set_oa_money(self):
        try:
            data_excel = xlrd.open_workbook("数据.xls")
            sheet_obj = data_excel.sheet_by_index(0)
            nrows = sheet_obj.nrows
            in_data = []
            for r in range(1, nrows):
                money = sheet_obj.cell(r, 5).value
                work_id = sheet_obj.cell(r, 2).value
                year = sheet_obj.cell(r, 0).value
                month = sheet_obj.cell(r, 1).value
                data = (money, work_id, year, month)
                in_data.append(data)

            b = indata.Indata()
            msg = b.set_worker_money(in_data)
            return msg
        except ValueError:
            return 0
