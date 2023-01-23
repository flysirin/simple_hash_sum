import os


def hash_sum(file_name: str):
    with open(file_name, "rb") as file_bin:
        res = 0
        while x := file_bin.read(2):
            if len(x) < 2:
                x += b'0'
            res ^= int.from_bytes(x, byteorder='big')
    return res


def start_create_hashsum(file_inp_dir: str = "input.txt") -> None:
    with open(file_inp_dir, "r", encoding="utf-8") as inp, open("output.txt", "w+", encoding="utf-8") as out:
        paths = inp.read().rstrip().replace("\\", "/")
        if os.path.exists(paths):
            for path1 in os.walk(paths):
                for file in path1[-1]:
                    file_path = f"{path1[0]}/{file}".replace("\\", "/")
                    out.write(f"{hash_sum(file_path)} {file_path}\n")
        print(f"file successful created")


def check_files_in_dir(file_control: str = "output.txt"):
    if not os.path.isfile(file_control):
        print(f"Control file is not created")
        return
    with open(file_control, "r", encoding="utf-8") as file_contr:
        for hash_file in file_contr.readlines():
            try:
                hash_, file = hash_file.split()
            except BaseException:
                print("Wrong read control file")
            if not os.path.isfile(file):
                print(f"{file}  is missing")
                continue
            if int(hash_) != hash_sum(file):
                print(f"{file}  have wrong hash sum")
                continue
            print(f"{file}  is validate")


input_work_command = input("Please input start command:\n'create' - for update or crate control file,\n'check' - for control files: ")
if input_work_command == "create":
    start_create_hashsum()
if input_work_command == "check":
    check_files_in_dir()
