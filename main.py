import sys
import os
from datetime import date
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QGridLayout, QTextEdit


stylesheet = """
    /* Main Window */
    QMainWindow {
        background-color: #f5f0eb;
    }
    
    QWidget#central_widget {
        background-color: #f5f0eb;
    }
    
    /* Calendar Section - Compact */
    QPushButton {
        background-color: #ffffff;
        color: #2c3e50;
        border: none;
        border-radius: 25px;
        font-size: 13px;
        font-weight: 500;
        padding: 8px;
        margin: 2px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    QPushButton:hover {
        background-color: #e8e0d5;
    }
    
    /* Selected Day */
    QPushButton#selectedDay {
        background-color: #e67e22;
        color: white;
        font-weight: 600;
    }
    
    /* Empty/Placeholder Buttons */
    QPushButton[text="x"] {
        background-color: transparent;
        color: transparent;
        border: none;
    }
    
    /* Weekday Headers - Compact */
    QPushButton[text="Sun"], 
    QPushButton[text="Mon"],
    QPushButton[text="Tue"],
    QPushButton[text="Wed"],
    QPushButton[text="Thu"],
    QPushButton[text="Fri"],
    QPushButton[text="Sat"] {
        background-color: transparent;
        color: #7f8c8d;
        font-size: 11px;
        font-weight: 600;
        padding: 5px;
        margin: 0px;
        border-bottom: 1px solid #ecf0f1;
        border-radius: 0px;
    }
    
    /* Navigation Buttons - Compact */
    QPushButton[text="<"], 
    QPushButton[text=">"] {
        background-color: transparent;
        color: #7f8c8d;
        font-size: 16px;
        font-weight: bold;
        padding: 4px 12px;
    }
    
    QPushButton[text="<"]:hover, 
    QPushButton[text=">"]:hover {
        color: #e67e22;
        background-color: rgba(230, 126, 34, 0.1);
    }
    
    /* Year & Month Display */
    QPushButton[text="2026"], 
    QPushButton[text="7"] {
        background-color: transparent;
        color: #2c3e50;
        font-size: 14px;
        font-weight: 600;
        padding: 4px 16px;
        border-bottom: 2px solid #e67e22;
        border-radius: 0px;
    }
    
    /* Text Editor - LARGE and prominent */
    QTextEdit {
        background-color: #ffffff;
        border: none;
        border-radius: 20px;
        padding: 30px;
        font-size: 18px;
        line-height: 1.8;
        color: #2c3e50;
        font-family: -apple-system, BlinkMacSystemFont, 'Georgia', 'Times New Roman', serif;
        margin: 15px 20px 20px 10px;
        selection-background-color: #e67e22;
        selection-color: white;
        min-height: 400px;
    }
    
    QTextEdit:focus {
        background-color: #fefefe;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    }
    
    /* Save Button - Prominent */
    QPushButton[text="save"] {
        background-color: #e67e22;
        color: white;
        font-size: 16px;
        font-weight: 600;
        padding: 12px 24px;
        border-radius: 40px;
        margin: 10px 20px 20px 10px;
        min-width: 120px;
    }
    
    QPushButton[text="save"]:hover {
        background-color: #f39c12;
        transform: translateY(-1px);
    }
    
    /* Sunday highlight */
    QPushButton[text="Sun"] {
        color: #e74c3c;
    }
"""

app = QApplication(sys.argv)
app.setStyleSheet(stylesheet)
window = QMainWindow()
window.resize(800, 600)
window.setWindowTitle("My Diary APP")

central_widget = QWidget()
window.setCentralWidget(central_widget)

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def save_file():
    file_name = f"{year}/{month}/{day}.txt"
    with open(file_name, "w") as file:
        text = text_display.toPlainText()
        file.write(text)
        print("saved")

def switch_year_left():
    global year
    year = str(int(year) - 1)
    button2.setText(year)

def switch_year_right():
    global year
    year = str(int(year) + 1)
    button2.setText(year)

def switch_month_left():
    global month
    if int(month) > 1:
        month = str(int(month) - 1)
        button5.setText(month)

    destroy_buttons()
    generate_buttons()
    disbplay_buttons()
def switch_month_right():
    global month
    if int(month) < 12:
        month = str(int(month) + 1)
        button5.setText(month)

    destroy_buttons()
    generate_buttons()
    disbplay_buttons()

def generate_buttons():
    global days_buttons
    index = int(month) - 1
    first_day = date(int(year), int(month), 1).weekday()
    for i in range(first_day):
        new_button = QPushButton("x")
        days_buttons.append(new_button)

    for i in range(month_days[index]):
        new_button = QPushButton(str(int(i) + 1))
        new_button.clicked.connect(lambda checked, num=i: switch_days(num))
        days_buttons.append(new_button)
    
def destroy_buttons():
    global days_buttons
    for button in days_buttons:
        button.deleteLater()
    days_buttons.clear()

def disbplay_buttons():
    global days_buttons
    index = int(month) - 1
    first_day = date(int(year), int(month), 1).weekday()
    for i in range(month_days[index] + first_day):
        column = i % 7
        row = i // 7
        column1.addWidget(days_buttons[i], (row + 2), column)


def switch_days(num):
    global day
    day = str(num)


    if not os.path.exists(str(year)):
        os.makedirs(str(year))
    
    if not os.path.exists(f"{year}/{month}"):
        os.makedirs(f"{year}/{month}")

    file_path = f"{year}/{month}/{day}.txt"
    if not os.path.exists(file_path):
        f = open(file_path, "w")
        f.close()

    global text
    with open(file_path, "r") as file:
        text = file.read()
    global text_display
    text_display.setText(text)

text = ""

    
year = "2026"
month = "7"
day = "10"


text_display = QTextEdit()
text_display.setText(text)

save_button = QPushButton("save")
save_button.clicked.connect(save_file)

button1 = QPushButton("<")
button2 = QPushButton(year)
button3 = QPushButton(">")

button4 = QPushButton("<")
button5 = QPushButton(month)
button6 = QPushButton(">")

week_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
week_buttons = []

for i in week_days:
    new_button = QPushButton(i)
    week_buttons.append(new_button)


days_buttons = []
generate_buttons()



#events
button1.clicked.connect(switch_year_left)
button3.clicked.connect(switch_year_right)
button4.clicked.connect(switch_month_left)
button6.clicked.connect(switch_month_right)

#layouts
main_layout = QGridLayout()
column1 = QGridLayout()
column2 = QVBoxLayout()

#adding Widgets
column1.addWidget(button1, 0, 0)
column1.addWidget(button2, 0, 1)
column1.addWidget(button3, 0, 2)
column1.addWidget(button4, 0, 3)
column1.addWidget(button5, 0, 4)
column1.addWidget(button6, 0, 5)
 
for i in range(len(week_buttons)):
    column1.addWidget(week_buttons[i], 1, i)
disbplay_buttons()


column2.addWidget(text_display)
column2.addWidget(save_button)


#Setting layouts
main_layout.addLayout(column1, 0, 0)
main_layout.addLayout(column2, 0, 1)

central_widget.setLayout(main_layout)


#start up
switch_days(day)


window.show()
app.exec()
