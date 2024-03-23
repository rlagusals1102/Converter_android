import os
from shutil import rmtree
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QTextEdit
from utils import create_folder, process_files, save_zip
class Converter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("파일 변환기")
        self.layout = QVBoxLayout()

        self.project_folder_label = QLabel("프로젝트 폴더:")
        self.project_folder_edit = QLineEdit()
        self.browse_button = QPushButton("찾아보기")
        self.browse_button.clicked.connect(self.browse_folder)

        self.folder_name_label = QLabel("생성할 폴더 이름:")
        self.folder_name_edit = QLineEdit("30309,김현민-")

        self.create_folder_button = QPushButton("폴더 생성")
        self.create_folder_button.clicked.connect(self.create_folder)

        self.process_button = QPushButton("변환 시작")
        self.process_button.clicked.connect(self.process_files)

        self.save_zip_button = QPushButton("Zip 파일로 저장")
        self.save_zip_button.clicked.connect(self.save_zip)

        self.status_label = QLabel("상태:")
        self.status_edit = QTextEdit()
        self.status_edit.setReadOnly(True)

        folder_layout = QHBoxLayout()
        folder_layout.addWidget(self.project_folder_label)
        folder_layout.addWidget(self.project_folder_edit)
        folder_layout.addWidget(self.browse_button)

        name_layout = QHBoxLayout()
        name_layout.addWidget(self.folder_name_label)
        name_layout.addWidget(self.folder_name_edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.create_folder_button)
        button_layout.addWidget(self.process_button)
        button_layout.addWidget(self.save_zip_button)

        self.layout.addLayout(folder_layout)
        self.layout.addLayout(name_layout)
        self.layout.addLayout(button_layout)
        self.layout.addWidget(self.status_label)
        self.layout.addWidget(self.status_edit)

        self.setLayout(self.layout)

    def browse_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "프로젝트 폴더 선택")
        if folder_path:
            self.project_folder_edit.setText(folder_path)

    def create_folder(self):
        folder_name = self.folder_name_edit.text()
        create_folder(folder_name, self.status_edit)

    def process_files(self):
        project_folder = self.project_folder_edit.text()
        folder_name = self.folder_name_edit.text()
        process_files(project_folder, folder_name, self.status_edit)

    def save_zip(self):
        folder_name = self.folder_name_edit.text()
        save_zip(folder_name, self.status_edit)

    # def closeEvent(self, event):
    #     # folder_name = self.folder_name_edit.text()
    #     folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "android_file")
    #     if os.path.exists(folder_path):
    #         rmtree(folder_path)
    #         self.status_edit.append("android_file 폴더 및 내용 삭제")
    #     event.accept()
