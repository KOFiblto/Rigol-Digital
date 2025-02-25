@echo off
setlocal

:ask_ip
:: Ask for the IP address
set /p IP="Enter IP address: "

:: Call the Python script in the tools folder to validate the IP address and replace it in run.py
python tools\validate_ip.py %IP%

:: Check the exit code from the Python script
if %errorlevel% neq 0 (
    echo Invalid IP address. Please enter a valid IP.
    goto ask_ip
) else (
    :: Run the Python script
    python Rigol1000z\run.py
)

endlocal
