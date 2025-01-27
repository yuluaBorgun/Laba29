import sys
from PySide6.QtCore import QSize, Qt
from random import choice
#from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)
'''# Требуется только для доступа к аргументам командной строки.
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window = QWidget()
window = QPushButton("Push Me")
window.show()# По умолчанию окно будет скрыто
# Запускаем цикл событий
app.exec()'''


'''
window_titles =[
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong",
]

# Подкласс QMainWindow для настройки главного окна вашего приложения.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked = 0
        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)
        #self.button_is_checked = True
      #  self.button.toggled.connect(self.the_button_was_toggled)
       # self.button.released.connect(self.the_button_was_released)

       # self.button.setChecked(self.button_is_checked)
       # self.setCentralWidget(self.button)


    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)
        if window_title == "Something went wrong":
            self.button.setDisabled(True)'''

'''class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)'''

'''class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
             self.label.setText("mouseDoubleClickEvent LEFT")
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")'''
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))

    def mousePressEvent(self, event):
        print("Mouse pressed!")
        super().mousePressEvent(event)

class CustomButton(QPushButton):
    def event(self, e):
        e.accept()'''

'''class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()

        widgets =[
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]
        for widget in widgets:
            layout.addWidget(widget())

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()'''


class ConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Единицы измерения")

        # Центральный виджет для базовой компоновки
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Вертикальный макет
        self.layout = QVBoxLayout(self.central_widget)

        # Метки и элементы управления
        self.label_kg = QLabel("кг", self)
        self.layout.addWidget(self.label_kg)

        self.input_value = QLineEdit(self)
        self.layout.addWidget(self.input_value)

        self.convert_button = QPushButton("Перевести", self)
        self.convert_button.clicked.connect(self.convert_units)
        self.layout.addWidget(self.convert_button)

        self.label_dg = QLabel("дг.: ", self)
        self.layout.addWidget(self.label_dg)

        self.label_g = QLabel("г.: ", self)
        self.layout.addWidget(self.label_g)

        self.label_mg = QLabel("мг.: ", self)
        self.layout.addWidget(self.label_mg)

    def convert_units(self):
        try:
            kg = float(self.input_value.text())
            dg = kg * 100
            g = kg * 1000
            mg = kg * 1000000

            self.label_dg.setText(f"дг.: {dg}")
            self.label_g.setText(f"г.: {g}")
            self.label_mg.setText(f"мг.: {mg}")
        except ValueError:
            self.label_dg.setText("дг: Ошибка ввода")
            self.label_g.setText("г.: Ошибка ввода")
            self.label_mg.setText("мг.: Ошибка ввода")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())

