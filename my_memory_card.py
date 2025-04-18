from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QMessageBox)
from random import randint, shuffle
class Question():
        def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
                self.question = question
                self.right_answer = right_answer
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3
question_list = list()
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Испанский', 'Итальянский', 'Русский' ))
question_list.append(Question("Сколько букв слове азбука?!?!?", '6', '2', '3', '1'))
question_list.append(Question('А теперь сколько букв слове сколько?', '7', '2', '3', '1'))
question_list.append(Question('Корень из 8*9*8?!?!?', '24', 'десять', '9*9*8', 'five'))
question_list.append(Question('Best item for Hoodwink?', 'armlet of mordiggian', 'glepnir', 'iron of branch', 'force of staff'))
app = QApplication([])
lb_Queshion = QLabel("Самый сложный вопрос в мире!")
btn_Ok = QPushButton("Ответить")

RadioGroupBox = QGroupBox("Варианты ответов:")
rbtn_1 = QRadioButton("Вариант 1")
rbtn_2 = QRadioButton("Вариант 2")
rbtn_3 = QRadioButton("Вариант 3")
rbtn_4 = QRadioButton("Вариант 4")
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout() 
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox("Результаты теста")
lb_Result = QLabel("Прав ты или нет?")
lb_Correct = QLabel("Ответ будет тут!")
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft|Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 =QHBoxLayout()
layout_line2 =QHBoxLayout()
layout_line3 =QHBoxLayout()
layout_line1.addWidget(lb_Correct, alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.show()
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_Ok, stretch=2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
def show_result():
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_Ok.setText('Следующий вопрос')
def show_question():
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_Ok.setText("Ответить")
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True)
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
        shuffle(answers)
        answers[0].setText(q.right_answer)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        lb_Queshion.setText(q.question)
        lb_Correct.setText(q.right_answer)
        show_question()
def show_correct(res):
        lb_Result.setText(res)
        show_result()
def check_answer():
        if answers[0].isChecked():
                show_correct("Умничка")
                window.score += 1
        else:
                if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                        show_correct("Не умничка")
lenght_questions = len(question_list)
def next_question():
        global lenght_questions
        if window.total >= lenght_questions:
                window.total += 1
        cur_quetion = randint(0, len(question_list) -1)
        q = question_list[window.cur_quetion]
        ask(q)
def click_OK():
        if btn_Ok.text() == 'Ответить':
                check_answer()
        else:
                next_question()

btn_Ok.clicked.connect(click_OK)
window = QWidget()
window.cur_quetion = -1
window.setLayout(layout_card)
window.setWindowTitle("Memory card")
window.resize(500, 300)
window.score = 0
window.total = 0
window.show()
app.exec()


