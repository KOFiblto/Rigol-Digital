@echo off
setlocal

:: Speichert das aktuelle Verzeichnis
set CUR_DIR=%CD%

:: Starte run.py mit IDLE aus dem Rigol1000z-Ordner und schließe CMD sofort
start "" pyw -m idlelib "%CUR_DIR%\Rigol1000z\run.py"

exit
