import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtOpenGL
from GraphGuiClasses import GraphScene
import numpy as np
import random
from collections import defaultdict

##########################################################################################################################    
#THE MAIN GUI
##########################################################################################################################    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 80, 31, 31))
        self.textEdit.setObjectName("lineEdit")
        self.textEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 80, 31, 31))
        self.textEdit_2.setObjectName("lineEdit_2")
        self.textEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(160, 80, 31, 31))
        self.textEdit_3.setObjectName("lineEdit_3")
        self.textEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(230, 80, 31, 31))
        self.textEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 120, 241, 21))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 60, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 60, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.QTextEdit_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.QTextEdit_1.setGeometry(QtCore.QRect(10, 170, 281, 281))
        self.QTextEdit_1.setObjectName("QTextEdit_1")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QTextEdit_1.setFont(font)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 150, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:red")
        self.label_6.setObjectName("label_6")
        self.label_6.setVisible(False)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(1110, 30, 221, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1180, -10, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 550, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(100, 550, 31, 31))
        self.textEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 530, 47, 13))
        self.label_8.setObjectName("label_8")
        self.textEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(30, 550, 31, 31))
        self.textEdit_6.setObjectName("lineEdit_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 470, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(100, 530, 47, 13))
        self.label_12.setObjectName("label_12")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 590, 180, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:red")
        self.label_9.setObjectName("label_9")
        self.label_9.setVisible(False)
        self.textEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(1210, 60, 31, 31))
        self.textEdit_7.setObjectName("lineEdit_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1190, 70, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1080, 100, 271, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.QTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.QTextEdit.setGeometry(QtCore.QRect(1080, 130, 281, 291))
        self.QTextEdit.setObjectName("QTextEdit")
        self.QTextEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.QTextEdit_3.setGeometry(QtCore.QRect(1070, 540, 281, 111))
        self.QTextEdit_3.setObjectName("QTextEdit_3")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1130, 440, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1090, 480, 171, 21))
        self.label_14.setObjectName("label_14")
        self.textEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(1270, 480, 31, 31))
        self.textEdit_8.setObjectName("lineEdit_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1080, 510, 271, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.graphView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphView.setGeometry(QtCore.QRect(310, 10, 751, 641))
        self.graphView.setObjectName("graphView")
        self.scene=self.MainWindow.graph_scene
        self.graphView.setScene(self.scene)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RWA"))
        self.pushButton.setText(_translate("MainWindow", "ADD A REQUEUEST"))
        self.label.setText(_translate("MainWindow", "NODE1"))
        self.label_2.setText(_translate("MainWindow", "NODE2"))
        self.label_3.setText(_translate("MainWindow", "FROM"))
        self.label_4.setText(_translate("MainWindow", "DURATION"))
        self.label_5.setText(_translate("MainWindow", "REQUESTS"))
        self.label_6.setText(_translate("MainWindow", "NONEXISTANT NODE!!"))
        self.comboBox.setItemText(0, _translate("MainWindow", "all paths"))
        self.comboBox.setItemText(1, _translate("MainWindow", "k shortest paths"))
        self.comboBox.setItemText(2, _translate("MainWindow", "shortest path"))
        self.label_7.setText(_translate("MainWindow", "PATHS"))
        self.pushButton_3.setText(_translate("MainWindow", "DELETE"))
        self.label_8.setText(_translate("MainWindow", "NODE1"))
        self.label_10.setText(_translate("MainWindow", "DELETE A  REQUEST"))
        self.label_12.setText(_translate("MainWindow", "NODE2"))
        self.label_9.setText(_translate("MainWindow", "NONEXISTANT REQUEST!!"))
        self.label_11.setText(_translate("MainWindow", "K:"))
        self.pushButton_2.setText(_translate("MainWindow", "SHOW PATHS"))
        self.label_13.setText(_translate("MainWindow", "OPTIMISATION"))
        self.label_14.setText(_translate("MainWindow", "THE MAXIMUM OF WAVELENGHTS:"))
        self.pushButton_4.setText(_translate("MainWindow", "OPTIMISE"))
##########################################################################################################################
#DEFINITION OF FUNCTIONS
##########################################################################################################################    
    def save(self):
        (nodes, edges) = self.MainWindow.switch_graph_type()
        global flag
        f=open("nodes.txt","a")
        for i in nodes:
            f.write(i+"\n")
        f.close()
        
        f=open("edges.txt","a")
        for i,j in edges:
            f.write(i+'-'+j+"\n")
            f.write(j+'-'+i+"\n")
        f.close()
        
        f=open("nodes.txt","r")
        ln=f.readlines()
        f.close()
        f1=open('requests.txt','r')
        nb=len(f1.readlines())
        node1=self.textEdit.text()
        node2=self.textEdit_2.text()
        if (node1+"\n") in ln and (node2+"\n") in ln:
            flag=True
        else:
            flag=False
        frm=int(self.textEdit_3.text())
        dur=int(self.textEdit_4.text())
        fin=frm+dur
        f1.close()
        if flag:
            with open("requests.txt","a") as f:
                f.write("Request: "+str(node1)+" --> "+str(node2)+" from:t= "+str(frm)+" ,to:t= "+str(fin))
                f.write("\n")
                f.close()
            f1=open('requests.txt','r')
            text1=f1.readlines()[-1]
            self.QTextEdit_1.append(text1)
            f1.close()
            self.textEdit.clear()
            self.textEdit_2.clear()
            self.textEdit_3.clear()
            self.textEdit_4.clear()
            self.label_6.setVisible(False)
        else:
            self.label_6.setVisible(True)
    
    def delete(self):
        node1=int(self.textEdit_6.text())
        node2=int(self.textEdit_5.text())        
        f1=open('requests.txt','r')
        global lines
        lines=f1.readlines()
        print(lines)
        global nb
        nb=len(lines)
        global n1
        global n2
        n1=[]
        n2=[]
        k=0
        for i in range(nb):
            if lines[i] !="\n":
                n1.append(int(lines[i].split(" ")[1]))
                n2.append(int(lines[i].split(" ")[3]))
            else:
                k+=1
        print(n1)
        print(n2)
        if node1 in n1 and node2 in n2:
            self.label_9.setVisible(False) 
        else:
            self.label_9.setVisible(True) 
        for i in range(nb-k):
            if n1[i]==node1 and n2[i]==node2:
                lines.pop(i)
                self.QTextEdit_1.clear()
                self.textEdit_6.clear()
                self.textEdit_5.clear()
        f1.close()
        
        with open("requests.txt","w") as f:        
            for i in range(len(lines)):
                if lines[i] !="\n":
                    f.write(lines[i])
                    f.write("\n")
            f.close()
            f1=open('requests.txt','r')
            text1=f1.read()
            self.QTextEdit_1.append(text1)
            f1.close()
            
##########################################################################################################################
#GENERATING MATRIXES
##########################################################################################################################  
    def createmat(self):
        ###########################################################################
        #the matrix of the Graph
        ###########################################################################
        f=open("nodes.txt",'r')
        ln1=f.readlines()
        nbn=len(ln1)
        ln2=[]
        for i in ln1:
            ln2.append(i.strip("\n"))
        f.close()
        M=np.zeros([nbn,nbn])
        f=open("edges.txt","r")
        le=f.readlines()
        nd=[]
        nf=[]
        for i in le:
            nd.append(i.split('-')[0])
            nf.append(i.strip("\n").split('-')[1])
        for i in range(len(nd)):
            x=ln2.index(nd[i])
            y=ln2.index(nf[i])
            M[x][y]=1
        f.close()
        ###########################################################################
        #matrix of connection requestes
        ###########################################################################
        dcij=np.zeros([nbn,nbn])
        f=open("requests.txt","r")
        global lr
        lr=f.readlines()
        ndr=[]
        nfr=[]
        for i in lr:
            if i !="\n":
                ndr.append(i.split(' ')[1])
                nfr.append(i.split(' ')[3])
        for i in range(len(ndr)):
            x=ln2.index(ndr[i])
            y=ln2.index(nfr[i])
            dcij[x][y]=1
        f.close()
        
        ###########################################################################
        #all possibilities for each request 
        ###########################################################################
        s=np.count_nonzero(np.tril(M) == 1)
        global g
        g=Graph(s)
        for i in range(len(M)):
        	for j in range(len(M)):
        		if M[i][j]==1:
        			g.addEdge(i+1, j+1) 
        global start
        global fin
        start=[]
        fin=[]
        orig_stdout = sys.stdout
        sys.stdout=open("paths.txt","w")
    
        for i in range(len(dcij)):
            for j in range(len(dcij)):
                if dcij[i][j]==1:
                    s=i+1
                    d=j+1
                    print("Following are all different paths from ",s,"to",d,":")
                    g.printAllPaths(s,d)
                    start.append(s)
                    fin.append(d)
        sys.stdout.close()
        sys.stdout=orig_stdout
        ###########################################################################
        #matrix of possibilities
        ###########################################################################
        global p
        p=[]
        p=g.pathsl()
        print(p)
        global n
        n=len(p)
        print("\n")
        ###########################################################################
        #list of durations
        ###########################################################################
        f=open("paths.txt",'r')
        npaths=(len(f.readlines()))-len(lr)
        f.close()
        if npaths>0:
            durees=np.zeros([npaths,2])
            f=open("requests.txt","r")
            ldur=f.readlines()
            fr=[]
            to=[]
            for i in ldur:
                if i !="\n":
                    fr.append(i.split(' ')[5])
                    to.append(i.split(' ')[7].strip('\n'))
            for j in range(len(ndr)):
                for i in range(npaths):
                    if p[i][0]==int(ndr[j]) and p[i][-1]==int(nfr[j]):
                        durees[i]=[fr[j],to[j]]
            f.close()        
            print("\n",durees)
        ###########################################################################
        #matrix of wavelenght overlap
        ###########################################################################
        print("matrix of wavelenght overlap")
        D=np.zeros([n,n])
        for i in range(n):
        	for k in range(n):
        		for j in range(len(p[k])-1):
        			a,b=p[k][j],p[k][j+1]
        			if p[i].count(a) == 1 and p[i].count(b) == 1:
        				if p[i].index(b) == p[i].index(a)+1:
        					D[i][k]=1
        print("  ",end = " ")
        i = 0                    
        while i < n-1:
            print(i,end = "  ")
            i = i + 1
        print(n-1)	
        for i in range(n):
            if i in range(10):
                print(i,D[i],sep = "  ")
            else:
                print(i,D[i])
        print("\n")
        ###########################################################################
        #matrix of time overlap
        ###########################################################################
        if npaths>0:
            print("matrix of time overlap")
            T = np.zeros([n,n])
            for i in range(len(durees)):
                for j in range(len(durees)):
                    if (-durees[i][1]-durees[j][0]) < 0 and durees[i][0]-durees[j][1] < 0:
                        T[i][j] = 1
            print("  ",end = " ")
            i = 0                    
            while i < n-1:
                print(i,end = "  ")
                i = i + 1
            print(n-1)	
            for i in range(n):
                if i in range(10):
                    print(i,T[i],sep = "  ")
                else:
                    print(i,T[i])
            print("\n")
        #################################################################################################################
        #matrix of paths/time overlap
        #################################################################################################################
        print("****************matrix of paths/time overlap(PT)****************")
        global PT
        PT = np.zeros([n,n])
        for i in range(n):
            for j in range(n):
                PT[i][j] = T[i][j] and D[i][j]
        print("  ",end = " ")
        i = 0                    
        while i < n-1:
            print(i,end = "  ")
            i = i + 1
        print(n-1)	
        for i in range(n):
            if i in range(10):
                print(i,PT[i],sep = "  ")
            else:
                print(i,PT[i])

    def k_createmat(self):
        ###########################################################################
        #the matrix of the Graph
        ###########################################################################
        f=open("nodes.txt",'r')
        ln1=f.readlines()
        nbn=len(ln1)
        ln2=[]
        for i in ln1:
            ln2.append(i.strip("\n"))
        f.close()
        M=np.zeros([nbn,nbn])
        f=open("edges.txt","r")
        le=f.readlines()
        nd=[]
        nf=[]
        for i in le:
            nd.append(i.split('-')[0])
            nf.append(i.strip("\n").split('-')[1])
        for i in range(len(nd)):
            x=ln2.index(nd[i])
            y=ln2.index(nf[i])
            M[x][y]=1
        f.close()
        ###########################################################################
        #matrix of connection requestes
        ###########################################################################
        dcij=np.zeros([nbn,nbn])
        f=open("requests.txt","r")
        global lr
        lr=f.readlines()
        ndr=[]
        nfr=[]
        for i in lr:
            if i !="\n":
                ndr.append(i.split(' ')[1])
                nfr.append(i.split(' ')[3])
        for i in range(len(ndr)):
            x=ln2.index(ndr[i])
            y=ln2.index(nfr[i])
            dcij[x][y]=1
        f.close()
        print(ndr)
        print(nfr)
        ###########################################################################
        #all possibilities for each request 
        ###########################################################################
        s=np.count_nonzero(np.tril(M) == 1)
        global g
        g=Graph(s)
        for i in range(len(M)):
        	for j in range(len(M)):
        		if M[i][j]==1:
        			g.addEdge(i+1, j+1) 
        global start
        global fin
        start=[]
        fin=[]
        for i in range(len(dcij)):
            for j in range(len(dcij)):
                if dcij[i][j]==1:
                    s=i+1
                    d=j+1
                    start.append(s)
                    fin.append(d)
        ###########################################################################
        #matrix of possibilities
        ###########################################################################
        #global p
        #p=[]
        #p=g.pathsl()
        print(p)
        global n
        n=len(p)
        print("\n")
        ###########################################################################
        #list of durations
        ###########################################################################
        f=open("paths.txt",'r')
        npaths=(len(f.readlines()))-len(lr)
        print(npaths)
        f.close()
        if npaths>0:
            durees=np.zeros([npaths,2])
            f=open("requests.txt","r")
            ldur=f.readlines()
            print(ldur)
            fr=[]
            to=[]
            for i in ldur:
                if i !="\n":
                    fr.append(i.split(' ')[5])
                    to.append(i.split(' ')[7].strip('\n'))
            for j in range(len(ndr)):
                for i in range(npaths):
                    if p[i][0]==int(ndr[j]) and p[i][-1]==int(nfr[j]):
                        durees[i]=[fr[j],to[j]]
                        
            print("\n",durees)
        ###########################################################################
        #matrix of wavelenght overlap
        ###########################################################################
        print("matrix of wavelenght overlap")
        D=np.zeros([n,n])
        for i in range(n):
        	for k in range(n):
        		for j in range(len(p[k])-1):
        			a,b=p[k][j],p[k][j+1]
        			if p[i].count(a) == 1 and p[i].count(b) == 1:
        				if p[i].index(b) == p[i].index(a)+1:
        					D[i][k]=1
        print("  ",end = " ")
        i = 0                    
        while i < n-1:
            print(i,end = "  ")
            i = i + 1
        print(n-1)	
        for i in range(n):
            if i in range(10):
                print(i,D[i],sep = "  ")
            else:
                print(i,D[i])
        print("\n")
        ###########################################################################
        #matrix of time overlap
        ###########################################################################
        if npaths>0:
            print("matrix of time overlap")
            global T
            T = np.zeros([n,n])
            for i in range(len(durees)):
                for j in range(len(durees)):
                    if (-durees[i][1]-durees[j][0]) < 0 and durees[i][0]-durees[j][1] < 0:
                        T[i][j] = 1
            print("  ",end = " ")
            i = 0                    
            while i < n-1:
                print(i,end = "  ")
                i = i + 1
            print(n-1)	
            for i in range(n):
                if i in range(10):
                    print(i,T[i],sep = "  ")
                else:
                    print(i,T[i])
            print("\n")
        #################################################################################################################
        #matrix of paths/time overlap
        #################################################################################################################
        print("****************matrix of paths/time overlap(PT)****************")
        global PT
        PT = np.zeros([n,n])
        for i in range(n):
            for j in range(n):
                PT[i][j] = T[i][j] and D[i][j]
        print("  ",end = " ")
        i = 0                    
        while i < n-1:
            print(i,end = "  ")
            i = i + 1
        print(n-1)	
        for i in range(n):
            if i in range(10):
                print(i,PT[i],sep = "  ")
            else:
                print(i,PT[i])
##########################################################################################################################
#DISPLAY PATHS
##########################################################################################################################  
    def affiche_paths(self):
        if str(self.comboBox.currentText())=="all paths":
            self.createmat()
        else:
            #self.k_createmat()
            self.k_ShortestPath()
            self.k_createmat()
        f=open('paths.txt','r')
        text=f.read()
        self.QTextEdit.clear()
        self.QTextEdit.append(text)
        f.close()
##########################################################################################################################
#RANDOM FUNCTIONS
##########################################################################################################################  
    def randpaths(self):
        x=[]
        l=0
        #print("prand:",p)
        for j in start:
            temp=[]
            h=fin[l]
            l=l+1
            for i in range(len(p)):
                if p[i][0]==j and p[i][-1]==h:
                    temp.append(p[i])
            k=random.randint(0,len(temp)-1)
            x.append(temp[k])
        return x
    
    def wavelenghts(self):
        #global rp
        #½rp=self.randpaths()
        ind=[]
        for i in rp:
            ind.append(p.index(i)) 
        global colors
        colors = []
        global nbr_colors
        nbr_colors=int(self.textEdit_8.text())
        for i in range(nbr_colors):
            colors.append([])  
        for i in ind:
            k = 0
            while k < len(colors):
                if len(colors[k]) == 0:
                    colors[k].append(i)
                    break
                else:
                    s1 = 0
                    for j in colors[k]:
                        #s1=0
                        s1 = s1 + PT[i][j]
                    if s1 == 0:
                        colors[k].append(i) 
                        break
                    else:
                        k = k + 1 
    
    #################################################################################################################
    #wavelenghts(colors) result 
    #################################################################################################################
    def wavelenghts_result(self):

        #for i in range(len(colors)):
            #print("paths have color" + str(i + 1) + ":",colors[i])
            #print("\n")        
        orig_stdout = sys.stdout
        sys.stdout=open("optimisation.txt","w")
        for i in range(len(rp)):
            print("R"+str(i+1),": ",end = " ")
            print(*rp[i],sep=" -> ",end="   ")
            j = 0
            while j < len(colors):
                if p.index(rp[i]) not in colors[j]:
                    j = j + 1
                    if j == len(colors) and p.index(rp[i]) not in colors[j-1]:
                        print("(wave lenght: none)")
                else:
                    print("(wave lenght: " + str(colors.index(colors[j]) + 1) + ")")
                    break
        global nbr_c_used
        for c in colors:
            if len(c) == 0:
                nbr_c_used = colors.index(c)
                print("the number of wave lenghts used: "+str(nbr_c_used)+"/"+str(nbr_colors))
                break
        if len(c) != 0: 
            nbr_c_used = len(colors)
            print("the number of wave lenghts used: "+str(nbr_c_used)+"/"+str(nbr_colors))
        global rate
        rate = 0
        for c in colors:
            rate = rate + len(c)
        print("the result of the optimisation: " + str(rate) + "/" + str(len(rp)))
        sys.stdout.close()   
        sys.stdout=orig_stdout
        
##########################################################################################################################
#OPTIMISATION FUNCTION
##########################################################################################################################       
    def optimise(self):
        print("*******************the best optimisation result******************")
        iteration =3000
        i = 0
        global rp
        while i < iteration:
            rp = self.randpaths()
            self.wavelenghts()
            self.wavelenghts_result()
            #i =i+1
            print(i)
            if rate >= len(rp) and nbr_c_used <= nbr_colors:
                print("********************************optimisation result************************")
                print("the best result is:")
                self.wavelenghts_result()
                break
            i = i + 1
        f=open('optimisation.txt','r')
        text=f.read()
        self.QTextEdit_3.clear()
        self.QTextEdit_3.append(text)
        f.close()
    
    
    #################################################################################################################
    #k-shortest path
    #################################################################################################################
    def k_ShortestPath(self):
        global x
        x = []
        global opt
        opt=str(self.comboBox.currentText())
        if opt=="k shortest paths":
            k=int(self.textEdit_7.text())
        elif opt=="shortest path":
            k=1
        
        global p
        p = []
        y=g.pathsl()
        n=len(y)
        l=0
        for j in start:
            temp=[]
            h=fin[l]
            l=l+1
            for i in range(n):
                if y[i][0]==j and y[i][-1]==h:
                    temp.append(y[i])
            x.append(temp)
            
        
        for m in range(len(x)):
            for i in range(k):
                for j in range(i + 1,len(x[m])):
                    if len(x[m][j]) < len(x[m][i]):
                        x[m][j],x[m][i] = x[m][i],x[m][j]
        for sl in x:
            for i in range(k):
                p.append(sl[i])
        print(p)
        
        global st
        global fn
        st=[]
        fn=[]
        
        orig_stdout = sys.stdout
        sys.stdout=open("paths.txt","w")
        for i in p:
            s=i[0]
            d=i[-1]
            st.append(s)
            fn.append(d)
            if i ==p[0]:
                print("Following are all different paths from ",s,"to",d,":")
            else:
                if s !=st[-2] or d !=fn[-2]:
                    print("Following are all different paths from ",s,"to",d,":")
            print(*list(i),sep=" -> ")
        sys.stdout.close()
        sys.stdout=orig_stdout
        
        self.textEdit_7.clear()
    
##########################################################################################################################
#DRAWING GRAPH FUNCTIONS
##########################################################################################################################  
    def change_graph_type(self):

        _translate = QtCore.QCoreApplication.translate
        (nodes, edges) = self.MainWindow.switch_graph_type() # switch graph type and get previously used nodes and edges from old graph
        self.setupUi(self.MainWindow) # reset the UI with the modified MainWindow 
        if self.scene.digraph: # if changed to digraph
            self.switch_graph_btn.setText(_translate("MainWindow", "TO GRAPH")) # button to change to graph
        else: 
            self.switch_graph_btn.setText(_translate("MainWindow", "TO DIGRAPH")) # button to change to digraph
        
        for node_val, node in nodes.items(): # for each node that was in the original graph
            node.selected = False 
            node.highlighted = False # remove higlights or selctions
            self.scene.addItem(node) # add the node to the windows graph scene
            self.scene.nodes[node_val] = node  # add the node to the scene's dictionary
            self.scene.graph.add_node(node_val) # add the node to the scene's underlying graph

        for (from_node, to_node), edge in edges.items(): # for each edge in the original graph
            self.scene.add_edge(from_node, to_node, edge.weight) # add it to the new graph
            if self.scene.digraph: # if changed from graph to digraph
                self.scene.add_edge(to_node, from_node, edge.weight) # add edges in both directions
        
 
    def edit_path_algorithm(self):

        # when algorithm combo box is edited reset the graph scenes current algorithm
        self.scene.current_path_algo = self.select_path_alg_comboBox.currentText()


    def update_data(self):
        # function is called when signel is sent indicating the graph has been updated 
        _translate = QtCore.QCoreApplication.translate

        if self.scene.path_displayed[0]: # if a path is being displayed indicate that it is and fill in relavent data from graph 
            self.path_shown_yes_no.setText(_translate("MainWindow", "YES"))   
            self.node1_val_lab.setText(_translate("MainWindow", str(self.scene.path_displayed[1])))
            self.node2__val_lab.setText(_translate("MainWindow", str(self.scene.path_displayed[2])))
            self.dist_val_lab.setText(_translate("MainWindow", str(self.scene.path_displayed[3])))
        else: # if no path indicate that nothing is shown
            self.path_shown_yes_no.setText(_translate("MainWindow", "NO"))
            self.node1_val_lab.setText(_translate("MainWindow", "N/A"))
            self.node2__val_lab.setText(_translate("MainWindow", "N/A"))
            self.dist_val_lab.setText(_translate("MainWindow", "N/A"))

        # set label to indicate if graph is connected
        if self.scene.graph.is_connected(): self.graph_status.setText(_translate("MainWindow", "YES"))
        else: self.graph_status.setText(_translate("MainWindow", "NO"))

        #show the current number of edges and nodes in graph
        self.num_nodes_val.setText(_translate("MainWindow", str(len(self.scene.nodes))))
        self.num_edges_val.setText(_translate("MainWindow", str(len(self.scene.edges))))

class SceneConnectedComboBox(QtWidgets.QComboBox):

    def __init__(self, widget, graph_scene):
        super().__init__(widget) # initialize a combo box as part of input widget
        self.scene = graph_scene # include a graph scene reference in combobox 

    
    def keyPressEvent(self, event):
        self.scene.keyPressEvent(event) # if the combobox is selected and a key is pressed send event to graph scene
          
         

class MainGraphWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # initialize the main window of the GUI
        super().__init__()
        self.graph_scene = GraphScene(True) # initialize it with a graph scene
        self.app = QtWidgets.QApplication([])
        self.screen_resolution = app.desktop().screenGeometry()
        self.width = self.screen_resolution.width()
        self.height = self.screen_resolution.height()  

    def switch_graph_type(self):
        
        edges = self.graph_scene.edges
        nodes = self.graph_scene.nodes
        digraph = not self.graph_scene.digraph
        
        self.graph_scene = GraphScene(digraph)

        
        return ((nodes, edges))

##########################################################################################################################
#THE GRAPH CLASS
##########################################################################################################################  
class Graph: 
        global pathslist
        pathslist=[]
        def __init__(self,vertices):  
            self.V= vertices  
            self.graph = defaultdict(list)  
        def addEdge(self,u,v): 
            self.graph[u].append(v) 
            
        def printAllPathsUtil(self, u, d, visited, path): 
            visited[u]= True
            path.append(u) 
            if u == d: 
                print(*list(path),sep=" -> ")
                if list(path) not in pathslist:
                    pathslist.append(list(path))
            else: 
                for i in self.graph[u]: 
                    if visited[i]==False: 
                        self.printAllPathsUtil(i, d, visited, path) 
            
            path.pop() 
            visited[u]= False
        def printAllPaths(self,s, d): 
            visited =[False]*(self.V) 
            path = [] 
            self.printAllPathsUtil(s, d,visited, path)
        def pathsl(self):
            return pathslist


##########################################################################################################################
#THE MAIN BLOCK
##########################################################################################################################  
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainGraphWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    f=open('optimisation.txt','w')
    f.close()
    f=open("paths.txt","w")
    f.close()
    ui.pushButton_2.clicked.connect(ui.affiche_paths)
    f=open("edges.txt","w")
    f.close()
    f=open("nodes.txt","w")
    f.close()
    f1=open('requests.txt','w')
    f1.close()    
    ui.pushButton.clicked.connect(ui.save)
    ui.pushButton.clicked.connect(ui.createmat)
    ui.pushButton_4.clicked.connect(ui.optimise)
    ui.pushButton_3.clicked.connect(ui.delete)
    sys.exit(app.exec_())
    
    
