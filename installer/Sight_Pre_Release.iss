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
Source:"dist"; DestDir: "{userdocuments}\Sight"; Flags: ignoreversion

; Create a Desktop Shortcut
[Icons]
Name: "{commondesktop}\Sight"; Filename: "{app}\Sight.exe"; WorkingDir: "{app}";
Name: "{commonprograms}\Sight"; Filename: "{app}\Sight.exe";

; Add Uninstaller
;[UninstallDelete]
;Type: filesandordirs; Name: "{app}"

; Setup arduino cli
[Run]
Filename: "{app}\MyPythonApp.exe"