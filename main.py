import sys, os, json, zipfile, winreg
import subprocess
import shutil
import time

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QFileDialog, QTreeWidgetItem, QSystemTrayIcon, QMenu, QWidget
from Screens.main_screen import Main_Screen, QIcon, QSize
from Screens.exit_screen import Exit_msg
from Screens.shut_screen import Shut_msg


class Main:
  
    ICON_PATH = "imgs\\icons\\"    
    data_app_path = os.getcwd()
    file_path = data_app_path + "\\Data\\data.JSON"
    data_theme = ""
    data_hour_schedule = ""
    data_min_schedule = ""
    data_format = ""
    data_dest_path = ""
    data_orig_folder = []
    data_ck_shutdown = ""
    data_ck_start = ""
    date_now = ""

    timer_time = 15
    shut_timer = QTimer()

    def data_read(self):
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.join(self.data_app_path, "Data"), exist_ok=True)

            data = {
                "j_app_path": "",
                "j_theme": "",
                "j_time":"",
                "j_data_format": "",
                "j_dest_path":"",
                "j_data_ck_shutdown":"",
                "j_data_ck_start": "",
                "j_origin_folder": []
                
            }
            with open(self.file_path, "w") as file:
                json.dump(data, file, indent=4)
            
        with open(self.file_path, "r") as file:
            data = json.load(file)

            if data["j_app_path"]:
                self.data_app_path = data["j_app_path"]
            else:
                self.data_app_path = os.getcwd()

            if data["j_time"]:
                self.data_hour_schedule, self.data_min_schedule = data["j_time"].split(":")
            else:
                self.data_hour_schedule, self.data_min_schedule = "15","45"
            
            if shutil.which("rar"):
                self.data_format = data.get("j_data_format") or "rar"
            else:
                self.data_format = "zip"
                self.ui_main.rbt_format_rar.setChecked(False)
                self.ui_main.rbt_format_rar.setEnabled(False)
                self.ui_main.rbt_format_zip.setChecked(True)

            if data["j_data_ck_shutdown"] == "True":
                self.data_ck_shutdown = "True"
                self.ui_main.ckb_shutdown.setChecked(True)
            else:
                self.data_ck_shutdown = "False"
                self.ui_main.ckb_shutdown.setChecked(False)
            
            if data["j_data_ck_start"] == "True":
                self.data_ck_start = "True"
                self.ui_main.ckb_start.setChecked(True)
                
            else:
                self.data_ck_start = "False"
                self.ui_main.ckb_start.setChecked(False)
                
            self.data_theme = data.get("j_theme", "light")
            self.data_orig_folder = data.get("j_origin_folder", [])

            self.data_dest_path = data.get("j_dest_path") or os.getcwd() + "\\Backups"

            if not os.path.exists(self.data_dest_path):
                os.mkdir(self.data_dest_path)


            self.update_data_file(
                j_app_path=self.data_app_path,
                j_time=f"{self.data_hour_schedule}:{self.data_min_schedule}",
                j_data_format=self.data_format,
                j_dest_path=self.data_dest_path,
                j_theme=self.data_theme,
                j_data_ck_shutdown=self.data_ck_shutdown,
                j_data_ck_start=self.data_ck_start
                )
        
    def __init__(self):
        self.ui_main = Main_Screen()
        self.ui_msg = Exit_msg()
        self.ui_shut = Shut_msg()
        self.setup_main_screen()
        self.data_read()
        self.fill_main()
        self.fill_config()
        self.fill_list()
        self.toggle_config(state=False)
        self.setup_theme()
        self.setup_tray_icon()
        self.start_time_monitor()
        

    def setup_main_screen(self):
        self.ui_main.ui_main_screen()
        self.ui_main.show()
        self.ui_main.btn_exit.clicked.connect(self.setup_shut_screen) #self.quit_app
        self.ui_main.btn_search_orig.clicked.connect(self.setup_origin_path)
        self.ui_main.btn_search_dest.clicked.connect(self.setup_dest_path)
        self.ui_main.btn_save_config.clicked.connect(self.save_config)
        self.ui_main.btn_save_folder.clicked.connect(self.save_folder)
        self.ui_main.btn_schedule_del.clicked.connect(self.del_folder)
        self.ui_main.btn_close.clicked.connect(self.app_hide)
        self.ui_main.btn_theme.clicked.connect(self.setup_theme)
        self.ui_main.btn_edit_config.clicked.connect(lambda: self.toggle_config(True))
        self.ui_main.btn_bkp_now.clicked.connect(self.exec_bakup)

    def setup_exit_screen(self):
        self.ui_msg.ui_exit_screen()
        self.ui_msg.show()

    def setup_shut_screen(self):
        self.ui_shut.ui_shut_screen()
        self.ui_shut.show()
        self.ui_shut.btn_cancel.clicked.connect(self.timer_stop)
        

    def update_data_file(self, **kwargs):
        with open(self.file_path, "r") as file:
            data = json.load(file)
        data.update(kwargs)

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def toggle_config(self, state):

        widgets = [
            self.ui_main.btn_save_config, self.ui_main.txt_dest_path,
            self.ui_main.spn_hour, self.ui_main.spn_min,
            self.ui_main.rbt_format_rar, self.ui_main.rbt_format_zip,
            self.ui_main.btn_search_dest,
            self.ui_main.ckb_start,
            self.ui_main.ckb_shutdown,
            self.ui_main.lbl_ckb_shutdown,
            self.ui_main.lbl_ckb_start
        ]
        for widget in widgets:
            widget.setEnabled(state)


    def setup_origin_path(self):
        origin_path = QFileDialog.getExistingDirectory(self.ui_main, "Selecione uma pasta")
        if origin_path:
            self.ui_main.txt_orig_path.setText(origin_path)
        
    def setup_dest_path(self):
        dest_path = QFileDialog.getExistingDirectory(self.ui_main, "Selecione uma pasta")
        if dest_path:
            self.ui_main.txt_dest_path.setText(dest_path)

    def fill_main(self):
        self.ui_main.txt_dest_path.setText(self.data_dest_path or "")
        self.ui_main.txt_schedule_time.setText(f"{self.data_hour_schedule}:{self.data_min_schedule}" or "")

    def fill_list(self):
        self.ui_main.lst_schedule_list.clear()
        for folder in self.data_orig_folder:
            item = QTreeWidgetItem([folder["name"], folder["path"]])
            self.ui_main.lst_schedule_list.addTopLevelItem(item)

    
    def save_folder(self):
        folder_path = self.ui_main.txt_orig_path.text()
        if not self.ui_main.txt_orig_name.text():
            folder_name = os.path.basename(folder_path)
        else:
            folder_name = self.ui_main.txt_orig_name.text()

        if folder_path and folder_name:
            for folder in self.data_orig_folder:
                if folder["path"] == folder_path:
                    return

            new_folder = {"path": folder_path, "name": folder_name}
            self.data_orig_folder.append(new_folder)
            self.update_data_file(j_origin_folder=self.data_orig_folder)

        self.fill_list()
        self.ui_main.txt_orig_path.setText("")
        self.ui_main.txt_orig_name.setText("")

    def del_folder(self):
        select_item = self.ui_main.lst_schedule_list.currentItem()
        if select_item:
            path_to_remove = select_item.text(1)

            self.data_orig_folder = [folder for folder in self.data_orig_folder if folder["path"] != path_to_remove]
            self.update_data_file(j_origin_folder = self.data_orig_folder)
        
        self.fill_list()

    def fill_config(self):
        self.data_read()
        
        self.ui_main.txt_dest_path.setText(self.data_dest_path)

        if not self.data_hour_schedule or not self.data_min_schedule:
            self.ui_main.spn_hour.setValue(12)
            self.ui_main.spn_min.setValue(0)
        else:
            self.ui_main.spn_hour.setValue(int(self.data_hour_schedule))
            self.ui_main.spn_min.setValue(int(self.data_min_schedule))

        if self.data_format == "rar":
            self.ui_main.rbt_format_zip.setChecked(False)
            self.ui_main.rbt_format_rar.setChecked(True)
        elif self.data_format == "zip":
            self.ui_main.rbt_format_rar.setChecked(False)
            self.ui_main.rbt_format_zip.setChecked(True)
            
        if self.data_theme == "dark":
            self.ui_main.btn_theme.setChecked(True)
        else:
            self.ui_main.btn_theme.setChecked(False)
        
        self.toggle_config(False)

    
    def setup_theme(self):
        theme_icon = QIcon()

        if self.ui_main.btn_theme.isChecked():
            with open("Screens/dark_theme.qss", "r") as file:
                self.ui_main.setStyleSheet(file.read())
                theme_icon = (f"{self.ICON_PATH}light_theme_ico")
        else:
            with open("Screens/light_theme.qss", "r") as file:
                self.ui_main.setStyleSheet(file.read())
                theme_icon = (f"{self.ICON_PATH}dark_theme_ico")
        self.ui_main.btn_theme.setIcon(QIcon(theme_icon))
        self.save_config()

        
    def save_config(self):
        self.data_hour_schedule = self.ui_main.spn_hour.text()
        self.data_min_schedule = self.ui_main.spn_min.text()
        self.data_dest_path = self.ui_main.txt_dest_path.text()

        if self.ui_main.rbt_format_rar.isChecked():
            self.data_format = "rar"
        elif self.ui_main.rbt_format_zip.isChecked():
            self.data_format = "zip"

        if self.ui_main.btn_theme.isChecked():
            self.data_theme = "dark"
        else:
            self.data_theme = "light"

        if self.ui_main.ckb_start.isChecked():
            self.data_ck_start = "True"
            self.auto_start()
        else:
            self.data_ck_start = "False"
            self.remove_auto_start()

        if self.ui_main.ckb_shutdown.isChecked():
            self.data_ck_shutdown = "True"
        else:
            self.data_ck_shutdown = "False"
            

        self.toggle_config(False)

        self.update_data_file(
            j_data_format = self.data_format, 
            j_time = f"{str(self.data_hour_schedule).zfill(2)}:{str(self.data_min_schedule).zfill(2)}",
            j_dest_path = self.data_dest_path,
            j_theme = self.data_theme,
            j_data_ck_shutdown = self.data_ck_shutdown,
            j_data_ck_start = self.data_ck_start
        )
            
        self.fill_main()

    def setup_tray_icon(self):
        self.tray_icon = QSystemTrayIcon(QIcon(f"{self.ICON_PATH}logo_small.png"))
        tray_menu = QMenu()
        open_action = tray_menu.addAction("Abrir")
        open_action.setIcon(QIcon(f"{self.ICON_PATH}search_dest.svg"))
        open_action.triggered.connect(self.ui_main.show)
        quit_action = tray_menu.addAction("Sair")
        quit_action.setIcon(QIcon(f"{self.ICON_PATH}close.svg"))
        quit_action.triggered.connect(self.quit_app)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()


    def start_time_monitor(self):
        self.timer = QTimer()
        self.timer.start(60000)
        self.data_read()
        if all([self.data_dest_path, self.data_format, self.data_orig_folder,
                self.data_hour_schedule, self.data_min_schedule]):
            self.timer.timeout.connect(self.monitor_time)

    def monitor_time(self):
        self.date_now = time.strftime("%y/%m/%d")
        self.time_now = time.strftime("%H:%M")
        self.my_time = f"{self.data_hour_schedule}:{self.data_min_schedule}"
        if self.time_now == self.my_time:
            self.exec_bakup()
            if self.data_ck_shutdown == "True":
                os.system("shutdown /s /t 30")
                self.app_shut()
            
    def exec_bakup(self):
        self.data_read()
        if self.data_format == "rar":
            self.rar_folder()
        
        elif self.data_format == "zip":
            self.zip_folder()
    
    def rar_folder(self):
        self.date_out = time.strftime("%y%m%d")
        for folder in self.data_orig_folder:
            folder_name = folder["name"]
            folder_path = folder["path"]
            dest_path = os.path.join(self.data_dest_path, f"{folder_name}_{self.date_out}.rar")
            subprocess.run(f'rar a -ep1 "{dest_path}" "{folder_path}"')
        

    def zip_folder(self):
        self.date_out = time.strftime("%y%m%d")
        for folder in self.data_orig_folder:
            folder_name = folder["name"]
            folder_path = folder["path"]
            dest_path = os.path.join(self.data_dest_path, f"{folder_name}_{self.date_out}.zip")

            with zipfile.ZipFile(dest_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, folder_path)
                        zipf.write(file_path, arcname = arcname)
            

    def auto_start(self):
        app_name = "Autobkp"
        app_path = self.data_app_path
        app_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        try:
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, app_key, 0, winreg.KEY_ALL_ACCESS)
            exist_value = winreg.QueryValueEx(reg_key, app_name)[0]
            winreg.CloseKey(reg_key)

            if exist_value == app_path:
                return
        except FileNotFoundError:
            pass
        except Exception as e:
            return
        
        try: 
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, app_key, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(reg_key, app_name, 0, winreg.REG_SZ, app_path)
            winreg.CloseKey(reg_key)
            
        except Exception as e:
            return
    
    def remove_auto_start(self):
        app_name = "Autobkp"
        app_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        try:

            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, app_key, 0, winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(reg_key, app_name)
            winreg.CloseKey(reg_key)
        
        except FileNotFoundError:
            pass
        except Exception as e:
            return


    def quit_app(self):
        self.setup_exit_screen()
        self.ui_msg.btn_exit.clicked.connect(self.app_shut)
        self.ui_msg.btn_exit.clicked.connect(self.set_timer)
        self.ui_msg.btn_close.clicked.connect(self.app_hide)
        
    def app_shut_down(self):
        self.setup_shut_screen()
        self.ui_shut.lbl_message_2.setText(f"em {self.timer_time} seg!")

    def set_timer(self):
        print("Timer Set")
        self.shut_timer.timeout.connect(self.timer_update)
        self.shut_timer.start(1000)
        
    def timer_update(self):
        print(self.timer_time)
        if self.timer_time > 0:
            self.timer_time -= 1
            self.ui_shut.lbl_message_2.setText(f"em {self.timer_time} seg!")
            
        else:
            self.shut_timer.stop()
            self.ui_shut.lbl_message_2.setText("TIME OUT")

    def timer_stop(self):
        self.shut_timer.stop()
        self.timer_time = 15
        self.ui_shut.lbl_message_2.setText(f"em {self.timer_time} seg!")
        print(self.timer_time)

    def app_shut(self):
        app.quit()

    def app_hide(self):
        self.ui_msg.close()
        self.ui_main.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Main()
    sys.exit(app.exec())
