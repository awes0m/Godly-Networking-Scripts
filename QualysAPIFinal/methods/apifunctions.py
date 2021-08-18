import requests


class ApiFunction:
    USERNAME = "wamsn_qa1"
    PASSWORD = "ruhn5rPWvsjGpJF"
    endpoint_url = "https://qualysapi.qualys.com/api/2.0/fo/session/"
    session_ID = None
    unique_id = '1525419'

    def __init__(self, username, password, uniqueid):
        self.USERNAME = username,
        self.PASSWORD = password,
        self.unique_id = uniqueid,

    # Update Host Asset-(Done)
    def add_ip(self):
        USERNAME = self.USERNAME,
        PASSWORD = self.PASSWORD,
        headers = {
            'X-Requested-With': 'Curl',
            'Content-Type': 'text/csv',
        }

        params = (
            ('action', 'add'),
            ('enable_vm', '1'),
            ('enable_pc', '1'),
            ('tracking_method', 'IP'),
        )
        data = open('processed_list.csv', 'rb').read()  # -----------------------TODO Create file- (not done)
        response = requests.post('https://qualysapi.qualys.com/api/2.0/fo/asset/ip/', headers=headers, params=params,
                                 data=data, auth=(f'{USERNAME}', f'{PASSWORD}'))

        with open('Hostassetlog.xml', 'w') as f:
            f.write(f'str({response.text})')
            f.write(f'str({response.headers})')

    # Update Asset Group-(Done)
    def clear_asset_group(self):
        USERNAME = self.USERNAME,
        PASSWORD = self.PASSWORD,
        unique_id = self.unique_id,
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
        with open('Assetgroupdeletionlog.xml', 'w') as f:
            f.write(f'str({responseA.text})')
            f.write(f'str({responseA.headers})')
            f.write(f'str({responseB.text})')
            f.write(f'str({responseB.headers})')

    def update_Asset_group(self):
        USERNAME = self.USERNAME,
        PASSWORD = self.PASSWORD,
        unique_id = self.unique_id,
        headers = {
            'X-Requested-With': 'Curl',
        }

        params = (
            ('action', 'edit'),
        )
        iplist = open('processed_list.csv', 'rb').read()

        data = {
            'id': unique_id,
            'add_ips': iplist,
        }

        response = requests.post('https://qualysapi.qualys.com/api/2.0/fo/asset/group/', headers=headers, params=params,
                                 data=data, auth=(f'{USERNAME}', f'{PASSWORD}'))
        with open('Assetgrouplog.xml', 'w') as f:
            f.write(f'str({response.text})')
            f.write(f'str({response.headers})')

    #TODO 4-Update Authentication--(Not tested)
    def auth_add_windows(self):
        USERNAME = self.USERNAME,
        PASSWORD = self.PASSWORD,
        unique_id = self.unique_id,
        headers = {
            'X-Requested-With': 'curl',
        }
        iplist = open('processed_list.csv', 'rb').read()



        params = {
            'action':'update',
            'id':f'{unique_id}',
            'add_ips': iplist,
        }

        response = requests.get('https://qualysapi.qualys.com/api/2.0/fo/auth/windows/', headers=headers, params=params,
                                auth=(f'{USERNAME}', f'{PASSWORD}'))
        print(response.text)
        print(response.headers)
    def add_auuth_unix(self):
        USERNAME = self.USERNAME,
        PASSWORD = self.PASSWORD,
        unique_id = self.unique_id,
        headers = {
            'X-Requested-With': 'curl',
        }
        iplist = open('processed_list.csv', 'rb').read()

        params = {
            'action':'update',
            'id':f'{unique_id}',
            'add_ips': iplist,
        }

        response = requests.get('https://qualysapi.qualys.com/api/2.0/fo/auth/unix/', headers=headers, params=params,
                                auth=(f'{USERNAME}', f'{PASSWORD}'))
        print(response.text)
        print(response.headers)

