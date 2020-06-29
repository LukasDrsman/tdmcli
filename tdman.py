import os
from datetime import datetime
from colors import *
from config import *

class Todolist:
    def __init__(self, file, path):
        self.todo = []
        self.title = ""
        self.file = file
        self.today = datetime.today()

    def cfile(self):
        if(writeonexit == True):
            self.save()
        todofiles = os.listdir(os.path.expanduser(defpath))
        for i in range(len(todofiles)):
            print(" ["+str(i)+"] " + (todofiles[i].split("."))[0])
        select = input("(number or name) " + prompt)
        try:
            select = int(select)
            try:
                self.file = os.path.expanduser(defpath) + todofiles[select]
            except:
                self.file = os.path.expanduser(deffile)
        except:
            self.file = os.path.expanduser(defpath) + select + ".tdff"
            if(os.path.isfile(self.file) != True):
                todofile = open(self.file, "w")
                todofile.close()
        self.parse()

    def parse(self):
        self.todo = []
        todofile = open(self.file, 'r+')
        pretitle, filetype = str(os.path.basename(todofile.name)).split(".")
        self.title = pretitle
        lines = todofile.readlines()
        for line in lines:
            data = (line.rstrip("\n")).split("::")
            if(len(data) >= 2):
                try:
                    due = datetime.strptime(data[2], '%Y-%m-%d-%H-%M')
                    self.todo.append([data[0], data[1], due])
                except:
                    self.todo.append([data[0], data[1], "NaD"])
        todofile.close()

    def show(self):
        self.today = datetime.today()
        print("\033c", end="")
        print(self.title+":")
        for task in range(len(self.todo)):
            if(lnnumf != ""):
                num = task + 1
                print(lnnumf % num, end="")
            for flag in flags:
                    if(self.todo[task][1] == flag[0]):
                        if(type(self.todo[task][2]) is datetime and (flag[4] == True or self.todo[task][2] > self.today)):
                            print(flag[2] + flag[1] + flag[3] + self.todo[task][0] + end + "  ~  " + self.todo[task][2].strftime(dateformat))
                        elif(type(self.todo[task][2]) is datetime and (flag[4] == False and self.todo[task][2] <= self.today)):
                            print(flag[2] + flag[1] + red + self.todo[task][0] + end + "  ~  " + self.todo[task][2].strftime(dateformat))
                        else:
                            print(flag[2] + flag[1] + flag[3] + self.todo[task][0] + end)
                        break
        print(" ")

    def new(self, param):
        if(param == "-i"):
            num = len(self.todo) - 1
            name = input("(name) " + prompt)
            self.todo.append([name, defflag, "NaD"])
            self.cdate(num)
            flaglist = "("
            for i in range(len(flags)):
                if(i + 1 == len(flags)):
                    flaglist = flaglist + flags[i][0] + ")"
                else:
                    flaglist = flaglist + flags[i][0] + ", "
            flag = input(flaglist + " " + prompt)
            self.todo[num + 1][1] = flag
        else:
            self.todo.append([param, defflag, "NaD"])

    def remove(self, num):
            try:
                tasknum = int(num) - 1
            except:
                tasknum = len(self.todo) + 1
            try:
                self.todo.pop(tasknum)
            except:
                pass

    def cdate(self, num):
            try:
                tasknum = int(num) - 1
            except:
                tasknum = len(self.todo) + 1

            try:
                preyear = input("(year) " + prompt)
                if(preyear == "."):
                    year = self.today.strftime("%Y")
                else:
                    year = preyear
                premonthday = input("(month day) " + prompt)
                if(premonthday == "."):
                    monthday = self.today.strftime("%m %d")
                else:
                    monthday = premonthday
                prehourminute = input("(hour minute) " + prompt)
                if(prehourminute == "."):
                    hourminute = self.today.strftime("%H %M")
                else:
                    hourminute = prehourminute

                dt = year+"-"+monthday+"-"+hourminute
                due = datetime.strptime(dt, '%Y-%m %d-%H %M')
            except:
                due = "NaD"
            try:
                self.todo[tasknum][2] = due
            except:
                pass

    def clear(self):
        consent = input("Are you sure you want to clear your todolist?\n([y]es or [n]o) " + prompt)
        consent.lower()
        if(consent == "y" or consent == "yes"):
            self.todo.clear()

    def cflag(self, flg, num):
        try:
            tasknum = int(num) - 1
        except:
            tasknum = len(self.todo) + 1
        for flag in flags:
            if(flag[5][0] == flg or flag[5][1] == flg):
                try:
                    self.todo[tasknum][1] = flag[0]
                except:
                    pass

    def save(self):
        todofile = open(self.file, 'w')
        todofile.write("")
        todofile.close()
        todofile = open(self.file, 'a')
        for task in self.todo:
            if(type(task[2]) is datetime):
                todofile.write(task[0] + "::" + task[1] + "::" + task[2].strftime('%Y-%m-%d-%H-%M') + "\n")
            else:
                todofile.write(task[0] + "::" + task[1] + "\n")
        todofile.close()

    def quit(self):
        if(writeonexit == True):
            self.save()
        print("\033c", end="")
        exit()

    def order(self, param):
        type, direction = param.split(" ", 1)
        type.lower()
        direction.lower()

        if(type == "date" or type == "d"):
            wdate = []
            wodate = []
            for task in self.todo:
                if(task[2] != "NaD"):
                    wdate.append(task)
                else:
                    wodate.append(task)
            self.todo.clear()
            if(direction == "h" or direction == "highest"):
                wdate.sort(key=lambda date: date[2], reverse=True)
            if(direction == "l" or direction == "lowest"):
                wdate.sort(key=lambda date: date[2])
            for task in wdate:
                self.todo.append(task)
            for task in wodate:
                self.todo.append(task)

        if(type == "priority" or type == "p"):
            wpriority = []
            for task in self.todo:
                for flag in flags:
                    if(task[1] == flag[0]):
                        wpriority.append(task + [flag[6]])
            if(direction == "h" or direction == "highest"):
                wpriority.sort(key=lambda p_index: p_index[3], reverse=True)
            elif(direction == "l" or direction == "lowest"):
                wpriority.sort(key=lambda p_index: p_index[3])
            self.todo.clear()
            for task in wpriority:
                self.todo.append([task[0], task[1], task[2]])
