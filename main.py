#FIRST STEP OF CODE WILL BE WRITTEN HERE
#This will be main file need to be Executed 
import os
import sys

def main_func(args,kwargs):
    pass
  

def relaunch_in_cmd():
    if os.name == 'nt':
        if not sys.stdin.isatty():
            script = os.path.abspath(sys.argv[0])
            os.system(f'start cmd /k python "{script}"')
            sys.exit()



# Your actual program logic below
print("This is your CLI app. It's running in a real terminal now.")
input("Press Enter to exit...")




if __name__ == '__main__':
  relaunch_in_cmd()
  pass #running main function 
  
