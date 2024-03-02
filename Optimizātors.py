import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import subprocess

# Function to configure services
def configure_services(services):
    for service, config in services.items():
        command = f'sc config "{service}" start= {config}'
        try:
            subprocess.run(command, check=True, shell=True)
            print(f"Setting Service {service} to {config}")
        except subprocess.CalledProcessError as e:
            error_output = getattr(e, 'output', None)
            if error_output is not None and "Access is denied." in error_output.decode('utf-8'):
                print(f"Access denied while configuring {service}. Please run the script as administrator.")
            elif "FAILED 87" in str(e):
                # Error 87 indicates that the parameter is incorrect,
                # often due to manual intervention required
                config = "Manual"  # Change to "Manual" instead of "demand"
                command = f'sc config "{service}" start= {config}'
                try:
                    subprocess.run(command, check=True, shell=True)
                    print(f"Setting Service {service} to {config} due to manual intervention")
                except subprocess.CalledProcessError as manual_e:
                    print(f"Error occurred while configuring {service}: {manual_e}")
            else:
                print(f"Error occurred while configuring {service}: {e}")

# Function to disable unnecessary services
def disable_unnecessary_services():
    try:
        services_to_configure = {
    "AJRouter": "disabled",
    "Themes": "auto",
    "TieringEngineService": "demand",
    "TokenBroker": "demand",
    "TrkWks": "auto",
    "TroubleshootingSvc": "demand",
    "TrustedInstaller": "demand",
    "UevAgentService": "disabled",
    "UmRdpService": "demand",
    "UserManager": "auto",
    "UsoSvc": "demand",
    "VSS": "demand",
    "VacSvc": "demand",
    "VaultSvc": "auto",
    "W32Time": "demand",
    "WEPHOSTSVC": "demand",
    "WFDSConMgrSvc": "demand",
    "WMPNetworkSvc": "demand",
    "WManSvc": "demand",
    "WPDBusEnum": "demand",
    "WSearch": "delayed-auto",
    "WalletService": "demand",
    "WarpJITSvc": "demand",
    "WbioSrvc": "demand",
    "Wcmsvc": "auto",
    "WdiServiceHost": "demand",
    "WdiSystemHost": "demand",
    "WebClient": "demand",
    "Wecsvc": "demand",
    "WerSvc": "demand",
    "WiaRpc": "demand",
    "WinRM": "demand",
    "Winmgmt": "auto",
    "WlanSvc": "auto",
    "WpcMonSvc": "demand",
    "WpnService": "demand",
    "WwanSvc": "demand",
    "XblAuthManager": "demand",
    "XblGameSave": "demand",
    "XboxGipSvc": "demand",
    "XboxNetApiSvc": "demand",
    "autotimesvc": "demand",
    "bthserv": "demand",
    "camsvc": "demand",
    "cloudidsvc": "demand",
    "dcsvc": "demand",
    "defragsvc": "demand",
    "diagnosticshub.standardcollector.service": "demand",
    "diagsvc": "demand",
    "dmwappushservice": "demand",
    "dot3svc": "demand",
    "edgeupdate": "demand",
    "edgeupdatem": "demand",
    "fdPHost": "demand",
    "fhsvc": "demand",
    "hidserv": "demand",
    "icssvc": "demand",
    "iphlpsvc": "auto",
    "lfsvc": "demand",
    "lltdsvc": "demand",
    "lmhosts": "demand",
    "netprofm": "demand",
    "nsi": "auto",
    "p2psvc": "demand",
    "perceptionsimulation": "demand",
    "pla": "demand",
    "seclogon": "demand",
    "shpamsvc": "disabled",
    "smphost": "demand",
    "spectrum": "demand",
    "ssh-agent": "disabled",
    "svsvc": "demand",
    "swprv": "demand",
    "tzautoupdate": "disabled",
    "uhssvc": "disabled",
    "upnphost": "demand",
    "vds": "demand",
    "vmicguestinterface": "demand",
    "vmicheartbeat": "demand",
    "vmickvpexchange": "demand",
    "vmicrdv": "demand",
    "vmicshutdown": "demand",
    "vmictimesync": "demand",
    "vmicvmsession": "demand",
    "vmicvss": "demand",
    "wbengine": "demand",
    "wcncsvc": "demand",
    "webthreatdefsvc": "demand",
    "wercplsupport": "demand",
    "wisvc": "demand",
    "wlidsvc": "demand",
    "wlpasvc": "demand",
    "wmiApSrv": "demand",
    "workfolderssvc": "demand",
    "wuauserv": "demand",
    "ALG": "demand",
    "AppMgmt": "demand",
    "AppReadiness": "demand",
    "AppVClient": "disabled",
    "Appinfo": "demand",
    "AssignedAccessManagerSvc": "disabled",
    "AudioEndpointBuilder": "auto",
    "AudioSrv": "auto",
    "Audiosrv": "auto",
    "AxInstSV": "demand",
    "BDESVC": "demand",
    "BITS": "delayed-auto",
    "BTAGService": "demand",
    "BthAvctpSvc": "auto",
    "CDPSvc": "demand",
    "COMSysApp": "demand",
    "CertPropSvc": "demand",
    "CryptSvc": "auto",
    "CscService": "demand",
    "DPS": "auto",
    "DevQueryBroker": "demand",
    "DeviceAssociationService": "demand",
    "DeviceInstall": "demand",
    "Dhcp": "auto",
    "DiagTrack": "disabled",
    "DialogBlockingService": "disabled",
    "DispBrokerDesktopSvc": "auto",
    "DisplayEnhancementService": "demand",
    "DmEnrollmentSvc": "demand",
    "DoSvc": "delayed-auto",
    "DsSvc": "demand",
    "DsmSvc": "demand",
    "DusmSvc": "auto",
    "EFS": "demand",
    "EapHost": "demand",
    "EventLog": "auto",
    "EventSystem": "auto",
    "FDResPub": "demand",
    "FontCache": "auto",
    "FrameServer": "demand",
    "FrameServerMonitor": "demand",
    "GraphicsPerfSvc": "demand",
    "HvHost": "demand",
    "IKEEXT": "demand",
    "InstallService": "demand",
    "InventorySvc": "demand",
    "IpxlatCfgSvc": "demand",
    "KeyIso": "auto",
    "KtmRm": "demand",
    "LanmanServer": "auto",
    "LanmanWorkstation": "auto",
    "LicenseManager": "demand",
    "LxpSvc": "demand",
    "MSDTC": "demand",
    "MSiSCSI": "demand",
    "MapsBroker": "delayed-auto",
    "McpManagementService": "demand",
    "MixedRealityOpenXRSvc": "demand",
    "MsKeyboardFilter": "demand",
    "NaturalAuthentication": "demand",
    "NcaSvc": "demand",
    "NcbService": "demand",
    "NcdAutoSetup": "demand",
    "NetSetupSvc": "demand",
    "NetTcpPortSharing": "disabled",
    "Netlogon": "auto",
    "Netman": "demand",
    "NlaSvc": "demand",
    "PNRPAutoReg": "demand",
    "PNRPsvc": "demand",
    "PcaSvc": "demand",
    "PeerDistSvc": "demand",
    "PerfHost": "demand",
    "PhoneSvc": "demand",
    "PlugPlay": "demand",
    "PolicyAgent": "demand",
    "Power": "auto",
    "PrintNotify": "demand",
    "ProfSvc": "auto",
    "PushToInstall": "demand",
    "QWAVE": "demand",
    "RasAuto": "demand",
    "RasMan": "demand",
    "RemoteAccess": "disabled",
    "RemoteRegistry": "disabled",
    "RetailDemo": "demand",
    "RmSvc": "demand",
    "RpcLocator": "demand",
    "SCPolicySvc": "demand",
    "SCardSvr": "demand",
    "SDRSVC": "demand",
    "SEMgrSvc": "demand",
    "SENS": "auto",
    "SNMPTRAP": "demand",
    "SNMPTrap": "demand",
    "SSDPSRV": "demand",
    "SamSs": "auto",
    "ScDeviceEnum": "demand",
    "SensorDataService": "demand",
    "SensorService": "demand",
    "SensrSvc": "demand",
    "SessionEnv": "demand",
    "SgrmBroker": "auto",
    "SharedAccess": "demand",
    "SharedRealitySvc": "demand",
    "ShellHWDetection": "auto",
    "SmsRouter": "demand",
    "Spooler": "auto",
    "SstpSvc": "demand",
    "StiSvc": "demand",
    "StorSvc": "demand",
    "SysMain": "demand",
    "TapiSrv": "demand",
    "TermService": "auto",
}
        
        # Call the function to configure the services
        configure_services(services_to_configure)
        
        messagebox.showinfo("Success", "Unnecessary services disabled successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"CalledProcessError: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def run_dism_and_sfc_commands():
    try:
        # Run DISM command
        dism_command = 'DISM /Online /Cleanup-Image /RestoreHealth'
        subprocess.run(dism_command, shell=True, check=True)
        messagebox.showinfo("Success", "DISM command executed successfully!")
        
        # Run sfc /scannow command
        sfc_command = 'sfc /scannow'
        subprocess.run(sfc_command, shell=True, check=True)
        messagebox.showinfo("Success", "sfc /scannow command executed successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"CalledProcessError: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to remove specified bloatware
def remove_bloatware():
    try:
        # List of PowerShell commands to remove bloatware
        bloatware_commands = [
'Get-AppxPackage Microsoft.Microsoft3DViewer | Remove-AppxPackage',
'Get-AppxPackage *3dbuilder* | Remove-AppxPackage',
'Get-AppxPackage *windowscommunicationsapps* | Remove-AppxPackage',
'Get-AppxPackage *windowsalarms* | Remove-AppxPackage',
'Get-AppxPackage *windowscamera* | Remove-AppxPackage',
'Get-AppxPackage *Microsoft.GetHelp* -AllUsers | Remove-AppxPackage',
'Get-AppxPackage *getstarted* | Remove-AppxPackage',
'Get-AppxPackage *skypeapp* | Remove-AppxPackage',
'Get-AppxPackage *windowsmaps* | Remove-AppxPackage',
'Get-AppxPackage *solitairecollection* | Remove-AppxPackage',
'Get-AppxPackage *bingfinance* | Remove-AppxPackage',
'Get-AppxPackage *bingnews* | Remove-AppxPackage',
'Get-AppxPackage *windowsphone* | Remove-AppxPackage',
'Get-AppxPackage *bingsports* | Remove-AppxPackage',
'Get-AppxPackage *soundrecorder* | Remove-AppxPackage',
'Get-AppxPackage *bingweather* | Remove-AppxPackage',
'Get-AppxPackage Microsoft.XboxApp | Remove-AppxPackage',
'Get-AppxPackage Microsoft.XboxGamingOverlay | Remove-AppxPackage',
'Get-AppxPackage *Microsoft.Getstarted* | Remove-AppxPackage',
'Get-AppxPackage -allusers Microsoft.ToDo | Remove-AppxPackage',
'Get-AppxPackage -allusers *clipchamp* | Remove-AppxPackage',
'Get-AppxPackage -allusers *Terminal* | Remove-AppxPackage',
'Get-AppxPackage -allusers *Sticky* | Remove-AppxPackage',
'Get-AppxPackage -allusers *Phone* | Remove-AppxPackage',
'Get-AppxPackage -allusers *Feedback* | Remove-AppxPackage',
'Get-AppxPackage -allusers *Paint* | Remove-AppxPackage',
'Get-AppxPackage -allusers *quickassist* | Remove-AppxPackage',
'Get-AppxPackage -allusers *getstarted* | Remove-AppxPackage',
'Get-AppxPackage -allusers *getstarted* | Remove-AppxPackage',
'Get-AppxPackage -allusers *Terminal* | Remove-AppxPackage',
'Get-AppxPackage -allusers *Sticky* | Remove-AppxPackage',
'Get-AppxPackage -allusers *Phone* | Remove-AppxPackage',
'Get-AppxPackage -allusers *Feedback* | Remove-AppxPackage',
'Get-AppxPackage -allusers *Paint* | Remove-AppxPackage',
'Get-AppxPackage -allusers *quickassist* | Remove-AppxPackage',
'Get-AppxPackage -allusers *getstarted* | Remove-AppxPackage',
'Get-AppxPackage -allusers *getstarted* | Remove-AppxPackage',
'Get-AppxPackage Microsoft.*devhome* | Remove-AppxPackage',
'Get-AppxPackage Microsoft.*automate* | Remove-AppxPackage',
        ]
        
        # Execute each PowerShell command
        for command in bloatware_commands:
            subprocess.run(["powershell.exe", "-Command", command], shell=True, check=True)
        
        messagebox.showinfo("Success", "Bloatware removed successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"CalledProcessError: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to install Brave browser using winget
def install_brave():
    try:
        subprocess.run(["winget", "install", "-e", "--id", "Brave.Brave"])
        messagebox.showinfo("Success", "Brave browser installed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to install Firefox browser using winget
def install_firefox():
    try:
        subprocess.run(["winget", "install", "-e", "-i", "Mozilla.Firefox"])
        messagebox.showinfo("Success", "Firefox browser installed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to install Opera GX browser using winget
def install_opera_gx():
    try:
        subprocess.run(["winget", "install", "-e", "--id", "Opera.OperaGX"])
        messagebox.showinfo("Success", "Opera GX browser installed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to install Opera regular browser using winget
def install_opera_regular():
    try:
        subprocess.run(["winget", "install", "-e", "--id", "Opera.Opera"])
        messagebox.showinfo("Success", "Opera regular browser installed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to install Google Chrome browser using winget
def install_google_chrome():
    try:
        subprocess.run(["winget", "install", "-e", "-i", "Google.Chrome"])
        messagebox.showinfo("Success", "Google Chrome browser installed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to add context menu entry
def add_context_menu_entry():
    try:
        command = 'reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve'
        subprocess.run(command, shell=True, check=True)
        messagebox.showinfo("Success", "Context menu entry added successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to add context menu entry: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Optimizātors Rinalds Rižikovs.")

# Create a tabbed interface
tab_control = ttk.Notebook(root)

# Create tabs
tab_services = ttk.Frame(tab_control)
tab_browsers = ttk.Frame(tab_control)

tab_control.add(tab_services, text='Optimizācija.')
tab_control.add(tab_browsers, text='Pārlūki.')

tab_control.pack(expand=1, fill='both')

# Create buttons for service configuration
button_configure_services = tk.Button(tab_services, text="Izslēgt nevajadzīgos Procesus.", command=disable_unnecessary_services)
button_configure_services.pack(pady=20)

# Create button for adding context menu entry
button_add_context_menu = tk.Button(tab_services, text="Atgūt Windows 10 Konteksta Izvelni.", command=add_context_menu_entry)
button_add_context_menu.pack(pady=5)


# Create buttons for installing browsers
button_brave = tk.Button(tab_browsers, text="Instalet Brave.", command=install_brave)
button_brave.pack(pady=5)

button_firefox = tk.Button(tab_browsers, text="Installet Firefox.", command=install_firefox)
button_firefox.pack(pady=5)

button_opera_gx = tk.Button(tab_browsers, text="Instalet Opera GX.", command=install_opera_gx)
button_opera_gx.pack(pady=5)

button_opera_regular = tk.Button(tab_browsers, text="Instalet Opera.", command=install_opera_regular)
button_opera_regular.pack(pady=5)

button_chrome = tk.Button(tab_browsers, text="Instalet Google Chrome.", command=install_google_chrome)
button_chrome.pack(pady=5)

button_remove_specified_apps = tk.Button(tab_services, text="Noņemt nevajadzīgās aplikācijas, kas tika uzstāditas windows operētaja sistēmas instalācijas laikā.", command=remove_bloatware)
button_remove_specified_apps.pack(pady=5)

button_run_dism_sfc_commands = tk.Button(tab_services, text="Salabo sistemas beigots failus.", command=run_dism_and_sfc_commands)
button_run_dism_sfc_commands.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()