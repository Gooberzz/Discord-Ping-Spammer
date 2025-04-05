import requests
import os
import json
import time
import subprocess
from pathlib import Path
import platform
import psutil

os.system('cls')
time.sleep(1)

logo = """
      ::::::::: :::   ::::::::::::::::::::::  :::::::: :::       :::::::: 
     :+:    :+::+:   :+:    :+:   :+:    :+::+:    :+::+:      :+:    :+: 
    +:+    +:+ +:+ +:+     +:+   +:+    +:++:+    +:++:+      +:+         
   +#++:++#+   +#++:      +#+   +#+    +:++#+    +:++#+      +#++:++#++   
  +#+          +#+       +#+   +#+    +#++#+    +#++#+             +#+    
 #+#          #+#       #+#   #+#    #+##+#    #+##+#      #+#    #+#     
###          ###       ###    ########  ######## ##################   
"""
print(logo)

print("1. Open Program | Opens a program of your choice.")
print("2. System Info | Displays your system information")

choice = input("Enter the number of a tool to get started: ")