from os import listdir, getcwd, renames
from os.path import splitext
from re import compile, match


# 현재 경로
current_path: str = getcwd()


def init(path_dir: str) -> list:
    """
    @Param
        path_dir    : str   - 파일 경로
    @Return
        dir_list    : list  - 확장자가 포함된 파일들의 리스트
    """
    print(f"[🛠 ] Now working on Dir: '{path_dir}'")

    dir_list: list = listdir(path_dir)

    return dir_list


# path_abs(파일 이름을 포함한 파일의 경로) = path + filename
def extract_extension(path_abs: str) -> str:
    """
    @Param
        path_abs    : str   - 파일 경로
    @Return
        ext     : str   - 파일 확장자
    """
    name, ext = splitext(path_abs)
    # ext : '.확장자' ('.' 이 포함되어 있음)
    return ext


# Default input value
str_raw: str = input("[🖍 ] Type the file name template: ")
str_alt: str = input("[🖍 ] Type the alt file name: ")

if str_raw == str_alt:
    raise Exception


def extract_list(file_names: list, str_raw: str) -> list:
    """
    @Param
        file_names  : list  - 리스트로 구성된 파일이름 목록
        str_raw     : str   - 파일 이름값, 비교값
    @Return
        file_names  : list
    """
    print(file_names)
    for item in file_names[:]:  # [:] -> 리스트 전체 복사
        if str_raw not in item:
            print(f"[🛠 ] EXCLUDED - {item}")
            file_names.remove(item)
        elif str_raw in item:
            print(f"[🛠 ] MATCH - {item}")
    print("[✔ ] List sorting... DONE\n")
    return file_names


# dir_file : dir_list에 포함되는 "파일명.확장자" 형태의 문자열
def name_modifier(file_names_refined: list, str_raw: str, str_alt: str, path: str) -> None:
    """
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

        # 유효성 검사

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


dir_list: list = init(current_path)
extract_list(dir_list, str_raw)
name_modifier(dir_list, str_raw, str_alt, current_path)
