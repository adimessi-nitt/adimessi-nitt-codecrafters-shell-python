from email.errors import NonPrintableDefect
from pathlib import Path
import sys
import os

def main():
    PATH  = os.environ.get("PATH")

    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        built_in = ["exit", "echo", "type"]
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
        else:
            sys.stdout.write(f"{command}: not found\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
