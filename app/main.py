import sys




def main():

    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        sys.stdout.write(f"{command}: command not found\n")
        sys.stdout.write("$ ")
        exit(0)


if __name__ == "__main__":
    main()
