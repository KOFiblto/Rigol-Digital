# Free Custom Version of AlexZettler's Rigol1000z Repository

This is a free custom version, for the private use, of the AlexZettlers repositor,[Rigol1000z](https://github.com/AlexZettler/Rigol1000z), which is a fork of jeanyvesb9s repository [Rigol1000z](https://github.com/jeanyvesb9/Rigol1000z), which is a fork of the original from jtambasco [RigolOscilloscope](https://github.com/jtambasco/RigolOscilloscope). It features an `Install.bat` that installs all dependencies and a `Run.bat` that runs the program.

## Install Guide:

### 1) Install Git (Skip if already installed)
   a) Download Git from here: [https://git-scm.com/downloads/win](https://git-scm.com/downloads/win)  
   b) Run the downloaded `.exe` file.

### 2) Install Python 3.13
   You can install Python from the Microsoft Store or download it directly from [Python.org](https://www.python.org/downloads/).

### 3) Choose a directory for the project
   Select a location where you want to store the project files (e.g., `C:\tools`).

### 4) Open a Console in the directory:
   - Right-click inside the folder and select **"Open in Terminal"**.

### 5) In the Console, run the following command to clone the repository:
   ```bash
   git clone https://github.com/KOFiblto/Rigol-Digital
```
### 8) Finish Install
1) In the Folder, start the Install.bat, and wait for it to say that it is finished
2) Start Run.bat, to start the programm.
3) Input the IP into the code that is displayed, in Row 14
4) On the top click Run -> Run Method

### 9) Input IP of Oscilloscope

#### Read IP from Oscilloscope:
1. Utility -> EA Settings -> LAN Settings -> Config -> Enable DHCP

#### Set IP in Program:
1. Start `Run.bat`
2. Go to line 14 and enter IP in that line:
   ```python
   instrument = rm.open_resource("TCPIP0::172.16.62.104::INSTR")
                                                \___________/
                                                Input IP here



## Lizense of jeanyvesb9:
MIT License

Copyright (c) for portions of the project are held by jtambasco, 2017 (original project creator). All other copyright (c) for the project are held by Jean Yves Beaucamp, 2019.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
