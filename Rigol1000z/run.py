import pyvisa as visa
from Rigol1000z import Rigol1000z
from Rigol1000z.constants import *
from time import sleep
import os

# https://github.com/AlexZettler/Rigol1000z

rm = visa.ResourceManager()

##### README #####
# Hier ist die IP des Oszilloskops einzugeben
# dazu: Utility -> EA Einstellungen -> LAN Einstellung -> Config -> DHCP aktivieren
# dann: "IP Address" abschreiben bzw. den String unter "VISA Address" in der nächsten Zeile einsetzen
instrument = rm.open_resource("TCPIP0::172.16.62.104::INSTR")
print(f"Using " + instrument.query("*IDN?") )


def get_next_filename(folder: str, prefix: str, extension: str) -> str:
    os.makedirs(folder, exist_ok=True)
    counter_file = os.path.join(folder, "counter.txt")
    
    # Load or initialize counter
    if os.path.exists(counter_file):
        with open(counter_file, "r") as f:
            counter = int(f.read().strip())
    else:
        counter = 1
    
    filename = os.path.join(folder, f"{prefix}{counter:03d}.{extension}")
    
    # Increment and save counter
    with open(counter_file, "w") as f:
        f.write(str(counter + 1))
    
    return filename

with Rigol1000z(instrument) as oszi:
    #### README: reset und autoscale nur EINMAL nötig, danach auskommentieren
    #oszi.ieee488.reset()
    #oszi.autoscale()
    ####
    
    oszi.run()  # Run the scope if not already

    # enable both channels
    for ch in range(1, 2):
        oszi[ch].enabled = True  # Enable the channel

    # stop before getting data
    oszi.stop()
    
    # Generate unique filename
    filename = get_next_filename("channels", "channels", "csv")
    oszi.get_data(EWaveformMode.Raw, filename)  # Collect and save waveform data
