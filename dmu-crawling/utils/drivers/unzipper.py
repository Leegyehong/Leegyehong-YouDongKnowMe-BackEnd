import sys
sys.path.append('.')

import zipfile
import os
from pathlib import Path
import argparse
import platform

def path_finder():
    root = Path('.')
    dir_path = f'{root}\\utils\\drivers'
    print(str(dir_path))
    return str(dir_path)

def InstallDriver():
    parser = argparse.ArgumentParser()
    
    '''
    platform.system()  결과
    - Linux : Linux
    - Mac : Darwin
    - Windows : Windows
    '''
    
    parser.add_argument('--OS', type=str, default=platform.system(), help='OS setting [OPTIONS : Windows, Darwin, Linux')
    parser.add_argument('--dst', type=str, default='./unzipped', help='Unzipped destination')
    args = parser.parse_args()
    
    assert args.OS in ['Windows', 'Darwin', 'Linux'], 'Unexpected OS Type, should be [ Windows, Darwin, Linux ] '
    print(args)
    
    dst_path = Path(args.dst)
    dst_path.mkdir(exist_ok=True)
    print('Create Destination directroty')
    driver_path = path_finder()
    print(driver_path)
    
    

    try:
        # mac, m1-mac, Linux 는 확장 예정 (mac의 경우 우리팀이 m1만 가지고 있어서 m1으로만 하게될 예정 )
        if args.OS =='Windows':
            with zipfile.ZipFile(driver_path + '\\chromedriver_win32.zip', 'r') as f:
                f.extractall(args.dst)
        print('Change Permission')
        os.chmod(args.dst,777)
    except Exception as e:
        print(f'FAIL |\n {e}')
        
