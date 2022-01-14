import sys
import subprocess
import pkg_resources
import signal
import sys
import hashlib
import random
import os
import json
import filecmp
import shutil
import platform
import logging
import glob
import socket
import urllib.request
import ctypes
from time import sleep
from termcolor import colored
from os import system, name
from os.path import exists
from datetime import datetime
from json.decoder import JSONDecodeError

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    pass
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def restart():
    file_exists = exists('ZeroOS-Dev.py')
    if file_exists == False:
        pass
    else:
        system('python ZeroOS-Dev.py')
        sys.exit(0)

    file_exists = exists('ZeroOS-Release.py')
    if file_exists == False:
        a = 'ZeroOS System File Not Found.'
        b = a.encode()
        c = hashlib.sha256(b).hexdigest().upper()[:8]

        print()
        print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
        print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{c}', 'yellow'))
        print(colored(f'[SYSTEM ERROR] ERROR MESSAGE: {str(a)}', 'yellow'))
        logger.error('[ERROR] An error has occured while using Advanche ZeroOS.')
        logger.error(f'[ERROR] ERROR CODE: 0x{c}')
        logger.error(f'[ERROR] ERROR MESSAGE: {str(a)}')
        input()
        print(colored('[SYSTEM] Shutting Down Advanche ZeroOS...', 'yellow'))
        directory = f'{os.getcwd()}\\tmp'
        found = os.path.isdir(directory)
        if found == True:
            shutil.rmtree(directory)
        sleep(3)
        sys.exit(0)
    else:
        system('python ZeroOS-Release.py')
        sys.exit(0)

now = datetime.now()
dt_string = now.strftime('%Y-%m-%d-%H-%M-%S')
directory = f'{os.getcwd()}\\log'
found = os.path.isdir(directory)
if found == True:
    logging.basicConfig(filename=f'{os.getcwd()}\\log\\{dt_string}.log', filemode='w', level=logging.DEBUG)
else:
    os.mkdir(directory)
    logging.basicConfig(filename=f'{os.getcwd()}\\log\\{dt_string}.log', filemode='w', level=logging.DEBUG)

logger = logging.getLogger()
logger.info('[LOG] Setting Up Advanche ZeroOS-Core...')

required = { 'colorama', 'guesslang', 'pkg', 'requests', 'pyttsx3' }
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

def signal_handler(sig, frame):
    print()
    print(colored('[SYSTEM] Shutting Down Advanche ZeroOS...', 'yellow'))
    directory = f'{os.getcwd()}\\tmp'
    found = os.path.isdir(directory)
    if found == True:
        shutil.rmtree(directory)
    sleep(3)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

system('title Advanche ZeroOS [Version 1.0.92261.5472]')

logger.info('[LOG] Advanche ZeroOS-Core Set.')
logger.info('[LOG] Checking If Advanche ZeroOS is outdaded...')

url = 'https://api.github.com/gists/cd0844ed451e218eeaccb8d53e01552e'
response = urllib.request.urlopen(url)
data = response.read()
data1 = json.loads(data)
if data1["files"]["ZeroOS-1.0-Status.txt"]["content"] == 'OUTDATED':
    clear()
    print(colored('Advanche ZeroOS [Version 1.0.92261.5472]', 'yellow'))
    print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
    print()
    print(colored('[SYSTEM] Hello! And thank you for using Advanche ZeroOS. It seems that this version is outdated and is no longer supported/compatible with this platform. Please upgrade to the latest version of Advanche ZeroOS and try again.', 'yellow'))
    input()
    print(colored('[SYSTEM] Shutting Down Advanche ZeroOS...', 'yellow'))
    directory = f'{os.getcwd()}\\tmp'
    found = os.path.isdir(directory)
    if found == True:
        shutil.rmtree(directory)
    sleep(3)
    exit()

logger.info('[LOG] Checking Python Version...')

ver = platform.python_version()
if ver != '3.8.0':
    a = 'Python Version Not Supported'
    b = a.encode()
    c = hashlib.sha256(b).hexdigest().upper()[:8]

    clear()
    print(colored('Advanche ZeroOS [Version 1.0.92261.5472]', 'yellow'))
    print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
    print()
    print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
    print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{c}', 'yellow'))
    print(colored(f'[SYSTEM ERROR] ERROR MESSAGE: {str(a)}', 'yellow'))
    logger.error(f'[ERROR] Python Version {ver} Not Supported.')
    input()
    print(colored('[SYSTEM] Shutting Down Advanche ZeroOS...', 'yellow'))
    directory = f'{os.getcwd()}\\tmp'
    found = os.path.isdir(directory)
    if found == True:
        shutil.rmtree(directory)
    sleep(3)
    sys.exit(0)

logger.info('[LOG] Checking If Configuration Exists...')

file_exists = exists('config/config.json')
if file_exists == False:
    a = 'Configuration Not Found.'
    b = a.encode()
    c = hashlib.sha256(b).hexdigest().upper()[:8]

    clear()
    print(colored('Advanche ZeroOS [Version 1.0.92261.5472]', 'yellow'))
    print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
    print()
    print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
    print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{c}', 'yellow'))
    print(colored(f'[SYSTEM ERROR] ERROR MESSAGE: {str(a)}', 'yellow'))
    logger.error('[ERROR] Configuration Not Found.')
    input()
    print(colored('[SYSTEM] Shutting Down Advanche ZeroOS...', 'yellow'))
    directory = f'{os.getcwd()}\\tmp'
    found = os.path.isdir(directory)
    if found == True:
        shutil.rmtree(directory)
    sleep(3)
    sys.exit(0)

