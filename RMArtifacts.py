#Simple Script to Remove Windows Artifacts
import winreg
from os import chmod
from sys import platform
from ctypes import windll
import stat
from shutil import rmtree
from subprocess import run
class RE:
    
    def __init__(self):
        directroyPrefetch = "C:\\Windows\\Prefetch\\"
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
                #stop service SysMain
                run(["powershell", "Stop-Service -Name 'SysMain'"], capture_output=True)
                try:
                    chmod(directroyPrefetch, 0o777)
                    rmtree(directroyPrefetch, ignore_errors=True)
                    print("[+]PreFetch Directory Deleted Successfully")
                except:
                    print("[+] PreFetch Directory Already Deleted Successfully")
                
        else:
            print("Please Run As Administrator")


ob = RE()
