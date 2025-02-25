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

:: Installiere benötigte Python-Pakete (verwende den Python-Interpreter aus der virtuellen Umgebung)
python -m pip install --upgrade pip
python -m pip install wheel matplotlib tqdm pyvisa pyvisa-py
python -m pip install pandas

:: Navigiere in den Rigol1000z-Ordner und installiere das Paket
cd /d "%CUR_DIR%\Rigol1000z"
python -m pip install -e .

:: Installiere PySide6 und die Abhängigkeiten für das Qt-Projekt
python -m pip install PySide6

:: Optional: Alle Pakete im aktuellen virtuellen Umfeld auflisten
python -m pip freeze

:: Zurück zum ursprünglichen Verzeichnis
cd /d "%CUR_DIR%"

echo Setup abgeschlossen!
pause
