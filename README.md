# Free Custom Version of AlexZettler's Rigol1000z Repository

This is my custom version, for private use, of AlexZettler's repository, [Rigol1000z](https://github.com/AlexZettler/Rigol1000z), which is a fork of jeanyvesb9's repository [Rigol1000z](https://github.com/jeanyvesb9/Rigol1000z), which is a fork of the original from jtambasco [RigolOscilloscope](https://github.com/jtambasco/RigolOscilloscope).  

It features:  
- `Install.bat` to install all dependencies  
- `Change_IP.bat` to change the IP  
- `Run.bat` to start the program  
---


## Install Guide

<details>
  <summary><b>Install Python 3.13</b>(Skip if already installed)</summary>

  1. Install Python Version 3.13 from the [Microsoft Store](https://apps.microsoft.com/detail/9PNRBTZXMB4Z?hl=en-us&gl=AT&ocid=pdpshare) or download it from [Python.org](https://www.python.org/downloads/) or directly from [here](https://www.python.org/ftp/python/3.13.0/python-3.13.0.exe)
  2. Run the downloaded `.exe` file. 

</details>

<details>
  <summary><b>Install Rigol-Digital with Git</b></summary>
  

  1. Install Git (Skip if already installed)

  - Download Git from here: [https://git-scm.com/downloads/win](https://git-scm.com/downloads/win)  
  - Run the downloaded `.exe` file.  

  3. Choose a directory for the project (e.g., `C:\tools`).  
  4. Open a terminal in that directory:  
     - Right-click inside the folder -> **"Show more Options"** -> **"Open GIT Bash here"**.  
  5. Run the following command:  

     ```bash
     git clone https://github.com/KOFiblto/Rigol-Digital
     ```

  6. Run `Install.bat` and wait for the installation to complete.  

</details> 

<details>
  <summary><b>Install Rigol-Digital without Git</b></summary>

  1. Go to the Release Tab of this Github and search for the latest working release ([here](https://github.com/KOFiblto/Rigol-Digital/releases/tag/WORKING))
  2. Download the zip File
  3. Go into your Downloads, right-click the zip and click **"Extract All..."** and then **"Extract"**
  4. Choose a directory (Folder) for the project (e.g., `C:\tools`).  
  5. Go back to your Downloads folder, and copy the extracted Folder to the new Location 
  9. Run `Install.bat` and wait for the installation to complete.  

</details> 

<details> 
  <summary><b>Start Program</b></summary>

  1. Open the project folder.  
  2. Run `Run.bat`.  
  3. In the program, go to **Run → Run Module**.  

</details> 

<details> 
  <summary><b>Change IP</b></summary>

  1. Connect the oscilloscope to the network via a LAN cable.  
  2. Ensure your PC/Laptop is on the same network.  
  3. On the Oscilloscope, go to **Utility → EA Settings → LAN Settings → Config → Enable DHCP**.  
  4. Start `Change_IP.bat` and enter the oscilloscope's IP.  

</details>

---

## License

<details> 
  <summary><b>MIT License (jeanyvesb9)</b></summary>

  Copyright (c) for portions of the project are held by jtambasco, 2017 (original project creator).  
  All other copyrights (c) for the project are held by Jean Yves Beaucamp, 2019.  

  Permission is hereby granted, free of charge, to any person obtaining a copy  
  of this software and associated documentation files (the "Software"), to deal  
  in the Software without restriction, including without limitation the rights  
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
  copies of the Software, and to permit persons to whom the Software is  
  furnished to do so, subject to the following conditions:  

  The above copyright notice and this permission notice shall be included in all  
  copies or substantial portions of the Software.  

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,  
  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR  
  PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE  
  LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,  
  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE  
  USE OR OTHER DEALINGS IN THE SOFTWARE.  

</details>
