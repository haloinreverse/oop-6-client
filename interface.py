from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# from matrix import Matrix
# from matrix import number


class TInterface(QMainWindow):

    def __init__(self):
        super().__init__()
        self.__setupUi(self)
        self.show()
        # self.__matrix = Matrix()
        self.hor_size = 2
        self.vert_size = 2
        # self.save_matrix()
        self.save_size_pb.clicked.connect(self.save_new_size)
        self.real_rb.clicked.connect(self.real_rb_clicked)
        self.type = 'real'
        self.rat_rb.clicked.connect(self.rat_rb_clicked)
        self.compl_rb.clicked.connect(self.compl_rb_clicked)

        # self.save_matrix_pb.clicked.connect(self.save_matrix)
        # self.transpose_pb.clicked.connect(self.transpose)
        # self.det_pb.clicked.connect(self.show_det)
        # self.rank_pb.clicked.connect(self.show_rank)

    def __setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(800, 600)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.vert_size_label = QLabel(self.centralwidget)
        self.vert_size_label.setObjectName(u"vert_size_label")

        self.gridLayout.addWidget(self.vert_size_label, 0, 0, 1, 1)

        self.result_le = QLineEdit(self.centralwidget)
        self.result_le.setObjectName(u"result_le")

        self.gridLayout.addWidget(self.result_le, 5, 1, 1, 1)

        self.real_rb = QRadioButton(self.centralwidget)
        self.real_rb.setObjectName(u"real_rb")
        self.real_rb.setChecked(True)

        self.gridLayout.addWidget(self.real_rb, 2, 0, 1, 2)

        self.save_size_pb = QPushButton(self.centralwidget)
        self.save_size_pb.setObjectName(u"save_size_pb")

        self.gridLayout.addWidget(self.save_size_pb, 0, 4, 1, 1)

        self.rank_pb = QPushButton(self.centralwidget)
        self.rank_pb.setObjectName(u"rank_pb")

        self.gridLayout.addWidget(self.rank_pb, 4, 4, 1, 1)

        self.compl_rb = QRadioButton(self.centralwidget)
        self.compl_rb.setObjectName(u"compl_rb")

        self.gridLayout.addWidget(self.compl_rb, 2, 4, 1, 1)

        self.vert_size_le = QLineEdit(self.centralwidget)
        self.vert_size_le.setObjectName(u"vert_size_le")

        self.gridLayout.addWidget(self.vert_size_le, 0, 1, 1, 1)

        self.transpose_pb = QPushButton(self.centralwidget)
        self.transpose_pb.setObjectName(u"transpose_pb")

        self.gridLayout.addWidget(self.transpose_pb, 4, 0, 1, 1)

        self.hor_size_label = QLabel(self.centralwidget)
        self.hor_size_label.setObjectName(u"hor_size_label")

        self.gridLayout.addWidget(self.hor_size_label, 0, 2, 1, 1)

        self.det_pb = QPushButton(self.centralwidget)
        self.det_pb.setObjectName(u"det_pb")

        self.gridLayout.addWidget(self.det_pb, 4, 1, 1, 1)

        self.result_label = QLabel(self.centralwidget)
        self.result_label.setObjectName(u"result_label")

        self.gridLayout.addWidget(self.result_label, 5, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 5)

        self.hor_size_le = QLineEdit(self.centralwidget)
        self.hor_size_le.setObjectName(u"hor_size_le")

        self.gridLayout.addWidget(self.hor_size_le, 0, 3, 1, 1)

        self.rat_rb = QRadioButton(self.centralwidget)
        self.rat_rb.setObjectName(u"rat_rb")

        self.gridLayout.addWidget(self.rat_rb, 2, 2, 1, 2)

        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)

    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Matrix", None))
        self.vert_size_label.setText(
            QCoreApplication.translate("main_window", u"\u0412\u0435\u0440\u0442. \u0440\u0430\u0437\u043c\u0435\u0440",
                                       None))
        self.real_rb.setText(QCoreApplication.translate("main_window",
                                                        u"\u0412\u0435\u0449\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435 \u0447\u0438\u0441\u043b\u0430",
                                                        None))
        self.save_size_pb.setText(
            QCoreApplication.translate("main_window", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.rank_pb.setText(QCoreApplication.translate("main_window", u"\u0420\u0430\u043d\u0433", None))
        self.compl_rb.setText(QCoreApplication.translate("main_window",
                                                         u"\u041a\u043e\u043c\u043f\u043b\u0435\u043a\u0441\u043d\u044b\u0435 \u0447\u0438\u0441\u043b\u0430",
                                                         None))
        self.transpose_pb.setText(QCoreApplication.translate("main_window",
                                                             u"\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c",
                                                             None))
        self.hor_size_label.setText(
            QCoreApplication.translate("main_window", u"\u0413\u043e\u0440. \u0440\u0430\u0437\u043c\u0435\u0440",
                                       None))
        self.det_pb.setText(QCoreApplication.translate("main_window",
                                                       u"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c",
                                                       None))
        self.result_label.setText(
            QCoreApplication.translate("main_window", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("main_window", u"1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("main_window", u"2", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("main_window", u"1", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("main_window", u"2", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("main_window", u"1", None));
        ___qtablewidgetitem5 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("main_window", u"0", None));
        ___qtablewidgetitem6 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("main_window", u"0", None));
        ___qtablewidgetitem7 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("main_window", u"1", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.rat_rb.setText(QCoreApplication.translate("main_window",
                                                       u"\u0420\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u0447\u0438\u0441\u043b\u0430",
                                                       None))

    # retranslateUi

    # retranslateUi
    # retranslateUi

    # def save_matrix(self):
    #     new_matrix = [[0 for j in range(self.__size)] for i in range(self.__size)]
    #     for i in range(self.__size):
    #         for j in range(self.__size):
    #             new_matrix[i][j] = number(self.tableWidget.item(i, j).text())
    #     self.__matrix.set_data(new_matrix)

    def save_new_size(self):
        # self.save_matrix()
        if self.hor_size_le.text() != "" and self.vert_size_le.text() != "":
            new_hor_size = int(self.hor_size_le.text())
            new_vert_size = int(self.vert_size_le.text())
            old_hor_size = self.hor_size
            old_vert_size = self.vert_size
            self.hor_size = new_hor_size
            self.vert_size = new_vert_size
            self.tableWidget.setColumnCount(self.hor_size)
            self.tableWidget.setRowCount(self.vert_size)

            # new_matrix = [[0 for j in range(new_size)] for i in range(new_size)]
            for i in range(new_vert_size):
                for j in range(new_hor_size):
                    if (i >= old_vert_size) or (j >= old_hor_size):
                        self.tableWidget.setItem(i, j, QTableWidgetItem())
                        self.tableWidget.item(i, j).setText('0/1')

            # for i in range(new_size):
            #     for j in range(new_size):
            #         new_matrix[i][j] = number(self.tableWidget.item(i, j).text())
            # self.__matrix.set_data(new_matrix)

    def transpose(self, matrix):
        # self.save_matrix()
        self.hor_size_le.setText(str(self.vert_size))
        self.vert_size_le.setText(str(self.hor_size))
        self.save_new_size()
        for i in range(self.vert_size):
            for j in range(self.hor_size):
                self.tableWidget.item(i, j).setText(str(matrix[i][j]))

    def show_det(self, det):
        # self.save_matrix()
        self.result_le.setText(str(det))

    def show_rank(self, rank):
        self.result_le.setText(str(rank))

    def real_rb_clicked(self):
        self.real_rb.setChecked(True)
        self.rat_rb.setChecked(False)
        self.compl_rb.setChecked(False)
        self.type = 'real'

    def rat_rb_clicked(self):
        self.rat_rb.setChecked(True)
        self.real_rb.setChecked(False)
        self.compl_rb.setChecked(False)
        self.type = 'rat'

    def compl_rb_clicked(self):
        self.rat_rb.setChecked(False)
        self.real_rb.setChecked(False)
        self.compl_rb.setChecked(True)
        self.type = 'compl'
