import sys
from urllib import request




def main():

    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        type = ["cat", "exit", "echo", "type"]
        if(command =="exit 0"):
            return 
        elif (command.find("echo")==0):
            content_start_index = command.find("o")
            sys.stdout.write(f"{command[content_start_index+2:]}\n")
        elif(command.find("type")==0):
            word, content = command.split(" ")
            if content in type:
                sys.stdout.write(f"{content} is a shell builtin\n")
            else:
                sys.stdout.write(f"{content}: not found\n")
        else:
            sys.stdout.write(f"{command}: not found\n")

if __name__ == "__main__":
    main()
