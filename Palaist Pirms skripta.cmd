@echo off
cls
 
echo Instale WinGet un tas vajadzigos komponentus...
powershell -Command "$progressPreference = 'silentlyContinue'; Invoke-WebRequest -Uri https://aka.ms/getwinget -OutFile Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle; Invoke-WebRequest -Uri https://aka.ms/Microsoft.VCLibs.x64.14.00.Desktop.appx -OutFile Microsoft.VCLibs.x64.14.00.Desktop.appx; Invoke-WebRequest -Uri https://github.com/microsoft/microsoft-ui-xaml/releases/download/v2.8.6/Microsoft.UI.Xaml.2.8.x64.appx -OutFile Microsoft.UI.Xaml.2.8.x64.appx; Add-AppxPackage Microsoft.VCLibs.x64.14.00.Desktop.appx; Add-AppxPackage Microsoft.UI.Xaml.2.8.x64.appx; Add-AppxPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle"
 
echo Installe Python...
winget install python --accept-package-agreements --accept-source-agreements
 
echo Python Installacija pabeigta.
 
echo Removing downloaded files...
del Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle
del Microsoft.VCLibs.x64.14.00.Desktop.appx
del Microsoft.UI.Xaml.2.8.x64.appx
echo Downloaded files removed.
 
echo Installe vajadzigos Python modulus...
pip install tk
 
echo Installacija complete.
 