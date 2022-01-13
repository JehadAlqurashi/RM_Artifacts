#Simple Script to Remove Windows Artifacts
import winreg
from os import chmod,getlogin
from sys import platform
from ctypes import windll
import stat
from shutil import rmtree
from subprocess import run
class RE:
    
    def __init__(self):
        print("""
        
    ____  __  ___     ___         __  _ ____           __      
   / __ \/  |/  /    /   |  _____/ /_(_) __/___ ______/ /______
  / /_/ / /|_/ /    / /| | / ___/ __/ / /_/ __ `/ ___/ __/ ___/
 / _, _/ /  / /    / ___ |/ /  / /_/ / __/ /_/ / /__/ /_(__  ) 
/_/ |_/_/  /_/____/_/  |_/_/   \__/_/_/  \__,_/\___/\__/____/  
            /_____/                                            

        """)
        directroyPrefetch = "C:\\Windows\\Prefetch\\"
        directoryHistroy = "C:\\Users\\"+getlogin()+"\\AppData\\Local\\Microsoft\\Windows\\History"
        if windll.shell32.IsUserAnAdmin():
            if platform != "win32":
                exit()
            else:
                #Disable Prefetch From Registry
                regPath = "SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters"
                connect = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
                Prefetch= winreg.OpenKey(connect,regPath,0,winreg.KEY_ALL_ACCESS)
                winreg.SetValueEx(Prefetch,"EnablePrefetcher",0,winreg.REG_DWORD,0)
                winreg.SetValueEx(Prefetch,"EnableSuperfetch",0,winreg.REG_DWORD,0)
                winreg.CloseKey(connect)
                winreg.CloseKey(Prefetch)
                run(["powershell", "Set-Service -Name 'SysMain' -Status stopped -StartupType disabled"], capture_output=True)
                print("[+] Disable Prefetch From Registry")
                try:
                    chmod(directroyPrefetch, 0o777)
                    rmtree(directroyPrefetch, ignore_errors=True)
                    print("[+] PreFetch Directory Deleted Successfully")
                except:
                    print("[+] PreFetch Directory Already Deleted Successfully")
                #Disable Recent Files Opend From Registry
                regPathRecent = "SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer"
                connect = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
                Recent = winreg.OpenKey(connect,regPathRecent,0,winreg.KEY_ALL_ACCESS)
                winreg.SetValueEx(Recent,"NoRecentDocsHistory",0,winreg.REG_DWORD,1)
                print("[+] Disable History And Recent Files From Registry")
                try:
                    chmod(directoryHistroy, 0o777)
                    rmtree(directoryHistroy, ignore_errors=True)
                    run(["powershell", "Clear-RecycleBin -Force"], capture_output=True)
                    print("[+] History Directory Deleted Successfully")
                    print("[+] Recent Directory Deleted Successfully")
                except:
                     print("[+] History Directory Already Deleted Successfully")
                     print("[+] Recent Directory Deleted Successfully")
                
                
                
        else:
            print("Please Run As Administrator")
            
    
ob = RE()