conf = open('config/config.json', 'r+')
x = conf.read()
readconf = json.loads(x)

file_exists = exists('config/user.json')
if file_exists == True:
    try:
        user = open('config/user.json', 'r+')
        y = user.read()
        readuser = json.loads(y)
    except JSONDecodeError:
        pass

logger.info('[LOG] Checking Settings...')

if name == 'nt':
    if readconf["system_conf"]["UseUnsupportedVersions"] == True:
        clear()
        print(colored('Advanche ZeroOS [Version 1.0.92261.5472]', 'yellow'))
        print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
        print()
        print(colored('[SYSTEM] Hello! And thank you for using Advanche ZeroOS. It seems that the "UseUnsupportedVersions" feature is enabled but is not supported on your platform. Please consider disabling the "UseUnsupportedVersions" config for Advanche ZeroOS.', 'yellow'))
        logger.warning('[WARNING] UseUnsupportedVersions Is Enabled While Using Windows.')
        input()
else:
    if readconf["system_conf"]["UseUnsupportedVersions"] == True:
        clear()
        print(colored('Advanche ZeroOS [Version 1.0.92261.5472]', 'yellow'))
        print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
        print()
        print(colored('[SYSTEM] Hello! And thank you for using Advanche ZeroOS. It seems that you are running on an Unsupported Platform which will cause lots of errors. Please consider disabling the "UseUnsupportedVersions" config for Advanche ZeroOS.', 'yellow'))
        logger.warning('[WARNING] UseUnsupportedVersions Is Enabled While Using macOS (Darwin).')
        input()
    else:
        clear()
        print(colored('Advanche ZeroOS [Version 1.0.92261.5472]', 'yellow'))
        print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
        print()
        print(colored('[SYSTEM] Hello! And thank you for using Advanche ZeroOS. It seems that you are running on an Unsupported Platform which will cause lots of errors. Please consider upgrading your platform to Windows 7/8/10 or later.', 'yellow'))
        logger.error('[ERROR] Platform Not Supported.')
        input()
        print(colored('[SYSTEM] Shutting Down Advanche ZeroOS...', 'yellow'))
        directory = f'{os.getcwd()}\\tmp'
        found = os.path.isdir(directory)
        if found == True:
            shutil.rmtree(directory)
        sleep(3)
        sys.exit(0)

logger.info('[LOG] Closing Configuration File...')

conf.close()

logger.info('[LOG] Configuration File Successfully Closed.')

def SetupZeroOS():
    logger.info('[LOG] Entering Setup Mode...')
    file_exists = exists('config/user.json')
    if file_exists == True:
        user.close()
        os.remove('config/user.json')
    clear()
    print(colored('Advanche ZeroOS [Version 1.0.92261.5472]', 'yellow'))
    print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
    print()
    print(colored('[SYSTEM] Hello! And thank you for using Advanche ZeroOS. It seems that this is your first time using the OS. We will guide you through the setup to install Advanche ZeroOS.', 'yellow'))
    print()
    print(colored('[SYSTEM] Please also take note that you can configure with Advanche ZeroOS after setup.', 'yellow'))
    input()
    username = input(colored('[SYSTEM] What is your username? : ', 'yellow'))
    password = input(colored('[SYSTEM] What is your password? : ', 'yellow'))
    print()
    print(colored('[SYSTEM] Please wait while we get Advanche ZeroOS ready for you...', 'yellow'))
    config = open('config/config.json', 'r+')
    text = """
{
    "user_conf": {
        "Username":
        "Password":
    }
}
"""
    splitted = text.split()
    splitted.insert(4, f' "{username}",')
    splitted.insert(6, f' "{password}"')
    final_string = ' '.join(splitted)
    parsed = json.loads(final_string)
    f = open('config/user.json', 'w+')
    f.write(json.dumps(parsed, indent=4, sort_keys=True))
    f.close()
    jsondata = config.read()
    modified = jsondata.replace('"SetupMode": true', '"SetupMode": false')
    config.seek(0)
    config.truncate()
    config.writelines(modified)
    config.close()
    print(colored('[SYSTEM] Congratulations! You have successfully installed Advanche ZeroOS. We will now restart Advanche ZeroOS...', 'yellow'))
    logger.info('[LOG] Successfully Installed Advanche ZeroOS.')
    input()
    print(colored('[SYSTEM] Restarting Advanche ZeroOS...', 'yellow'))
    directory = f'{os.getcwd()}\\tmp'
    found = os.path.isdir(directory)
    if found == True:
        shutil.rmtree(directory)
    logging.shutdown()
    sleep(3)
    restart()

if readconf["system_conf"]["SetupMode"] == True:
    SetupZeroOS()
else:
    pass

file_exists = exists('config/user.json')
if file_exists == False:
    a = 'User Configuration Not Found.'
    b = a.encode()
    c = hashlib.sha256(b).hexdigest().upper()[:8]

    clear()
    print(colored('Advanche ZeroOS [Version 1.0.92261.5472]', 'yellow'))
    print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
    print()
    print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
    print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{c}', 'yellow'))
    print(colored(f'[SYSTEM ERROR] ERROR MESSAGE: {str(a)}', 'yellow'))
    logger.error('[ERROR] User Configuration Not Found.')
    input()
    print(colored('[SYSTEM] Shutting Down Advanche ZeroOS...', 'yellow'))
    directory = f'{os.getcwd()}\\tmp'
    found = os.path.isdir(directory)
    if found == True:
        shutil.rmtree(directory)
    sleep(3)
    sys.exit(0)

