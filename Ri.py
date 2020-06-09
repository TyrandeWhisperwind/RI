from PyQt4 import QtCore, QtGui
import fnmatch,os,glob, re
from math import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(917, 435)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.tableWidget_7 = QtGui.QTableWidget(self.tab_5)
        self.tableWidget_7.setMaximumSize(QtCore.QSize(16777215, 300))
        self.tableWidget_7.setObjectName(_fromUtf8("tableWidget_7"))
        self.tableWidget_7.setColumnCount(1)
        self.tableWidget_7.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        self.verticalLayout_13.addWidget(self.tableWidget_7)
        self.checkBox_2 = QtGui.QCheckBox(self.tab_5)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout_13.addWidget(self.checkBox_2)
        self.checkBox = QtGui.QCheckBox(self.tab_5)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_13.addWidget(self.checkBox)
        self.pushButton_6 = QtGui.QPushButton(self.tab_5)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout_13.addWidget(self.pushButton_6)
        self.comboBox_3 = QtGui.QComboBox(self.tab_5)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.verticalLayout_13.addWidget(self.comboBox_3)
        self.pushButton_7 = QtGui.QPushButton(self.tab_5)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.verticalLayout_13.addWidget(self.pushButton_7)
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.textEdit_2 = QtGui.QTextEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 24))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.horizontalLayout_6.addWidget(self.textEdit_2)
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout.addWidget(self.label_13)
        self.tableWidget = QtGui.QTableWidget(self.tab)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.textEdit = QtGui.QTextEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout_5.addWidget(self.textEdit)
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout.addWidget(self.label_12)
        self.tableWidget_2 = QtGui.QTableWidget(self.tab)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.textEdit_3 = QtGui.QTextEdit(self.tab_2)
        self.textEdit_3.setMaximumSize(QtCore.QSize(16777215, 24))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.horizontalLayout_2.addWidget(self.textEdit_3)
        self.pushButton_3 = QtGui.QPushButton(self.tab_2)
        self.pushButton_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_3.addWidget(self.label_11)
        self.tableWidget_3 = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        self.verticalLayout_3.addWidget(self.tableWidget_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_9.addWidget(self.label_4)
        self.comboBox = QtGui.QComboBox(self.tab_3)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout_9.addWidget(self.comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_5 = QtGui.QLabel(self.tab_3)
        self.label_5.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_11.addWidget(self.label_5)
        self.textEdit_4 = QtGui.QTextEdit(self.tab_3)
        self.textEdit_4.setMaximumSize(QtCore.QSize(16777215, 24))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.horizontalLayout_11.addWidget(self.textEdit_4)
        self.pushButton_4 = QtGui.QPushButton(self.tab_3)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_11.addWidget(self.pushButton_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.label_10 = QtGui.QLabel(self.tab_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_5.addWidget(self.label_10)
        self.tableWidget_4 = QtGui.QTableWidget(self.tab_3)
        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        self.verticalLayout_5.addWidget(self.tableWidget_4)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_6 = QtGui.QLabel(self.tab_4)
        self.label_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_12.addWidget(self.label_6)
        self.comboBox_2 = QtGui.QComboBox(self.tab_4)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.horizontalLayout_12.addWidget(self.comboBox_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_7 = QtGui.QLabel(self.tab_4)
        self.label_7.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_13.addWidget(self.label_7)
        self.textEdit_5 = QtGui.QTextEdit(self.tab_4)
        self.textEdit_5.setMaximumSize(QtCore.QSize(16777215, 24))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.horizontalLayout_13.addWidget(self.textEdit_5)
        self.pushButton_5 = QtGui.QPushButton(self.tab_4)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_13.addWidget(self.pushButton_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.verticalLayout_12.addLayout(self.verticalLayout_6)
        self.label_9 = QtGui.QLabel(self.tab_4)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_12.addWidget(self.label_9)
        self.tableWidget_5 = QtGui.QTableWidget(self.tab_4)
        self.tableWidget_5.setObjectName(_fromUtf8("tableWidget_5"))
        self.tableWidget_5.setColumnCount(3)
        self.tableWidget_5.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        self.verticalLayout_12.addWidget(self.tableWidget_5)
        self.label_8 = QtGui.QLabel(self.tab_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_12.addWidget(self.label_8)
        self.pushButton_8 = QtGui.QPushButton(self.tab_4)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.verticalLayout_12.addWidget(self.pushButton_8)
        self.tableWidget_6 = QtGui.QTableWidget(self.tab_4)
        self.tableWidget_6.setObjectName(_fromUtf8("tableWidget_6"))
        self.tableWidget_6.setColumnCount(2)
        self.tableWidget_6.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        self.verticalLayout_12.addWidget(self.tableWidget_6)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Documents", None))
        self.checkBox_2.setText(_translate("Form", "Fichier inverse", None))
        self.checkBox.setText(_translate("Form", "Fichier inverse poids", None))
        self.pushButton_6.setText(_translate("Form", "Mettre à jour", None))
        self.pushButton_7.setText(_translate("Form", "Ouvrir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Géstion fichier inverse", None))
        self.label.setText(_translate("Form", "Terme:", None))
        self.pushButton.setText(_translate("Form", "Recherche", None))
        self.label_13.setText(_translate("Form", "Résultat:", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Documents", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Fréquences", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Poids", None))
        self.label_2.setText(_translate("Form", "Document:", None))
        self.pushButton_2.setText(_translate("Form", "Recherche", None))
        self.label_12.setText(_translate("Form", "Résultat:", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Terms", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Fréquences", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Poids", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Documents et terms", None))
        self.label_3.setText(_translate("Form", "Requete booleenne:", None))
        self.pushButton_3.setText(_translate("Form", "Recherche", None))
        self.label_11.setText(_translate("Form", "Résultat:", None))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Documents", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Recherche Booleenne", None))
        self.label_4.setText(_translate("Form", "Choix de la formule:", None))
        self.label_5.setText(_translate("Form", "Requete:", None))
        self.pushButton_4.setText(_translate("Form", "Recherche", None))
        self.label_10.setText(_translate("Form", "Résultat:", None))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Documents", None))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Similarité", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Recherche vectorielle", None))
        self.label_6.setText(_translate("Form", "Choix de la formule:", None))
        self.label_7.setText(_translate("Form", "Requete:", None))
        self.pushButton_5.setText(_translate("Form", "Recherche", None))
        self.label_9.setText(_translate("Form", "Résultat Vectoriel:", None))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Documents", None))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Similarité", None))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Echantillon", None))
        self.label_8.setText(_translate("Form", "Résultat probabiliste:", None))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Documents", None))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Similarité", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Recherche probabiliste", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "Evaluation", None))
        self.pushButton_8.setText(_translate("Form", "Recherche", None))

        ####################################################################################################
        self.pushButton_7.clicked.connect(self.open)
        self.pushButton_6.clicked.connect(self.fichInver)
        self.pushButton.clicked.connect(self.term)
        self.pushButton_2.clicked.connect(self.doc)
        self.pushButton_3.clicked.connect(self.booleen)
        self.pushButton_4.clicked.connect(self.vectoriel)
        self.pushButton_5.clicked.connect(self.probabiliste)
        self.tableWidget.itemClicked.connect(self.cell_was_clicked)
        self.tableWidget_3.itemClicked.connect(self.cell_was_clicked_3)
        self.tableWidget_4.itemClicked.connect(self.cell_was_clicked_4)
        self.pushButton_8.clicked.connect(self.searchProba)
        self.tableWidget_7.itemClicked.connect(self.cell_was_clicked_5)
        self.tableWidget_6.itemClicked.connect(self.cell_was_clicked_6)


        self.comboBox.addItem("")
        self.comboBox.addItem("produit d'inverse")
        self.comboBox.addItem("coefficient de dice")
        self.comboBox.addItem("cosinus")
        self.comboBox.addItem("jaccord")

        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("produit d'inverse")
        self.comboBox_2.addItem("coefficient de dice")
        self.comboBox_2.addItem("cosinus")
        self.comboBox_2.addItem("jaccord")


        path = 'C:/Users/HP/Desktop/RI/TP/TP2/inverse' 
        files = os.listdir(path)
        files_txt = [i for i in files if i.endswith('.txt') and i !='stopwords_fr.txt' ]
        self.comboBox_3.addItem("")
        for p in files_txt:
            self.comboBox_3.addItem(p)
        
        path2 = 'C:/Users/HP/Desktop/RI/TP/TP2/' 
        files = os.listdir(path2)
        files_txt = [i for i in files if i.endswith('.txt')  ]
      
        rowPosition = self.tableWidget_7.rowCount()
        self.tableWidget_7.insertRow(rowPosition)
        for p in files_txt:
            self.tableWidget_7.setItem(rowPosition , 0, QtGui.QTableWidgetItem(p))
            self.tableWidget_7.insertRow(rowPosition)  
        self.tableWidget_7.removeRow(0)

    def open(self):
        osCommandString = "notepad.exe inverse/"+self.comboBox_3.currentText()
        os.system(osCommandString)
#########################################frequence if doc and mot given ################################################################
    def frequence(mot,doc):
        f = open('inverse/inverse.txt', 'r')      
        for line in f:
            k, v = line.strip().split(':')
            www=re.search('([0-9]+)', k)
            if www:
                if (www.group(1)==doc):#if it is the same number as the document im looking for
                    ww=re.search('([a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ]+)', k)
                    if ww:
                        if (ww.group(1)==mot):
                            frequency=v
                            break

        f.close()
        return frequency

###################################function Checkbox##################################################################
    def fichInver(self):
        for ii in reversed(range(self.tableWidget_7.rowCount())):
            self.tableWidget_7.removeRow(ii)

        if self.checkBox_2.isChecked:
            self.indexFreq()
        if self.checkBox.isChecked:
            self.inversPoid()
        path2 = 'C:/Users/HP/Desktop/RI/TP/TP2/' 
        files = os.listdir(path2)
        files_txt = [i for i in files if i.endswith('.txt')  ]
      
        rowPosition = self.tableWidget_7.rowCount()
        self.tableWidget_7.insertRow(rowPosition)
        for p in files_txt:
            self.tableWidget_7.setItem(rowPosition , 0, QtGui.QTableWidgetItem(p))
            self.tableWidget_7.insertRow(rowPosition)  
        self.tableWidget_7.removeRow(0)
###################################function création fiche inversé###################################################################
    def indexFreq(self):
            n = len(fnmatch.filter(os.listdir('C:/Users/HP/Desktop/RI/TP/TP2'),'*.txt'))
            k = 1
            
            listCar = {'.', ',', '!', '?', '\''}
            stoplist = open('inverse/stopwords_fr.txt', 'r')
            stoplist = stoplist.read()
            stoplist = stoplist.lower()
            stoplist = stoplist.split()
            while k <= n:
                f = open('D' + str(k) +'.txt', 'r')
                t = f.read()
                t = t.lower()
                i = 0
                while i < len(t):
                    if t[i] in listCar:
                        t = t.replace(t[i], " ")
                    i += 1
                a = t.split()
                nb = len(a)
                for w in a:
                     if not w in stoplist and len(w) > 1:
                        if not (w, k) in freq:
                            freq[w, k] = a.count(w)
                            
                k += 1
            f.close()
            print(n)
            f = open('inverse/inverse.txt', 'w')
            for k in freq:
                f.write("%s:%s\n" % (k, freq[k]))
            f.close()
###################################function de calcul poids###################################################################
    def inversPoid(self):
        # calcul de ni pour chaque mot dans freq
        ni = {}
        n = len(fnmatch.filter(os.listdir('C:/Users/HP/Desktop/RI/TP/TP2'),'*.txt'))
        for (w, d) in freq:
            if not w in ni:
                ni[w] = 1
            else:
                ni[w] += 1
# calcul de la fréquence max de chaque document
        max = {}
        for(w, d) in freq:
            if not d in max:
                max[d] = freq[w, d]
            else:
                if freq[w, d] > max[d]:
                    max[d] = freq[w, d]
# calcul du fichier inverse avec poids TF*IDF
        poids = {}
        for (w, d) in freq:
                poids[w, d] = (float(freq[w, d])/max[d]) * log10((float(n))/ni[w]+1)
        print("Le fichier des poids est: ")        
        f = open('inverse/inversePoids.txt', 'w')
        for k in poids:
            f.write("%s:%s\n" % (k, poids[k]))
        f.close()
################################### term affichage###################################################################
    def term(self):
        for i in reversed(range(self.tableWidget.rowCount())):
            self.tableWidget.removeRow(i)

        mot=self.textEdit_2.toPlainText()
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        
        f = open('inverse/inversePoids.txt', 'r')

        for line in f:
            k, v = line.strip().split(':')
            www=re.search('([a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ]+)', k)
            if www:
                if (www.group(1)==mot):
                    doc=re.search('([0-9]+)', k)#grab doc
                    if doc:
                        g = open('inverse/inverse.txt', 'r')      
                        for li in g:
                            kk, vv = li.strip().split(':')
                            w=re.search('([0-9]+)', kk)
                            if w:
                                if (w.group(1)==doc.group(1)):#if it is the same number as the document im looking for
                                    w=re.search('([a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ]+)', kk)
                                    if w:
                                        if (w.group(1)==mot):
                                            frequency=vv
                                            break
                        g.close()
                        self.tableWidget.setItem(rowPosition , 0, QtGui.QTableWidgetItem(doc.group(1)))
                        self.tableWidget.setItem(rowPosition , 1, QtGui.QTableWidgetItem(frequency))
                        self.tableWidget.setItem(rowPosition , 2, QtGui.QTableWidgetItem(v))    
                        self.tableWidget.insertRow(rowPosition)   
        f.close()
        self.tableWidget.removeRow(0)
############################################# Document affichage #####################################################################################
    def doc(self):
        for i in reversed(range(self.tableWidget_2.rowCount())):
            self.tableWidget_2.removeRow(i)

        mot=self.textEdit.toPlainText()
        rowPosition = self.tableWidget_2.rowCount()
        self.tableWidget_2.insertRow(rowPosition)
        
        f = open('inverse/inversePoids.txt', 'r')
        
        for line in f:
            k, v = line.strip().split(':')
            www=re.search('([0-9]+)', k)
            if www:
                if (www.group(1)==mot):
                    doc=re.search('([a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ]+)', k)#grab word
                    if doc:
                        g = open('inverse/inverse.txt', 'r')      
                        for li in g:
                            kk, vv = li.strip().split(':')
                            w=re.search('([0-9]+)', kk)
                            if w:
                                if (w.group(1)==mot):#if it is the same number as the document im looking for
                                    w=re.search('([a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ]+)', kk)
                                    if w:
                                        if (w.group(1)==doc.group(1)):
                                            frequency=vv
                                            break
                        g.close()
                        self.tableWidget_2.setItem(rowPosition , 0, QtGui.QTableWidgetItem(doc.group(1)))
                        self.tableWidget_2.setItem(rowPosition , 1, QtGui.QTableWidgetItem(frequency))
                        self.tableWidget_2.setItem(rowPosition , 2, QtGui.QTableWidgetItem(v))    
                        self.tableWidget_2.insertRow(rowPosition)   
        f.close()
        self.tableWidget_2.removeRow(0)
############################################# Modele booleen #####################################################################################
    def booleen(self):
        query=self.textEdit_3.toPlainText()
        docs=[]
        copie=query.split()
        wordsAndDocs={}
        n= len(fnmatch.filter(os.listdir('C:/Users/HP/Desktop/RI/TP/TP2'),'*.txt'))
        cpt=1
        words=[]
        
        f = open('inverse/inverse.txt', 'r')      
        for line in f:
            k, v = line.strip().split(':')
            wordsAndDocs[k.strip()]= v.strip()
        f.close()
        # pour chaque files appliqué eval if yes add name doc in the list 
        while cpt <= n:

            words=[]
            splitquery =query.split()

            for key, value in wordsAndDocs.items() :# recupéré tt les mot du ieme doc
                mot=re.search('([a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ]+)', key)
                www=re.search('([0-9]+)', key)
                if mot and www:
                    if www.group(1) == str(cpt):
                        words.append(mot.group(1))                      

            for w in splitquery:
                if (w!='not' and w!='and' and w!='or' and w!='(' and w!=')'):
                    i=0
                    thereis=False
                    while (i<len(words)  and thereis==False ):
                        if (words[i]==w):
                            splitquery[splitquery.index(w)] = '1'
                            theseis=True
                        i+=1
            
            for ww in splitquery:
                if (ww!='not' and ww!='and' and ww!='or' and ww!='1' and ww!='(' and ww!=')'):
                    splitquery[splitquery.index(ww)] = '0'


            if(eval(" ".join(splitquery))):
                docs.append(cpt)

            cpt+=1
        for ii in reversed(range(self.tableWidget_3.rowCount())):
            self.tableWidget_3.removeRow(ii)

        rowPosition = self.tableWidget_3.rowCount()
        self.tableWidget_3.insertRow(rowPosition)

        for i in range(len(docs)):
            self.tableWidget_3.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(docs[i])))
            self.tableWidget_3.insertRow(rowPosition)  

        self.tableWidget_3.removeRow(0)
################################### clicked item of tables ####################################################################################
    def cell_was_clicked(self):
        row = self.tableWidget.currentRow()
        column = self.tableWidget.currentColumn()
        osCommandString = "notepad.exe D"+self.tableWidget.item(row,column).text()+".txt"
        os.system(osCommandString)
    def cell_was_clicked_3(self):
        row = self.tableWidget_3.currentRow()
        column = self.tableWidget_3.currentColumn()
        osCommandString = "notepad.exe D"+self.tableWidget_3.item(row,column).text()+".txt"
        os.system(osCommandString)
    def cell_was_clicked_4(self):
        row = self.tableWidget_4.currentRow()
        column = self.tableWidget_4.currentColumn()
        osCommandString = "notepad.exe D"+self.tableWidget_4.item(row,column).text()+".txt"
        os.system(osCommandString)
    def cell_was_clicked_5(self):
        row = self.tableWidget_7.currentRow()
        column = self.tableWidget_7.currentColumn()
        osCommandString = "notepad.exe "+self.tableWidget_7.item(row,column).text()
        os.system(osCommandString)
    def cell_was_clicked_6(self):
        row = self.tableWidget_6.currentRow()
        column = self.tableWidget_6.currentColumn()
        osCommandString = "notepad.exe D"+self.tableWidget_6.item(row,column).text()+".txt"
        os.system(osCommandString)
    
                
#################################### vectoriel #######################################################################################
    def vectoriel(self):
        def ttMotsDocs():
            words=[]
            wordsAndDocs={}
            f = open('inverse/inverse.txt', 'r')      
            for line in f:
                k, v = line.strip().split(':')
                wordsAndDocs[k.strip()]= v.strip()
            f.close()

            for key,value in wordsAndDocs.items() :# recupéré tt les mot 
                mot=re.search('([a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ]+)', key)
                if mot:
                    words.append(mot.group(1)) 
            words=list(set(words))
            return words
            #########################################################
        def poidsMotsDocument(numDoc):
            wordsPoids={}
            f = open('inverse/inversePoids.txt', 'r')   

            for line in f:
                k, v = line.strip().split(':')
                www=re.search('([0-9]+)', k)
                if www:
                    if (www.group(1)==numDoc):#if it is the same number as the document im looking for
                        mot=re.search('([a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ]+)', k)#grab the word
                        if mot:
                            kk,vv = mot.group(1), v
                            wordsPoids.update({kk:vv})        
            f.close()
            return wordsPoids
            #########################################################
        def poidsCarre(numDoc):
            poids=0
            listCarrePoids=[]
            f = open('inverse/inversePoids.txt', 'r')      
            for line in f:
                k, v = line.strip().split(':')
                www=re.search('([0-9]+)', k)
                if www:
                    if (www.group(1)==numDoc):#if it is the same number as the document im looking for
                        listCarrePoids.append(float(v)**2)      
            f.close()
            poids=sum(listCarrePoids)
            return poids
            #########################################################
        choice=self.comboBox.currentText()
        query=self.textEdit_4.toPlainText()
        for ii in reversed(range(self.tableWidget_4.rowCount())):
            self.tableWidget_4.removeRow(ii)

        k=1
        splitQuery=query.split()
        n= len(fnmatch.filter(os.listdir('C:/Users/HP/Desktop/RI/TP/TP2'),'*.txt'))
        allmot=[]
        allmot=ttMotsDocs()
        formuleInverse={}
        formuledice={}
        formulecos={}
        formulejac={}
        compteur=0

        while k <= n:
                sommePoids=0
                allWords=poidsMotsDocument(str(k))
                #teste if mot query = another one in allwords if yes add weight 
                for w in splitQuery:
                    if ( w in allWords.keys() ):
                        sommePoids=sommePoids+float(allWords[w])
                #when i'm done put the k le numero du file  with la somme dns forumule inverse
                formuleInverse.update({k:sommePoids})
                k=k+1

        for w in splitQuery:
            if(w in allmot):
                compteur=compteur+1 


        if choice=='produit d\'inverse':
            rowPosition = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(rowPosition)
            for k,v in formuleInverse.items():
                self.tableWidget_4.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(k)))
                self.tableWidget_4.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(v)))
                self.tableWidget_4.insertRow(rowPosition)  
            self.tableWidget_4.removeRow(0)
            

        if choice=='coefficient de dice':
            #grab formuleinverse list make a copy and applay to it the formula and return it 
            formuledice=formuleInverse
            for key,val in formuledice.items():
                val=(val*2)/(poidsCarre(str(key))+compteur)
                formuledice.update({key:val})
            rowPosition = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(rowPosition)
            for k,v in formuledice.items():
                self.tableWidget_4.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(k)))
                self.tableWidget_4.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(v)))
                self.tableWidget_4.insertRow(rowPosition)  
            self.tableWidget_4.removeRow(0)
            

        if choice=='cosinus':
            formulecos=formuleInverse
            for key,val in formulecos.items():
                val= val / sqrt(poidsCarre(str(key)) * compteur)
                formulecos.update({key:val})
            rowPosition = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(rowPosition)
            for k,v in formulecos.items():
                self.tableWidget_4.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(k)))
                self.tableWidget_4.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(v)))
                self.tableWidget_4.insertRow(rowPosition)  
            self.tableWidget_4.removeRow(0)
            
            
        if choice=='jaccord':
            formulejac=formuleInverse
            for key,val in formulejac.items():
                val=(val)/( poidsCarre(str(key)) + compteur - (val) )
                formulejac.update({key:val})
            rowPosition = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(rowPosition)
            for k,v in formulejac.items():
                self.tableWidget_4.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(k)))
                self.tableWidget_4.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(v)))
                self.tableWidget_4.insertRow(rowPosition)  
            self.tableWidget_4.removeRow(0)
