import os
from shutil import copy
from zipfile import ZipFile


def create_folder(folder_name, status_edit):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    android_file = os.path.join(desktop_path, "android_file")

    if not os.path.exists(android_file):
        os.makedirs(android_file)

    full_folder_path = os.path.join(android_file, folder_name)
    if not os.path.exists(full_folder_path):
        os.makedirs(full_folder_path)
        status_edit.append("폴더 생성이 완료되었습니다.")
    else:
        status_edit.append("폴더가 이미 존재합니다.")


def process_files(project_folder, folder_name, status_edit):
    if not os.path.exists(project_folder):
        status_edit.append("에러: 폴더를 찾을 수 없습니다.")
        return

    all_path = os.path.join(os.path.expanduser("~"), "Desktop", "android_file", folder_name)
    if not os.path.exists(all_path):
        status_edit.append("에러: 폴더가 생성되지 않았습니다. 먼저 폴더를 생성해주세요.")
        return

    java_folder = os.path.join(project_folder, "app", "src", "main", "java", "com", "example", "myapplication")
    if os.path.exists(java_folder):
        for java_file in os.listdir(java_folder):
            if java_file.endswith(".java"):
                copy(os.path.join(java_folder, java_file), all_path)
                new_java_file_name = f"30309,김현민-{java_file}"
                os.rename(os.path.join(all_path, java_file), os.path.join(all_path, new_java_file_name))
                status_edit.append(f"{java_file}을(를) 변환하여 {new_java_file_name}으로 저장했습니다.")

    xml_folder = os.path.join(project_folder, "app", "src", "main", "res", "layout")
    if os.path.exists(xml_folder):
        for xml_file in os.listdir(xml_folder):
            if xml_file.endswith(".xml"):
                copy(os.path.join(xml_folder, xml_file), all_path)
                new_xml_file_name = f"30309,김현민-{xml_file}"
                os.rename(os.path.join(all_path, xml_file), os.path.join(all_path, new_xml_file_name))
                status_edit.append(f"{xml_file}을(를) 변환하여 {new_xml_file_name}으로 저장했습니다.")

    status_edit.append("모든 파일 변환이 완료")


def save_zip(folder_name, status_edit):
    all_path = os.path.join(os.path.expanduser("~"), "Desktop", "android_file", folder_name)
    zip_name = os.path.join(os.path.expanduser("~"), "Desktop", "android_file", f"{folder_name}.zip")

    with ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(all_path):
            for i in files:
                file_path = os.path.join(root, i)
                arcname = os.path.relpath(file_path, all_path)
                zipf.write(file_path, arcname=arcname)

    status_edit.append(f"파일들이 {zip_name}로 압축되었습니다.")
