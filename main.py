from os import listdir, getcwd, renames
from os.path import splitext
from re import compile, match


# 현재 경로
current_path: str = getcwd()


def _input() -> None:
    while True:
        # Default input value
        str_raw: str = input("[🖍 ] Type the filename - template: ")

        while True:
            str_alt: str = input("[🖍 ] Type the filename - ALT: ")

            # Input validity check
            if str_alt[-1].isnumeric():
                print("[⚠ ] Last letter of alt file name CAN't be number.\n")
            else:
                break

        if str_raw == str_alt:
            print("[⚠ ] Template name and ALT name CAN'T be same.\n")
        else:
            break
    return str_raw, str_alt


def list_files(path_dir: str) -> list:
    """
    디렉토리 경로값을 받고 파일 목록을 list값으로 반환합니다
    @Param
        path_dir    : str   - 파일 경로
    @Return
        dir_list    : list  - 확장자가 포함된 파일들의 리스트
    """
    print(f"[🛠 ] Now working on Dir: '{path_dir}'")

    dir_list: list = listdir(path_dir)

    return dir_list


def extract_extension(path_abs: str) -> str:
    """
    파일 경로값을 받고 파일의 확장자를 str값으로 반환합니다
    @Param
        path_abs    : str   - 파일 경로(파일 이름을 포함한 파일의 경로) = path + filenam
    @Return
        ext     : str   - 파일 확장자
    """
    name, ext = splitext(path_abs)
    # ext : '.확장자' ('.' 이 포함되어 있음)
    return ext


def extract_list(file_names: list, str_raw: str) -> list:
    """
    파일들의 list값을 받고 str_raw값과 일치하지 않는 값을 배제한 새로운 list값을 반환합니다
    @Param
        file_names  : list  - 리스트로 구성된 파일이름 목록
        str_raw     : str   - 파일 이름값, 비교값
    @Return
        file_names  : list
    """
    for item in file_names[:]:  # [:] -> 리스트 전체 복사
        if str_raw not in item:
            print(f"[🛠 ] EXCLUDED from list- {item}")
            file_names.remove(item)
        elif str_raw in item:
            print(f"[🛠 ] MATCH with template- {item}")
    print("[✔ ] List sorting... DONE\n")

    if len(file_names) == 0:
        print("[✖ ] Nothing matched from file list")
        raise Exception

    return file_names


# dir_file : dir_list에 포함되는 "파일명.확장자" 형태의 문자열
def name_modifier(file_names_refined: list, str_raw: str, str_alt: str, path: str) -> None:
    """
    파일값 뒤의 숫자(인덱스)를 제외한 파일이름을 변경합니다
    @Param
        file_names_refined   : list  - 리스트로 구성된 파일이름 목록
        str_raw     : str   - 파일 이름값, 비교값
        str_alt     : str   - 변경할 파일 이름값
        path        : str   - 파일의 경로
    @Return
        None
    """
    count: int = 0  # Default

    for dir_file in file_names_refined:
        file_path: str = path + '\\' + dir_file

        regex = compile(fr'{str_raw}(\d+).(.+)')    # ex) itemname1.ext
        matched = regex.match(dir_file)

        number_index: str = matched.group(1)
        str_modified: str = str_alt + number_index + \
            extract_extension(file_path)

        print(
            f"[🛠 ] filename '{dir_file}' has been modified to {str_modified}")
        renames(dir_file, str_modified)
        count += 1
    print(f"[✔✔✔ ] DONE. {str(count)} file(s) has been renamed in total!")


# Operating part
str_raw, str_alt = _input()
dir_list: list = list_files(current_path)
extract_list(dir_list, str_raw)
name_modifier(dir_list, str_raw, str_alt, current_path)
