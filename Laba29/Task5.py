import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")

        # Центральный виджет для базовой компоновки
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Вертикальный макет
        self.layout = QVBoxLayout(self.central_widget)

        # Метки и элементы управления
        self.label_exp = QLabel("Введите выражение:", self)
        self.layout.addWidget(self.label_exp)

        self.input_expression = QLineEdit(self)
        self.layout.addWidget(self.input_expression)

        self.calculate_button = QPushButton("Вычислить", self)
        self.calculate_button.clicked.connect(self.calculate_expression)
        self.layout.addWidget(self.calculate_button)

        self.label_result = QLabel("Результат:", self)
        self.layout.addWidget(self.label_result)

        self.output_result = QLineEdit(self)
        self.output_result.setReadOnly(True)  # Поле только для чтения
        self.layout.addWidget(self.output_result)

    def calculate_expression(self):
        expression = self.input_expression.text()
        try:
            result = eval(expression)  # Вычисляем выражение
            self.output_result.setText(str(result))
        except Exception as e:
            self.output_result.setText("Ошибка")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())