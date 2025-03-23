; Define installation
[Setup]
AppName=Sight
AppVersion=0.0.1
DefaultDirName={autopf}\Sight
SetupIconFile=Sight\Ui\SideKick.ico
LicenseFile=license.txt
DisableProgramGroupPage=yes

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional shortcuts:"
Name: "startmenuicon"; Description: "Create a Start Menu shortcut"; GroupDescription: "Additional shortcuts:"

; Files to be Installed
[Files]
Source:"Sight\*"; DestDir: "{autopf}\Sight"; Flags: ignoreversion recursesubdirs

; Create a Desktop Shortcut
[Icons]
Name: "{userdesktop}\Sight"; Filename: "{app}\Sight.exe"; WorkingDir: "{app}"; Tasks: desktopicon
Name: "{commonprograms}\Sight"; Filename: "{app}\Sight.exe"; Tasks: startmenuicon

; Add Uninstaller
[UninstallDelete]
Type: filesandordirs; Name: "{app}"

; Setup arduino cli TODO
[Run]
Filename: "cmd.exe"; Parameters: "/C cd /d ""{app}/installer"" && configure.exe"