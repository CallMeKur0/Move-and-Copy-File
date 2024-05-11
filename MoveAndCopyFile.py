import os
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox

class FileCopyMoveApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Sao chép và di chuyển tệp")
        self.setGeometry(100, 100, 400, 200)

        # Create labels, line edits, and buttons
        self.source_label = QLabel("Thư mục nguồn:")
        self.source_entry = QLineEdit()
        self.source_entry.setPlaceholderText("Chọn thư mục nguồn")
        self.source_browse_button = QPushButton("Chọn")
        self.source_browse_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; border: none; padding: 5px 10px; }"
                                                "QPushButton:hover { background-color: #45a049; }")
        self.source_browse_button.clicked.connect(self.browse_source_folder)

        self.destination_label = QLabel("Thư mục đích:")
        self.destination_entry = QLineEdit()
        self.destination_entry.setPlaceholderText("Chọn thư mục đích")
        self.destination_browse_button = QPushButton("Chọn")
        self.destination_browse_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; border: none; padding: 5px 10px; }"
                                                      "QPushButton:hover { background-color: #45a049; }")
        self.destination_browse_button.clicked.connect(self.browse_destination_folder)

        self.extension_label = QLabel("Đuôi file:")
        self.extension_entry = QLineEdit()
        self.extension_entry.setPlaceholderText("Nhập đuôi file (ví dụ: txt)")

        self.copy_button = QPushButton("Sao chép và di chuyển")
        self.copy_button.setStyleSheet("QPushButton { background-color: #008CBA; color: white; border: none; padding: 10px 20px; font-size: 16px; }"
                                       "QPushButton:hover { background-color: #0073e6; }")
        self.copy_button.clicked.connect(self.copy_and_move_files)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.source_label)
        layout.addWidget(self.source_entry)
        layout.addWidget(self.source_browse_button)
        layout.addWidget(self.destination_label)
        layout.addWidget(self.destination_entry)
        layout.addWidget(self.destination_browse_button)
        layout.addWidget(self.extension_label)
        layout.addWidget(self.extension_entry)
        layout.addWidget(self.copy_button)

        self.setLayout(layout)

    def browse_source_folder(self):
        folder_selected = QFileDialog.getExistingDirectory(self, "Chọn thư mục nguồn")
        self.source_entry.setText(folder_selected)

    def browse_destination_folder(self):
        folder_selected = QFileDialog.getExistingDirectory(self, "Chọn thư mục đích")
        self.destination_entry.setText(folder_selected)

    def copy_and_move_files(self):
        source_folder = self.source_entry.text()
        destination_folder = self.destination_entry.text()
        file_extension = self.extension_entry.text()

        if not source_folder or not destination_folder or not file_extension:
            QMessageBox.critical(self, "Lỗi", "Vui lòng nhập đuôi file!")
            return

        file_extension = file_extension.strip('.')  # Remove leading and trailing dots if any
        file_extension_with_dot = '.' + file_extension  # Add dot before the file extension

        found_files = False

        try:
            for file_name in os.listdir(source_folder):
                if file_name.endswith(file_extension_with_dot):
                    found_files = True
                    source_file = os.path.join(source_folder, file_name)
                    destination_file = os.path.join(destination_folder, file_name)
                    shutil.copy(source_file, destination_file)
                    os.remove(source_file)

            if not found_files:
                QMessageBox.warning(self, "Cảnh báo", f"Không tìm thấy bất kỳ tệp nào có đuôi .{file_extension} trong thư mục nguồn!")
            else:
                QMessageBox.information(self, "Thông báo", f"Đã sao chép và di chuyển tất cả các tệp .{file_extension} Thành công!")

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Có lỗi xảy ra: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileCopyMoveApp()
    window.show()
    sys.exit(app.exec_())
