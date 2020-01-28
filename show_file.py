import sys
import openpyxl
from docxtpl import DocxTemplate
import datetime
import pyodbc as pdb
from PyQt5 import QtWidgets, QtCore

from changes import Ui_changes
from inform import Ui_inform
from main import Ui_MainWindow
from select import Ui_select
from order import Ui_Order

class Inform_bd(QtWidgets.QDialog, Ui_inform):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("Нет подключения к базе данных")

class Inform_file(QtWidgets.QDialog, Ui_inform):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("Файл не может быть сохранен")

try:
    conn = pdb.connect(Trusted_Connection='yes', driver='{SQL Server}', server='DESKTOP-96KVUH2', database='SPbPU')
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
            for i in range(9):
                for j in range(count):
                    students[j].append(line[:line.find(',')])
                    line = line[line.find(',') + 1: len(line)]
                line = line[1: len(line)]
            return students
        else:
            return temp

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


    class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)

            self.pushButton.clicked.connect(self.ClicedButton1)  # вход
            self.pushButton_2.clicked.connect(self.ClicedButton2)  # регистрация

        def Information(self, text):
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Информация")
            msg.setText(text)
            msg.exec_()

        def ClicedButton1(self):
            if (self.lineEdit.text().isspace() or self.lineEdit_2.text().isspace() or
                    self.lineEdit.text() == "" or self.lineEdit_2.text() == ""):
                self.Information("Введите логин и пароль")
            else:
                cursor.execute("SELECT dbo.Check_Enter('" + self.lineEdit.text() + "', '"
                               + self.lineEdit_2.text() + "')")
                flag = cursor.fetchone()[0]
                if (flag == 1):
                    self.Information("Неверный логин или пароль")
                elif (flag == 0):
                    self.close()
                    window = Select()
                    window.show()
                    window.exec_()

        def ClicedButton2(self):
            if (self.lineEdit.text().isspace() or self.lineEdit_2.text().isspace() or
                    self.lineEdit.text() == "" or self.lineEdit_2.text() == ""):
                self.Information("Введите логин и пароль")
            else:
                cursor.execute("SELECT dbo.Check_Login('" + self.lineEdit.text() + "')")
                flag = cursor.fetchone()[0]
                if (flag == 1):
                    self.Information("Такой логин уже существует")
                    self.lineEdit.setText("")
                elif (flag == 0):
                    cursor.execute("INSERT INTO LogPss VALUES('" + self.lineEdit.text() + "', '"
                                   + self.lineEdit_2.text() + "')")
                    conn.commit()
                    self.close()
                    window = Select()
                    window.show()
                    window.exec_()

    class Select(QtWidgets.QDialog, Ui_select):
        def __init__(self):
            super().__init__()
            self.setupUi(self)

            self.pushButton.clicked.connect(self.ClicedButton1)  # открытвается редактор
            self.pushButton_2.clicked.connect(self.ClicedButton2)  # открывается создание заявления
            self.pushButton_3.clicked.connect(self.ClicedButton3)  # выход на окно входа должен быть,
                                                       # пока тут закрытие программы, потому что я хз, как

        def ClicedButton1(self):
            self.close()
            window = Changes()
            window.show()
            window.exec_()

        def ClicedButton2(self):
            self.close()
            window = Order()
            window.show()
            window.exec_()

        def ClicedButton3(self):
            self.close()

    class Changes(QtWidgets.QDialog, Ui_changes):
        def __init__(self):
            super().__init__()
            self.setupUi(self)

            self.row = []
            self.column = []
            self.text = []
            self.students = ''

            self.pushButton.clicked.connect(self.ClicedButton)  # появляются студенты в таблице
            self.pushButton_2.clicked.connect(self.ClicedButton2)  # сохранение изменений
            self.pushButton_3.clicked.connect(self.ClicedButton3)  # назад

            self.comboBox.addItem("Все")  # заполнение комбобокса с направлениями
            cursor.execute("SELECT dbo.Find_Direct()")
            line = str(cursor.fetchone())
            line = line[2:len(line)]
            while (line[0] != "'"):
                self.comboBox.addItem(line[:line.find(',')])
                line = line[line.find(',') + 1: len(line) + 1]

            self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
            self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
            self.tableWidget.itemDoubleClicked.connect(self.DoubleClicked)

        def Information(self, text):
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Информация")
            msg.setText(text)
            msg.exec_()

        def DoubleClicked(self):
            self.row.append(self.tableWidget.currentRow())
            self.column.append(self.tableWidget.currentColumn())
            self.text.append(self.tableWidget.item(self.tableWidget.currentRow(),
                                                   self.tableWidget.currentColumn()).text())

        def ClicedButton(self):  # тут заполняется таблица
            if (self.lineEdit.text() == "" or self.lineEdit.text().isspace()):
                self.Information("Введите фамилию студента")
            else:
                self.tableWidget.clear()
                self.tableWidget.setColumnCount(9)
                self.tableWidget.setHorizontalHeaderLabels(["Фамилия", "Имя", "Отчество",
                                                            "Институт", "Направление", "Группа",
                                                            "Курс", "Бюджет/Контр", "Форма обучения"])

                self.students = findStudent(self.lineEdit.text(), self.comboBox.currentText(), "Все", "Все")

                if (self.students != ''):
                    self.tableWidget.setRowCount(len(self.students))

                    # заполняем строки
                    for i in range(len(self.students)):
                        for j in range(len(self.students[i]) - 1):
                            self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(self.students[i][j]))

        def ClicedButton2(self):
            if (self.lineEdit.text() == "" or self.lineEdit.text().isspace()):
                self.Information("Введите фамилию студента")
            elif (len(self.row) != 0):
                for i in range(len(self.column)):
                    if (self.column[i] == 0):
                        cursor.execute("UPDATE Students SET LastName = '"
                                       + self.tableWidget.item(self.row[i], self.column[i]).text() +
                                       "' WHERE ID = " + self.students[self.row[i]][9])
                    elif (self.column[i] == 1):
                        cursor.execute("UPDATE Students SET FirstName = '"
                                       + self.tableWidget.item(self.row[i], self.column[i]).text() +
                                       "' WHERE ID = " + self.students[self.row[i]][9])
                    elif (self.column[i] == 2):
                        cursor.execute("UPDATE Students SET SecondName = '"
                                       + self.tableWidget.item(self.row[i], self.column[i]).text() +
                                       "' WHERE ID = " + self.students[self.row[i]][9])
                    elif (self.column[i] == 3):
                        self.Information("Институт не может быть изменен.")
                        self.tableWidget.item(self.row[i], self.column[i]).setText(self.text[i])
                        # cursor.execute(
                        #     "SELECT dbo.Check_Inst('" + self.tableWidget.item(self.row[i],
                        #                                                       self.column[i]).text() + "')")
                        # if (cursor.fetchone()[0] == 1):
                        #     self.Information(" Институт не найден.")
                        #     self.tableWidget.item(self.row[i], self.column[i]).setText(self.text[i])
                    elif (self.column[i] == 4):
                        self.Information("Направление не может быть изменено.")
                        self.tableWidget.item(self.row[i], self.column[i]).setText(self.text[i])
                        # cursor.execute(
                        #     "SELECT dbo.Check_Direct('" + self.tableWidget.item(self.row[i],
                        #                                                         self.column[i]).text() + "')")
                        # if (cursor.fetchone()[0] == 1):
                        #     self.Information(" Направление не найдено.")
                        #     self.tableWidget.item(self.row[i], self.column[i]).setText(self.text[i])
                    elif (self.column[i] == 5):
                        cursor.execute(
                            "SELECT dbo.Check_Group('" + self.tableWidget.item(self.row[i],
                                                                               self.column[i]).text() + "')")
                        flag = cursor.fetchone()[0]
                        if (flag == 1):
                            self.Information(" Группа не найдена.")
                            self.tableWidget.item(self.row[i], self.column[i]).setText(self.text[i])
                        elif (flag == 0):
                            cursor.execute("UPDATE Students SET GroupID = (SELECT ID From Groups WHERE Number = '"
                                           + self.tableWidget.item(self.row[i], self.column[i]).text() +
                                           "') WHERE ID = " + self.students[self.row[i]][9])
                    elif (self.column[i] == 6):
                        if (int(self.tableWidget.item(self.row[i], self.column[i]).text()) < 1 or
                                int(self.tableWidget.item(self.row[i], self.column[i]).text()) > 4):
                            self.Information("Неверный номер курса.")
                            self.tableWidget.item(self.row[i], self.column[i]).setText(self.text[i])
                        else:
                            cursor.execute("UPDATE Students SET CourseYear = '"
                                           + self.tableWidget.item(self.row[i], self.column[i]).text() +
                                           "' WHERE ID = " + self.students[self.row[i]][9])
                    elif (self.column[i] == 7):
                        if (self.tableWidget.item(self.row[i], self.column[i]).text() != 'Бюджет' and
                                self.tableWidget.item(self.row[i], self.column[i]).text() != 'Контракт'):
                            self.Information("Неверно указан источник финансирования.")
                            self.tableWidget.item(self.row[i], self.column[i]).setText(self.text[i])
                        else:
                            cursor.execute("UPDATE Students SET BudgContr = '"
                                           + self.tableWidget.item(self.row[i], self.column[i]).text() +
                                           "' WHERE ID = " + self.students[self.row[i]][9])
                    elif (self.column[i] == 8):
                        if (self.tableWidget.item(self.row[i], self.column[i]).text() != 'Очное' and
                                self.tableWidget.item(self.row[i], self.column[i]).text() != 'Очно-заочное' and
                                self.tableWidget.item(self.row[i], self.column[i]).text() != 'Заочное'):
                            self.Information("Неверно указана форма обучения.")
                            self.tableWidget.item(self.row[i], self.column[i]).setText(self.text[i])
                        else:
                            cursor.execute("UPDATE Students SET FOE = '"
                                           + self.tableWidget.item(self.row[i], self.column[i]).text() +
                                           "' WHERE ID = " + self.students[self.row[i]][9])
                self.row.clear()
                self.column.clear()
                self.text.clear()
                conn.commit()

        def ClicedButton3(self):
            self.close()
            window = Select()
            window.show()
            window.exec_()


    class Order(QtWidgets.QDialog, Ui_Order):
        def __init__(self):
            super().__init__()
            self.setupUi(self)

            self.pushButton.clicked.connect(self.ClicedButton)  # появляются студенты в таблице
            self.pushButton_2.clicked.connect(self.ClicedButton2)  # формирование заявления
            self.pushButton_3.clicked.connect(self.ClicedButton3)  # назад

            self.comboBox.currentIndexChanged.connect(self.Change)  # заполняются комбобоксы
            self.comboBox_2.currentIndexChanged.connect(self.Change_2)

            self.comboBox_2.setEnabled(False)
            self.comboBox_3.setEnabled(False)

            self.comboBox.addItem("Все")
            cursor.execute("SELECT dbo.Find_Direct()")
            line = str(cursor.fetchone())
            line = line[2:len(line)]
            while (line[0] != "'"):
                self.comboBox.addItem(line[:line.find(',')])
                line = line[line.find(',') + 1: len(line) + 1]

            self.tableWidget.setSelectionMode(
                QtWidgets.QAbstractItemView.SingleSelection)  # можно выбрать только одну строку
            self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self.students = ''

        def Information(self, text):
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Информация")
            msg.setText(text)
            msg.exec_()

        def ClicedButton(self):
            if (self.lineEdit.text() == "" or self.lineEdit.text().isspace()):
                self.Information("Введите фамилию студента")
            else:
                self.tableWidget.clear()
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(9)
                self.tableWidget.setHorizontalHeaderLabels(["Фамилия", "Имя", "Отчество",
                                                            "Институт", "Направление", "Группа",
                                                            "Курс", "Бюджет/Контр", "Форма обучения"])

                self.students = findStudent(self.lineEdit.text(), self.comboBox.currentText(),
                                            self.comboBox_2.currentText(),
                                            self.comboBox_3.currentText())

                if (self.students != ''):
                    self.tableWidget.setRowCount(len(self.students))

                    # заполняем строки
                    for i in range(len(self.students)):
                        for j in range(len(self.students[i])-1):
                            self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(self.students[i][j]))

        def ClicedButton2(self):
            if (self.tableWidget.currentRow() != -1):
                i = self.tableWidget.currentRow()
                printOrder(self.students[i][0] + " " + self.students[i][1] + " " + self.students[i][2],
                           self.students[i][3], self.students[i][4], self.students[i][6], self.students[i][5],
                           self.students[i][8], self.students[i][7])
                self.Information("Заявление успешно сформировано")
            else:
                self.Information("Студент не выбран")

        def ClicedButton3(self):
            self.close()
            window = Select()
            window.show()
            window.exec_()

        def Change(self):
            self.comboBox_2.setEnabled(True)
            self.comboBox_2.clear()
            self.comboBox_2.addItem("Все")
            cursor.execute("SELECT dbo.Find_Profile('" + self.comboBox.currentText() + "')")
            line = str(cursor.fetchone())
            line = line[2:len(line)]
            while (line[0] != "'"):
                self.comboBox_2.addItem(line[:line.find(',')])
                line = line[line.find(',') + 1: len(line) + 1]

        def Change_2(self):
            self.comboBox_3.setEnabled(True)
            self.comboBox_3.clear()
            self.comboBox_3.addItem("Все")
            cursor.execute("SELECT dbo.Find_Group('" + self.comboBox_2.currentText() + "')")
            line = str(cursor.fetchone())
            line = line[2:len(line)]
            while (line[0] != "'"):
                self.comboBox_3.addItem(line[:line.find(',')])
                line = line[line.find(',') + 1: len(line) + 1]


    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        application = mywindow()
        application.show()
        app.exec_()

except pdb.ProgrammingError:
    app = QtWidgets.QApplication(sys.argv)
    application = Inform_bd()
    application.show()
    app.exec_()

except IOError:
    app = QtWidgets.QApplication(sys.argv)
    application = Inform_file()
    application.show()
    app.exec_()