##################################### probabiliste ####################################################################################################
    def probabiliste(self):
        def ttMotsDocs():
            words=[]
            wordsAndDocs={}
            f = open('inverse/inverse.txt', 'r')      
            for line in f:
                k, v = line.strip().split(':')
                wordsAndDocs[k.strip()]= v.strip()
            f.close()

            for key,value in wordsAndDocs.items() :# recupéré tt les mot 
                mot=re.search('([a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ]+)', key)
                if mot:
                    words.append(mot.group(1)) 
            words=list(set(words))
            return words
            #########################################################
        def poidsMotsDocument(numDoc):
            wordsPoids={}
            f = open('inverse/inversePoids.txt', 'r')   

            for line in f:
                k, v = line.strip().split(':')
                www=re.search('([0-9]+)', k)
                if www:
                    if (www.group(1)==numDoc):#if it is the same number as the document im looking for
                        mot=re.search('([a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ]+)', k)#grab the word
                        if mot:
                            kk,vv = mot.group(1), v
                            wordsPoids.update({kk:vv})        
            f.close()
            return wordsPoids
            #########################################################
        def poidsCarre(numDoc):
            poids=0
            listCarrePoids=[]
            f = open('inverse/inversePoids.txt', 'r')      
            for line in f:
                k, v = line.strip().split(':')
                www=re.search('([0-9]+)', k)
                if www:
                    if (www.group(1)==numDoc):#if it is the same number as the document im looking for
                        listCarrePoids.append(float(v)**2)      
            f.close()
            poids=sum(listCarrePoids)
            return poids
            #########################################################
        choice=self.comboBox_2.currentText()
        query=self.textEdit_5.toPlainText()
        for ii in reversed(range(self.tableWidget_5.rowCount())):
            self.tableWidget_5.removeRow(ii)

        k=1
        splitQuery=query.split()
        n= len(fnmatch.filter(os.listdir('C:/Users/HP/Desktop/RI/TP/TP2'),'*.txt'))
        allmot=[]
        allmot=ttMotsDocs()
        formuleInverse={}
        formuledice={}
        formulecos={}
        formulejac={}
        compteur=0
     

        while k <= n:
                sommePoids=0
                allWords=poidsMotsDocument(str(k))
                #teste if mot query = another one in allwords if yes add weight 
                for w in splitQuery:
                    if ( w in allWords.keys() ):
                        sommePoids=sommePoids+float(allWords[w])
                #when i'm done put the k le numero du file  with la somme dns forumule inverse
                formuleInverse.update({k:sommePoids})
                k=k+1

        for w in splitQuery:
            if(w in allmot):
                compteur=compteur+1 

        chkBoxItem = QtGui.QTableWidgetItem()
        chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        chkBoxItem.setCheckState(QtCore.Qt.Unchecked) 

        if choice=='produit d\'inverse':
            rowPosition = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(rowPosition)
            for k,v in formuleInverse.items():
                self.tableWidget_5.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(k)))
                self.tableWidget_5.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(v)))
                self.tableWidget_5.setItem(rowPosition , 2, QtGui.QTableWidgetItem(chkBoxItem))
                self.tableWidget_5.insertRow(rowPosition)  
            self.tableWidget_5.removeRow(0)
            

        if choice=='coefficient de dice':
            #grab formuleinverse list make a copy and applay to it the formula and return it 
            formuledice=formuleInverse
            for key,val in formuledice.items():
                val=(val*2)/(poidsCarre(str(key))+compteur)
                formuledice.update({key:val})
            rowPosition = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(rowPosition)
            for k,v in formuledice.items():
                self.tableWidget_5.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(k)))
                self.tableWidget_5.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(v)))
                self.tableWidget_5.setItem(rowPosition , 2, QtGui.QTableWidgetItem(chkBoxItem))
                self.tableWidget_5.insertRow(rowPosition)  
            self.tableWidget_5.removeRow(0)
            

        if choice=='cosinus':
            formulecos=formuleInverse
            for key,val in formulecos.items():
                val= val / sqrt(poidsCarre(str(key)) * compteur)
                formulecos.update({key:val})
            rowPosition = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(rowPosition)
            for k,v in formulecos.items():
                self.tableWidget_5.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(k)))
                self.tableWidget_5.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(v)))
                self.tableWidget_5.setItem(rowPosition , 2, QtGui.QTableWidgetItem(chkBoxItem))
                self.tableWidget_5.insertRow(rowPosition)  
            self.tableWidget_5.removeRow(0)
            
            
        if choice=='jaccord':
            formulejac=formuleInverse
            for key,val in formulejac.items():
                val=(val)/( poidsCarre(str(key)) + compteur - (val) )
                formulejac.update({key:val})
            rowPosition = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(rowPosition)
            for k,v in formulejac.items():
                self.tableWidget_5.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(k)))
                self.tableWidget_5.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(v)))
                self.tableWidget_5.setItem(rowPosition , 2, QtGui.QTableWidgetItem(chkBoxItem))
                self.tableWidget_5.insertRow(rowPosition)  
            self.tableWidget_5.removeRow(0)
