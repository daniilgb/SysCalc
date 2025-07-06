from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(647, 515)
        MainWindow.setStyleSheet(u"background-color: rgb(40, 129, 123);\n"
"font: 18pt \"Helvetica\";\n"
"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"margin: 3px;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label)

        self.InputNumber = QLineEdit(self.centralwidget)
        self.InputNumber.setObjectName(u"InputNumber")
        self.InputNumber.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.InputNumber)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.SystemInput = QLineEdit(self.centralwidget)
        self.SystemInput.setObjectName(u"SystemInput")
        self.SystemInput.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.SystemInput)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_3)

        self.ToSystemInput = QLineEdit(self.centralwidget)
        self.ToSystemInput.setObjectName(u"ToSystemInput")
        self.ToSystemInput.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.ToSystemInput)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.get_input_text_and_show_reuslt)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.Result = QLabel(self.centralwidget)
        self.Result.setObjectName(u"Result")
        self.Result.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.Result)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SysCalc", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0427\u0438\u0441\u043b\u043e:</p><p>Number:</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0441\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f:</p><p>Number system:</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438 \u0432:</p><p>Convert to:</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 (get the result)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:</p><p>Result:</p></body></html>", None))
        self.Result.setText(QCoreApplication.translate("MainWindow", u"---------------------------------------------------", None))
    # retranslateUi

    def get_input_text_and_show_reuslt(self):
        self.input_num = self.InputNumber.text()
        self.input_num_system = self.SystemInput.text()
        self.input_to_system = self.ToSystemInput.text()
        self.Result.setText(swap_system(self.input_num, self.input_num_system, self.input_to_system))


def swap_system(num:str, num_system:str, to_system: str) -> str:
    sup_systems = [str(i) for i in range(2, 37)]
    alp_systems = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = [] #Остатки при делении
    int_num = 0

    if num_system in sup_systems and to_system in sup_systems:
        num_system = int(num_system)
        to_system = int(to_system)
    else:
        return "Error: Unsupported system\nSupported systems: 2-36"
    
    try:
        int_num = int(num, num_system)
    except:
        return "Error: Сheck the correctness of the data\nПроверьте корректность введённых данных"
    else:
        pass
    
    if int_num == 0:
        return "0"
    
    while int_num >= to_system:
        result.append(alp_systems[int_num % to_system])
        int_num //= to_system
    
    result.append(alp_systems[int_num])
    result.reverse()
    return "".join(result)


