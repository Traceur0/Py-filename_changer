from os import listdir, getcwd, renames
from os.path import splitext


path: str = getcwd()


def init(path) -> list:
    print(f"Now working on Dir: '{path}'")

    dir_list: list = listdir(path)

    return dir_list


# path = path + filename
def extract_extension(path: str) -> str:
    name, ext = splitext(path)
    # ext : .확장자
    return ext


str_raw: str = input("Type the file name template: ")
str_alt: str = input("Type the alt file name: ")


def extract_list(file_list: list, str_raw: str) -> list:
    for item in file_list:
        if str_raw not in item:
            print(f"[Modifier]EXCLUDED - {item}")
            file_list.remove(item)
        else:
            print(f"[Modifier]MATCH - {item}")
        print("[✔]List sorting DONE")
    return file_list


# dir_file : dir_list에 포함되는 "파일명.확장자" 형태의 문자열
def name_modifier(file_list: list, str_alt: str, path: str) -> None:
    for dir_file in range(0, len(file_list)):
        file_path = path + '\\' + dir_file  # Backslash str
        alt = str_alt + "." + extract_extension(filepath)
        renames(dir_file, alt)
        print(f"[Modifier]filename '{dir_file}' has been modified to {alt}")
    count: str = "NaN"
    print(f"[✔]DONE. {count}file(s) has been renamed in total!")


dir_list: list = init(path)
extract_list(dir_list, str_raw)
name_modifier(dir_list, str_alt)
