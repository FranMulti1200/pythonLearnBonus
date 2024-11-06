import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("C:/Users/Johnny Me Lavo/Documents/PythonProject/pythonProject_bonusExc/bonus/compressed.zip",
                    "C:/Users/Johnny Me Lavo/Documents/PythonProject/pythonProject_bonusExc/bonus/dest")