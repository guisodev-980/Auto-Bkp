from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QFrame, QHBoxLayout, QVBoxLayout, QGridLayout
from PySide6.QtGui import QGuiApplication, Qt, QIcon, QPixmap, QColor

class Exit_msg(QWidget):
    def ui_exit_screen(self):
        self.setWindowIcon(QIcon("imgs/icons/alerta.png"))
        self.setWindowTitle("Alerta!")
        self.setFixedSize(300,180)
        self.setStyleSheet("background-color: #dae3f1")
        self.center_window()
        
        pmap_msg_ico = QPixmap("imgs/icons/alerta.png")
        
        #Labels
        self.lbl_message_1 = QLabel("Sair do Programa")
        self.lbl_message_1.setAlignment(Qt.AlignCenter)
        
        self.lbl_message_1.setStyleSheet("font-size: 12pt")
        self.lbl_message_2 = QLabel("interromperá suas funções!")
        self.lbl_message_2.setAlignment(Qt.AlignCenter)
        
        self.lbl_message_2.setStyleSheet("font-size: 12pt")
        self.lbl_msg_ico = QLabel()
        self.lbl_msg_ico.setFixedSize(50,50)
        self.lbl_msg_ico.setPixmap(pmap_msg_ico)
        self.lbl_msg_ico.setScaledContents(True)
        self.lbl_msg_confirm = QLabel("O que deseja Fazer?")

        #Buttons
        self.btn_cancel = QPushButton("Cancelar")
        self.btn_cancel.setIcon(QIcon("imgs/icons/delete.svg"))
        self.btn_cancel.setStyleSheet("color: white;  background-color: #3D7A84")
        self.btn_cancel.clicked.connect(self.msg_close)

        self.btn_exit = QPushButton("Sair")
        self.btn_exit.setIcon(QIcon("imgs/icons/exit.svg"))
        self.btn_exit.setStyleSheet("color: white;  background-color: #3D7A84")

        self.btn_close = QPushButton("Fechar")
        self.btn_close.setIcon(QIcon("imgs/icons/close.svg"))
        self.btn_close.setStyleSheet("color: white;  background-color: #3D7A84")

        self.frm_message = QFrame()
        self.frm_message.setStyleSheet("background-color: #dae3f1; border-radius: 15px;")
        self.frm_msg_confi = QFrame()
        self.frm_msg_confi.setStyleSheet("background-color: #dae3f1; border-radius: 15px;")
        self.frm_msg_btns = QFrame()
        self.frm_msg_btns.setStyleSheet("background-color: #dae3f1; border-radius: 15px;")

        self.layout_setup()
    
    def layout_setup(self):

        #Messages
        g_layout_msg = QGridLayout()
        g_layout_msg.addWidget(self.lbl_msg_ico, 0, 0, 2, 1, alignment=Qt.AlignCenter)
        g_layout_msg.addWidget(self.lbl_message_1, 0, 1, alignment=Qt.AlignLeft)
        g_layout_msg.addWidget(self.lbl_message_2, 1, 1, alignment=Qt.AlignLeft)
        self.frm_message.setLayout(g_layout_msg)

        h_layout_msg_confi = QHBoxLayout()
        h_layout_msg_confi.addWidget(self.lbl_msg_confirm)
        self.frm_msg_confi.setLayout(h_layout_msg_confi)

        h_layout_msg_btns = QHBoxLayout()
        h_layout_msg_btns.addWidget(self.btn_cancel)
        h_layout_msg_btns.addWidget(self.btn_close)
        h_layout_msg_btns.addWidget(self.btn_exit)
        self.frm_msg_btns.setLayout(h_layout_msg_btns)

        v_layout_lbls = QVBoxLayout()
        v_layout_lbls.addWidget(self.frm_message)
        v_layout_lbls.addWidget(self.frm_msg_confi)
        v_layout_lbls.addWidget(self.frm_msg_btns)
        
        #Buttons
        h_layout_btns = QHBoxLayout()
        h_layout_btns.addWidget(self.btn_cancel)
        h_layout_btns.addWidget(self.btn_close)
        h_layout_btns.addWidget(self.btn_exit)

        #Main Layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(v_layout_lbls)
        main_layout.addLayout(h_layout_btns)
        self.setLayout(main_layout)

    def center_window(self):
        desktop = QGuiApplication.primaryScreen().availableGeometry()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

    def msg_close(self):
        self.close()
        
