"""
This file no longer works due to undefined dependencies and Rigol1000z library rewrite.
# todo: rewrite this in order to adhere to pep8, and use new library interface
"""

import visa
import rigol1000z
from tqdm import tqdm
import numpy as np
import keyboard
import time


class BodePlot_Point:
    def __init__(self, vin, vout, delay, frequency):
        self.vin = vin
        self.vout = vout
        self.delay = delay
        self.frequency = frequency

        self.phase = (delay * frequency) * 2 * np.pi
        self.H = 20 * np.log10(vout / vin)


def captureBodePlot(scope, num, time_total_ms=4000, time_setup_ms=1400):
    '''
    Captures the amplitude of signals on channel 1 (Vin) and 2 (Vout), the time delay 
    between the signals, and the frequency of the signal on Channel 1. It repeats the 
    measurement 'num' times, every 'time_total_ms' milliseconds, with 'time_setup_ms'
    milliseconds given to change the frequency setting in the signal generator 
    connected to the circuit. After the setup time, the measurements statistics are
    cleared and the following measurement begins.
    
    In order to stop the measurement before the completion of 'num' iterations and still 
    retrieve the measurements already made, press 'q' at any time.
    
    Args:
        num (int): The number of times to repeat the measurements
        time_total_ms (int): The time (in milliseconds) between measurements. Default 
                             is 4000 (4 seconds).
        time_setup_ms (int): The time between the ending of a measurement, and the begining
                             of the next measurement (time to change the frequency setting of 
                             the generator). Default is 1400 (1.4 seconds).
    
    Returns:
        np.array() of BodePlot_Points with the measurements.
    '''
    scope.visa_write(':MEASure:COUNter:SOURce CHANnel1')
    scope.visa_write(':MEASure:SETup:DSA CHANnel1')
    scope.visa_write(':MEASure:SETup:DSB CHANnel2')
    scope.visa_write(':MEASure:STATistic:DISPlay ON')
    scope.visa_write(':MEASure:STATistic:MODE DIFFerence')
    scope.visa_write(':MEASure:STATistic:ITEM VPP,CHANnel1')
    scope.visa_write(':MEASure:STATistic:ITEM VPP,CHANnel2')
    scope.visa_write(':MEASure:STATistic:ITEM RDELay')

    data = []

    mills_time = lambda: int(round(time.time() * 1000))
    numPointsTaken = 0
    lastMeasurement = mills_time()
    inSetup = True
    with tqdm(total=num) as pbar:
        while True:
            try:
                if keyboard.is_pressed('q'):
                    break
                else:
                    timeNow = mills_time()
                    if inSetup:
                        if timeNow >= lastMeasurement + time_setup_ms:
                            inSetup = False
                            scope.visa_write(':MEASure:STATistic:RESet')
                    elif timeNow >= lastMeasurement + time_total_ms:
                        vin = float(scope.visa_ask(':MEASure:STATistic:ITEM? AVERages,VPP,CHANnel1'))
                        vout = float(scope.visa_ask(':MEASure:STATistic:ITEM? AVERages,VPP,CHANnel2'))
                        delay = float(scope.visa_ask(':MEASure:STATistic:ITEM? AVERages,RDELay'))
                        freq = float(scope.visa_ask(':MEASure:COUNter:VALue?'))

                        data += [BodePlot_Point(vin, vout, delay, freq)]

                        pbar.update(1)
                        numPointsTaken += 1
                        if numPointsTaken == num:
                            break
                        lastMeasurement = mills_time()
                        inSetup = True
            except:
                break

    return data


rm = visa.ResourceManager()
print('VISA Resources: ', rm.list_resources())

scope = rm.open_resource(rm.list_resources()[0])
rigolScope = Rigol1000z.Rigol1000z(scope)
print('ID: ', rigolScope.get_id())

data = captureBodePlot(rigolScope, 10)

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
#                           DATA PROCESSING AND GRAPHING GOES HERE
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

scope.close()
