##PROJECT BLUE ROAD RUNNER 
##MODULE BLUE BOX

##v0.01 

## IMPORT LIBRARIES
import os

import numpy as np
import pandas as pd

#LOCATION DEFINATIONS
excel ="../Data/Main/Master.xlsx"

#VARIABALE DEFINATIONS


#IMPORT DATA
fin_data = pd.read_excel(excel, sheet_name = "Transactions1" )
fin_data = fin_data[~fin_data['category'].isna()]
acct = pd.read_excel(excel, sheet_name = "Acct" )
category = pd.read_excel(excel, sheet_name = "Category" )

#DUMP CSV FILES
fin_data.to_csv("../Data/Hold/findata.csv")
acct.to_csv("../Data/Hold/acct.csv")
category.to_csv("../Data/Hold/category.csv")

#UPLOAD TO GCS
os.system("gsutil cp ../Data/Hold/* gs://blue-road-runner-cloud-storage/blue-box/current-personal-finance")

