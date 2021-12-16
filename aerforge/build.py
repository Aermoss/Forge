import os
import shutil

class Builder:
    def __init__(self, file_name, noconsole = True, flags = ""):
        self.file_name = file_name
        self.flags = flags
        self.default_flags = ""

        space = 0

        if noconsole:
            if space != 0:
                self.default_flags += " "
                space -= 1
                
            self.default_flags += "--noconsole"
            space += 1

    def build(self):
        shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "./assets/icon/icon.png"), ".")
        shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "./assets/icon/icon_white.png"), ".")
        shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "./assets/icon/icon_ico.ico"), ".")
        shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "./assets/logo/logo.png"), ".")
        os.system(f"pyinstaller --onefile --clean --icon=icon_ico.ico {self.default_flags} {self.flags} {self.file_name}")
        shutil.copy(f"dist/{os.path.splitext(os.path.basename(self.file_name))[0]}.exe", ".")
        shutil.rmtree("build", ignore_errors = True)
        shutil.rmtree("dist", ignore_errors = True)
        os.remove(f"{os.path.splitext(os.path.basename(self.file_name))[0]}.spec")