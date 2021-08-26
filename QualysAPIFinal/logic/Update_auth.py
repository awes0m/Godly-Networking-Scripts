import requests,os

unixAuthlog_path=os.path.join(os.path.dirname("QualysAPIFinal/Logs/ApiLogs/UnixAuth_log.xml"),'UnixAuth_log.xml')
windowsAuthlog_path=os.path.join(os.path.dirname('QualysAPIFinal\Logs\ApiLogs\WindowsAuth_log.xml'),'WindowsAuth_log.xml')

def auth_add_windows(USERNAME,PASSWORD,unique_id,ipdata):
        headers = {
            'X-Requested-With': 'curl',
        }

        params = {
            'action':'update',
            'ids':unique_id,
            'add_ips': ipdata,
        }

        response = requests.post('https://qualysapi.qualys.com/api/2.0/fo/auth/windows/', headers=headers, params=params,auth=(f'{USERNAME}', f'{PASSWORD}'))
        with open(windowsAuthlog_path,'w') as f:
            f.write(f'str({response.text})')
            f.write(f'str({response.headers})')
            
            
            
def add_auth_unix(USERNAME,PASSWORD,unique_id,ipdata):
        headers = {
            'X-Requested-With': 'curl',
        }
        iplist = open('processed_list.csv','rb').read()

        params = {
            'action':'update',
            'ids':unique_id,
            'add_ips': ipdata,
        }

        response = requests.post('https://qualysapi.qualys.com/api/2.0/fo/auth/unix/', headers=headers, params=params,auth=(f'{USERNAME}', f'{PASSWORD}'))
        
        
        with open(unixAuthlog_path,"w") as f:
            f.write(f'str({response.text})')
            f.write(f'str({response.headers})')

