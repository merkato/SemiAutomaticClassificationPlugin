# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_semiautomaticclassificationplugin_scatter_plot.ui'
#
# Created: Fri Jan 27 19:37:23 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_ScatterPlot(object):
    def setupUi(self, ScatterPlot):
        ScatterPlot.setObjectName(_fromUtf8("ScatterPlot"))
        ScatterPlot.resize(710, 527)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScatterPlot.sizePolicy().hasHeightForWidth())
        ScatterPlot.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/semiautomaticclassificationplugin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ScatterPlot.setWindowIcon(icon)
        self.gridLayout_7 = QtGui.QGridLayout(ScatterPlot)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scatter_list_plot_tableWidget = QtGui.QTableWidget(ScatterPlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scatter_list_plot_tableWidget.sizePolicy().hasHeightForWidth())
        self.scatter_list_plot_tableWidget.setSizePolicy(sizePolicy)
        self.scatter_list_plot_tableWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.scatter_list_plot_tableWidget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.scatter_list_plot_tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.scatter_list_plot_tableWidget.setObjectName(_fromUtf8("scatter_list_plot_tableWidget"))
        self.scatter_list_plot_tableWidget.setColumnCount(6)
        self.scatter_list_plot_tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(5, item)
        self.scatter_list_plot_tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.scatter_list_plot_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.scatter_list_plot_tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.gridLayout_2.addWidget(self.scatter_list_plot_tableWidget, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.Scatter_Widget_2 = ScatterWidget2(ScatterPlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Scatter_Widget_2.sizePolicy().hasHeightForWidth())
        self.Scatter_Widget_2.setSizePolicy(sizePolicy)
        self.Scatter_Widget_2.setObjectName(_fromUtf8("Scatter_Widget_2"))
        self.gridLayout_3.addWidget(self.Scatter_Widget_2, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.frame = QtGui.QFrame(ScatterPlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_26 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSans"))
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(_fromUtf8("background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #535353, stop:1 #a6a6a6); color : white"))
        self.label_26.setFrameShape(QtGui.QFrame.Panel)
        self.label_26.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_6.addWidget(self.label_26, 9, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_49 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.horizontalLayout_8.addWidget(self.label_49)
        self.scatter_ROI_Button = QtGui.QToolButton(self.frame)
        self.scatter_ROI_Button.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_enter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scatter_ROI_Button.setIcon(icon1)
        self.scatter_ROI_Button.setIconSize(QtCore.QSize(22, 22))
        self.scatter_ROI_Button.setObjectName(_fromUtf8("scatter_ROI_Button"))
        self.horizontalLayout_8.addWidget(self.scatter_ROI_Button)
        self.gridLayout_6.addLayout(self.horizontalLayout_8, 6, 0, 1, 1)
        self.gridLayout_14 = QtGui.QGridLayout()
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.show_polygon_area_pushButton = QtGui.QToolButton(self.frame)
        self.show_polygon_area_pushButton.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        self.show_polygon_area_pushButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_scatter_show_raster.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_polygon_area_pushButton.setIcon(icon2)
        self.show_polygon_area_pushButton.setIconSize(QtCore.QSize(22, 22))
        self.show_polygon_area_pushButton.setObjectName(_fromUtf8("show_polygon_area_pushButton"))
        self.horizontalLayout_7.addWidget(self.show_polygon_area_pushButton)
        self.add_signature_list_pushButton = QtGui.QToolButton(self.frame)
        self.add_signature_list_pushButton.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        self.add_signature_list_pushButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_save_plot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_signature_list_pushButton.setIcon(icon3)
        self.add_signature_list_pushButton.setIconSize(QtCore.QSize(22, 22))
        self.add_signature_list_pushButton.setObjectName(_fromUtf8("add_signature_list_pushButton"))
        self.horizontalLayout_7.addWidget(self.add_signature_list_pushButton)
        self.gridLayout_14.addLayout(self.horizontalLayout_7, 1, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem, 3, 3, 1, 1)
        self.value_label_2 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        font.setBold(True)
        font.setWeight(75)
        self.value_label_2.setFont(font)
        self.value_label_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.value_label_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.value_label_2.setObjectName(_fromUtf8("value_label_2"))
        self.gridLayout_14.addWidget(self.value_label_2, 7, 3, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.fitToAxes_pushButton_2 = QtGui.QToolButton(self.frame)
        self.fitToAxes_pushButton_2.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        self.fitToAxes_pushButton_2.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_fit_plot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fitToAxes_pushButton_2.setIcon(icon4)
        self.fitToAxes_pushButton_2.setIconSize(QtCore.QSize(22, 22))
        self.fitToAxes_pushButton_2.setObjectName(_fromUtf8("fitToAxes_pushButton_2"))
        self.horizontalLayout_4.addWidget(self.fitToAxes_pushButton_2)
        self.save_plot_pushButton_2 = QtGui.QToolButton(self.frame)
        self.save_plot_pushButton_2.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        self.save_plot_pushButton_2.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_save_plot_image.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_plot_pushButton_2.setIcon(icon5)
        self.save_plot_pushButton_2.setIconSize(QtCore.QSize(22, 22))
        self.save_plot_pushButton_2.setObjectName(_fromUtf8("save_plot_pushButton_2"))
        self.horizontalLayout_4.addWidget(self.save_plot_pushButton_2)
        self.gridLayout_14.addLayout(self.horizontalLayout_4, 6, 3, 1, 1)
        self.label_27 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSans"))
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(_fromUtf8("background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #535353, stop:1 #a6a6a6); color : white"))
        self.label_27.setFrameShape(QtGui.QFrame.Panel)
        self.label_27.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_14.addWidget(self.label_27, 4, 3, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_50 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy)
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.horizontalLayout_6.addWidget(self.label_50)
        self.colormap_comboBox = QtGui.QComboBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colormap_comboBox.sizePolicy().hasHeightForWidth())
        self.colormap_comboBox.setSizePolicy(sizePolicy)
        self.colormap_comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.colormap_comboBox.setObjectName(_fromUtf8("colormap_comboBox"))
        self.horizontalLayout_6.addWidget(self.colormap_comboBox)
        self.plot_color_ROI_pushButton = QtGui.QToolButton(self.frame)
        self.plot_color_ROI_pushButton.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        self.plot_color_ROI_pushButton.setText(_fromUtf8(""))
        self.plot_color_ROI_pushButton.setIcon(icon1)
        self.plot_color_ROI_pushButton.setIconSize(QtCore.QSize(22, 22))
        self.plot_color_ROI_pushButton.setObjectName(_fromUtf8("plot_color_ROI_pushButton"))
        self.horizontalLayout_6.addWidget(self.plot_color_ROI_pushButton)
        self.gridLayout_14.addLayout(self.horizontalLayout_6, 5, 3, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_51 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy)
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.horizontalLayout_5.addWidget(self.label_51)
        self.extent_comboBox = QtGui.QComboBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extent_comboBox.sizePolicy().hasHeightForWidth())
        self.extent_comboBox.setSizePolicy(sizePolicy)
        self.extent_comboBox.setObjectName(_fromUtf8("extent_comboBox"))
        self.extent_comboBox.addItem(_fromUtf8(""))
        self.extent_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.extent_comboBox)
        self.gridLayout_14.addLayout(self.horizontalLayout_5, 2, 3, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_14, 11, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.draw_polygons_pushButton = QtGui.QToolButton(self.frame)
        self.draw_polygons_pushButton.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_scatter_edit_polygon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.draw_polygons_pushButton.setIcon(icon6)
        self.draw_polygons_pushButton.setIconSize(QtCore.QSize(22, 22))
        self.draw_polygons_pushButton.setObjectName(_fromUtf8("draw_polygons_pushButton"))
        self.horizontalLayout_3.addWidget(self.draw_polygons_pushButton)
        self.label_22 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_3.addWidget(self.label_22)
        self.polygon_color_Button = QtGui.QPushButton(self.frame)
        self.polygon_color_Button.setStyleSheet(_fromUtf8("background-color : #FFAA00"))
        self.polygon_color_Button.setText(_fromUtf8(""))
        self.polygon_color_Button.setObjectName(_fromUtf8("polygon_color_Button"))
        self.horizontalLayout_3.addWidget(self.polygon_color_Button)
        self.remove_polygons_pushButton = QtGui.QToolButton(self.frame)
        self.remove_polygons_pushButton.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_scatter_reset_polygon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_polygons_pushButton.setIcon(icon7)
        self.remove_polygons_pushButton.setIconSize(QtCore.QSize(22, 22))
        self.remove_polygons_pushButton.setObjectName(_fromUtf8("remove_polygons_pushButton"))
        self.horizontalLayout_3.addWidget(self.remove_polygons_pushButton)
        self.gridLayout_6.addLayout(self.horizontalLayout_3, 10, 0, 1, 1)
        self.gridLayout_40 = QtGui.QGridLayout()
        self.gridLayout_40.setObjectName(_fromUtf8("gridLayout_40"))
        self.label_48 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.gridLayout_40.addWidget(self.label_48, 0, 0, 1, 1)
        self.bandY_spinBox = QtGui.QSpinBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bandY_spinBox.sizePolicy().hasHeightForWidth())
        self.bandY_spinBox.setSizePolicy(sizePolicy)
        self.bandY_spinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.bandY_spinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bandY_spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bandY_spinBox.setMinimum(1)
        self.bandY_spinBox.setMaximum(2000)
        self.bandY_spinBox.setProperty("value", 2)
        self.bandY_spinBox.setObjectName(_fromUtf8("bandY_spinBox"))
        self.gridLayout_40.addWidget(self.bandY_spinBox, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_40, 2, 0, 1, 1)
        self.gridLayout_38 = QtGui.QGridLayout()
        self.gridLayout_38.setObjectName(_fromUtf8("gridLayout_38"))
        self.label_46 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy)
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.gridLayout_38.addWidget(self.label_46, 0, 0, 1, 1)
        self.bandX_spinBox = QtGui.QSpinBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bandX_spinBox.sizePolicy().hasHeightForWidth())
        self.bandX_spinBox.setSizePolicy(sizePolicy)
        self.bandX_spinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.bandX_spinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bandX_spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bandX_spinBox.setMinimum(1)
        self.bandX_spinBox.setMaximum(2000)
        self.bandX_spinBox.setProperty("value", 1)
        self.bandX_spinBox.setObjectName(_fromUtf8("bandX_spinBox"))
        self.gridLayout_38.addWidget(self.bandX_spinBox, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_38, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.precision_checkBox = QtGui.QCheckBox(self.frame)
        self.precision_checkBox.setObjectName(_fromUtf8("precision_checkBox"))
        self.horizontalLayout_2.addWidget(self.precision_checkBox)
        self.precision_comboBox = QtGui.QComboBox(self.frame)
        self.precision_comboBox.setObjectName(_fromUtf8("precision_comboBox"))
        self.precision_comboBox.addItem(_fromUtf8(""))
        self.precision_comboBox.addItem(_fromUtf8(""))
        self.precision_comboBox.addItem(_fromUtf8(""))
        self.precision_comboBox.addItem(_fromUtf8(""))
        self.precision_comboBox.addItem(_fromUtf8(""))
        self.precision_comboBox.addItem(_fromUtf8(""))
        self.precision_comboBox.addItem(_fromUtf8(""))
        self.precision_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.precision_comboBox)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 8, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.remove_Signature_Button = QtGui.QToolButton(self.frame)
        self.remove_Signature_Button.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_Signature_Button.setIcon(icon8)
        self.remove_Signature_Button.setIconSize(QtCore.QSize(22, 22))
        self.remove_Signature_Button.setObjectName(_fromUtf8("remove_Signature_Button"))
        self.horizontalLayout.addWidget(self.remove_Signature_Button)
        self.plot_temp_ROI_pushButton = QtGui.QToolButton(self.frame)
        self.plot_temp_ROI_pushButton.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        self.plot_temp_ROI_pushButton.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_scatter_raster_temp_ROI.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plot_temp_ROI_pushButton.setIcon(icon9)
        self.plot_temp_ROI_pushButton.setIconSize(QtCore.QSize(22, 22))
        self.plot_temp_ROI_pushButton.setObjectName(_fromUtf8("plot_temp_ROI_pushButton"))
        self.horizontalLayout.addWidget(self.plot_temp_ROI_pushButton)
        self.plot_display_pushButton = QtGui.QToolButton(self.frame)
        self.plot_display_pushButton.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        self.plot_display_pushButton.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_scatter_raster_display.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plot_display_pushButton.setIcon(icon10)
        self.plot_display_pushButton.setIconSize(QtCore.QSize(22, 22))
        self.plot_display_pushButton.setObjectName(_fromUtf8("plot_display_pushButton"))
        self.horizontalLayout.addWidget(self.plot_display_pushButton)
        self.plot_image_pushButton = QtGui.QToolButton(self.frame)
        self.plot_image_pushButton.setStyleSheet(_fromUtf8("margin: 0px;padding: 0px;"))
        self.plot_image_pushButton.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/icons/semiautomaticclassificationplugin_scatter_raster_image.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plot_image_pushButton.setIcon(icon11)
        self.plot_image_pushButton.setIconSize(QtCore.QSize(22, 22))
        self.plot_image_pushButton.setObjectName(_fromUtf8("plot_image_pushButton"))
        self.horizontalLayout.addWidget(self.plot_image_pushButton)
        self.gridLayout_6.addLayout(self.horizontalLayout, 7, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 1, 1, 2, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_25 = QtGui.QLabel(ScatterPlot)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSans"))
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(_fromUtf8("background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #535353, stop:1 #a6a6a6); color : white"))
        self.label_25.setFrameShape(QtGui.QFrame.Panel)
        self.label_25.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_4.addWidget(self.label_25, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 2)
        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.retranslateUi(ScatterPlot)
        self.colormap_comboBox.setCurrentIndex(-1)
        self.extent_comboBox.setCurrentIndex(0)
        self.precision_comboBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ScatterPlot)

    def retranslateUi(self, ScatterPlot):
        ScatterPlot.setWindowTitle(_translate("ScatterPlot", "SCP: Scatter Plot", None))
        self.scatter_list_plot_tableWidget.setSortingEnabled(True)
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ScatterPlot", "S", None))
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ScatterPlot", "MC ID", None))
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ScatterPlot", "MC Info", None))
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ScatterPlot", "C ID", None))
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ScatterPlot", "C Info", None))
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ScatterPlot", "Color", None))
        self.label_26.setText(_translate("ScatterPlot", " Scatter raster", None))
        self.label_49.setText(_translate("ScatterPlot", "Calculate", None))
        self.scatter_ROI_Button.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Calculate scatter plot</p></body></html>", None))
        self.show_polygon_area_pushButton.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Calculate and display scatter raster</p></body></html>", None))
        self.add_signature_list_pushButton.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Calculate and save to signature list</p></body></html>", None))
        self.value_label_2.setText(_translate("ScatterPlot", "x=0.000000 y=0.000000", None))
        self.fitToAxes_pushButton_2.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Automatically fit the plot to data</p></body></html>", None))
        self.save_plot_pushButton_2.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Save the plot to file (jpg, png, pdf)</p></body></html>", None))
        self.label_27.setText(_translate("ScatterPlot", " Plot", None))
        self.label_50.setText(_translate("ScatterPlot", "Colormap", None))
        self.colormap_comboBox.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Select a colormap</p></body></html>", None))
        self.plot_color_ROI_pushButton.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Set colormap for highlighted spectral plots</p></body></html>", None))
        self.label_51.setText(_translate("ScatterPlot", "Extent", None))
        self.extent_comboBox.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Select extent of scatter raster</p></body></html>", None))
        self.extent_comboBox.setItemText(0, _translate("ScatterPlot", "same as display", None))
        self.extent_comboBox.setItemText(1, _translate("ScatterPlot", "same as image", None))
        self.draw_polygons_pushButton.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Create selection polygons</p></body></html>", None))
        self.label_22.setText(_translate("ScatterPlot", "color", None))
        self.polygon_color_Button.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Select polygon color</p></body></html>", None))
        self.remove_polygons_pushButton.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Remove selection polygons</p></body></html>", None))
        self.label_48.setText(_translate("ScatterPlot", "Band Y", None))
        self.bandY_spinBox.setToolTip(_translate("ScatterPlot", "<html><head/><body><p align=\"justify\">Band Y</p></body></html>", None))
        self.label_46.setText(_translate("ScatterPlot", "Band X", None))
        self.bandX_spinBox.setToolTip(_translate("ScatterPlot", "<html><head/><body><p align=\"justify\">Band X</p></body></html>", None))
        self.precision_checkBox.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Use custom decimal precision</p></body></html>", None))
        self.precision_checkBox.setText(_translate("ScatterPlot", "Precision", None))
        self.precision_comboBox.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Select decimal precision:</p><p>4 = 10^<span style=\" vertical-align:super;\">−4</span></p><p>3 = 10^<span style=\" vertical-align:super;\">−3</span></p><p>2 = 10^<span style=\" vertical-align:super;\">−2</span></p><p>1 = 10^<span style=\" vertical-align:super;\">−1</span></p><p>0 = 1</p><p>-1 = 10</p><p>-2 = 10^<span style=\" vertical-align:super;\">2</span></p><p>-3 = 10^<span style=\" vertical-align:super;\">3</span></p></body></html>", None))
        self.precision_comboBox.setItemText(0, _translate("ScatterPlot", "4", None))
        self.precision_comboBox.setItemText(1, _translate("ScatterPlot", "3", None))
        self.precision_comboBox.setItemText(2, _translate("ScatterPlot", "2", None))
        self.precision_comboBox.setItemText(3, _translate("ScatterPlot", "1", None))
        self.precision_comboBox.setItemText(4, _translate("ScatterPlot", "0", None))
        self.precision_comboBox.setItemText(5, _translate("ScatterPlot", "-1", None))
        self.precision_comboBox.setItemText(6, _translate("ScatterPlot", "-2", None))
        self.precision_comboBox.setItemText(7, _translate("ScatterPlot", "-3", None))
        self.remove_Signature_Button.setToolTip(_translate("ScatterPlot", "<html><head/><body><p >Delete row</p></body></html>", None))
        self.remove_Signature_Button.setText(_translate("ScatterPlot", "Plot", None))
        self.plot_temp_ROI_pushButton.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Calculate scatter plot from temporary ROI</p></body></html>", None))
        self.plot_display_pushButton.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Calculate scatter plot from the current display extent</p></body></html>", None))
        self.plot_image_pushButton.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Calculate scatter plot from entire image</p></body></html>", None))
        self.label_25.setText(_translate("ScatterPlot", " Scatter list", None))

from scatterwidget2 import ScatterWidget2
import resources_rc
