@echo off
setlocal enabledelayedexpansion

:: Speichert das aktuelle Verzeichnis
set CUR_DIR=%CD%

:: Prüft, ob Python 3.13 installiert ist
py -3.13 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3.13 nicht gefunden. Bitte installiere es von https://www.python.org/downloads/ und starte dieses Skript erneut.
    pause
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

:: Installiere PySide6 und die Abhängigkeiten für das Qt-Projekt
py -m pip install PySide6

:: Optional: Alle Pakete im aktuellen virtuellen Umfeld auflisten
py -m pip freeze

:: Zurück zum ursprünglichen Verzeichnis
cd /d "%CUR_DIR%"

echo Setup abgeschlossen!
pause
