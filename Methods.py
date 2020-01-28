import openpyxl
from docxtpl import DocxTemplate
import datetime
import pyodbc as pdb

conn = pdb.connect(Trusted_Connection='yes', driver='{SQL Server}', server='DESKTOP-96KVUH2', database='SPbP')
cursor = conn.cursor()

def printOrder(fiostudent, institut, specialnost, kurs, gruppa, formaobucheniya, osnovaobucheniya):
    doc = DocxTemplate('C:\\Users\\Таня\\Documents\\Order.docx')
    today = datetime.date.today()
    data = str(today.day) + '.' + str(today.month) + '.' + str(today.year)
    if osnovaobucheniya == 'Бюджет':
        osnova = 'бюджетной'
    else:
        osnova = 'контрактной'
    if formaobucheniya == 'Очное':
        forma = 'очной'
    if formaobucheniya == 'Заочное':
        forma = 'заочной'
    if formaobucheniya == 'Очно-заочное':
        forma = 'очно-заочной'
    context = {'fiostudent': fiostudent, 'institut': institut, 'specialnost': specialnost, 'kurs': kurs,
               'gruppa': gruppa, 'formaobucheniya': forma, 'osnovaobucheniya': osnova, 'data': data}
    doc.render(context)
    doc.save('order-final.docx')

# printOrder('Былин Владимир Игоревич', 'ИКНТ', 'Разработка ПО', '4', '3530904/60104', 'Очное', 'Бюджет')

def findStudent(LastName, Direction, Profile, Group):
    cursor.execute("SELECT dbo.Find_Student('" +
                   LastName + "', '" + Direction + "', '" + Profile + "', '" + Group + "')")
    students = []
    temp = ''
    count = 0
    line = str(cursor.fetchone())
    if (line != "('', )"):
        while (line[0] != '.'):
            temp = line[:line.find(',')]
            line = line[line.find(',') + 1: len(line) + 1]
            count += 1
        line = line[1: len(line)]
        if count == 1:
            temp = temp[2:len(temp)]
        for i in range(count):
            students.append([])
        for i in range(len(students)):
            students[i].append(temp)
        for i in range(10):
            for j in range(count):
                students[j].append(line[:line.find(',')])
                line = line[line.find(',') + 1: len(line)]
            line = line[1: len(line)]
        return students
    else:
        return temp

# print(findStudent('Агеев', 'Все', 'Все', 'Все'))

def fillDB():
    wb = openpyxl.load_workbook('students.xlsx')
    sheet = wb['vshpi']

    student = []

    for i in range(sheet.max_row):
        line = str(sheet['A' + str(i + 1)].value)
        line = line.replace(line[:line.find(',') + 2], "")
        while len(line) > 1:
            student.append(line[:line.find('"')])
            line = line[line.find('"') + 3:len(line) + 1]

        cursor.execute("EXEC Insert_Inst '" + student[7] + "'")
        cursor.execute("EXEC Insert_Department '" + student[8] + "', '" + student[7] + "'")
        cursor.execute("EXEC Insert_YGSN '" + student[9] + "'")

        if (student[4][0:1] != 'в' and student[4][0:1] != 'з'):
            num_inst = int(student[4][0:2])
            dgr = student[4][2:3]
            prof = student[10] + '_' + student[4][9:11]
        elif (student[4][0:1] == 'в' or student[4][0:1] == 'з'):
            num_inst = int(student[4][1:3])
            dgr = student[4][3:4]
            prof = student[10] + '_' + student[4][10:12]

        degree = ''
        if dgr == '3':
            degree = 'бакалавриат'
        elif dgr == '4':
            degree = 'магистратура'
        elif dgr == '6':
            degree = 'аспирантура'
        cursor.execute("EXEC Insert_Direction '" + student[10] + "', '" + student[9] + "'")
        cursor.execute("EXEC Insert_Profile '" + prof + "', '" + student[10] + "'")
        values = (student[4], student[7], degree, prof, num_inst)
        cursor.execute("EXEC Insert_Group ?, ?, ?, ?, ?", values)
        values = (student[0], student[1], student[2], student[3], student[4], int(student[5]), student[6],
                  student[8], student[11], student[12], student[13], student[14], student[15], student[16],
                  student[17][0])
        cursor.execute("EXEC Insert_Student ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?", values)
        conn.commit()
        student.clear()

# fillDB() этот вызов запускать нужно только один раз, потом обязательно закомментировать