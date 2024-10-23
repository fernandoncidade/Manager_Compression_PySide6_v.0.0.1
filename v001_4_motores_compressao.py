import os
import sys
import subprocess
from PySide6.QtCore import QThread, Signal


def buscar_winrar_executavel():
    dir_atual = getattr(sys, '_MEIPASS', os.path.dirname(os.path.realpath(__file__)))
    winrar_path = os.path.join(dir_atual, "WinRAR")
    caminho_winrar = os.path.join(winrar_path, 'WinRAR.exe')

    if os.path.exists(caminho_winrar):
        return caminho_winrar

    possible_locations = [
        rf"C:\Program Files\WinRAR\WinRAR.exe",
        rf"C:\Program Files (x86)\WinRAR\WinRAR.exe",
    ]
    for location in possible_locations:
        if os.path.isfile(location):
            return location

    return None


def buscar_sevenzip_executavel():
    dir_atual = getattr(sys, '_MEIPASS', os.path.dirname(os.path.realpath(__file__)))
    sevenzip_path = os.path.join(dir_atual, "7-Zip")
    caminho_sevenzip = os.path.join(sevenzip_path, '7zG.exe')

    if os.path.exists(caminho_sevenzip):
        return caminho_sevenzip

    possible_locations = [
        rf"C:\Program Files\7-Zip\7zG.exe",
        rf"C:\Program Files (x86)\7-Zip\7zG.exe",
    ]
    for location in possible_locations:
        if os.path.isfile(location):
            return location

    return None


class CompressaoRAR(QThread):
    finished = Signal()

    def __init__(self, winrar_executable, update_existing, output_listbox, folder_listbox, compress_as_rar=False,
                 compression_method=None):
        super(CompressaoRAR, self).__init__()
        self.format = "rar"
        self.winrar_executable = winrar_executable
        self.update_existing = update_existing
        self.output_listbox = output_listbox
        self.folder_listbox = folder_listbox
        self.compress_as_rar = compress_as_rar
        self.compression_method = compression_method

    def run(self):
        output_paths = [self.output_listbox.item(idx).text() for idx in range(self.output_listbox.count())]
        if not output_paths:
            return

        compressed_files = []

        for idx in range(self.folder_listbox.count()):
            folder_path = self.folder_listbox.item(idx).text()
            folder_name = os.path.basename(folder_path)

            for output_path in output_paths:
                compressed_file_rar = os.path.join(output_path, f"{folder_name}.rar")
                command = f'"{self.winrar_executable}" a -r -ep1 -m{self.compression_method} -md32 -afrar "{compressed_file_rar}" "{folder_path}"'

                if self.update_existing:
                    command = f'"{self.winrar_executable}" u -r -ep1 -m{self.compression_method} -md32 -afrar -o+ "{compressed_file_rar}" "{folder_path}"'

                subprocess.run(command, shell=True)
                compressed_files.append(compressed_file_rar)


class CompressaoZIP(QThread):
    finished = Signal()

    def __init__(self, sevenzip_executable, update_existing, output_listbox, folder_listbox, compress_as_zip=False,
                 compression_method=None):
        super(CompressaoZIP, self).__init__()
        self.format = "zip"
        self.sevenzip_executable = sevenzip_executable
        self.update_existing = update_existing
        self.output_listbox = output_listbox
        self.folder_listbox = folder_listbox
        self.compress_as_zip = compress_as_zip
        self.compression_method = compression_method

    def run(self):
        output_paths = [self.output_listbox.item(idx).text() for idx in range(self.output_listbox.count())]
        if not output_paths:
            return

        compressed_files = []

        for idx in range(self.folder_listbox.count()):
            folder_path = self.folder_listbox.item(idx).text()
            folder_name = os.path.basename(folder_path)

            for output_path in output_paths:
                compressed_file_zip = os.path.join(output_path, f"{folder_name}.zip")
                command = f'"{self.sevenzip_executable}" a -r -tzip -mx={self.compression_method} "{compressed_file_zip}" "{folder_path}"'

                if self.update_existing:
                    command = f'"{self.sevenzip_executable}" u -r -tzip -mx={self.compression_method} "{compressed_file_zip}" "{folder_path}"'

                subprocess.run(command, shell=True)
                compressed_files.append(compressed_file_zip)


