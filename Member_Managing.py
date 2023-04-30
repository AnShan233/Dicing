import Global_Var

mem_=open("member.txt",encoding="utf-8")
Global_Var.num_list=mem_.readlines()
Global_Var.num_lines=len(open("member.txt",encoding="utf-8").readlines())
