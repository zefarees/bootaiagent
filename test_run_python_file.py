from functions.run_python_file import run_python_file


def main():
    print("print the calculator's usage instructions:")
    print(run_python_file("calculator", "main.py"))

    print('Run the calculator:')
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("run the calculator's tests:")
    print(run_python_file("calculator", "tests.py"))

    print("Run Calculator")
    print(run_python_file("calculator", "../main.py"))

    print("Check if exists:")
    print(run_python_file("calculator", "nonexistent.py"))

    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    main()
