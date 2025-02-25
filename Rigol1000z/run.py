import pyvisa as visa
from Rigol1000z import Rigol1000z
from Rigol1000z.constants import *
from time import sleep, strftime
import os

# https://github.com/AlexZettler/Rigol1000z

rm = visa.ResourceManager()

##### README #####
# Hier ist die IP des Oszilloskops einzugeben
# dazu: Utility -> EA Einstellungen -> LAN Einstellung -> Config -> DHCP aktivieren
# dann: "IP Address" abschreiben bzw. den String unter "VISA Address" in der nächsten Zeile einsetzen
instrument = rm.open_resource("TCPIP0::172.16.58.70::INSTR")
print(f"Using " + instrument.query("*IDN?"))

def get_next_filename(folder: str, prefix: str, extension: str) -> str:
    os.makedirs(folder, exist_ok=True)
    timestamp = strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(folder, f"{prefix}_{timestamp}.{extension}")
    return filename

with Rigol1000z(instrument) as oszi:

    #### README: reset und autoscale nut EINMAL nötig, danach auskommentieren
    #oszi.ieee488.reset()
    #oszi.autoscale()
    ####
    
    oszi.run()  # Run the scope if not already

    # enable both channels
    for ch in range(1, 2):
        oszi[ch].enabled = True  # Enable the channel

    # Set the horizontal timebase
    #oszi.timebase.mode = ETimebaseMode.Main  # Set the timebase mode to main (normal operation)
    #oszi.timebase.scale = 10E-6  # Set the timebase scale in seconds / div
        
    # we can set the y axis scale in V / div
    #oszi[1].scale_v = 2

    # stop before getting data
    oszi.stop()
    
    #Screenshot 
    screenshot_filename = get_next_filename("screenshots", "screenshot", "png")
    oszi.get_screenshot(screenshot_filename)  # Save the screenshot with the generated filename 
    
    #Channels
    channel_filename = get_next_filename("channels", "channels", "csv")
    oszi.get_data(EWaveformMode.Raw, channel_filename)  # Collect and save waveform data from all enabled channels