file_exists = exists('config/data.txt')
if file_exists == False:
    a = 'Data Configuration Not Found.'
    b = a.encode()
    c = hashlib.sha256(b).hexdigest().upper()[:8]

    clear()
    print(colored('Advanche ZeroOS [Version 1.0.92261.5472]', 'yellow'))
    print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
    print()
    print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
    print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{c}', 'yellow'))
    print(colored(f'[SYSTEM ERROR] ERROR MESSAGE: {str(a)}', 'yellow'))
    logger.error('[ERROR] Data Configuration Not Found.')
    input()
    print(colored('[SYSTEM] Shutting Down Advanche ZeroOS...', 'yellow'))
    directory = f'{os.getcwd()}\\tmp'
    found = os.path.isdir(directory)
    if found == True:
        shutil.rmtree(directory)
    sleep(3)
    sys.exit(0)

if readconf["system_conf"]["LoginRequired"] == True:
    clear()
    print(colored('Advanche ZeroOS [Version 1.0.92261.5472]', 'yellow'))
    print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
    print()
    print(colored('[SYSTEM] NOTE: Login Is Required To Boot Advanche ZeroOS.', 'yellow'))
    logger.info('[LOG] Login Required To Start Advanche ZeroOS.')
    while True:
        username = input(colored('[SYSTEM] Login Username: ', 'yellow'))
        password = input(colored('[SYSTEM] Login Password: ', 'yellow'))
        if username == readuser["user_conf"]["Username"]:
            if password == readuser["user_conf"]["Password"]:
                break
            else:
                print()
                print(colored('[SYSTEM] Username/Password is Incorrect, please try again.', 'yellow'))
        else:
            print(colored('[SYSTEM] Username/Password is Incorrect, please try again.', 'yellow'))
    clear()
    print(colored('Advanche ZeroOS [Version 1.0.92261.5472]', 'yellow'))
    print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
    print()
    print(colored('[SYSTEM] Starting Advanche ZeroOS...', 'yellow'))
else:
    clear()
    print(colored('Advanche ZeroOS [Version 1.0.92261.5472]', 'yellow'))
    print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
    print()
    print(colored('[SYSTEM] Starting Advanche ZeroOS...', 'yellow'))
if readconf["system_conf"]["CheckRequiredModules"] == True:
    print(colored('[SYSTEM] Checking If Required Modules Are Installed...', 'yellow'))
    logger.info('[LOG] Checking For Required Modules...')
    if missing:
        print(colored('[SYSTEM] Installing Required Modules...', 'yellow'))
        logger.info('[LOG] Installing Required Modules...')
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
        print(colored('[SYSTEM] Restarting Advanche ZeroOS...', 'yellow'))
        directory = f'{os.getcwd()}\\tmp'
        found = os.path.isdir(directory)
        if found == True:
            shutil.rmtree(directory)
        logging.shutdown()
        sleep(3)
        restart()
    else:
        try:
            import requests
            import pyttsx3
            from guesslang import Guess
            from colorama import *
        except ImportError as e:
            a = type(e).__name__.encode()
            b = hashlib.sha256(a).hexdigest().upper()[:8]

            print()
            print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
            print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{b}', 'yellow'))
            print(colored(f'[SYSTEM ERROR] ERROR MESSAGE: {e}', 'yellow'))
            logger.error("[ERROR] Some or more modules we're not found.")
            input()
            print(Fore.YELLOW, '[SYSTEM] Shutting Down Advanche ZeroOS...')
            directory = f'{os.getcwd()}\\tmp'
            found = os.path.isdir(directory)
            if found == True:
                shutil.rmtree(directory)
                sleep(3)
                sys.exit(0)
else:
    try:
        import requests
        import pyttsx3
        from guesslang import Guess
        from colorama import *
    except ImportError as e:
        a = type(e).__name__.encode()
        b = hashlib.sha256(a).hexdigest().upper()[:8]

        print()
        print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
        print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{b}', 'yellow'))
        print(colored(f'[SYSTEM ERROR] ERROR MESSAGE: {e}', 'yellow'))
        logger.error("[ERROR] Some or more modules we're not found.")
        input()
        print(Fore.YELLOW, '[SYSTEM] Shutting Down Advanche ZeroOS...')
        directory = f'{os.getcwd()}\\tmp'
        found = os.path.isdir(directory)
        if found == True:
            shutil.rmtree(directory)
            sleep(3)
            sys.exit(0)
logger.info('[LOG] Checking if Advanche ZeroOS was Modified...')
url = 'https://api.github.com/gists/d011805cb066539a6d5fa531e99eaad7'
response = urllib.request.urlopen(url)
data = response.read()
data1 = json.loads(data)
file_exists = exists('ZeroOS-Dev.py')
if file_exists == True:
    f1 = 'ZeroOS-Dev.py'

directory = f'{os.getcwd()}\\tmp'
found = os.path.isdir(directory)
if found == False:
    os.mkdir(directory)
f21 = open('tmp/sys.zmx', 'w+')
f21.write(data1["files"]["ZeroOS-1.0-Release.py"]["content"])
f21.close()

file_exists = exists('ZeroOS-Release.py')
if file_exists == True:
    f1 = 'ZeroOS-Release.py'
