
from pathlib import Path
import sys
import os

def file_path(PATH, file_name):
    paths = PATH.split(":")
    for path in paths:
        path_name = os.path.join(path, file_name)
        if os.path.isfile(path_name):
            return path
    return None

def main():
    PATH  = os.environ.get("PATH")

    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        built_in = ["exit", "echo", "type","pwd", "cd"]
        if(command =="exit 0"):
            return 
        elif (command.find("echo")==0):
            content_start_index = command.find("o")
            sys.stdout.write(f"{command[content_start_index+2:]}\n")
        elif(command.find("type")==0):
            word, content = command.split(" ")
            Paths = PATH.split(":")
            cmd_path  = None
            for path in Paths:
                if os.path.isfile(f"{path}/{content}"):
                    cmd_path = f"{path}/{content}"
            if content in built_in:
                sys.stdout.write(f"{content} is a shell builtin\n")
            elif cmd_path:
                sys.stdout.write(f"{content} is {cmd_path}\n")
            else:
                sys.stdout.write(f"{content}: not found\n")
        elif command.find("my_exe")==0:
            files, name = command.split(" ")
            path = file_path(PATH, files)
            if(path):
                os.system(command)
            else:
                sys.stdout.write(f"{command}: command not found\n")
        elif command.startswith("pwd"):
            sys.stdout.write(f"{os.getcwd()}\n")
        elif command.startswith("cd"):
            path = command.split(" ")[1]
            if path.startswith("/"):
                absolute= path
                if  os.path.isdir(path):
                    os.chdir(path)
                else:
                    sys.stdout.write(f"cd: {path}: No such file or directory\n")
            elif path.startswith("."):
                absolute = os.path.join(os.getcwd(), path)
                absolute = os.path.normpath(absolute)
                if  os.path.isdir(path):
                    os.chdir(path)
                else:
                    sys.stdout.write(f"cd: {path}: No such file or directory\n")
            else:
                absolute = None
                sys.stdout.write(f"{path}: unsupported path\n")
            # if absolute:
            #     os.chdir(path)

        else:
            sys.stdout.write(f"{command}: command not found\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
