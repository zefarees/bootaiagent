from functions.run_python_file import run_python_file
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file


def main():
    print("read the contents of main.py:")
    print(get_file_content({'file_path': 'main.py'}))

    print("write 'hello' to main.txt:")
    print(write_file({'file_path': 'main.txt', 'content': 'hello'}))

    print("run main.py:")
    print(run_python_file({'file_path': 'main.py'}))

    print("list the contents of the pkg directory:")
    print(get_files_info({'directory': 'pkg'}))

if __name__ == "__main__":
    main()