f2 = 'tmp/sys.zmx'
result = filecmp.cmp(f1, f2, shallow=False)
if result != True:
    clear()
    print(colored('Advanche ZeroOS [Version 1.0.92261.5472]', 'yellow'))
    print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
    print()
    print(colored('[SYSTEM] Hello! And thank you for using Advanche ZeroOS. It seems that Advanche ZeroOS was Modified. It is recommended to re-download Advanche ZeroOS from the official site before continuing.', 'yellow'))
    logger.warning('[WARNING] Advanche ZeroOS was Modified. It is recommended to re-download Advanche ZeroOS from the official site before continuing.')
    input()
    clear()
    print(colored('Advanche ZeroOS [Version 1.0.92261.5472]', 'yellow'))
    print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
    print()
    print(colored('[SYSTEM] Starting Advanche ZeroOS...', 'yellow'))
logger.info('[LOG] Importing Modules...')
guess = Guess()
engine = pyttsx3.init()
init(convert=True)
if readconf["system_conf"]["CheckForLogs"] == True:
    print(colored('[SYSTEM] Checking for Logs...', 'yellow'))
    logger.info('[LOG] Checking For Logs...')
    num = 0
    dir = 'log'
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            num += 1
    if num >= 7:
        print(colored('[SYSTEM] Deleting Overloading Logs...', 'yellow'))
        logger.info('[LOG] Deleting Overloading Logs...')
        file_path = f'{os.getcwd()}\\log\\{dt_string}.log'
        if os.path.isfile(file_path):
            for clean_up in glob.glob(f'{os.getcwd()}\\log\\*.*'):
                if not clean_up.endswith(f'{dt_string}.log'):
                    os.remove(clean_up)
        logger.info('[LOG] Successfully deleted Overloading Logs.')

if readconf["system_conf"]["CheckForUpdates"] == True:
    logger.info('[LOG] Checking for Updates...')
    print(colored('[SYSTEM] Checking for Updates...', 'yellow'))
    url = 'https://api.github.com/gists/23907230390ac16891eb23930266ef1b'
    response = urllib.request.urlopen(url)
    data = response.read()
    data1 = json.loads(data)
    directory = f'{os.getcwd()}\\tmp'
    found = os.path.isdir(directory)
    if found == False:
        os.mkdir(directory)
    file2 = open('tmp/data.txt', 'w+')
    file2.write(data1["files"]["data.txt"]["content"])
    file2.close()
    f1 = 'config/data.txt'
    f2 = 'tmp/data.txt'
    result = filecmp.cmp(f1, f2, shallow=False)
    if result != True:
        logger.info('[LOG] Updating Advanche ZeroOS...')
        print(colored('[SYSTEM] Updating ZeroOS...', 'yellow'))
        url = 'https://api.github.com/gists/d011805cb066539a6d5fa531e99eaad7'
        response = urllib.request.urlopen(url)
        data = response.read()
        data1 = json.loads(data)
        open(os.path.abspath(__file__), 'wb').write(data1["files"]["ZeroOS-1.0-Release.py"]["content"])
        r2 = bytes(data1["files"]["data.txt"]["content"])
        open(os.getcwd() + '/config/data.txt', 'w').write(str(r2))
        print(colored('[SYSTEM] Restarting Advanche ZeroOS...', 'yellow'))
        directory = f'{os.getcwd()}\\tmp'
        found = os.path.isdir(directory)
        if found == True:
            shutil.rmtree(directory)
        logging.shutdown()
        sleep(3)
        restart()
    else:
        logger.info('[LOG] No Updates Found.')
        print(colored('[SYSTEM] No Updates Found!', 'yellow'))

