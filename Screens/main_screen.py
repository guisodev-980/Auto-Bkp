from PySide6.QtWidgets import QWidget, QLabel, QCheckBox, QPushButton, QFrame, QSizePolicy, QLineEdit, QTreeWidget, QVBoxLayout, QGridLayout, QHBoxLayout, QSpinBox, QRadioButton
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QGuiApplication, QCursor, QIcon, QPixmap, QColor

class Main_Screen(QWidget):

    ICON_PATH = "imgs/icons/"

    def ui_main_screen(self):
        self.setWindowIcon(QIcon("imgs/logo_light.png"))
        self.setWindowTitle("Auto Backup")
        self.center_window()
        self.setup_labels()
        self.setup_texts()
        self.setup_btns()
        self.setup_misc()
        self.setup_frame()
        self.setup_layout()
        
    def setup_labels(self):

        style_font_sub_title = "font-size: 14pt"
        
        pmap_logo_comp = QPixmap("imgs/logo_light_comp.png")
        
        self.lbl_title = QLabel()
        self.lbl_title.setFixedSize(300,100)
        self.lbl_title.setObjectName("s_lbl_title")
        self.lbl_title.setPixmap(pmap_logo_comp)
        self.lbl_title.setScaledContents(True)
        self.resize(pmap_logo_comp.width(), pmap_logo_comp.height())
        
        self.lbl_schedule_list = QLabel("Agendados")
        self.lbl_schedule_list.setAlignment(Qt.AlignCenter)
        self.lbl_schedule_list.setStyleSheet(style_font_sub_title)

        self.lbl_schedule_time = QLabel("Horário")
        self.lbl_schedule_time.setAlignment(Qt.AlignCenter)
        self.lbl_schedule_time.setStyleSheet(style_font_sub_title)
        
        self.txt_schedule_time = QLineEdit()
        self.txt_schedule_time.setPlaceholderText("Configure um Horário")

        self.lbl_orig_path = QLabel("Origem")
        self.lbl_orig_name = QLabel("Nome")

        self.lbl_dest_path = QLabel("Destino")
        self.lbl_dest_path.setAlignment(Qt.AlignCenter)
        self.lbl_dest_path.setStyleSheet(style_font_sub_title)

        self.lbl_compac_format = QLabel("Formato")
        self.lbl_compac_format.setAlignment(Qt.AlignCenter)
        self.lbl_compac_format.setStyleSheet(style_font_sub_title)
        self.lbl_time_hour = QLabel("Horas")
        self.lbl_time_hour.setAlignment(Qt.AlignCenter)
        self.lbl_time_min = QLabel("Min")
        self.lbl_time_min.setAlignment(Qt.AlignCenter)

        self.lbl_ckb_shutdown = QLabel("Desligar\nApós Backup")
        self.lbl_ckb_shutdown.setObjectName("s_lbl_ckb_shutdown")
        self.lbl_ckb_shutdown.setAlignment(Qt.AlignCenter)

        self.lbl_ckb_start = QLabel("Iniciar junto \nao Windows")
        self.lbl_ckb_start.setObjectName("s_lbl_ckb_start")
        self.lbl_ckb_start.setAlignment(Qt.AlignCenter)
    
    def setup_texts(self):

        self.txt_orig_path = QLineEdit()
        self.txt_orig_path.setObjectName("s_txt_orig_path")
        self.txt_orig_path.setPlaceholderText("Selecione Diretório de Origem")
        self.txt_orig_path.setEnabled(False)
        self.txt_orig_name = QLineEdit()
        self.txt_orig_name.setPlaceholderText("Digite um Nome para Salvar")
        
        self.txt_dest_path = QLineEdit()
        self.txt_dest_path.setPlaceholderText("Configurar Diretório de Destino")
        self.txt_dest_path.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def setup_btns(self):

        self.btn_theme = QPushButton()
        self.btn_theme.setFixedSize(25,25)
        self.btn_theme.setObjectName("s_btn_theme")
        self.btn_theme.setCheckable(True)
        self.btn_theme.setIconSize(QSize(30,30))
        self.btn_theme.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_save_config = QPushButton("Confirmar")
        self.btn_save_config.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.btn_save_config.setIcon(QIcon(f"{self.ICON_PATH}check_small.svg"))
        
        self.btn_search_orig = QPushButton("Buscar")
        self.btn_search_orig.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.btn_search_orig.setIcon(QIcon(f"{self.ICON_PATH}search_origin.svg"))

        self.btn_search_dest = QPushButton("Buscar")
        self.btn_search_dest.setToolTip("Escolhe pasta de destino")
        self.btn_search_dest.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.btn_search_dest.setIcon(QIcon(f"{self.ICON_PATH}search_dest.svg"))

        self.btn_edit_config = QPushButton("Editar")
        self.btn_edit_config.setToolTip("Edita configurações de Saída")
        self.btn_edit_config.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.btn_edit_config.setIcon(QIcon(f"{self.ICON_PATH}edit.svg"))
        
        self.btn_save_folder = QPushButton("Salvar")
        self.btn_save_folder.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.btn_save_folder.setIcon(QIcon(f"{self.ICON_PATH}save-origin.svg"))
        
        self.btn_schedule_del = QPushButton("Excluir")
        self.btn_schedule_del.setToolTip("Exclui Paste de Origem Selecionada")
        self.btn_schedule_del.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.btn_schedule_del.setIcon(QIcon(f"{self.ICON_PATH}delete.svg"))
        
        self.btn_bkp_now = QPushButton("Fazer Backup")
        self.btn_bkp_now.setToolTip("Executa Rotina de Bakup")
        self.btn_bkp_now.setIcon(QIcon(f"{self.ICON_PATH}bkp_now.svg"))
        self.btn_bkp_now.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        self.btn_exit = QPushButton("Sair")
        self.btn_exit.setIcon(QIcon(f"{self.ICON_PATH}exit.svg"))
        self.btn_exit.setToolTip("Sai do Sistema e interrompe suas funções")
        self.btn_exit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.btn_close = QPushButton("Fechar")
        self.btn_close.setToolTip("Fecha a janela e mantém as funções de backup")
        self.btn_close.setIcon(QIcon(f"{self.ICON_PATH}close.svg"))
        self.btn_close.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)


    def setup_misc(self):

        self.lst_schedule_list = QTreeWidget()
        self.lst_schedule_list.setIndentation(0)
        self.lst_schedule_list.setObjectName("s_lst_schedule_list")
        self.lst_schedule_list.setHeaderLabels(["Nome", "Caminho"])
        
        self.spn_hour = QSpinBox()
        self.spn_hour.setAlignment(Qt.AlignCenter)
        self.spn_hour.setRange(0, 23)
        self.spn_hour.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.spn_min = QSpinBox()
        self.spn_min.setAlignment(Qt.AlignCenter)
        self.spn_min.setRange(0,59)
        self.spn_min.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.rbt_format_zip = QRadioButton("Zip")
        self.rbt_format_rar = QRadioButton("Rar")

        self.ckb_shutdown = QCheckBox()
        self.ckb_shutdown.setObjectName("s_ckb_shutdown")
        self.ckb_start = QCheckBox()
        self.ckb_start.setObjectName("s_ckb_start")
        

        #Frames
        
        
        self.frm_header = QFrame()
        self.frm_header.setObjectName("s_frm_header")
        self.frm_btn_theme = QFrame()
        self.frm_btn_theme.setFixedSize(45,45)
        self.frm_btn_theme.setObjectName("s_frm_btn_theme")
        self.frm_config_path = QFrame()
        self.frm_config_path.setObjectName("s_frm_config_path")
        self.frm_config_time = QFrame()
        self.frm_config_time.setObjectName("s_frm_config_time")
        self.frm_config_format = QFrame()
        self.frm_config_format.setObjectName("s_frm_config_format")
        self.frm_schedule_list = QFrame()

        self.frm_functions = QFrame()
        self.frm_functions.setObjectName("s_frm_function")
        self.frm_start = QFrame()
        self.frm_start.setObjectName("s_frm_start")
        self.frm_shutdown = QFrame()
        self.frm_shutdown.setObjectName("s_frm_shutdown")
        self.frm_shutdown.setToolTip("Desliga o Computador após execultar o backup")
        self.frm_dir_path = QFrame()
        self.frm_btns = QFrame()

    def setup_frame(self):
        
        #Theme Button Frame
        h_layout_frm_btn_theme = QHBoxLayout()
        h_layout_frm_btn_theme.setContentsMargins(0,0,0,0)
        h_layout_frm_btn_theme.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        h_layout_frm_btn_theme.addWidget(self.btn_theme)
        self.frm_btn_theme.setLayout(h_layout_frm_btn_theme)

        #Header Frame
        h_layout_frm_header = QHBoxLayout()
        h_layout_frm_header.addWidget(self.lbl_title, alignment=Qt.AlignLeft)
        h_layout_frm_header.addWidget(self.frm_btn_theme, alignment=Qt.AlignRight | Qt.AlignCenter)
        self.frm_header.setLayout(h_layout_frm_header)

        #Config path Frames
        g_layout_frm_config_path = QGridLayout()
        g_layout_frm_config_path.addWidget(self.lbl_dest_path, 0, 0, 1, 4)
        g_layout_frm_config_path.addWidget(self.txt_dest_path, 1, 0, 1, 4)
        g_layout_frm_config_path.addWidget(self.btn_edit_config, 2, 0)
        g_layout_frm_config_path.addWidget(self.btn_search_dest, 2, 1)
        g_layout_frm_config_path.addWidget(self.btn_save_config, 2 ,2)
        self.frm_config_path.setLayout(g_layout_frm_config_path)
        
        #Config time Frames
        g_layout_frm_config_time = QGridLayout()
        g_layout_frm_config_time.addWidget(self.lbl_schedule_time, 0, 0, 1, 2)
        g_layout_frm_config_time.addWidget(self.lbl_time_hour, 2, 0)
        g_layout_frm_config_time.addWidget(self.lbl_time_min, 2, 1)
        g_layout_frm_config_time.addWidget(self.spn_hour, 1, 0)
        g_layout_frm_config_time.addWidget(self.spn_min, 1, 1)
        self.frm_config_time.setLayout(g_layout_frm_config_time)

        #Config Format Frames
        v_layout_frm_config_format = QVBoxLayout()
        v_layout_frm_config_format.addWidget(self.lbl_compac_format, alignment=Qt.AlignCenter)
        v_layout_frm_config_format.addWidget(self.rbt_format_rar, alignment=Qt.AlignCenter)
        v_layout_frm_config_format.addWidget(self.rbt_format_zip, alignment=Qt.AlignCenter)
        self.frm_config_format.setLayout(v_layout_frm_config_format)        

        #New Folder Frame
        g_layout_frm_new_folder = QGridLayout()
        g_layout_frm_new_folder.addWidget(self.lbl_orig_path, 0, 0, 1, 2)
        g_layout_frm_new_folder.addWidget(self.txt_orig_path, 1, 0, 1, 2)
        g_layout_frm_new_folder.addWidget(self.btn_search_orig, 1, 3)
        g_layout_frm_new_folder.addWidget(self.lbl_orig_name, 2, 0, 1, 1)
        g_layout_frm_new_folder.addWidget(self.txt_orig_name, 3, 0, 1, 1)
        g_layout_frm_new_folder.addWidget(self.btn_save_folder, 3, 3)
        self.frm_dir_path.setLayout(g_layout_frm_new_folder)

        #Shutdown Check frame
        h_layout_frm_shutdown = QHBoxLayout()
        h_layout_frm_shutdown.addWidget(self.ckb_shutdown, alignment=Qt.AlignCenter)
        h_layout_frm_shutdown.addWidget(self.lbl_ckb_shutdown, alignment=Qt.AlignCenter)
        self.frm_shutdown.setLayout(h_layout_frm_shutdown)

        #Start Check frame
        h_layout_frm_start = QHBoxLayout()
        h_layout_frm_start.addWidget(self.ckb_start, alignment=Qt.AlignCenter)
        h_layout_frm_start.addWidget(self.lbl_ckb_start, alignment=Qt.AlignCenter)
        self.frm_start.setLayout(h_layout_frm_start)

        #Schedule List Frame
        g_layout_frm_schedule_list = QGridLayout()
        self.btn_schedule_del.setMaximumWidth(self.frm_shutdown.width())
        self.btn_bkp_now.setMaximumWidth(self.frm_shutdown.width())
        g_layout_frm_schedule_list.addWidget(self.lbl_schedule_list, 0, 0, 1, 4)
        g_layout_frm_schedule_list.addWidget(self.lst_schedule_list, 1, 0, 3, 4)
        g_layout_frm_schedule_list.addWidget(self.btn_schedule_del, 1, 5)
        g_layout_frm_schedule_list.addWidget(self.btn_bkp_now, 2, 5)
        g_layout_frm_schedule_list.addWidget(self.frm_shutdown, 3, 5, alignment=Qt.AlignCenter)
        self.frm_schedule_list.setLayout(g_layout_frm_schedule_list)

        #Functions Frame
        h_layout_frm_funtions = QHBoxLayout()
        h_layout_frm_funtions.addWidget(self.frm_start, alignment=Qt.AlignLeft)
        h_layout_frm_funtions.addWidget(self.frm_shutdown, alignment=Qt.AlignLeft)
        h_layout_frm_funtions.addWidget(self.frm_btns, alignment=Qt.AlignRight)
        self.frm_functions.setLayout(h_layout_frm_funtions)
        
        #Buttons Frame
        v_layout_frm_btns = QHBoxLayout()
        v_layout_frm_btns.addStretch(3)
        v_layout_frm_btns.addWidget(self.btn_close, alignment=(Qt.AlignRight))
        v_layout_frm_btns.addWidget(self.btn_exit, alignment=(Qt.AlignRight))
        self.frm_btns.setLayout(v_layout_frm_btns)


    def setup_layout(self):
        v_layout_main = QVBoxLayout()
        h_layout_main_config = QHBoxLayout()
        h_layout_main_functions = QHBoxLayout()

        #Config in Main Layout
        h_layout_main_config.addWidget(self.frm_config_path, 3)
        h_layout_main_config.addWidget(self.frm_config_time, 1)
        h_layout_main_config.addWidget(self.frm_config_format, 1)

        #Main Functions Layout

        h_layout_main_functions.addWidget(self.frm_functions)
        h_layout_main_functions.addWidget(self.frm_btns, alignment=Qt.AlignRight)

        #main Layout
        v_layout_main.addWidget(self.frm_header, 1)
        v_layout_main.addLayout(h_layout_main_config, 2)
        v_layout_main.addWidget(self.frm_dir_path, 2)
        v_layout_main.addWidget(self.frm_schedule_list, 3)
        v_layout_main.addLayout(h_layout_main_functions)

        self.setLayout(v_layout_main)

    def center_window(self):
        desktop = QGuiApplication.primaryScreen().availableGeometry()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)