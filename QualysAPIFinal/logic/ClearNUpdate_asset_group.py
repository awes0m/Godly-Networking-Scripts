import requests,os

dellog_path = os.path.join(os.path.dirname('QualysAPIFinal\Logs\ApiLogs\Asset_group_deletion_log.xml'),'Asset_group_deletion_log.xml')
updatelog_path = os.path.join(os.path.dirname('QualysAPIFinal\Logs\ApiLogs\Asset_group_updation_log.xml'),'Asset_group_updation_log.xml')

def clear_asset_group(USERNAME,PASSWORD,unique_id):
        headers = {
            'X-Requested-With': 'Curl',
        }

        params = (
            ('action', 'edit'),
        )

        dataA = {
            'id': unique_id,
            'remove_ips': '10.0.0.0-10.255.255.255',
        }
        dataB = {
            'id': unique_id,
            'remove_ips': '128.0.0.0-192.0.0.255',
        }

        responseA = requests.post('https://qualysapi.qualys.com/api/2.0/fo/asset/group/', headers=headers,
                                  params=params,
                                  data=dataA, auth=(f'{USERNAME}', f'{PASSWORD}'))
        responseB = requests.post('https://qualysapi.qualys.com/api/2.0/fo/asset/group/', headers=headers,
                                  params=params,
                                  data=dataB, auth=(f'{USERNAME}', f'{PASSWORD}'))
        with open(dellog_path, 'w') as f:
            f.write(f'str({responseA.text})')
            f.write(f'str({responseA.headers})')
            f.write(f'str({responseB.text})')
            f.write(f'str({responseB.headers})')
            
def update_Asset_group(USERNAME,PASSWORD,unique_id,ipdata):
        headers = {
            'X-Requested-With': 'Curl',
        }

        params = (
            ('action', 'edit'),
        )
        

        data = {
            'id': unique_id,
            'add_ips': ipdata,
        }

        response = requests.post('https://qualysapi.qualys.com/api/2.0/fo/asset/group/', headers=headers, params=params,data=data, auth=(f'{USERNAME}', f'{PASSWORD}'))
        with open(updatelog_path, 'w') as f:
            f.write(f'str({response.text})')
            f.write(f'str({response.headers})')
