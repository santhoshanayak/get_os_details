#Author Santhosha Nayak <santhoshanayakk@gmail.com>
#Thank you https://endoflife.date
import platform
import requests
dataurl="https://endoflife.date/api/linux.json"

currnet_kernal=platform.release()
#print(currnet_kernal)
exact_version=currnet_kernal[0:4]
datavalues = requests.get(dataurl).json()
for a in datavalues:
    if a['cycle'] == exact_version:
        print('The installed kernel is: {}'.format(currnet_kernal),end='\n')
        print('The end of life of current kernel : {}'.format(a['eol'],end='\n'))
        print('The latest version in current series is : {}'.format(a['latest'],end='\n'))
        print('The latest version in release date : {}'.format(a['latestReleaseDate'],end='\n'))
