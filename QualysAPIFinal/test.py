from logic.Add_ip import add_ip
import requests


USERNAME = "wamsn_qa1"
PASSWORD = "WlqZwBKh7Fn72pUr"
unique_id="4712898"


with open("processedip_list.txt",'r') as df:
                data=df.read()             
                       
def update_Asset_group(USERNAME,PASSWORD,unique_id,data):
        headers = {
            'X-Requested-With': 'Curl',
        }

        params = (
            ('action', 'edit'),
        )
        

        data = {
            'id': unique_id,
            'add_ips': data,
        }

        response = requests.post('https://qualysapi.qualys.com/api/2.0/fo/asset/group/', headers=headers, params=params,
                                 data=data, auth=(f'{USERNAME}', f'{PASSWORD}'))
        with open('Assetgrouplog.xml', 'w') as f:
            f.write(f'str({response.text})')
            f.write(f'str({response.headers})')
        print("done !!")

update_Asset_group(USERNAME,PASSWORD,unique_id,data)
