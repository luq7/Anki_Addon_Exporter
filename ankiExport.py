"""
Author     : Lck Huang
Date       : Dec-31-2020
Description: ANKI addons exporter
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys,os,getpass,platform
import anki_addon_exporter


class MyApp(QtWidgets.QMainWindow, anki_addon_exporter.Ui_Dialog):
    """
    A GUI class for the app
    ...
    
    Constructor-Parameters
    ----------------------------
    QtWidgets.QMainWindow         : the main scene for the GUI
    anki_addon_exporter.Ui_Dialog : the class of the front-end designed imported from 'anki_addon_exporter'
    ...

    Attributes
    ----------------------------
    directory : str
    addonList : list of str
    copyAll   : str
    msgBox    : QMessageBox
    clipboard : QApplication.Clipboard
    bt_Broswe : QPushbutton
    bt_Copy   : QPushbutton
    bt_Default: QPushbutton
    bt_Xport  : QPushbutton
    lineEdit  : QLineEdit
    textBrowser:QTextBrowser
    ...

    Methods
    ------------------------------
    lockUpText()
        Clear textBrowser and set it unenabled

    lineE_handle()
        Store the input in lineEdit to directory 

    bt_Browse_handle()
        Handle bt_Browse click and pop a QFileDialog to browse directory for the lineEdit

    bt_Copy_handle()
        Handle bt_Copy click by copying textBrowser's content(addon codes) to clipboard

    bt_Default_handle()
        Handle bt_Default click by filling the lineEdit with the default anki addons directory for different
        operating systems

    bt_Export_handle()
        Handel bt_Xport click by exporting all the addon's code to the textBrowser
    """

    def __init__(self, parent=None):
        """
        Initialize the anki addon's app's scene
        ...

        Parameters
        ------------
        parent   :   some QtWidgets? 
        """
        super(MyApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("anki_exporter_logo.png")) # Set icon for main scene
        
        # Varaible declaration
        self.directory=None
        self.addonList=None
        self.copyAll=""

        # Creating a messagebox
        self.msgBox=QtWidgets.QMessageBox()
        self.msgBox.setWindowIcon(QtGui.QIcon("anki_exporter_logo.png")) #Set icon for msgbox
        # Set a clipboard
        self.clipboard = QtWidgets.QApplication.clipboard()

        # Event handling 
        self.bt_Broswe.clicked.connect(self.bt_Browse_handle)  # Browse button handle
        self.bt_Copy.clicked.connect(self.bt_Copy_handle)      # Copy button handle
        self.bt_Default.clicked.connect(self.bt_Default_handle)# Default button handle
        self.bt_Xport.clicked.connect(self.bt_Export_handle)   # Export button hanlde
        self.lineEdit.textChanged.connect(self.lineE_handle)   # Line edit handle

        #Pop-up msgBox
        self.msgBox.setText("""
        You could use the \"Default\" to get the addon directory 
        if you haven't move anki's files. Otherwise, use \"Browse\".
        (\"Default\" works only for Anki2.1.x ) 
        """)
        self.msgBox.exec()

        
    def lockUpText(self):
        """
        Clear textBrowser and set it unenabled
        ...
        """
        self.textBrowser.setEnabled(False)
        self.textBrowser.clear()
        self.directory=""
        self.copyAll=""

    def lineE_handle(self):
        """
        Get the entered input in the lineEdit as directory
        """
        self.lockUpText()
        self.directory=self.lineEdit.text()

    def bt_Browse_handle(self):
        """
        Handle bt_Browse click and pop a QFileDialog to browse addon's path. Store browsed path 
        in directory and show in on lineEdit
        """
        self.lockUpText()
        self.directory=QFileDialog.getExistingDirectory(self)
        self.lineEdit.setText(self.directory)

    def bt_Copy_handle(self):
        """
        Copy the extracted addon's code to the clipboard. If it is empty then show error
        """
        if self.textBrowser.isEnabled():
            self.clipboard.setText(self.copyAll)
            self.msgBox.setText("Got'em! (Copied to your clipboard.)")
            self.msgBox.exec()
        else:
            self.msgBox.setText("Nothing to copy!")
            self.msgBox.exec()

    
    def bt_Default_handle(self):
        """
        Handle bt_Default that fills the lineEdit by the default anki's addon path for different OS.
        Also, store the default path to directory
        ----------
        OJO:
        platform.system() returns the current running OS (from import platform)
        getpass.getuser() returns the machine's username (from import getpass)
        """
        self.lockUpText()
        if platform.system()=='Windows':
            self.directory="C:/Users/"+getpass.getuser()+"/AppData/Roaming/Anki2/addons21" 
            self.lineEdit.setText(self.directory.replace("/","\\"))
        elif platform.system()=='Linux':
            self.directory='/home/'+getpass.getuser()+'/.local/share/Anki2/addons21'
            self.lineEdit.setText(self.directory)
        elif platform.system()=='Darwin':
            self.directory='/Users/'+getpass.getuser()+'/Library/Application Support/Anki2/addons21'
            self.lineEdit.setText(self.directory)
        else:
            self.msgBox.setText("Unsupported system. Use \"Browse\" button to find your addons directory instead.")
            self.msgBox.exec()


    def bt_Export_handle(self):
        """
        Handle bt_Xport by extracting the addon's code and show it on textBrowser
        """
        if len(self.lineEdit.text())<1:
            self.msgBox.setText("Please provide a directroy to export the addons!")
            self.msgBox.exec()
            self.lockUpText()
        elif not os.path.isdir(self.lineEdit.text()):
            self.msgBox.setText("No such directory")
            self.msgBox.exec()
            self.lockUpText()
        else:
            self.textBrowser.clear()
            self.addonList=[folder for folder in os.listdir(self.directory) if os.path.isdir(self.directory+"/"+folder)]
            self.textBrowser.setEnabled(True)
            for folder in self.addonList:
                self.textBrowser.append(folder)
                self.copyAll= self.copyAll + folder + "\n"

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyApp()
    form.show()
    app.exec_()
