import sys




def main():

    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        if(command =="exit 0"):
            return 
        elif (command.find("echo")==0):
            content_start_index = command.find("o")
            sys.stdout.write(f"{command[content_start_index+2:]}\n")
        else:
            sys.stdout.write(f"{command}: command not found\n")

if __name__ == "__main__":
    main()