###################################### clicked search probabiliste ##############################################################################################
    def searchProba(self):
        for ii in reversed(range(self.tableWidget_6.rowCount())):
            self.tableWidget_6.removeRow(ii)

        def nbrDocPertinant(listDoc,terme):
            cpt=0
            f = open('inverse/inversePoids.txt', 'r')   
            for line in f:
                k, v = line.strip().split(':')
                mot=re.search('([a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ]+)', k)#grab the word
                if mot:
                    if (mot.group(1)==terme):
                        www=re.search('([0-9]+)', k)
                        if www:
                            if (www.group(1) in listDoc):
                                cpt=cpt+1
                                 
            f.close()
            return cpt
        ############################################
        def nbrDoc(terme):
            cpt=0
            f = open('inverse/inversePoids.txt', 'r')   
            for line in f:
                k, v = line.strip().split(':')
                mot=re.search('([a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ]+)', k)#grab the word
                if mot:
                    if (mot.group(1)==terme):
                        cpt=cpt+1 
                                 
            f.close()
            return cpt
        #############################################
        def poidsMot(numDoc,elkalima):
        
            f = open('inverse/inversePoids.txt', 'r')
            poids=0.0   
            trouve=False
            for line in f:
                k, v = line.strip().split(':')
                www=re.search('([0-9]+)', k)
                if trouve==True:
                    break
                if www:
                    if (www.group(1)==numDoc):#if it is the same number as the document im looking for
                        mot=re.search('([a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ]+)', k)#grab the word
                        if mot:
                            if (mot.group(1)==elkalima):
                                poids= float(v)
                                trouve=True

            return poids                        
            
            
        #############################################
        def ttMotsDocs():
            words=[]
            wordsAndDocs={}
            f = open('inverse/inverse.txt', 'r')      
            for line in f:
                k, v = line.strip().split(':')
                wordsAndDocs[k.strip()]= v.strip()
            f.close()

            for key,value in wordsAndDocs.items() :# recupéré tt les mot 
                mot=re.search('([a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ]+)', key)
                if mot:
                    words.append(mot.group(1)) 
            words=list(set(words))
            return words
        #################################################
        #get all the documents that r checked in a list
        checkedDocs=[]
        query=self.textEdit_5.toPlainText()
        splitedQuery=query.split()
        rowCount = self.tableWidget_5.rowCount()
        for row in range(rowCount):
                item = self.tableWidget_5.item(row, 2)
                if item.checkState() == QtCore.Qt.Checked:
                    checkedDocs.append(self.tableWidget_5.item(row,0).text())#list of echantillion
        #create a vector that countains all the words with 0 or 1 if present in the query then open
        dicQuery={}
        words=ttMotsDocs()
        for element in (words):
            if element in splitedQuery:
                kk,vv = element, 1
                dicQuery.update({kk:vv})
                #add it to dicQuery with1
            else:
                kk,vv = element, 0
                dicQuery.update({kk:vv})

        #the inversePoids file too look for the weight of the words in the vector and multply weight * weightQ
        docsProba={}
        n= len(fnmatch.filter(os.listdir('C:/Users/HP/Desktop/RI/TP/TP2'),'*.txt'))

        for i in range(1,(n+1)):
            somme=float(0)
            for wordus in splitedQuery:
                logus=(nbrDocPertinant(checkedDocs,wordus) + 0.5)/(len(checkedDocs)-nbrDocPertinant(checkedDocs,wordus)+0.5)/(nbrDoc(wordus)-nbrDocPertinant(checkedDocs,wordus)+0.5)/(n-nbrDoc(wordus)-len(checkedDocs)+nbrDocPertinant(checkedDocs,wordus)+0.5) 

                somme = somme + (   float(log10(logus)) * float (poidsMot(str(i),wordus))  ) 
                
                
            kk,vv = i , somme
            docsProba.update({kk:vv})

        rowPosition = self.tableWidget_6.rowCount()
        self.tableWidget_6.insertRow(rowPosition)
        for k,v in docsProba.items():
            self.tableWidget_6.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(k)))
            self.tableWidget_6.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(v)))
            self.tableWidget_6.insertRow(rowPosition)  
        self.tableWidget_6.removeRow(0)


##################################################################################################################################################               
if __name__ == "__main__":
    import sys
    freq={}
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

