import requests

def auth_add_windows(USERNAME,PASSWORD,unique_id,ipdata):
        headers = {
            'X-Requested-With': 'curl',
        }

        params = {
            'action':'update',
            'id':f'{unique_id}',
            'add_ips': ipdata,
        }

        response = requests.get('https://qualysapi.qualys.com/api/2.0/fo/auth/windows/', headers=headers, params=params,
                                auth=(f'{USERNAME}', f'{PASSWORD}'))
        print(response.text)
        print(response.headers)
def add_auth_unix(USERNAME,PASSWORD,unique_id,ipdata):
        headers = {
            'X-Requested-With': 'curl',
        }
        iplist = open('processed_list.csv', 'rb').read()

        params = {
            'action':'update',
            'id':f'{unique_id}',
            'add_ips': ipdata,
        }

        response = requests.get('https://qualysapi.qualys.com/api/2.0/fo/auth/unix/', headers=headers, params=params,
                                auth=(f'{USERNAME}', f'{PASSWORD}'))
        print(response.text)
        print(response.headers)

