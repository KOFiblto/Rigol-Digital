@echo off
setlocal

:: Ask for the IP address
set /p IP="Enter IP address: "

:: Replace the IP address in the run.py file
powershell -Command "(Get-Content Rigol1000z\run.py) -replace 'TCPIP0::.*::INSTR', 'TCPIP0::%IP%::INSTR' | Set-Content Rigol1000z\run.py"

:: Run the Python script
python Rigol1000z\run.py

endlocal
