import os

def run_command():
    # 사용자로부터 명령어 입력 받기
    command = input("Enter the command you want to run: ")
    

    os.system(command)

if __name__ == "__main__":
    run_command()
