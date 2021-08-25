# Update Host Asset/Add to environment
import requests

def add_ip(USERNAME,PASSWORD,data,enable_vm=1,enable_pc=1):
        headers = {
            'X-Requested-With': 'Curl',
            'Content-Type': 'text/csv',
        }

        params = (
            ('action', 'add'),
            ('enable_vm', f'{enable_vm}'),
            ('enable_pc', f'{enable_pc}'),
            ('tracking_method', 'IP'),
        )
        response = requests.post('https://qualysapi.qualys.com/api/2.0/fo/asset/ip/', headers=headers, params=params,
                                 data=data, auth=(f'{USERNAME}', f'{PASSWORD}'))

        with open('Hostassetlog.xml', 'w') as f:
            f.write(f'str({response.text})')
            f.write(f'str({response.headers})')