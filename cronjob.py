import requests
from datetime import datetime
import pathlib

now = datetime.now()
site = "https://b24-iu5stq.bitrix24.site/backend_test/"
this_dir = str(pathlib.Path(__file__).parent.resolve())

with open(this_dir + '/cronjob_output.txt', 'a+') as f:
    try:
        response = requests.get(site)
        f.write(f"{now} - Website is reachable \n")
    except:
        f.write(f"{now} - Website is unreachable \n")
    f.close()
