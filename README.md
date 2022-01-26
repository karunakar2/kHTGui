# kHTGui
GUI to enable user selection of measurement and station in kHTConnector module.

# Helper tool for PowerBI users
If you're planning to import data into powerBI using the kHilltopConnector module (https://github.com/hawkes-bay-rc/kHilltopConnector)  
1. click getdata option from the ribbon
2. Select other in filter menu and select python script
3. Use the following code in the script window

import kHTGui
selection = kHTGui.kHTGui()
import kHilltopConnector as kHK
kHTop = kHK.kHilltopConnector(apiUrl='https://data.hbrc.govt.nz/Envirodata/EMAR.hts',refreshInterval=24*3600)
kHTop.selectMeasurement = selection.measurementAndSite['selectMeasurement']
kHTop.selectSite = selection.measurementAndSite['selectSite']
data = kHTop.fetchData(fetchYearsAtATime=0,scaleFactor=1000)

Hope it helps

No warranty or guarantee. 
