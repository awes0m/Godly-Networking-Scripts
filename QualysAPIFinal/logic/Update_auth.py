import requests,os,datetime





def auth_add_windows(USERNAME,PASSWORD,unique_id,ipdata,file_id):
    windowsAuthlog_path=os.path.join(os.path.dirname('QualysAPIFinal\Logs\ApiLogs\WindowsAuth_log.xml'),f'WindowsAuth_{file_id}_log.xml')
    
    
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
            
            
            
def add_auth_unix(USERNAME,PASSWORD,unique_id,ipdata,file_id):
    
    unixAuthlog_path=os.path.join(os.path.dirname("QualysAPIFinal/Logs/ApiLogs/UnixAuth_log.xml"),f'UnixAuth_{file_id}_log.xml')
    
    
    headers = {
        'X-Requested-With': 'curl',
    }

    params = {
        'action':'update',
        'ids':unique_id,
        'add_ips': ipdata,
    }

    response = requests.post('https://qualysapi.qualys.com/api/2.0/fo/auth/unix/', headers=headers, params=params,auth=(f'{USERNAME}', f'{PASSWORD}'))
        
        
    with open(unixAuthlog_path,"w") as f:
        f.write(f'str({response.text})')
        f.write(f'str({response.headers})')

