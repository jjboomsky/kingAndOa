import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import services


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 400
        height = 300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_968 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        GLabel_968["font"] = ft
        GLabel_968["fg"] = "#333333"
        GLabel_968["justify"] = "center"
        GLabel_968["text"] = "年"
        GLabel_968.place(x=10, y=50, width=61, height=36)

        # 年
        self.year = tk.Entry(root)
        self.year["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.year["font"] = ft
        self.year["fg"] = "#333333"
        self.year["justify"] = "center"
        self.year["text"] = "year"
        self.year.place(x=70, y=50, width=120, height=36)

        GLabel_672 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        GLabel_672["font"] = ft
        GLabel_672["fg"] = "#333333"
        GLabel_672["justify"] = "center"
        GLabel_672["text"] = "月"
        GLabel_672.place(x=190, y=50, width=61, height=36)

        # 月
        self.month = tk.Entry(root)
        self.month["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.month["font"] = ft
        self.month["fg"] = "#333333"
        self.month["justify"] = "center"
        self.month["text"] = "month"
        self.month.place(x=240, y=50, width=120, height=36)

        GButton_79 = tk.Button(root)
        GButton_79["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=14)
        GButton_79["font"] = ft
        GButton_79["fg"] = "#000000"
        GButton_79["justify"] = "center"
        GButton_79["text"] = "生成数据"
        GButton_79.place(x=60, y=140, width=130, height=46)
        GButton_79["command"] = self.GButton_79_command

        GMessage_553 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_553["font"] = ft
        GMessage_553["fg"] = "#333333"
        GMessage_553["justify"] = "center"
        GMessage_553["text"] = "Message"
        GMessage_553.place(x=150, y=210, width=80, height=25)

        GButton_576 = tk.Button(root)
        GButton_576["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=14)
        GButton_576["font"] = ft
        GButton_576["fg"] = "#000000"
        GButton_576["justify"] = "center"
        GButton_576["text"] = "excel导入到数据库，确认了再点！"
        GButton_576.place(x=230, y=140, width=130, height=46)
        GButton_576["command"] = self.GButton_576_command

    # 生成excel
    def GButton_79_command(self):
        year = self.year.get()
        month = self.month.get()
        s = services.ServerMain()
        msg = s.get_report(year, month)
        flag = s.get_worker_mooney(year, month)
        if flag == 1:
            msg2 = s.set_user_name(year, month)
            print(msg + msg2)
            tk.messagebox.showinfo('提示', msg + msg2)
        else:
            tk.messagebox.showinfo('提示', "请先关闭excel！")

    def GButton_576_command(self):
        year = self.year.get()
        month = self.month.get()
        s = services.ServerMain()
        msg = s.set_oa_money()
        if msg == 1:
            msg2 = s.set_king_mooney(year, month)
            tk.messagebox.showinfo('提示', 'OA写入加班工资成功！' + msg2)
        else:
            tk.messagebox.showinfo('提示', '失败！请先关闭excel')


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
