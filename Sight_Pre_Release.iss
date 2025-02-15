; Define installation
AppName=Sight
AppVersion=0.0.1
DefaultDirName={pf}\SideKick
DefaultGroupName=SideKick
OutputDir=.
OutputBaseFilename=MyPythonApp_Setup
Compression=lzma
SolidCompression=yes
SetupIconFile=icon.ico

; Files to be Installed
[Files]
Source: "dist\SideKick.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

; Create a Desktop Shortcut
[Icons]
Name: "{commondesktop}\Sight"; Filename: "{app}\Sight.exe"

; Add Uninstaller
;[UninstallDelete]
;Type: filesandordirs; Name: "{app}"

; Run Post-Install Commands
;[Run]
;Filename: "{app}\MyPythonApp.exe"