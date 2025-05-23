; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Gerenciador BackUp"
#define MyAppVersion "0.0.1"
#define MyAppPublisher "fernandoncidade"
#define MyAppURL "https://github.com/fernandoncidade"
#define MyAppExeName "Gerenciador BackUp.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{F521D749-A4B2-4C23-9E81-D5873AC40F55}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
UninstallDisplayName={#MyAppName}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}
; "ArchitecturesAllowed=x64compatible" specifies that Setup cannot run
; on anything but x64 and Windows 11 on Arm.
ArchitecturesAllowed=x64compatible
; "ArchitecturesInstallIn64BitMode=x64compatible" requests that the
; install be done in "64-bit mode" on x64 or Windows 11 on Arm,
; meaning it should use the native 64-bit Program Files directory and
; the 64-bit view of the registry.
ArchitecturesInstallIn64BitMode=x64compatible
DisableProgramGroupPage=yes
; Remover referências a arquivos que não existem
;InfoBeforeFile=CAMINHO_PARA_ARQUIVO_INFO.txt
;LicenseFile=CAMINHO_PARA_ARQUIVO_LICENCA.txt
; Uncomment the following line to run in non administrative install mode (install for current user only).
;PrivilegesRequired=lowest
OutputDir=C:\Users\ferna\WORK\Projetos_Python\Manager_Compression_PySide6_v.0.0.1\dist
OutputBaseFilename=Gerenciador_BackUp_Windows_x64_setup_v0.0.1
SetupIconFile=C:\Users\ferna\WORK\Projetos_Python\Manager_Compression_PySide6_v.0.0.1\icones\Manager-BackUp.ico
SolidCompression=yes
WizardStyle=modern
; Simplificar para apenas português, já que não temos os arquivos de tradução
ShowLanguageDialog=no
; Adicionar suporte explícito para instalação silenciosa
AllowNoIcons=yes
DisableReadyPage=yes
DisableFinishedPage=no

[Languages]
; Usar apenas o português brasileiro, já que aparentemente é o idioma principal do aplicativo
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[CustomMessages]
; Mensagens personalizadas em português
brazilianportuguese.InstallFor=Instalar para
brazilianportuguese.AllUsers=Todos os usuários
brazilianportuguese.JustMe=Apenas para mim
brazilianportuguese.CreateDesktopIcon=Criar ícone na Área de Trabalho
brazilianportuguese.LaunchApp=Iniciar {#MyAppName} após a instalação

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\ferna\WORK\Projetos_Python\Manager_Compression_PySide6_v.0.0.1\dist\Gerenciador BackUp\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\ferna\WORK\Projetos_Python\Manager_Compression_PySide6_v.0.0.1\dist\Gerenciador BackUp\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
;Registry data for the application
Root: HKLM; Subkey: "SOFTWARE\Gerenciador BackUp"; Flags: uninsdeletekeyifempty
Root: HKLM; Subkey: "SOFTWARE\Gerenciador BackUp"; ValueType: string; ValueName: "InstallPath"; ValueData: "{app}"; Flags: uninsdeletevalue
Root: HKLM; Subkey: "SOFTWARE\Gerenciador BackUp"; ValueType: string; ValueName: "Version"; ValueData: "0.0.1"; Flags: uninsdeletevalue

; Menu de contexto para pastas
Root: HKCR; Subkey: "Directory\shell\GerenciadorBackUp"; Flags: uninsdeletekeyifempty
Root: HKCR; Subkey: "Directory\shell\GerenciadorBackUp"; ValueType: string; ValueName: ""; ValueData: "Comprimir com Gerenciador BackUp"; Flags: uninsdeletevalue
Root: HKCR; Subkey: "Directory\shell\GerenciadorBackUp"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\icones\Manager-BackUp.ico"; Flags: uninsdeletevalue
Root: HKCR; Subkey: "Directory\shell\GerenciadorBackUp\command"; Flags: uninsdeletekeyifempty
Root: HKCR; Subkey: "Directory\shell\GerenciadorBackUp\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""; Flags: uninsdeletevalue

; Menu de contexto para o fundo do Explorer
Root: HKCR; Subkey: "Directory\Background\shell\GerenciadorBackUp"; Flags: uninsdeletekeyifempty
Root: HKCR; Subkey: "Directory\Background\shell\GerenciadorBackUp"; ValueType: string; ValueName: ""; ValueData: "Abrir Gerenciador BackUp"; Flags: uninsdeletevalue
Root: HKCR; Subkey: "Directory\Background\shell\GerenciadorBackUp"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\icones\Manager-BackUp.ico"; Flags: uninsdeletevalue
Root: HKCR; Subkey: "Directory\Background\shell\GerenciadorBackUp\command"; Flags: uninsdeletekeyifempty
Root: HKCR; Subkey: "Directory\Background\shell\GerenciadorBackUp\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"""; Flags: uninsdeletevalue

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
; Adicionar acesso completo para todos os usuários
Filename: "{sys}\icacls.exe"; Parameters: """{app}"" /grant *S-1-5-32-545:(OI)(CI)F"; Flags: runhidden; Description: "Configurando permissões..."
; Iniciar aplicativo após instalação
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent; WorkingDir: "{app}"

; Código para desinstalação completa
[Code]
procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
var
  AppPath: string;
begin
  // Executar apenas no final da desinstalação
  if CurUninstallStep = usPostUninstall then
  begin
    // Caminho do aplicativo
    AppPath := ExpandConstant('{app}');
    
    // Verificar se o diretório ainda existe e remover completamente
    if DirExists(AppPath) then
      DelTree(AppPath, True, True, True);
  end;
end;

[ReturnCodes]
; Códigos de retorno personalizados
0=Success
6000=UserCancelled
6001=AppAlreadyExists
6002=AnotherInstallationRunning
6003=DiskSpaceFull
6004=RebootRequired
6005=NetworkFailure_DownloadError