from functions.get_files_info import get_files_info


def main():
    print('Result for current directory:')
    print(get_files_info("calculator", "."))

    print('get_files_info("calculator", "/bin"):')
    print(get_files_info("calculator", "/bin"))

    print('get_files_info("calculator", "../"):')
    print(get_files_info("calculator", "../"))

    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))


if __name__ == "__main__":
    main()
