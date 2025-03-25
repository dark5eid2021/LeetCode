import os
import shlex
import subprocess

def run_shell():
    while True:
        try:
            # 1. Prompt
            cmd_input = input("mysh> ").strip()
            if not cmd_input:
                continue

            # 2. Parse input
            tokens = shlex.split(cmd_input) # this handles quoted args properly
            command = tokens[0]
            args = tokens[1:]

            # 3. Built-in: exit
            if command == "exit":
                print("Bye!")
                break

            # 4. Built-in: cd
            elif command == "cd":
                path = args[0] if args else os.path.expanduser("~")
            try:
                os.chdir(path)
            except FileNotFoundError:
                print(f"cd: no such file or directory: {path}")

            # 5. Run external command
            else:
                result = subprocess.run([command] + args)

        except KeyboardInterrupt:
            print() # move to new line on Ctrl + c
        except EOFError:
            print("\nBye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_shell()

"""
What This Shell Can Do:
    - Run external commands like ls, echo, pwd
    - Handle Ctrl+C (KeyboardInterrupt) and Ctrl+D (EOFError)
    - Change directories with cd
    - Exit gracefully with exit
    - Handles quoted strings correctly (shlex.split())

What It Doesn't Do (Yet):
    - Pipes (ls | grep foo)
    - Redirects (echo hi > out.txt)
    - Background jobs (sleep 5 &)
    - Command history or autocomplete

"""