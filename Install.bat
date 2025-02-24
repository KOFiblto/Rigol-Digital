@echo off
setlocal enabledelayedexpansion

:: Speichert das aktuelle Verzeichnis
set CUR_DIR=%CD%

:: Prüft, ob Python 3.13 installiert ist
py -3.13 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3.13 nicht gefunden. Installiere nun Python 3.13. Bitte warten Sie, während es heruntergeladen und installiert wird...
    
    :: Download und Installation von Python 3.13
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe -OutFile python-3.13.0-amd64.exe"
    
    echo Installiere Python 3.13...
    start /wait python-3.13.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
    
    del python-3.13.0-amd64.exe
    
    echo Python 3.13 wurde erfolgreich installiert.
    echo Starte das Skript jetzt neu...

    :: Neustart des Skripts
    start "" "%~f0"
    exit /b
)



:: Erstelle eine virtuelle Umgebung im aktuellen Verzeichnis
py -3.13 -m venv "%CUR_DIR%\pyLab"

:: Aktiviere die virtuelle Umgebung
call "%CUR_DIR%\pyLab\Scripts\activate.bat"

:: Installiere benötigte Python-Pakete
py -m pip install --upgrade pip
py -m pip install wheel matplotlib tqdm pyvisa pyvisa-py

:: Navigiere in den Rigol1000z-Ordner und installiere das Paket
cd /d "%CUR_DIR%\Rigol1000z"
py -m pip install -e .

:: Zurück zum ursprünglichen Verzeichnis
cd /d "%CUR_DIR%"

echo Setup abgeschlossen!
pause
