import os
import subprocess

run =True
while run:
    command=input("Please enter the shell command: ")
    result= subprocess.run(command,shell=True)
    if command=="exit":
        run=False
