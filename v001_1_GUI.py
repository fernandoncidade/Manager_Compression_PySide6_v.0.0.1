import os
import sys
import json
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel,
                               QListWidget, QPushButton, QWidget)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QAction
from v001_2_gerente_GUI_layouts import GerenciadorInterface
from v001_3_metodos_compressao import MetodoCompressao
from v001_5_colors import apply_neutral_standart_theme


class InterfaceGrafica(QMainWindow, MetodoCompressao):
    def __init__(self):
        super(InterfaceGrafica, self).__init__()
        self.gerenciador_interface = GerenciadorInterface(self)

        self.menu_bar = self.menuBar()

        self.config_menu = self.menu_bar.addMenu('Configurações')

        self.compression_method_action = QAction('Selecionar Método de Compressão', self)
        self.compression_method_action.triggered.connect(self.select_compression_method)
        self.config_menu.addAction(self.compression_method_action)
        self.config_menu.aboutToShow.connect(self.select_compression_method)

        self.init_ui()
        self.load_compression_method()

    def load_compression_method(self):
        config_method = getattr(sys, '_MEIPASS', os.path.dirname(os.path.realpath(__file__)))
        config_path = os.path.join(config_method, "Config_Method")
        caminho_metodo = os.path.join(config_path, 'config.json')
        try:
            with open(caminho_metodo, 'r') as f:
                config = json.load(f)
                self.set_compression_method(config['compress_type_rar'], 'rar')
                self.set_compression_method(config['compress_type_zip'], 'zip')
                self.set_compression_method(config['compress_type_7z'], '7z')
                self.set_compression_method(config['compress_type_tar'], 'tar')
        except FileNotFoundError:
            pass

    def init_ui(self):
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(base_path, "icones")
        self.setWindowTitle("Gerenciador de BackUp")
        icon_title_path = os.path.join(icon_path, "Manager-BackUp.ico")
        self.setWindowIcon(QIcon(icon_title_path))

        main_layout_1 = QHBoxLayout()

        primeiro_quadrante_layout = QVBoxLayout()

        folder_button = QPushButton("Adicionar Pastas")
        folder_button.clicked.connect(lambda: self.gerenciador_interface.browse_folder(self))
        primeiro_quadrante_layout.addWidget(folder_button)

        file_button = QPushButton("Adicionar Arquivos")
        file_button.clicked.connect(lambda: self.gerenciador_interface.browse_file(self))
        primeiro_quadrante_layout.addWidget(file_button)

        output_button_output_extract = QPushButton("Especificar Diretório(s) de Extração")
        output_button_output_extract.clicked.connect(self.gerenciador_interface.output_button_output_EXTRACT_clicked)
        primeiro_quadrante_layout.addWidget(output_button_output_extract)

        extract_button = QPushButton("Extrair Arquivos e Pastas")
        extracao_icon_path = os.path.join(icon_path, "extracao4.png")
        extract_button.setIcon(QIcon(extracao_icon_path))
        extract_button.clicked.connect(self.gerenciador_interface.extract_files)
        primeiro_quadrante_layout.addWidget(extract_button)

        test_button = QPushButton("Testar Integridade")
        test_icon_path = os.path.join(icon_path, "teste_integridade2.png")
        test_button.setIcon(QIcon(test_icon_path))
        test_button.clicked.connect(self.gerenciador_interface.testar_integridade)
        primeiro_quadrante_layout.addWidget(test_button)

        main_layout_1.addLayout(primeiro_quadrante_layout)
        main_layout_1.setAlignment(primeiro_quadrante_layout, Qt.AlignmentFlag.AlignBottom)

        segundo_quadrante_layout = QVBoxLayout()

        clear_button_folders = QPushButton("Limpar Entrada")
        limpar_folders_icon_path = os.path.join(icon_path, "clear_button3.png")
        clear_button_folders.setIcon(QIcon(limpar_folders_icon_path))
        clear_button_folders.clicked.connect(self.gerenciador_interface.clear_folders)
        segundo_quadrante_layout.addWidget(clear_button_folders)

        folder_label = QLabel("Diretório(s) Pastas e Arquivos:")
        segundo_quadrante_layout.addWidget(folder_label)
        self.gerenciador_interface.folder_listbox = QListWidget()
        segundo_quadrante_layout.addWidget(self.gerenciador_interface.folder_listbox)
        main_layout_1.addLayout(segundo_quadrante_layout)

        terceiro_quadrante_layout = QVBoxLayout()

        clear_button_output = QPushButton("Limpar Saídas")
        limpar_output_icon_path = os.path.join(icon_path, "clear_button2.png")
        clear_button_output.setIcon(QIcon(limpar_output_icon_path))
        clear_button_output.clicked.connect(self.gerenciador_interface.clear_output)
        terceiro_quadrante_layout.addWidget(clear_button_output)

        output_label_extract = QLabel("Diretório(s) para Extração:")
        terceiro_quadrante_layout.addWidget(output_label_extract)
        self.gerenciador_interface.output_listbox_extract = QListWidget()
        terceiro_quadrante_layout.addWidget(self.gerenciador_interface.output_listbox_extract)
        main_layout_1.addLayout(terceiro_quadrante_layout)

        main_layout_2 = QHBoxLayout()

        quarto_quadrante_layout = QVBoxLayout()

        output_button_output_rar = QPushButton("Especificar Diretório(s) de Saída .RAR")
        output_button_output_rar.clicked.connect(self.gerenciador_interface.output_button_output_RAR_clicked)
        quarto_quadrante_layout.addWidget(output_button_output_rar)

        create_rar_button = QPushButton("Armazenar como .RAR")
        rar_icon_path = os.path.join(icon_path, "winrar3.png")
        create_rar_button.setIcon(QIcon(rar_icon_path))
        create_rar_button.clicked.connect(self.gerenciador_interface.store_as_rar)
        quarto_quadrante_layout.addWidget(create_rar_button)

        output_button_output_zip = QPushButton("Especificar Diretório(s) de Saída .ZIP")
        output_button_output_zip.clicked.connect(self.gerenciador_interface.output_button_output_ZIP_clicked)
        quarto_quadrante_layout.addWidget(output_button_output_zip)

        create_zip_button = QPushButton("Armazenar como .ZIP")
        zip_icon_path = os.path.join(icon_path, "winzip4.png")
        create_zip_button.setIcon(QIcon(zip_icon_path))
        create_zip_button.clicked.connect(self.gerenciador_interface.store_as_zip)
        quarto_quadrante_layout.addWidget(create_zip_button)

        main_layout_2.addLayout(quarto_quadrante_layout)
        main_layout_2.setAlignment(quarto_quadrante_layout, Qt.AlignmentFlag.AlignBottom)

        quinto_quadrante_layout = QVBoxLayout()

        output_label_rar = QLabel("Diretório(s) de saída .RAR:")
        quinto_quadrante_layout.addWidget(output_label_rar)
        self.gerenciador_interface.output_listbox_rar = QListWidget()
        quinto_quadrante_layout.addWidget(self.gerenciador_interface.output_listbox_rar)
        main_layout_2.addLayout(quinto_quadrante_layout)

        sexto_quadrante_layout = QVBoxLayout()

        output_label_zip = QLabel("Diretório(s) de saída .ZIP:")
        sexto_quadrante_layout.addWidget(output_label_zip)
        self.gerenciador_interface.output_listbox_zip = QListWidget()
        sexto_quadrante_layout.addWidget(self.gerenciador_interface.output_listbox_zip)
        main_layout_2.addLayout(sexto_quadrante_layout)

        main_layout_3 = QHBoxLayout()

        setimo_quadrante_layout = QVBoxLayout()

        output_button_output_7z = QPushButton("Especificar Diretório(s) de Saída .7Z")
        output_button_output_7z.clicked.connect(self.gerenciador_interface.output_button_output_7Z_clicked)
        setimo_quadrante_layout.addWidget(output_button_output_7z)

        create_7z_button = QPushButton("Armazenar como .7Z")
        sevenzip_icon_path = os.path.join(icon_path, "sevenzip4.png")
        create_7z_button.setIcon(QIcon(sevenzip_icon_path))
        create_7z_button.clicked.connect(self.gerenciador_interface.store_as_7z)
        setimo_quadrante_layout.addWidget(create_7z_button)

        output_button_output_tar = QPushButton("Especificar Diretório(s) de Saída .TAR")
        output_button_output_tar.clicked.connect(self.gerenciador_interface.output_button_output_TAR_clicked)
        setimo_quadrante_layout.addWidget(output_button_output_tar)

        create_tar_button = QPushButton("Armazenar como .TAR")
        tar_icon_path = os.path.join(icon_path, "tar1.png")
        create_tar_button.setIcon(QIcon(tar_icon_path))
        create_tar_button.clicked.connect(self.gerenciador_interface.store_as_tar)
        setimo_quadrante_layout.addWidget(create_tar_button)

        main_layout_3.addLayout(setimo_quadrante_layout)
        main_layout_3.setAlignment(setimo_quadrante_layout, Qt.AlignmentFlag.AlignBottom)

        oitavo_quadrante_layout = QVBoxLayout()

        output_label_7z = QLabel("Diretório(s) de saída .7Z:")
        oitavo_quadrante_layout.addWidget(output_label_7z)
        self.gerenciador_interface.output_listbox_7z = QListWidget()
        oitavo_quadrante_layout.addWidget(self.gerenciador_interface.output_listbox_7z)
        main_layout_3.addLayout(oitavo_quadrante_layout)

        nono_quadrante_layout = QVBoxLayout()

        output_label_tar = QLabel("Diretório(s) de saída .TAR:")
        nono_quadrante_layout.addWidget(output_label_tar)
        self.gerenciador_interface.output_listbox_tar = QListWidget()
        nono_quadrante_layout.addWidget(self.gerenciador_interface.output_listbox_tar)
        main_layout_3.addLayout(nono_quadrante_layout)

        widget_1 = QWidget(self)
        widget_1.setLayout(main_layout_1)

        widget_2 = QWidget(self)
        widget_2.setLayout(main_layout_2)

        widget_3 = QWidget(self)
        widget_3.setLayout(main_layout_3)

        main_layout = QVBoxLayout()

        main_layout.addWidget(widget_1)
        main_layout.addWidget(widget_2)
        main_layout.addWidget(widget_3)

        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.aplicacao_tema_padrao_neutro()

    def aplicacao_tema_padrao_neutro(self):
        apply_neutral_standart_theme(self)


if __name__ == "__main__":
    app = QApplication([])
    window = InterfaceGrafica()
    window.show()
    app.exec()
