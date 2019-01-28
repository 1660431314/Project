import sys
from PyQt5 import QtWidgets
from hello import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import re
import pyperclip
from PyQt5.QtWidgets import QFileDialog
from itertools import groupby
class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

    def createCode(self):
        print ('This is CreateCode')
        rowCount=self.tableWidget.rowCount()
        i = 0
        strCode = ''
        while (i<rowCount):
            strline = '========================' + self.tableWidget.item(i, 0).text() + '========================\r\n'
            strIp = str(self.tableWidget.item(i, 0).text())
            strMask = self.tableWidget.item(i, 1).text()
            strGateway = self.tableWidget.item(i, 2).text()
            strPortNum = int(self.tableWidget.item(i, 3).text())
            strUplinkPort = self.tableWidget.item(i, 4).text()
            strTelnet = self.tableWidget.item(i, 5).text()
            strSsh = self.tableWidget.item(i, 6).text()
            strUserName = self.tableWidget.item(i, 7).text()
            strPassword = self.tableWidget.item(i, 8).text()
            strLocalVlan = self.tableWidget.item(i, 9).text()
            strUplinkVlan = self.tableWidget.item(i, 10).text()
            strDeviceName = self.tableWidget.item(i, 11).text()
            strDesLocalVlan = self.tableWidget.item(i, 12).text()
            strDesUplinkVlan = self.tableWidget.item(i, 13).text()
            strDesUplinkPort = self.tableWidget.item(i, 14).text()
            strSimplifyCode = self.tableWidget.item(i, 15).text()
            strCodedefault = self.codeDefault(strDeviceName)
            print('1111111111111111111111')
            strCodeCreatVlan = self.codeCreatVlanif(strLocalVlan, strIp, strMask,strUplinkVlan,strDesLocalVlan,strDesUplinkVlan)
            strCodeAAA = self.codeAAA(strTelnet, strSsh, strUserName, strPassword)
            if (strSimplifyCode != 'True' ):
                strCodeEdgedPort = self.codeEdgedPort(strPortNum, strLocalVlan,strUplinkPort,strUplinkVlan,strDesUplinkPort)   #portnum,localvlan,uplinkPort,uplinkVlan,desUplinkPort
            else:
                strCodeEdgedPort = self.codePortSimplify(strPortNum, strLocalVlan,strUplinkPort,strUplinkVlan,strDesUplinkPort)
            print('222222222222222222222222222')
            #strCodeUplinkPort = self.codeUplinkPort(strUplinkPort, strPortNum, strUplinkVlan,strDesUplinkPort)
            strCodeRoute = self.codeRoute(strGateway)
            strCodeSsh = self.codeSSH(strUserName,strSsh)
            strCode = strCode+strline+strCodedefault + strCodeCreatVlan + strCodeEdgedPort + strCodeAAA+strCodeSsh + strCodeRoute + self.textEdit_command.toPlainText()
            i = i + 1
            #print(strCode)
        if (rowCount == 1):
            strCode = strCodedefault + strCodeCreatVlan + strCodeEdgedPort  + strCodeAAA + strCodeSsh + strCodeRoute + self.textEdit_command.toPlainText()
        self.textBrowser_Code.setText(strCode)
        return strCode

    def copyCode(self):
        strCopyCode = self.textBrowser_Code.toPlainText()
        strCopyCode = strCopyCode.replace('\n','\r\n')
        pyperclip.copy(strCopyCode)
        return  True

    def deleteTableItem(self):
        print('This is DeleteTableItem:')
        #print (self.tableWidget.currentRow())
        self.tableWidget.removeRow(self.tableWidget.currentRow())

    def checkIP(self,str):
        p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        if p.match(str):
            return True
        else:
            return  False

    def addTableItem(self):
        print('This is AddTableItem')
        print (self.lineEdit_IP.text())
        print (self.checkIP(self.lineEdit_IP.text()))
        if (self.lineEdit_IP.text()==''):
            self.tableWidget.insertRow(0)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(self.lineEdit_IP.text()))
            self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(''))
            self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(self.lineEdit_Gateway.text()))
            self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(self.spinBox_PortNum.text()))
            self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(self.lineEdit_UplinkPort.text()))
            self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(str(self.checkBox_Telnet.isChecked())))
            self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem(str(self.checkBox_Ssh.isChecked())))
            self.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem(str(self.lineEdit_UserName.text())))
            self.tableWidget.setItem(0, 8, QtWidgets.QTableWidgetItem(str(self.lineEdit_Password.text())))
            self.tableWidget.setItem(0, 9, QtWidgets.QTableWidgetItem(str(self.spinBox_LocalVlan.text())))
            self.tableWidget.setItem(0, 10, QtWidgets.QTableWidgetItem(str(self.spinBox_UplinkVlan.text())))
            self.tableWidget.setItem(0, 11, QtWidgets.QTableWidgetItem(str(self.lineEdit_DeviceName.text())))
            self.tableWidget.setItem(0, 12, QtWidgets.QTableWidgetItem(str(self.lineEdit_DesLocalVlan.text())))
            self.tableWidget.setItem(0, 13, QtWidgets.QTableWidgetItem(str(self.lineEdit_DesUplinkVlan.text())))
            self.tableWidget.setItem(0, 14, QtWidgets.QTableWidgetItem(str(self.lineEdit_DesUplinkPort.text())))
            self.tableWidget.setItem(0, 15, QtWidgets.QTableWidgetItem(str(self.checkBox_SimpilyCode.isChecked())))
        if (self.checkIP(self.lineEdit_IP.text())==True and self.checkIP(self.lineEdit_Gateway.text() )==True):  # and int (self.lineEdit_UplinkPort.text())<= int(self.spinBox_PortNum.text())
            self.tableWidget.insertRow(0)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(self.lineEdit_IP.text()))
            self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(self.comboBox_Mask.currentText()))
            self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(self.lineEdit_Gateway.text()))
            self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(self.spinBox_PortNum.text()))
            self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(self.lineEdit_UplinkPort.text()))
            self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(str(self.checkBox_Telnet.isChecked())))
            self.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem(str(self.checkBox_Ssh.isChecked())))
            self.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem(str(self.lineEdit_UserName.text())))
            self.tableWidget.setItem(0, 8, QtWidgets.QTableWidgetItem(str(self.lineEdit_Password.text())))
            self.tableWidget.setItem(0, 9, QtWidgets.QTableWidgetItem(str(self.spinBox_LocalVlan.text())))
            self.tableWidget.setItem(0, 10, QtWidgets.QTableWidgetItem(str(self.spinBox_UplinkVlan.text())))
            self.tableWidget.setItem(0, 11, QtWidgets.QTableWidgetItem(str(self.lineEdit_DeviceName.text())))
            self.tableWidget.setItem(0, 12, QtWidgets.QTableWidgetItem(str(self.lineEdit_DesLocalVlan.text())))
            self.tableWidget.setItem(0, 13, QtWidgets.QTableWidgetItem(str(self.lineEdit_DesUplinkVlan.text())))
            self.tableWidget.setItem(0, 14, QtWidgets.QTableWidgetItem(str(self.lineEdit_DesUplinkPort.text())))
            self.tableWidget.setItem(0, 15, QtWidgets.QTableWidgetItem(str(self.checkBox_SimpilyCode.isChecked())))

    def codeAAA(self,strtelnet,strSsh,username,password):
        strCodeAAA='aaa \r\n local-user testusername password irreversible-cipher testpassword  \r\n local-user testusername privilege level 15 \r\n local-user testusername service-type ssh telnet terminal  \r\n undo local-aaa-user password policy administrator\r\nquit \r\nuser-interface con 0 \r\n authentication-mode aaa \r\nquit\r\nuser-interface vty 0 4 \r\n authentication-mode aaa\r\n protocol inbound all \r\nquit\r\n'
        strCodeAAA = strCodeAAA.replace('testusername',username)
        strCodeAAA = strCodeAAA.replace('testpassword', password)
        if (strtelnet != 'True'):
            strCodeAAA = strCodeAAA.replace('telnet','')
        if (strSsh  != 'True'):
            strCodeAAA = strCodeAAA.replace('ssh', '')
        if (strtelnet != 'True'and strSsh  != 'True'):
            strCodeAAA = ''
        return  strCodeAAA

    def codeSSH(self,usernmae,strSsh):
        strCodeSsh = 'stelnet server enable \r\nssh user testusername \r\nssh user testusername authentication-type password \r\nssh user testusername service-type stelnet\r\n'
        strCodeSsh = strCodeSsh.replace('testusername',usernmae)
        if (strSsh  != 'True'):
            strCodeSsh = ''
        return  strCodeSsh

    def codeDefault(self,devicename):
        strCodeDefault = 'sysname 9999 \r\ntelnet server enable \r\nstp bpdu-protection \r\nerror-down  auto-recovery  cause  bpdu-protection interval  30 \r\nsnmp-agent sys-info  version  all\r\nsnmp-agent community  read  cipher customs@sz\r\n'
        strCodeDefault = strCodeDefault.replace('9999',devicename)
        return strCodeDefault

    def codeCreatVlanif(self,localvlan,ip,mask,uplinkvlan,desloaclvlan,desuplinkvlan):
        strVlanif = ''
        strVlan = 'vlan  9999 \r\n description 7777 \r\n'
        strVlan = strVlan.replace('9999',localvlan)
        strVlan = strVlan.replace('7777', desloaclvlan)
        if (localvlan != uplinkvlan):
            strVlan = strVlan+'vlan  8888 \r\n description 6666 \r\n'
            strVlan = strVlan.replace('8888',uplinkvlan)
            strVlan = strVlan.replace('6666', desuplinkvlan)
        if (len(ip)!=0):    #判断vlanif是否为空
            strVlanif ='interface Vlanif9999 \r\n description 8888 \r\n ip address 999.999.999.999 111.111.111.111 \r\nquit\r\n'
            strVlanif = strVlanif.replace('8888',desloaclvlan)
            strVlanif = strVlanif.replace('9999', localvlan)
            strVlanif = strVlanif.replace('999.999.999.999',ip)
            strVlanif = strVlanif.replace('111.111.111.111',mask)
        return  strVlan+strVlanif

    def codeEdgedPort(self,portnum,localvlan,uplinkPort,uplinkVlan,desUplinkPort):   #已经包含边缘端口和上联口
        arr =self.getuplinkport(uplinkPort,portnum)
        portnum = int(portnum)
        print ('portnum:',portnum)
        strCodeEdgedPort = ''
        i = 1
        while (i<=portnum): #添加边缘端口
            if i not in arr:
                strCodeEdgedPort1 ='interface gigabitethernet 0/0/9999 \r\n port link-type access \r\n port default vlan 8888 \r\n stp edged-port enable \r\n'
                strCodeEdgedPort1 = strCodeEdgedPort1.replace('9999',str(i))
                strCodeEdgedPort1 = strCodeEdgedPort1.replace('8888', localvlan)
                strCodeEdgedPort = strCodeEdgedPort + strCodeEdgedPort1
            else:   #添加上联口
                strtest = 'interface GigabitEthernet 0/0/9999 \r\n description 7777 \r\n port link-type access \r\n port default vlan 8888\r\n stp disable \r\n stp bpdu-filter enable \r\n'
                strtest = strtest.replace('8888', uplinkVlan)
                strtest = strtest.replace('9999', str(i))
                strtest = strtest.replace('7777', desUplinkPort)
                strCodeEdgedPort = strCodeEdgedPort + strtest
            i = i+1
        strCodeEdgedPort = strCodeEdgedPort + 'quit\r\n'
        return  strCodeEdgedPort

    def codePortSimplify(self,portnum,localvlan,uplinkPort,uplinkVlan,desUplinkPort):
        print(uplinkPort)
        arrEdgedPort = self.splitEdgedPort(uplinkPort,portnum)
        print('jjjjjjjjjjjjjjjjjjjjjjjj')

        print (arrEdgedPort)
        i = 0
        strCodeEdgedPort = ''
        while (i < len(arrEdgedPort)):
            print('11111111111111111')
            if (len(arrEdgedPort[i])==1):
                print('ssssssssssssssssssssss')
                strCodeEdgedPort = strCodeEdgedPort + 'interface gigabitethernet 0/0/9999 \r\n port link-type access \r\n port default vlan 8888 \r\n stp edged-port enable \r\nquit \r\n'
                strCodeEdgedPort = strCodeEdgedPort.replace('9999',str(arrEdgedPort[i][0]))
                strCodeEdgedPort = strCodeEdgedPort.replace('8888', localvlan)
            else:
                print('cccccccccccccccccccccccccc')
                strCodeEdgedPort = strCodeEdgedPort + 'interface range gigabitethernet 0/0/8888 to gigabitethernet 0/0/7777 \r\n port link-type access \r\n port default vlan 6666 \r\n stp edged-port enable \r\nquit \r\n'
                strCodeEdgedPort = strCodeEdgedPort.replace('8888', str(arrEdgedPort[i][0]))
                strCodeEdgedPort = strCodeEdgedPort.replace('7777', str(arrEdgedPort[i][-1]))
                strCodeEdgedPort = strCodeEdgedPort.replace('6666', localvlan)
            i = i +1
        j = 0
        print (strCodeEdgedPort)
        arrUplinkPort = self.splitUplinkPort(uplinkPort, portnum)
        print(arrUplinkPort)
        strCodeUplinkPort = ''
        print ('bbbbbbbbbbbbbb')
        while (j < len(arrUplinkPort)):
            print ('nnnnnnnnnnnnnn')
            if  (len(arrUplinkPort[j])==1):
                print ('xxxxxxxxxxxxxxxx')
                strCodeUplinkPort = strCodeUplinkPort +'interface GigabitEthernet 0/0/9999 \r\n description 7777 \r\n port link-type access \r\n port default vlan 8888\r\n stp disable \r\n stp bpdu-filter enable \r\nquit \r\n'
                strCodeUplinkPort = strCodeUplinkPort.replace('8888', uplinkVlan)
                strCodeUplinkPort = strCodeUplinkPort.replace('9999', str(arrUplinkPort[j][0]))
                strCodeUplinkPort = strCodeUplinkPort.replace('7777', desUplinkPort)
            else:
                strCodeUplinkPort = strCodeUplinkPort + 'interface range gigabitethernet 0/0/9999 to gigabitethernet 0/0/8888 \r\n description 7777 \r\n port link-type access \r\n port default vlan 6666\r\n stp disable \r\n stp bpdu-filter enable \r\nquit \r\n'
                strCodeUplinkPort = strCodeUplinkPort.replace('9999', str(arrUplinkPort[j][0]))
                strCodeUplinkPort = strCodeUplinkPort.replace('8888', str(arrUplinkPort[j][-1]))
                strCodeUplinkPort = strCodeUplinkPort.replace('7777', desUplinkPort)
                strCodeUplinkPort = strCodeUplinkPort.replace('6666', uplinkVlan)
            j = j + 1
        return strCodeEdgedPort +strCodeUplinkPort

    def getuplinkport(self,uplinkPort,PortNum):  #获取上联口数组
        uplinkPort = re.findall(r"\d+", uplinkPort)  # 正则表达式d+代表1或多连续的数字
        arr = list(map(int, uplinkPort))  # 字符数组转int数组
        num = int(PortNum)
        j = len(arr)
        i = 0
        while (i < j):
            if (arr[i] > num):
                arr.pop(i)
                i = i - 1
                j = j - 1
            i = i + 1
        arr=sorted(arr)
        return arr

    def codeUplinkPort(self,uplinkPort,PortNum,uplinkVlan,desUplinkPort):
        arr =self.getuplinkport(uplinkPort,PortNum)
        strCodeUplinkPort = ''
        index = 0
        while ( index < len(arr)):
            print (arr[index])
            strtest = 'interface GigabitEthernet 0/0/9999 \r\n description 7777 \r\n port link-type access \r\n port default vlan 8888\r\n stp disable \r\n stp bpdu-filter enable \r\nquit\r\n'
            strtest = strtest.replace('8888', uplinkVlan)
            strtest = strtest.replace('9999', str(arr[index]))
            strtest = strtest.replace('7777', desUplinkPort)
            strCodeUplinkPort = strCodeUplinkPort+strtest
            index = index +1
        print ('uplinkport end')
        return  strCodeUplinkPort

    def codeRoute(self,geteWay):
        if (geteWay==''):
            strCodeRoute=''
        else:
            strCodeRoute = 'ip route-static 0.0.0.0 0.0.0.0 999.999.999.999\r\n'
            strCodeRoute = strCodeRoute.replace('999.999.999.999',geteWay)
        return  strCodeRoute

    def clearCode(self):
        self.textBrowser_Code.setText('')

    def checkSameVlan(self):
        if (self.spinBox_UplinkVlan.text()==self.spinBox_LocalVlan.text()):
            print ('Same Vlan')
            self.lineEdit_DesUplinkVlan.setText(self.lineEdit_DesLocalVlan.text())

    def saveConfiguration(self):
        print (' saveConfiguration')
        # directory1 = QFileDialog.getExistingDirectory(self,"选取文件夹","C:/")  # 起始路径
        # print(directory1)
        # fileName1, filetype = QFileDialog.getOpenFileName(self,"选取文件", "C:/","All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        # print(fileName1, filetype)
        # files, ok1 = QFileDialog.getOpenFileNames(self,"多文件选择","C:/","All Files (*);;Text Files (*.txt)")
        # print(files, ok1)
        fileName,ok = QFileDialog.getSaveFileName(self,"文件保存", "C:/Users/Administrator/Desktop","Text Files (*.txt);;All Files (*)")  #C:\Users\Administrator\Desktop
        #print(str(fileName), str(ok) )
        if (fileName!='' and ok != ''):
            print ('12222222222')
            strCopyCode = self.textBrowser_Code.toPlainText()
            strCopyCode = strCopyCode.replace('\n', '\r\n')
            f = open(fileName, "w")
            f.write(strCopyCode)
            f.close

    def splitEdgedPort(self,uplinkPort,portNum):
        arr = self.getuplinkport(uplinkPort,portNum)
        num = list(range(1, int(portNum)+1))
        print ('num：')
        print (num)
        # print(num[10:20])
        # print(num[10:11])
        arredged = []
        i = 0
        arrstart=0
        while ( i <len(arr)):
            #print(arr[i])
            if (arrstart != arr[i]-1):
                arredged.append(num[arrstart:arr[i]-1])
            arrstart = arr[i]
            i = i + 1
        print ('NUm:',portNum)
        print('arr',arr[-1])
        if (arr[-1] != int(portNum)):
            arredged.append(num[arr[-1]:int(portNum)])
        return  arredged

    def splitUplinkPort(self,uplinkPort,portNum):
        lst = self.getuplinkport(uplinkPort, portNum)  # 连续数字
        print(lst)
        arruplink = []
        fun = lambda x: x[1] - x[0]
        for k, g in groupby(enumerate(lst), fun):
            list1 = []
            l1 = [j for i, j in g]  # 连续数字的列表
            if len(l1) > 1:
                # scop = str(min(l1)) + '-' + str(max(l1))  # 将连续数字范围用"-"连接
                list1.append(min(l1))
                list1.append(max(l1))
            else:
                #scop = l1[0]
                list1.append(l1[0])
            # print("连续数字范围：{}".format(scop))
            arruplink.append(list1)
        return arruplink

 #定义槽函数
    def setTest(self):
        print (123)
        #self.lineEdit_IP.setText("hello world")
        print(self.lineEdit_Gateway.text())
        print(self.spinBox_PortNum.text())
        print(self.comboBox_Mask.currentIndex())
        print(self.comboBox_Mask.currentText())
        #print(self.listWidget.selectedItems())
        #print(self.listWidget.currentItem())
        #self.listWidget.addItem(self.lineEdit_UplinkPort.text())  #添加
        #print(self.listWidget.item(1).text())  #获取Item中的内容
        print (self.checkBox_Telnet.text())
        print(self.checkBox_Ssh.isChecked())
        print (self.codeAAA('True','True','wlkadmin','Sznet@789'))
        #print (self.codeSSH('wlkadmin','True'))

        print (self.codeCreatVlanif('10','192.168.1.1','255.255.255.0','10','Loacl vlan','Uplink Vlan'))
        #print(self.codeEdgedPort('24','20','20'))
        print(self.codeUplinkPort('123，,013,223.4','24','10','Uplink Port'))
        print(self.codeRoute('192.168.1.254'))
        #print(self.codeDefault('123'))
        print(self.spinBox_PortNum.text())
        print(self.spinBox_LocalVlan.text())
        print(self.spinBox_UplinkVlan.text())
        #print (self.checkIP(self.lineEdit_IP.text()))
        print(self.splitEdgedPort('4,35 45 49 5 ','52'))
        #print(self.splitUplinkPort('4,49,50,52','52'))
        #print(self.codePortSimplify('24','10','10 23,24','10','tet'))

app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())
#        self.setFixedSize(self.width(), self.height())
#      (在terminal中输入可以生成exe文件)pyinstaller -F -w test.py