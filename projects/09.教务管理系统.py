from random import choice
#
school_control={}
menu="""
*****学生管理系统*****
*   1.添加学生信息   *
*   2.删除学生信息   *
*   3.修改学生信息   *
*   4.查询学生信息   *
*   5.列出所有学生   *
*   6.统计班级成绩   *
*   7.退出系统      *
"""
print("欢迎使用学生管理系统")

while True:
    print(menu)

    choice=int(input("请选择执行的操作(1-7)"))
    match choice:
        case 1:
            student_name=input("请输入学生姓名")
            student_chinese= int(input("请输入学生语文成绩"))
            student_math= int(input("请输入学生数学成绩"))
            student_English = int(input("请输入学生英语成绩"))
            if student_name in school_control:
                print("该学生已经录入过了")
            else:
                school_control[student_name]={"语文成绩":student_chinese,"数学成绩":student_math,"英语成绩":student_English}
            print("学生信息录入完毕")

        case 2:
            student_name=input("请选择要删除的学生信息:")

            if student_name  not in  school_control:
                print("该学生不在系统内，请重新选择学生")
            else:
                del school_control[student_name]
                print("该学生信息以删除")

        case 3:
            student_name=input("请输入要修改信息的学生")
            if student_name not in school_control:
                print("该学生不在系统内，请重新选择学生")
                continue
            student_chinese=int(input("请输入新的语文成绩："))
            student_math = int(input("请输入新的数学成绩："))
            student_English = int(input("请输入新的英语成绩："))
            school_control[student_name]={"语文成绩":student_chinese,"数学成绩":student_math,"英语成绩":student_English}
            print("学生信息修改完毕")

        case 4:
            name=input("输入你要查询的学生")
            found = False
            for student_name in school_control:
                if student_name== name:
                    print(f"姓名: {name}, 语文: {school_control[student_name]['语文成绩']}, 数学: {school_control[student_name]['数学成绩']}, 英语: {school_control[student_name]['英语成绩']}")
                    found = True
                    break
            if not found:
                print("未找到该学生。")

        case 5:
            for student_name in school_control.keys():
                xx = school_control[student_name]
                print(f"学生：{student_name},语文成绩：{xx['语文成绩']},数学成绩{xx['数学成绩']},英语成绩{xx['英语成绩']}")

        case 6:
            pass
        case 7:
            print("成功退出")
            break
        case _:
            print("操作有误,请重试")