logger.info('[LOG] Successfully Loaded Advanche ZeroOS.')
print(colored('[SYSTEM] Welcome To Advanche ZeroOS!', 'yellow'))
print()
try:
    while True:
        print()
        cmd = input(Fore.YELLOW + f'A:\{readuser["user_conf"]["Username"]}>')
        if cmd == '':
            cmd = 'EmptyCommand'
        split = cmd.split()
        if split[0] == 'clear' or split[0] == 'cls' or split[0] == 'CLEAR' or split[0] == 'CLS':
            clear()
        elif split[0] == 'echo' or split[0] == 'say' or split[0] == 'ECHO' or split[0] == 'SAY':
            chars = []
            str = ""
            chars[:0] = cmd
            if chars[0] == "e" and chars[1] == "c" and chars[2] == "h" and chars[3] == "o" and chars[4] == " ":
                chars.remove("e")
                chars.remove("c")
                chars.remove("h")
                chars.remove("o")
                str = "".join(chars)
                print(str)
            elif chars[0] == "E" and chars[1] == "C" and chars[2] == "H" and chars[3] == "O" and chars[4] == " ":
                chars.remove("E")
                chars.remove("C")
                chars.remove("H")
                chars.remove("O")
                str = "".join(chars)
                print(str)
            elif chars[0] == "s" and chars[1] == "a" and chars[2] == "y" and chars[3] == " ":
                chars.remove("s")
                chars.remove("a")
                chars.remove("y")
                str = "".join(chars)
                print(str)
            elif chars[0] == "S" and chars[1] == "A" and chars[2] == "Y" and chars[3] == " ":
                chars.remove("S")
                chars.remove("A")
                chars.remove("Y")
                str = "".join(chars)
                print(str)
        elif split[0] == 'cmd' or split[0] == 'CMD':
            print(Fore.YELLOW, 'Advanche ZeroOS [Version 1.0.92261.5472]')
            print(Fore.YELLOW, '(c) Advanche Corporation. All rights reserved.')
        elif split[0] == 'help' or split[0] == 'HELP' or split[0] == 'cmds' or split[0] == 'CMDS':
            print(Fore.YELLOW, 'CLEAR/CLS               CLEARS THE ADVANCHE ZEROOS COMMAND LOG')
            print(Fore.YELLOW, 'ECHO/SAY                ECHOES ANY TEXT TO ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'RECHO/RSAY              ECHOES ANY TEXT TO ADVANCHE ZEROOS (REVERSED)')
            print(Fore.YELLOW, 'TTS/SAYTTS              ECHOES ANYTHING IN TTS TO ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'CMD                     LAUNCHES ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'HELP/CMDS               SHOWS COMMANDS FOR ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'START                   START CERTAIN PROGRAM IN *.ZRO/*.ZERO/*.ZRX FORMAT')
            print(Fore.YELLOW, '*.ZRO/*.ZERO/*.ZRX      START CERTAIN PROGRAM IN *.ZRO/*.ZERO/*.ZRX FORMAT')
            print(Fore.YELLOW, 'COPY/CP                 COPIES ANY FILE TO ANOTHER DIRECTORY')  
            print(Fore.YELLOW, 'MOVE/MV                 MOVES ANY FILE TO ANOTHER DIRECTORY')
            print(Fore.YELLOW, 'EXIT/CTRL+C/SHUTDOWN    EXITS ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'RESTART                 RESTARTS ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'RANDOM                  CHOOSES A RANDOM NUMBER BETWEEN A & B')
            print(Fore.YELLOW, 'UPDATE/RESTORE          UPDATES ADVANCHE ZEROOS TO THE LATEST VERSION')
            print(Fore.YELLOW, 'INSTALL/INS             INSTALLS AN APPLICATION PACKAGE IN *.ZPX/*.ZPPX/*.ZPP FORMAT')
            print(Fore.YELLOW, 'SEND/RQSEND             SENDS GET REQUEST TO SPECIFIED URL')
            print(Fore.YELLOW, 'DATE                    OUTPUTS CURRENT DATE TO ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'TIME                    OUTPUTS CURRENT TIME TO ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'IP                      OUTPUTS PUBLIC/PRIVATE IP ADDRESSES TO ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'USER/USERNAME           CHANGES CURRENT USERNAME TO NEW USERNAME FOR ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'PSWD/PASSWORD           CHANGES CURRENT PASSWORD TO NEW PASSWORD FOR ADVANCHE ZEROOS')
        elif split[0] == 'start' or split[0] == 'START':
            if split[1].endswith('.zro') or split[1].endswith('.zero') or split[1].endswith('.ZRO') or split[1].endswith('.ZERO'):
                print(Fore.YELLOW, '[SYSTEM] Launching Program...')
                print()
                if 1 < len(split):
                    file_exists = exists(split[1])
                    if file_exists == True:
                        f = open(split[1], 'r')
                        data = f.read()
                        name = guess.language_name(data)
                        if name == 'Python':
                            try:
                                subprocess.check_call(["python.exe", f"{split[1]}"], shell=False)
                            except subprocess.CalledProcessError as e:
                                a = type(e).__name__.encode()
                                b = hashlib.sha256(a).hexdigest().upper()[:8]

                                print()
                                print(colored(f'[PROGRAM ERROR] An error has occured while using {split[1]}. Please report this error to the Main Developer.\n', 'yellow'))
                                print(colored(f'[PROGRAM ERROR] ERROR CODE: 0x{b}', 'yellow'))
                        else:
                            a = 'Program File Is In Unknown Format.'
                            b = a.encode()
                            c = hashlib.sha256(b).hexdigest().upper()[:8]

                            print()
                            print(colored(f'[PROGRAM ERROR] An error has occured while using {split[1]}. Please report this error to the Main Developer.\n', 'yellow'))
                            print(colored(f'[PROGRAM ERROR] ERROR CODE: 0x{c}', 'yellow'))
                    else:
                        print(Fore.YELLOW, f"[SYSTEM] '{split[1]}' is not recognized as an operable program.")   
                else:
                    print(Fore.YELLOW, f"[SYSTEM] The syntax of the command '{split[0]}' is incorrect.")
            elif split[1].endswith('.zrx') or split[1].endswith('.ZRX'):
                print(Fore.YELLOW, '[SYSTEM] Launching Program...')
                print()
                if 1 < len(split):
                    file_exists = exists(split[1])
                    if file_exists == True:
                        try:
                            system(split[1]) 
                        except subprocess.CalledProcessError as e:
                            a = type(e).__name__.encode()
                            b = hashlib.sha256(a).hexdigest().upper()[:8]

                            print()
                            print(colored(f'[PROGRAM ERROR] An error has occured while using {split[1]}. Please report this error to the Main Developer.\n', 'yellow'))
                            print(colored(f'[PROGRAM ERROR] ERROR CODE: 0x{b}', 'yellow'))
                    else:
                        print(Fore.YELLOW, f"[SYSTEM] '{split[1]}' is not recognized as an operable program.")   
                else:
                    print(Fore.YELLOW, f"[SYSTEM] The syntax of the command '{split[0]}' is incorrect.")
            else:
                print(Fore.YELLOW, f"[SYSTEM] '{split[1]}' is not recognized as an operable program.")
        elif split[0] == 'copy' or split[0] == 'cp' or split[0] == 'COPY' or split[0] == 'CP':
            system(f'copy {split[1]} {split[2]}')
        elif split[0] == 'move' or split[0] == 'mv' or split[0] == 'MOVE' or split[0] == 'MV':
            system(f'move {split[1]} {split[2]}')
        elif split[0] == 'exit' or split[0] == 'EXIT' or split[0] == 'shutdown' or split[0] == 'SHUTDOWN':
            print(Fore.YELLOW, '[SYSTEM] Shutting Down Advanche ZeroOS...')
            directory = f'{os.getcwd()}\\tmp'
            found = os.path.isdir(directory)
            if found == True:
                shutil.rmtree(directory)
            sleep(3)
            sys.exit(0)
        elif split[0].endswith('.zro') or split[0].endswith('.zero') or split[0].endswith('.ZRO') or split[0].endswith('.ZERO'):
            print(Fore.YELLOW, '[SYSTEM] Launching Program...')
            print()
            file_exists = exists(split[0])
            if file_exists == True:
                try:
                    subprocess.check_call(["python.exe", f"{split[0]}"], shell=False)
                except subprocess.CalledProcessError as e:
                    a = type(e).__name__.encode()
                    b = hashlib.sha256(a).hexdigest().upper()[:8]

                    print()
                    print(colored(f'[PROGRAM ERROR] An error has occured while using {split[0]}. Please report this error to the Main Developer.\n', 'yellow'))
                    print(colored(f'[PROGRAM ERROR] ERROR CODE: 0x{b}', 'yellow'))
            else:
                print(Fore.YELLOW, f"[SYSTEM] '{split[0]}' is not recognized as an operable program.")   
        elif split[0].endswith('.zrx') or split[0].endswith('.ZRX'):
            print(Fore.YELLOW, '[SYSTEM] Launching Program...')
            print()
            file_exists = exists(split[0])
            if file_exists == True:
                try:
                    system(split[0]) 
                except subprocess.CalledProcessError as e:
                    a = type(e).__name__.encode()
                    b = hashlib.sha256(a).hexdigest().upper()[:8]

                    print()
                    print(colored(f'[PROGRAM ERROR] An error has occured while using {split[0]}. Please report this error to the Main Developer.\n', 'yellow'))
                    print(colored(f'[PROGRAM ERROR] ERROR CODE: 0x{b}', 'yellow'))
            else:
                print(Fore.YELLOW, f"[SYSTEM] '{split[0]}' is not recognized as an operable program.")   
        elif split[0] == 'random' or split[0] == 'RANDOM':
            print(Fore.YELLOW, random.randint(int(split[1]), int(split[2])))
        elif split[0] == 'EmptyCommand':
            pass
        elif split[0] == 'update' or split[0] == 'UPDATE' or split[0] == 'restore' or split[0] == 'RESTORE':
            note = input(Fore.YELLOW + '[SYSTEM] Note that this will update Advanche ZeroOS and new changes will be made. Are you sure you want to continue? (Y/N) : ')
            if note == 'y' or note == 'Y':
                logger.info('[LOG] Checking for Updates...')
                print(colored('[SYSTEM] Checking for Updates...', 'yellow'))
                url = 'https://api.github.com/gists/23907230390ac16891eb23930266ef1b'
                response = urllib.request.urlopen(url)
                data = response.read()
                data1 = json.loads(data)
                directory = f'{os.getcwd()}\\tmp'
                found = os.path.isdir(directory)
                if found == False:
                    os.mkdir(directory)
                file2 = open('tmp\\data.txt', 'w+')
                file2.write(data1["files"]["data.txt"]["content"])
                file2.close()
                f1 = 'config/data.txt'
                f2 = 'tmp/data.txt'
                result = filecmp.cmp(f1, f2, shallow=False)
                if result != True:
                    logger.info('[LOG] Updating Advanche ZeroOS...')
                    print(colored('[SYSTEM] Updating ZeroOS...', 'yellow'))
                    url = 'https://api.github.com/gists/d011805cb066539a6d5fa531e99eaad7'
                    response = urllib.request.urlopen(url)
                    data = response.read()
                    data1 = json.loads(data)
                    open(os.path.abspath(__file__), 'wb').write(data1["files"]["ZeroOS-1.0-Release.py"]["content"])
                    r2 = bytes(data1["files"]["data.txt"]["content"])
                    open(os.getcwd() + '/config/data.txt', 'w').write(str(r2))
                    print(colored('[SYSTEM] Restarting Advanche ZeroOS...', 'yellow'))
                    directory = f'{os.getcwd()}\\tmp'
                    found = os.path.isdir(directory)
                    if found == True:
                        shutil.rmtree(directory)
                    logging.shutdown()
                    sleep(3)
                    restart()
                else:
                    logger.info('[LOG] No Updates Found.')
                    print(colored('[SYSTEM] No Updates Found!', 'yellow'))
            elif note == 'n' or note == 'N':
                print(Fore.YELLOW, '[SYSTEM] Advanche ZeroOS Update Check Aborted.')
        elif split[0] == 'version' or split[0] == 'VERSION' or split[0] == 'ver' or split[0] == 'VER':
            print(Fore.YELLOW, 'Advanche ZeroOS [Version 1.0.92261.5472]')
        elif split[0] == 'restart' or split[0] == 'RESTART':
            print(colored('[SYSTEM] Restarting Advanche ZeroOS...', 'yellow'))
            directory = f'{os.getcwd()}\\tmp'
            found = os.path.isdir(directory)
            if found == True:
                shutil.rmtree(directory)
            logging.shutdown()
            sleep(3)
            restart()
        elif split[0] == 'install' or split[0] == 'INSTALL' or split[0] == 'ins' or split[0] == 'INS':
            print(Fore.YELLOW, '[SYSTEM] Checking If Application Package Exists...')
            print()
            if split[1].endswith('.zpx') or split[1].endswith('.zppx') or split[1].endswith('.zpp') or split[1].endswith('.ZPX') or split[1].endswith('.ZPPX') or split[1].endswith('.ZPP'):
                if 1 < len(split):
                    file_exists = exists(split[1])
                    if file_exists == True:
                        print(Fore.YELLOW, '[SYSTEM] Installing Application Package...')
                        try:
                            cmd = f'Add-AppxPackage -Path {split[1]}'
                            subprocess.run(['powershell', '-Command', cmd])
                            print(Fore.YELLOW, '[SYSTEM] Successfully Installed Application Package.')
                        except subprocess.CalledProcessError as e:
                            a = type(e).__name__.encode()
                            b = hashlib.sha256(a).hexdigest().upper()[:8]

                            print()
                            print(colored(f'[INSTALLATION ERROR] An error has occured while using {split[0]}. Please report this error to the Main Developer.\n', 'yellow'))
                            print(colored(f'[INSTALLATION ERROR] ERROR CODE: 0x{b}', 'yellow'))
                    else:
                        print(Fore.YELLOW, f"[SYSTEM] Application Package '{split[1]}' does not exist.")
                else:
                    print(Fore.YELLOW, f"[SYSTEM] The syntax of the command '{split[0]}' is incorrect.")
        elif split[0] == 'recho' or split[0] == 'rsay' or split[0] == 'RECHO' or split[0] == 'RSAY':
            chars = []
            str = ""
            chars[:0] = cmd
            if chars[0] == "r" and chars[1] == "e" and chars[2] == "c" and chars[3] == "h" and chars[4] == "o" and chars[5] == " ":
                chars.remove("r")
                chars.remove("e")
                chars.remove("c")
                chars.remove("h")
                chars.remove("o")
                str = "".join(chars)[::-1]
                print(str)
            elif chars[0] == "R" and chars[1] == "E" and chars[2] == "C" and chars[3] == "H" and chars[4] == "O" and chars[5] == " ":
                chars.remove("R")
                chars.remove("E")
                chars.remove("C")
                chars.remove("H")
                chars.remove("O")
                str = "".join(chars)[::-1]
                print(str)
            elif chars[0] == "r" and chars[1] == "s" and chars[2] == "a" and chars[3] == "y" and chars[4] == " ":
                chars.remove("r")
                chars.remove("s")
                chars.remove("a")
                chars.remove("y")
                str = "".join(chars)[::-1]
                print(str)
            elif chars[0] == "R" and chars[1] == "S" and chars[2] == "A" and chars[3] == "Y" and chars[4] == " ":
                chars.remove("R")
                chars.remove("S")
                chars.remove("A")
                chars.remove("Y")
                str = "".join(chars)[::-1]
                print(str)
        elif split[0] == 'tts' or split[0] == 'TTS' or split[0] == 'saytts' or split[0] == 'SAYTTS':
            chars = []
            str = ""
            chars[:0] = cmd
            if chars[0] == "t" and chars[1] == "t" and chars[2] == "s" and chars[3] == " ":
                chars.remove("t")
                chars.remove("t")
                chars.remove("s")
                str = "".join(chars)
                engine.say(str)
                engine.runAndWait()
            if chars[0] == "T" and chars[1] == "T" and chars[2] == "S" and chars[3] == " ":
                chars.remove("T")
                chars.remove("T")
                chars.remove("S")
                str = "".join(chars)
                engine.say(str)
                engine.runAndWait()
            elif chars[0] == "s" and chars[1] == "a" and chars[2] == "y" and chars[3] == "t" and chars[4] == "t" and chars[5] == "s" and chars[6] == " ":
                chars.remove("s")
                chars.remove("a")
                chars.remove("y")
                chars.remove("t")
                chars.remove("t")
                chars.remove("s")
                str = "".join(chars)
                engine.say(str)
                engine.runAndWait()
            elif chars[0] == "S" and chars[1] == "A" and chars[2] == "Y" and chars[3] == "T" and chars[4] == "T" and chars[5] == "S" and chars[6] == " ":
                chars.remove("S")
                chars.remove("A")
                chars.remove("Y")
                chars.remove("T")
                chars.remove("T")
                chars.remove("S")
                str = "".join(chars)
                engine.say(str)
                engine.runAndWait()
        elif split[0] == 'send' or split[0] == 'SEND' or split[0] == 'rqsend' or split[0] == 'RQSEND':
            if 1 < len(split):
                print(Fore.YELLOW, '[SYSTEM] Sending GET Request...')
                logger.info('[LOG] Sending GET Request...')
                try:
                    res = requests.get(split[1])
                    res_code = res.status_code
                    print(Fore.YELLOW, f'[SYSTEM] Response Status Code: {res_code}')
                    logger.info('[LOG] Request Successfully Sent.')
                    logger.info(f'[LOG] Response Status Code: {res_code}')
                except requests.RequestException as e:
                    a = type(e).__name__.encode()
                    b = hashlib.sha256(a).hexdigest().upper()[:8]

                    print()
                    print(Fore.YELLOW, '[RQSEND ERROR] An error has occured while sending the GET Request. Maybe the URL is invalid or the server is down.')
                    print(Fore.YELLOW, f'[RQSEND ERROR] ERROR CODE: 0x{b}')
                    print(Fore.YELLOW, f'[RQSEND ERROR] ERROR MESSAGE: {e}')
                    logger.error('[ERROR] An error has occured while sending the GET Request.')
                    logger.error(f'[ERROR] ERROR CODE: 0x{b}')
                    logger.error(f'[ERROR] ERROR MESSAGE: {e}')
            else:
                print(Fore.YELLOW, f"[SYSTEM] The syntax of the command '{split[0]}' is incorrect.")
        elif split[0] == 'date' or split[0] == 'DATE':
            now = datetime.now()
            date = now.strftime('[SYSTEM] Current Date: %A %m/%d/%Y')
            print(Fore.YELLOW, date)
        elif split[0] == 'time' or split[0] == 'TIME':
            now = datetime.now()
            time = now.strftime('[SYSTEM] Current Time: %H:%M:%S')
            print(Fore.YELLOW, time)
        elif split[0] == 'ip' or split[0] == 'IP':
            hostname = socket.gethostname()
            public_ip = requests.get('https://api.ipify.org').text
            private_ip = socket.gethostbyname(hostname)
            print(Fore.YELLOW, f'[SYSTEM] Public IP Address: {public_ip}')
            print(Fore.YELLOW, f'[SYSTEM] Private IP Address: {private_ip}')
        elif split[0] == 'pswd' or split[0] == 'PSWD' or split[0] == 'password' or split[0] == 'PASSWORD':
            print(Fore.YELLOW, f'[SYSTEM] Current Password: {readuser["user_conf"]["Password"]}')
            while True:
                new_pswd = input(Fore.YELLOW + '[SYSTEM] New Password: ')
                if new_pswd == '':
                    print(Fore.YELLOW, '[SYSTEM] Please enter a new password.')
                else:
                    break
            print()
            print(Fore.YELLOW, f'[SYSTEM] Changing Current Password...')
            logger.info(f'[LOG] Changing Current Password To {new_pswd}...')
            config = open('config/user.json', 'r+')
            jsondata = config.read()
            modified = jsondata.replace(f'"Password": "{readuser["user_conf"]["Password"]}"', f'"Password": "{new_pswd}"')
            config.seek(0)
            config.truncate()
            config.writelines(modified)
            config.close()
            print(Fore.YELLOW, f"[SYSTEM] Successfully Changed Password To '{new_pswd}'.")
            logger.info(f'[LOG] Successfully Changed Password To {new_pswd}.')
            print()
            print(colored('[SYSTEM] Restarting Advanche ZeroOS...', 'yellow'))
            directory = f'{os.getcwd()}\\tmp'
            found = os.path.isdir(directory)
            if found == True:
                shutil.rmtree(directory)
            logging.shutdown()
            sleep(3)
            restart()
        elif split[0] == 'user' or split[0] == 'USER' or split[0] == 'username' or split[0] == 'USERNAME':
            print(Fore.YELLOW, f'[SYSTEM] Current Username: {readuser["user_conf"]["Username"]}')
            while True:
                new_user = input(Fore.YELLOW + '[SYSTEM] New Username: ')
                if new_user == '':
                    print(Fore.YELLOW, '[SYSTEM] Please enter a new username.')
                else:
                    break
            print()
            print(Fore.YELLOW, f'[SYSTEM] Changing Current Username...')
            logger.info(f'[LOG] Changing Current Username To {new_user}...')
            config = open('config/user.json', 'r+')
            jsondata = config.read()
            modified = jsondata.replace(f'"Username": "{readuser["user_conf"]["Username"]}"', f'"Username": "{new_user}"')
            config.seek(0)
            config.truncate()
            config.writelines(modified)
            config.close()
            print(Fore.YELLOW, f"[SYSTEM] Successfully Changed Username To '{new_user}'.")
            logger.info(f'[LOG] Successfully Changed Username To {new_user}.')
            print()
            print(colored('[SYSTEM] Restarting Advanche ZeroOS...', 'yellow'))
            directory = f'{os.getcwd()}\\tmp'
            found = os.path.isdir(directory)
            if found == True:
                shutil.rmtree(directory)
            logging.shutdown()
            sleep(3)
            restart()
        else:
            print(Fore.YELLOW, f"[SYSTEM] '{split[0]}' is not recognized as an internal command or an operable program.")
except Exception as e:
    a = type(e).__name__.encode()
    b = hashlib.sha256(a).hexdigest().upper()[:8]

    print()
    print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
    print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{b}', 'yellow'))
    print(colored(f'[SYSTEM ERROR] ERROR MESSAGE: {e}', 'yellow'))
    logger.error('[ERROR] An error has occured while using Advanche ZeroOS.')
    logger.error(f'[ERROR] ERROR CODE: 0x{b}')
    logger.error(f'[ERROR] ERROR MESSAGE: {e}')
    input()
    print(Fore.YELLOW, '[SYSTEM] Shutting Down Advanche ZeroOS...')
    directory = f'{os.getcwd()}\\tmp'
    found = os.path.isdir(directory)
    if found == True:
        shutil.rmtree(directory)
    sleep(3)
    sys.exit(0)