class Compressao7Z(QThread):
    finished = Signal()

    def __init__(self, sevenzip_executable, update_existing, output_listbox, folder_listbox, compress_as_7z=False,
                 compression_method=None):
        super(Compressao7Z, self).__init__()
        self.format = "7z"
        self.sevenzip_executable = sevenzip_executable
        self.update_existing = update_existing
        self.output_listbox = output_listbox
        self.folder_listbox = folder_listbox
        self.compress_as_7z = compress_as_7z
        self.compression_method = compression_method

    def run(self):
        output_paths = [self.output_listbox.item(idx).text() for idx in range(self.output_listbox.count())]
        if not output_paths:
            return

        compressed_files = []

        for idx in range(self.folder_listbox.count()):
            folder_path = self.folder_listbox.item(idx).text()
            folder_name = os.path.basename(folder_path)

            for output_path in output_paths:
                compressed_file_7z = os.path.join(output_path, f"{folder_name}.7z")
                command = f'"{self.sevenzip_executable}" a -r -t7z -mx={self.compression_method} "{compressed_file_7z}" "{folder_path}"'

                if self.update_existing:
                    command = f'"{self.sevenzip_executable}" u -r -t7z -mx={self.compression_method} "{compressed_file_7z}" "{folder_path}"'

                subprocess.run(command, shell=True)
                compressed_files.append(compressed_file_7z)


class CompressaoTAR(QThread):
    finished = Signal()

    def __init__(self, sevenzip_executable, update_existing, output_listbox, folder_listbox, compress_as_tar=False,
                 compression_method=None):
        super(CompressaoTAR, self).__init__()
        self.format = "tar"
        self.sevenzip_executable = sevenzip_executable
        self.update_existing = update_existing
        self.output_listbox = output_listbox
        self.folder_listbox = folder_listbox
        self.compress_as_tar = compress_as_tar
        self.compression_method = compression_method

    def run(self):
        output_paths = [self.output_listbox.item(idx).text() for idx in range(self.output_listbox.count())]
        if not output_paths:
            return

        compressed_files = []

        for idx in range(self.folder_listbox.count()):
            folder_path = self.folder_listbox.item(idx).text()
            folder_name = os.path.basename(folder_path)

            for output_path in output_paths:
                compressed_file_tar = os.path.join(output_path, f"{folder_name}.tar")
                command = f'"{self.sevenzip_executable}" a -r -ttar "{compressed_file_tar}" "{folder_path}"'

                if self.update_existing:
                    command = f'"{self.sevenzip_executable}" u -r -ttar "{compressed_file_tar}" "{folder_path}"'

                subprocess.run(command, shell=True)
                compressed_files.append(compressed_file_tar)


class TestarIntegridade(QThread):
    finished = Signal()

    def __init__(self, sevenzip_executable, compressed_files):
        super(TestarIntegridade, self).__init__()
        self.sevenzip_executable = sevenzip_executable
        self.compressed_files = compressed_files

    def run(self):
        for compressed_file in self.compressed_files:
            if compressed_file.endswith(".rar"):
                command = f'"{self.sevenzip_executable}" t "{compressed_file}"'
                result = subprocess.run(command, shell=True, check=True)
                if result.returncode != 0:
                    raise Exception("A verificação da integridade do arquivo falhou")

            elif compressed_file.endswith(".zip"):
                command = f'"{self.sevenzip_executable}" t "{compressed_file}"'
                result = subprocess.run(command, shell=True, check=True)
                if result.returncode != 0:
                    raise Exception("A verificação da integridade do arquivo falhou")

            elif compressed_file.endswith(".7z"):
                command = f'"{self.sevenzip_executable}" t "{compressed_file}"'
                result = subprocess.run(command, shell=True, check=True)
                if result.returncode != 0:
                    raise Exception("A verificação da integridade do arquivo falhou")

            elif compressed_file.endswith(".tar"):
                command = f'"{self.sevenzip_executable}" t "{compressed_file}"'
                result = subprocess.run(command, shell=True, check=True)
                if result.returncode != 0:
                    raise Exception("A verificação da integridade do arquivo falhou")


class Extracao(QThread):
    finished = Signal()

    def __init__(self, winrar_executable, sevenzip_executable, output_listbox, folder_listbox):
        super(Extracao, self).__init__()
        self.winrar_executable = winrar_executable
        self.sevenzip_executable = sevenzip_executable
        self.output_listbox = output_listbox
        self.folder_listbox = folder_listbox

    def run(self):
        output_paths = [self.output_listbox.item(idx).text() for idx in range(self.output_listbox.count())]
        if not output_paths:
            return

        for idx in range(self.folder_listbox.count()):
            archive_path = self.folder_listbox.item(idx).text()

            for output_path in output_paths:
                if archive_path.endswith(".rar"):
                    command = f'"{self.winrar_executable}" x -y "{archive_path}" "{output_path}"'
                    subprocess.run(command, shell=True)

                elif archive_path.endswith(".zip"):
                    command = f'"{self.sevenzip_executable}" x -y "{archive_path}" -o"{output_path}"'
                    subprocess.run(command, shell=True)

                elif archive_path.endswith(".7z"):
                    command = f'"{self.sevenzip_executable}" x -y "{archive_path}" -o"{output_path}"'
                    subprocess.run(command, shell=True)

                elif archive_path.endswith(".tar"):
                    command = f'"{self.sevenzip_executable}" x -y "{archive_path}" -o"{output_path}"'
                    subprocess.run(command, shell=True)
