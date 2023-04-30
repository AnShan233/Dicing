from PySide2.QtUiTools import QUiLoader
from os import startfile
import random
import Global_Var 
#初始界面
#将来记得改
class Main_Window:
    def __init__(self):
        self.ui=QUiLoader().load("ui/Main.ui")
        self.ui.button_number_select.clicked.connect(self.num_Select_open)
        self.ui.button_member_manage.clicked.connect(self.member_Managing_open)
    def num_Select_open(self):
        self.num_Sel = Num_Select()
        self.num_Sel.ui.move(650,800)        
        self.num_Sel.ui.show()
        self.ui.close()
    def member_Managing_open(self):
        startfile("member.txt")

#Number selecting window
class Num_Select:
    def __init__(self):
        self.ui=QUiLoader().load("ui/Num_Select.ui")
        self.ui.Enter.clicked.connect(self.enter_Pressed)
    def enter_Pressed(self):
        try:
            num_input=int(self.ui.Num.text()) 
            #这里num_lines,num_list有调用问题
            if num_input>=1 and num_input<=Global_Var.num_lines:
                num_list_chosen=[]
                self.ending = Ending()
                self.ending.ui.move(650,800) 
                for i in range(num_input):
                    num_chosen=random.choice(Global_Var.num_list)
                    num_list_chosen.append(num_chosen)
                    Global_Var.num_list.remove(num_chosen)
                self.ending.ui.textEdit.insertPlainText("\n".join(num_list_chosen)) 
                self.ending.ui.move(650,800) 
                self.ending.ui.show()
                self.ui.close()
            else :
                self.wrong_input = Wrong_input()
                self.wrong_input.ui.move(650,800)
                self.wrong_input.ui.show()
                self.ui.close()
                print(Global_Var.num_lines)
        except:
            self.wrong_input = Wrong_input()
            self.wrong_input.ui.move(650,800)
            self.wrong_input.ui.show()
            self.ui.close()
            print("gosh")
        self.ui.close()

#报错问题
class Wrong_input:
    def __init__(self):
        self.ui=QUiLoader().load("ui/wrong_input.ui")

#Ending
class Ending:
    def __init__(self):
        self.ui=QUiLoader().load("ui/Ending.ui")