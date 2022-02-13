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
import math
import string
import ctypes
import re
import pwinput
from time import sleep
from termcolor import colored
from os import system, name
from os.path import exists
from datetime import datetime
from json.decoder import JSONDecodeError

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

if isAdmin():
    pass
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(0)

try:
    class advanche:
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

        def convert_size(size_bytes):
            if size_bytes == 0:
                return "0B"
            size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
            i = int(math.floor(math.log(size_bytes, 1024)))
            p = math.pow(1024, i)
            s = round(size_bytes / p, 2)
            return "%s %s" % (s, size_name[i])

        def random_string(length):
            return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

        def connect(host):
            try:
                urllib.request.urlopen(host)
                return True
            except:
                return False

        def processor():
            if platform.system() == "Windows":
                return platform.processor()
            elif platform.system() == "Darwin":
                os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
                command ="sysctl -n machdep.cpu.brand_string"
                return subprocess.check_output(command).strip()
            elif platform.system() == "Linux":
                command = "cat /proc/cpuinfo"
                all_info = subprocess.check_output(command, shell=True).strip()
                for line in all_info.split("\n"):
                    if "model name" in line:
                        return re.sub( ".*model name.*:", "", line,1)
            return ""

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

    required = { 'colorama', 'guesslang', 'pkg', 'requests', 'pyttsx3', 'psutil' }
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    cw2 = False

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

    system('title Advanche ZeroOS [Version 1.1.84335.9465]')

    logger.info('[LOG] Advanche ZeroOS-Core Set.')
    logger.info('[LOG] Checking If Configuration Exists...')

    file_exists = exists('config/config.json')
    if file_exists == True:
        try:
            conf = open('config/config.json', 'r+')
            x = conf.read()
            readconf = json.loads(x)
        except JSONDecodeError as e:
            a = 'User Configuration Not Found.'
            b = a.encode()
            c = hashlib.sha256(b).hexdigest().upper()[:8]

            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno

            advanche.clear()
            print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
            print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
            print()
            print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
            print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{c}', 'yellow'))
            print(colored(f'[SYSTEM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
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
    else:
        a = 'Configuration Not Found.'
        b = a.encode()
        c = hashlib.sha256(b).hexdigest().upper()[:8]

        advanche.clear()
        print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
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

    logger.info('[LOG] Checking If User Configuration Exists...')

    file_exists = exists('config/user.json')
    if file_exists == True:
        try:
            user = open('config/user.json', 'r+')
            y = user.read()
            readuser = json.loads(y)
        except JSONDecodeError:
            a = 'User Configuration Not Found.'
            b = a.encode()
            c = hashlib.sha256(b).hexdigest().upper()[:8]

            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno

            advanche.clear()
            print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
            print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
            print()
            print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
            print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{c}', 'yellow'))
            print(colored(f'[SYSTEM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
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

    if readconf["system_conf"]["OfflineMode"] == False and advanche.connect('https://www.google.com') == True:
        logger.info('[LOG] Checking If Advanche ZeroOS is outdaded...')
        try:
            url = 'https://api.github.com/gists/a91afe5c8f77755fa6ea9ca0a7bab366'
            response = urllib.request.urlopen(url)
            data = response.read()
            data1 = json.loads(data)
            if data1["files"]["ZeroOS-1.1-Status.txt"]["content"] == 'OUTDATED':
                advanche.clear()
                print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
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
        except Exception as e:
            a = type(e).__name__.encode()
            b = hashlib.sha256(a).hexdigest().upper()[:8]

            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno

            advanche.clear()
            print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
            print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
            print()
            print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
            print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{b}', 'yellow'))
            print(colored(f'[SYSTEM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
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

    logger.info('[LOG] Checking Python Version...')

    ver = platform.python_version()
    if ver != '3.8.0':
        a = 'Python Version Not Supported'
        b = a.encode()
        c = hashlib.sha256(b).hexdigest().upper()[:8]

        advanche.clear()
        print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
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

    logger.info('[LOG] Checking Settings...')

    if name == 'nt':
        if readconf["system_conf"]["UseUnsupportedVersions"] == True:
            advanche.clear()
            print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
            print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
            print()
            print(colored('[SYSTEM] Hello! And thank you for using Advanche ZeroOS. It seems that the "UseUnsupportedVersions" feature is enabled but is not supported on your platform. Please consider disabling the "UseUnsupportedVersions" config for Advanche ZeroOS.', 'yellow'))
            logger.warning('[WARNING] UseUnsupportedVersions Is Enabled While Using Windows.')
            input()
    else:
        if readconf["system_conf"]["UseUnsupportedVersions"] == True:
            advanche.clear()
            print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
            print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
            print()
            print(colored('[SYSTEM] Hello! And thank you for using Advanche ZeroOS. It seems that you are running on an Unsupported Platform which will cause lots of errors. Please consider disabling the "UseUnsupportedVersions" config for Advanche ZeroOS.', 'yellow'))
            logger.warning('[WARNING] UseUnsupportedVersions Is Enabled While Using macOS (Darwin).')
            input()
        else:
            advanche.clear()
            print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
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
        user = open('config/user.json', 'r+')
        y = user.read()
        readuser = json.loads(y)
        file_exists = exists('config/user.json')
        if file_exists == True:
            user.close()
            os.remove('config/user.json')
        advanche.clear()
        print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
        print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
        print()
        print(colored('[SYSTEM] Hello! And thank you for using Advanche ZeroOS. It seems that this is your first time using the OS. We will guide you through the setup to install Advanche ZeroOS.', 'yellow'))
        print()
        print(colored('[SYSTEM] Please also take note that you can configure with Advanche ZeroOS after setup.', 'yellow'))
        input()
        username = input(colored('[SYSTEM] What is your username? : ', 'yellow'))
        password = pwinput.pwinput(colored('[SYSTEM] What is your password? : ', 'yellow'), '●')
        print()
        continue1 = input(colored('[SYSTEM] Would you like to set an administrator password? [Y/n] ', 'yellow'))
        if continue1 == 'y' or continue1 == 'Y':
            adminPassword = pwinput.pwinput(colored('[SYSTEM] What is your administrator password? : ', 'yellow'), '●')
        else:
            adminPassword = 'advanche'
        print()
        print(colored('[SYSTEM] Please wait while we get Advanche ZeroOS ready for you...', 'yellow'))
        config = open('config/config.json', 'r+')
        text = """
    {
        "user_conf": {
            "Username":
            "Password":
            "ProductID":
            "AdministratorPassword":
            "Username2":
            "Password2":
            "Username3":
            "Password3":
        }
    }
    """
        splitted = text.split()
        splitted.insert(4, f' "{username}",')
        splitted.insert(6, f' "{password}",')
        splitted.insert(8, f' "{advanche.random_string(5)}-{advanche.random_string(5)}-{advanche.random_string(5)}-{advanche.random_string(5)}",')
        splitted.insert(10, f' "{adminPassword}",')
        splitted.insert(12, f' "",')
        splitted.insert(14, f' "",')
        splitted.insert(16, f' "",')
        splitted.insert(18, f' ""')
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
        print(colored('[SYSTEM] Congratulations! You have successfully installed Advanche ZeroOS.', 'yellow'))
        print()
        print(colored(f'[SYSTEM] System Product ID: {readuser["user_conf"]["ProductID"]}'))
        logger.info('[LOG] Successfully Installed Advanche ZeroOS.')
        input()
        print(colored('[SYSTEM] Restarting Advanche ZeroOS...', 'yellow'))
        directory = f'{os.getcwd()}\\tmp'
        found = os.path.isdir(directory)
        if found == True:
            shutil.rmtree(directory)
        logging.shutdown()
        sleep(3)
        advanche.restart()

    if readconf["system_conf"]["SetupMode"] == True:
        SetupZeroOS()
    else:
        pass

    file_exists = exists('config/data.txt')
    if file_exists == False:
        a = 'Data Configuration Not Found.'
        b = a.encode()
        c = hashlib.sha256(b).hexdigest().upper()[:8]

        advanche.clear()
        print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
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

    def reset_password():
        advanche.clear()
        print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
        print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
        print()
        print(colored('[SYSTEM] To reset your password, you will need your Product ID which is given to you from the Post-Setup.', 'yellow'))
        print(colored("[SYSTEM] If you can't find your Product ID, you will need to re-install Advanche ZeroOS completely using the Pre-Setup.", 'yellow'))
        print()
        while True:
            productID = input(colored('[SYSTEM] System Product ID: ', 'yellow'))
            if productID == readuser["user_conf"]["ProductID"]:
                new_pswd = pwinput.pwinput(colored('[SYSTEM] New System Password: ', 'yellow'), '●')
                print()
                print(colored('[SYSTEM] Changing Current System Password...', 'yellow'))
                logger.info(f'[LOG] Changing Current System Password To {new_pswd}...')
                config = open('config/user.json', 'r+')
                jsondata = config.read()
                modified = jsondata.replace(f'"Password": "{readuser["user_conf"]["Password"]}"', f'"Password": "{new_pswd}"')
                config.seek(0)
                config.truncate()
                config.writelines(modified)
                config.close()
                print(colored(f"[SYSTEM] Successfully Changed Current System Password To '{new_pswd}'.", 'yellow'))
                logger.info(f'[LOG] Successfully Changed Current System Password To {new_pswd}.')
                print()
                print(colored('[SYSTEM] Restarting Advanche ZeroOS...', 'yellow'))
                directory = f'{os.getcwd()}\\tmp'
                found = os.path.isdir(directory)
                if found == True:
                    shutil.rmtree(directory)
                logging.shutdown()
                sleep(3)
                advanche.restart()
            else:
                print()
                print(colored('[SYSTEM] Product ID is Invalid, please try again.', 'yellow'))

    cwcmd = f'A:\{readuser["user_conf"]["Username"]}>'
    cwa2 = False

    if readconf["system_conf"]["FWCAdministratorMode"] == True:
        cwa2 = True

    if readconf["system_conf"]["AdministratorMode"] == True:
        cw2 = True

    if readconf["system_conf"]["LoginRequired"] == True:
        advanche.clear()
        print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
        print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
        print()
        print(colored('[SYSTEM] NOTE: Login Is Required To Boot Advanche ZeroOS.', 'yellow'))
        print(colored("[SYSTEM] NOTE: Forgot your password? Type in 'PSWDFR' to reset your password.", 'yellow'))
        print()
        logger.info('[LOG] Login Required To Start Advanche ZeroOS.')
        while True:
            username = input(colored('[SYSTEM] Login Username: ', 'yellow'))
            if username == 'pswdfr' or username == 'PSWDFR':
                reset_password()
            else:
                password = pwinput.pwinput(colored('[SYSTEM] Login Password: ', 'yellow'), '●')
                if username == '':
                    print()
                    print(colored('[SYSTEM] Username/Password is Invalid, please try again.', 'yellow'))
                elif username == 'system' or username == 'SYSTEM' or username == 'sys' or username == 'SYS':
                    if password == 'advanche' or password == 'ADVANCHE' or password == 'admin' or password == 'ADMIN':
                        cwcmd = f'(Administrator) A:\{username}>'
                        cw2 = True
                        cwa2 = True
                        break
                    else:
                        print()
                        print(colored('[SYSTEM] Username/Password is Invalid, please try again.', 'yellow'))
                elif username == 'admin' or username == 'ADMIN' or username == 'administrator' or username == 'ADMINISTRATOR':
                    if password == readuser["user_conf"]["AdministratorPassword"]:
                        cwcmd = f'(Administrator) A:\{username}>'
                        cw2 = True
                        cwa2 = True
                        break
                    else:
                        print()
                        print(colored('[SYSTEM] Username/Password is Invalid, please try again.', 'yellow'))
                elif username == readuser["user_conf"]["Username"] or username == readuser["user_conf"]["Username"].lower() or readuser["user_conf"]["Username"].upper():
                    if password == readuser["user_conf"]["Password"]:
                        cwcmd = f'A:\{readuser["user_conf"]["Username"]}>'
                        if cw2 or cwa2 == True:
                            cwcmd = f'(Administrator) A:\{readuser["user_conf"]["Username"]}>'
                        else:
                            cwcmd = f'A:\{readuser["user_conf"]["Username"]}>'
                        break
                    else:
                        print()
                        print(colored('[SYSTEM] Username/Password is Invalid, please try again.', 'yellow'))
                elif username == readuser["user_conf"]["Username2"] or username == readuser["user_conf"]["Username2"].lower() or readuser["user_conf"]["Username2"].upper():
                    if password == readuser["user_conf"]["Password2"]:
                        cwcmd = f'A:\{readuser["user_conf"]["Username2"]}>'
                        if cw2 or cwa2 == True:
                            cwcmd = f'(Administrator) A:\{readuser["user_conf"]["Username2"]}>'
                        else:
                            cwcmd = f'A:\{readuser["user_conf"]["Username2"]}>'
                        break
                    else:
                        print()
                        print(colored('[SYSTEM] Username/Password is Invalid, please try again.', 'yellow'))
                elif username == readuser["user_conf"]["Username3"] or username == readuser["user_conf"]["Username3"].lower() or readuser["user_conf"]["Username3"].upper():
                    if password == readuser["user_conf"]["Password3"]:
                        cwcmd = f'A:\{readuser["user_conf"]["Username3"]}>'
                        if cw2 or cwa2 == True:
                            cwcmd = f'(Administrator) A:\{readuser["user_conf"]["Username3"]}>'
                        else:
                            cwcmd = f'A:\{readuser["user_conf"]["Username3"]}>'
                        break
                    else:
                        print()
                        print(colored('[SYSTEM] Username/Password is Invalid, please try again.', 'yellow'))
                else:
                    print()
                    print(colored('[SYSTEM] Username/Password is Invalid, please try again.', 'yellow'))
        advanche.clear()
        print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
        print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
        print()
        print(colored('[SYSTEM] Starting Advanche ZeroOS...', 'yellow'))
    else:
        advanche.clear()
        print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
        print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
        print()
        print(colored('[SYSTEM] Starting Advanche ZeroOS...', 'yellow'))

    if readconf["system_conf"]["OfflineMode"] == True:
        advanche.clear()
        print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
        print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
        print()
        print(colored('[SYSTEM] Hello! And thank you for using Advanche ZeroOS. It seems that the "OfflineMode" feature is enabled, please consider disabling the "OfflineMode" config for Advanche ZeroOS.', 'yellow'))
        logger.warning('[WARNING] OfflineMode is enabled, disabling all online modules & commands...')
        logger.info('[LOG] Successfully disabled all online modules & commands.')
        input()
        advanche.clear()
        print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
        print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
        print()
        print(colored('[SYSTEM] Starting Advanche ZeroOS...', 'yellow'))

    if readconf["system_conf"]["OfflineMode"] == False and advanche.connect('https://www.google.com') == True:
        try:
            logger.info('[LOG] Checking if Advanche ZeroOS was Modified...')
            url = 'https://api.github.com/gists/db5d2f6eb911036e354822298606b671'
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
            f21.write(data1["files"]["ZeroOS-1.1-Source.py"]["content"])
            f21.close()

            file_exists = exists('ZeroOS-Release.py')
            if file_exists == True:
                f1 = 'ZeroOS-Release.py'
            f2 = 'tmp/sys.zmx'
            result = filecmp.cmp(f1, f2, shallow=False)
            if result != True:
                advanche.clear()
                print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
                print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
                print()
                print(colored('[SYSTEM] Hello! And thank you for using Advanche ZeroOS. It seems that Advanche ZeroOS was Modified. It is recommended to re-download Advanche ZeroOS from the official site before continuing.', 'yellow'))
                logger.warning('[WARNING] Advanche ZeroOS was Modified. It is recommended to re-download Advanche ZeroOS from the official site before continuing.')
                input()
                advanche.clear()
                print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
                print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
                print()
                print(colored('[SYSTEM] Starting Advanche ZeroOS...', 'yellow'))
        except Exception as e:
            a = type(e).__name__.encode()
            b = hashlib.sha256(a).hexdigest().upper()[:8]

            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno

            print()
            print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
            print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{b}', 'yellow'))
            print(colored(f'[SYSTEM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
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

    if readconf["system_conf"]["CheckRequiredModules"] == True:
        if readconf["system_conf"]["OfflineMode"] == False and advanche.connect('https://www.google.com') == True:
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
                advanche.restart()
            else:
                try:
                    import requests
                    import pyttsx3
                    import psutil
                    from guesslang import Guess
                    from requests.structures import CaseInsensitiveDict
                    from colorama import *
                except ImportError as e:
                    a = type(e).__name__.encode()
                    b = hashlib.sha256(a).hexdigest().upper()[:8]

                    exception_type, exception_object, exception_traceback = sys.exc_info()
                    line_number = exception_traceback.tb_lineno

                    print()
                    print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
                    print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{b}', 'yellow'))
                    print(colored(f'[SYSTEM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
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
        elif readconf["system_conf"]["OfflineMode"] == True and advanche.connect('https://www.google.com') == False:
            try:
                import requests
                import pyttsx3
                import psutil
                from guesslang import Guess
                from requests.structures import CaseInsensitiveDict
                from colorama import *
            except ImportError as e:
                a = type(e).__name__.encode()
                b = hashlib.sha256(a).hexdigest().upper()[:8]

                exception_type, exception_object, exception_traceback = sys.exc_info()
                line_number = exception_traceback.tb_lineno

                print()
                print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
                print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{b}', 'yellow'))
                print(colored(f'[SYSTEM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
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
            import psutil
            from guesslang import Guess
            from requests.structures import CaseInsensitiveDict
            from colorama import *
        except ImportError as e:
            a = type(e).__name__.encode()
            b = hashlib.sha256(a).hexdigest().upper()[:8]

            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno

            print()
            print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
            print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{b}', 'yellow'))
            print(colored(f'[SYSTEM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
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
        if readconf["system_conf"]["OfflineMode"] == False and advanche.connect('https://www.google.com') == True:
            try:
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
                    url = 'https://api.github.com/gists/db5d2f6eb911036e354822298606b671'
                    response = urllib.request.urlopen(url)
                    data = response.read()
                    data1 = json.loads(data)
                    open(os.path.abspath(__file__), 'wb').write(data1["files"]["ZeroOS-1.1-Source.py"]["content"])
                    r2 = bytes(data1["files"]["data.txt"]["content"])
                    open(os.getcwd() + '/config/data.txt', 'w').write(str(r2))
                    print(colored('[SYSTEM] Restarting Advanche ZeroOS...', 'yellow'))
                    directory = f'{os.getcwd()}\\tmp'
                    found = os.path.isdir(directory)
                    if found == True:
                        shutil.rmtree(directory)
                    logging.shutdown()
                    sleep(3)
                    advanche.restart()
                else:
                    logger.info('[LOG] No Updates Found.')
                    print(colored('[SYSTEM] No Updates Found!', 'yellow'))
            except Exception as e:
                a = type(e).__name__.encode()
                b = hashlib.sha256(a).hexdigest().upper()[:8]

                exception_type, exception_object, exception_traceback = sys.exc_info()
                line_number = exception_traceback.tb_lineno

                print()
                print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
                print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{b}', 'yellow'))
                print(colored(f'[SYSTEM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
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

    if readuser["user_conf"]["Username"] == "":
        if readuser["user_conf"]["Username2"] == "":
            if readuser["user_conf"]["Username3"] == "":
                a = "No existing users we're found, please re-run the Post-Setup or re-install Advanche ZeroOS."
                b = a.encode()
                c = hashlib.sha256(a).hexdigest().upper()[:8]

                print()
                print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
                print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{c}', 'yellow'))
                print(colored(f'[SYSTEM ERROR] ERROR MESSAGE: {a}', 'yellow'))
                logger.error('[ERROR] An error has occured while using Advanche ZeroOS.')
                logger.error(f'[ERROR] ERROR CODE: 0x{c}')
                logger.error(f'[ERROR] ERROR MESSAGE: {a}')
                input()
                print(Fore.YELLOW, '[SYSTEM] Shutting Down Advanche ZeroOS...')
                directory = f'{os.getcwd()}\\tmp'
                found = os.path.isdir(directory)
                if found == True:
                    shutil.rmtree(directory)
                sleep(3)
                sys.exit(0)

    def delete_user(username):
        if username == readuser["user_conf"]["Username"]:
            config = open('config/user.json', 'r+')
            jsondata = config.read()
            modified = jsondata.replace(f'"Username": "{readuser["user_conf"]["Username"]}"', f'"Username": ""')
            config.seek(0)
            config.truncate()
            config.writelines(modified)
            config.close()
            config = open('config/user.json', 'r+')
            jsondata = config.read()
            modified = jsondata.replace(f'"Password": "{readuser["user_conf"]["Password"]}"', f'"Password": ""')
            config.seek(0)
            config.truncate()
            config.writelines(modified)
            config.close()
        elif username == readuser["user_conf"]["Username2"]:
            config = open('config/user.json', 'r+')
            jsondata = config.read()
            modified = jsondata.replace(f'"Username2": "{readuser["user_conf"]["Username2"]}"', f'"Username2": ""')
            config.seek(0)
            config.truncate()
            config.writelines(modified)
            config.close()
            config = open('config/user.json', 'r+')
            jsondata = config.read()
            modified = jsondata.replace(f'"Password2": "{readuser["user_conf"]["Password2"]}"', f'"Password2": ""')
            config.seek(0)
            config.truncate()
            config.writelines(modified)
            config.close()
        elif username == readuser["user_conf"]["Username3"]:
            config = open('config/user.json', 'r+')
            jsondata = config.read()
            modified = jsondata.replace(f'"Username3": "{readuser["user_conf"]["Username3"]}"', f'"Username3": ""')
            config.seek(0)
            config.truncate()
            config.writelines(modified)
            config.close()
            config = open('config/user.json', 'r+')
            jsondata = config.read()
            modified = jsondata.replace(f'"Password3": "{readuser["user_conf"]["Password3"]}"', f'"Password3": ""')
            config.seek(0)
            config.truncate()
            config.writelines(modified)
            config.close()
        else:
            a = 'User Not Found.'
            b = a.encode()
            c = hashlib.sha256(a).hexdigest().upper()[:8]

            print()
            print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
            print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{c}', 'yellow'))
            print(colored(f'[SYSTEM ERROR] ERROR MESSAGE: {a}', 'yellow'))
            logger.error('[ERROR] An error has occured while using Advanche ZeroOS.')
            logger.error(f'[ERROR] ERROR CODE: 0x{c}')
            logger.error(f'[ERROR] ERROR MESSAGE: {a}')
            input()
            print(Fore.YELLOW, '[SYSTEM] Shutting Down Advanche ZeroOS...')
            directory = f'{os.getcwd()}\\tmp'
            found = os.path.isdir(directory)
            if found == True:
                shutil.rmtree(directory)
            sleep(3)
            sys.exit(0)

    logger.info('[LOG] Successfully Loaded Advanche ZeroOS.')
    print(colored('[SYSTEM] Welcome To Advanche ZeroOS!', 'yellow'))

    while True:
        print()
        cmd = input(Fore.YELLOW + cwcmd)
        if cmd == '':
            cmd = 'EmptyCommand'
        split = cmd.split()
        if split[0] == 'clear' or split[0] == 'cls' or split[0] == 'CLEAR' or split[0] == 'CLS':
            advanche.clear()
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
            print(Fore.YELLOW, 'Advanche ZeroOS [Version 1.1.84335.9465]')
            print(Fore.YELLOW, '(c) Advanche Corporation. All rights reserved.')
        elif split[0] == 'help' or split[0] == 'HELP' or split[0] == 'cmds' or split[0] == 'CMDS':
            print(Fore.YELLOW, 'CLEAR/CLS                       CLEARS THE ADVANCHE ZEROOS COMMAND LOG')
            print(Fore.YELLOW, 'ECHO/SAY                        ECHOES ANY TEXT TO ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'RECHO/RSAY                      ECHOES ANY TEXT TO ADVANCHE ZEROOS (REVERSED)')
            print(Fore.YELLOW, 'TTS/SAYTTS                      ECHOES ANYTHING IN TTS TO ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'CMD                             LAUNCHES ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'HELP/CMDS                       SHOWS COMMANDS FOR ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'START                           START CERTAIN PROGRAM IN *.ZRO/*.ZERO/*.ZRX FORMAT')
            print(Fore.YELLOW, '*.ZRO/*.ZERO/*.ZRX              START CERTAIN PROGRAM IN *.ZRO/*.ZERO/*.ZRX FORMAT')
            print(Fore.YELLOW, 'COPY/CP                         COPIES ANY FILE TO ANOTHER DIRECTORY')  
            print(Fore.YELLOW, 'MOVE/MV                         MOVES ANY FILE TO ANOTHER DIRECTORY')
            print(Fore.YELLOW, 'EXIT/CTRL+C/SHUTDOWN            EXITS ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'RESTART                         RESTARTS ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'RANDOM                          CHOOSES A RANDOM NUMBER BETWEEN A & B')
            print(Fore.YELLOW, 'UPDATE/RESTORE (ONLINE)         UPDATES ADVANCHE ZEROOS TO THE LATEST VERSION')
            print(Fore.YELLOW, 'INSTALL/INS                     INSTALLS AN APPLICATION PACKAGE IN *.ZPX/*.ZPPX/*.ZPP FORMAT')
            print(Fore.YELLOW, 'SEND/RQSEND (ONLINE)            SENDS GET REQUEST TO SPECIFIED URL')
            print(Fore.YELLOW, 'DATE                            OUTPUTS CURRENT DATE TO ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'TIME                            OUTPUTS CURRENT TIME TO ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'IP/IPIFY (ONLINE)               THE IP/IPIFY MODULE FOR ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'USER/USERNAME                   CHANGES CURRENT USERNAME TO NEW USERNAME FOR ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'PSWD/PASSWORD                   CHANGES CURRENT PASSWORD TO NEW PASSWORD FOR ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'RESET (ONLINE)                  RESETS THE ENTIRE OPERATING SYSTEM OF ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'ABOUT/SYSTEM                    SHOWS ABOUT FOR ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'ADMIN/ADMINISTRATOR (USER)      ENABLES/DISABLES ADMINISTRATOR MODE FOR ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'LOGOFF                          LOGS OFF USER ACCOUNT FOR ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'CUSER/CREATEUSER (ADMIN)        CREATES A NEW USER FOR ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'DUSER/DELETEUSER (ADMIN)        DELETES AN EXISTING USER FOR ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'NONCORE/CHATBOT (ONLINE)        CHAT WITH A BUILT-IN AI LEARNING CHATBOT FOR ADVANCHE ZEROOS')
            print(Fore.YELLOW, 'SCAN/VSCAN (ONLINE)             LETS YOU SCAN FILES ON YOUR COMPUTER FOR VIRUSES')
        elif split[0] == 'start' or split[0] == 'START':
            if 1 < len(split):
                if split[1].endswith('.zro') or split[1].endswith('.zero') or split[1].endswith('.ZRO') or split[1].endswith('.ZERO'):
                    print(Fore.YELLOW, '[SYSTEM] Launching Program...')
                    print()
                    file_exists = exists(split[1])
                    if file_exists == True:
                        f = open(split[1], 'r')
                        data = f.read()
                        name = guess.language_name(data)
                        if name == 'Python':
                            try:
                                subprocess.check_call(["python.exe", f"{split[1]}"], shell=False)
                            except subprocess.CalledProcessError:
                                a = type(e).__name__.encode()
                                b = hashlib.sha256(a).hexdigest().upper()[:8]

                                exception_type, exception_object, exception_traceback = sys.exc_info()
                                line_number = exception_traceback.tb_lineno

                                print()
                                print(colored(f'[PROGRAM ERROR] An error has occured while using {split[1]}. Please report this error to the Main Developer.\n', 'yellow'))
                                print(colored(f'[PROGRAM ERROR] ERROR CODE: 0x{b}', 'yellow'))
                                print(colored(f'[PROGRAM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
                        else:
                            a = 'Program File Is In Unknown Format.'
                            b = a.encode()
                            c = hashlib.sha256(b).hexdigest().upper()[:8]

                            exception_type, exception_object, exception_traceback = sys.exc_info()
                            line_number = exception_traceback.tb_lineno

                            print()
                            print(colored(f'[PROGRAM ERROR] An error has occured while using {split[1]}. Please report this error to the Main Developer.\n', 'yellow'))
                            print(colored(f'[PROGRAM ERROR] ERROR CODE: 0x{c}', 'yellow'))
                            print(colored(f'[PROGRAM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
                    else:
                        print(Fore.YELLOW, f"[SYSTEM] '{split[1]}' is not recognized as an operable program.")   
                elif split[1].endswith('.zrx') or split[1].endswith('.ZRX'):
                    if 1 < len(split):
                        print(Fore.YELLOW, '[SYSTEM] Launching Program...')
                        print()
                        file_exists = exists(split[1])
                        if file_exists == True:
                            try:
                                system(split[1]) 
                            except subprocess.CalledProcessError:
                                a = type(e).__name__.encode()
                                b = hashlib.sha256(a).hexdigest().upper()[:8]

                                exception_type, exception_object, exception_traceback = sys.exc_info()
                                line_number = exception_traceback.tb_lineno

                                print()
                                print(colored(f'[PROGRAM ERROR] An error has occured while using {split[1]}. Please report this error to the Main Developer.\n', 'yellow'))
                                print(colored(f'[PROGRAM ERROR] ERROR CODE: 0x{b}', 'yellow'))
                                print(colored(f'[PROGRAM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
                        else:
                            print(Fore.YELLOW, f"[SYSTEM] '{split[1]}' is not recognized as an operable program.")   
                    else:
                        print(Fore.YELLOW, f"[SYSTEM] The syntax of the command '{split[0]}' is incorrect.")
                else:
                    print(Fore.YELLOW, f"[SYSTEM] '{split[1]}' is not recognized as an operable program.")
            else:
                print(Fore.YELLOW, f"[SYSTEM] The syntax of the command '{split[0]}' is incorrect.")
        elif split[0] == 'copy' or split[0] == 'cp' or split[0] == 'COPY' or split[0] == 'CP':
            if 2 < len(split):
                system(f'copy {split[1]} {split[2]}')
            else:
                print(Fore.YELLOW, f"[SYSTEM] The syntax of the command '{split[0]}' is incorrect.")
        elif split[0] == 'move' or split[0] == 'mv' or split[0] == 'MOVE' or split[0] == 'MV':
            if 2 < len(split):
                system(f'move {split[1]} {split[2]}')
            else:
                print(Fore.YELLOW, f"[SYSTEM] The syntax of the command '{split[0]}' is incorrect.")
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
                except subprocess.CalledProcessError:
                    a = type(e).__name__.encode()
                    b = hashlib.sha256(a).hexdigest().upper()[:8]

                    exception_type, exception_object, exception_traceback = sys.exc_info()
                    line_number = exception_traceback.tb_lineno

                    print()
                    print(colored(f'[PROGRAM ERROR] An error has occured while using {split[0]}. Please report this error to the Main Developer.\n', 'yellow'))
                    print(colored(f'[PROGRAM ERROR] ERROR CODE: 0x{b}', 'yellow'))
                    print(colored(f'[PROGRAM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
            else:
                print(Fore.YELLOW, f"[SYSTEM] '{split[0]}' is not recognized as an operable program.")   
        elif split[0].endswith('.zrx') or split[0].endswith('.ZRX'):
            print(Fore.YELLOW, '[SYSTEM] Launching Program...')
            print()
            file_exists = exists(split[0])
            if file_exists == True:
                try:
                    system(split[0]) 
                except subprocess.CalledProcessError:
                    a = type(e).__name__.encode()
                    b = hashlib.sha256(a).hexdigest().upper()[:8]

                    exception_type, exception_object, exception_traceback = sys.exc_info()
                    line_number = exception_traceback.tb_lineno

                    print()
                    print(colored(f'[PROGRAM ERROR] An error has occured while using {split[0]}. Please report this error to the Main Developer.\n', 'yellow'))
                    print(colored(f'[PROGRAM ERROR] ERROR CODE: 0x{b}', 'yellow'))
                    print(colored(f'[PROGRAM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
            else:
                print(Fore.YELLOW, f"[SYSTEM] '{split[0]}' is not recognized as an operable program.")   
        elif split[0] == 'random' or split[0] == 'RANDOM':
            if 2 < len(split):
                print(Fore.YELLOW, random.randint(int(split[1]), int(split[2])))
            else:
                print(Fore.YELLOW, f"[SYSTEM] The syntax of the command '{split[0]}' is incorrect.")
        elif split[0] == 'EmptyCommand':
            pass
        elif split[0] == 'update' or split[0] == 'UPDATE' or split[0] == 'restore' or split[0] == 'RESTORE':
            if readconf["system_conf"]["OfflineMode"] == False and advanche.connect('https://www.google.com') == True:
                try:
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
                        file2 = open('tmp/data.txt', 'w+')
                        file2.write(data1["files"]["data.txt"]["content"])
                        file2.close()
                        f1 = 'config/data.txt'
                        f2 = 'tmp/data.txt'
                        result = filecmp.cmp(f1, f2, shallow=False)
                        if result != True:
                            logger.info('[LOG] Updating Advanche ZeroOS...')
                            print(colored('[SYSTEM] Updating ZeroOS...', 'yellow'))
                            url = 'https://api.github.com/gists/db5d2f6eb911036e354822298606b671'
                            response = urllib.request.urlopen(url)
                            data = response.read()
                            data1 = json.loads(data)
                            open(os.path.abspath(__file__), 'wb').write(data1["files"]["ZeroOS-1.1-Source.py"]["content"])
                            r2 = bytes(data1["files"]["data.txt"]["content"])
                            open(os.getcwd() + '/config/data.txt', 'w').write(str(r2))
                            print(colored('[SYSTEM] Restarting Advanche ZeroOS...', 'yellow'))
                            directory = f'{os.getcwd()}\\tmp'
                            found = os.path.isdir(directory)
                            if found == True:
                                shutil.rmtree(directory)
                            logging.shutdown()
                            sleep(3)
                            advanche.restart()
                        else:
                            logger.info('[LOG] No Updates Found.')
                            print(colored('[SYSTEM] No Updates Found!', 'yellow'))
                    else:
                        print(Fore.YELLOW, '[SYSTEM] Advanche ZeroOS Update Check Aborted.')
                except Exception as e:
                    a = type(e).__name__.encode()
                    b = hashlib.sha256(a).hexdigest().upper()[:8]

                    exception_type, exception_object, exception_traceback = sys.exc_info()
                    line_number = exception_traceback.tb_lineno

                    print()
                    print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
                    print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{b}', 'yellow'))
                    print(colored(f'[SYSTEM ERROR] ERROR MESSAGE: {e}', 'yellow'))
                    print(colored(f'[SYSTEM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
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
            else:
                print(Fore.YELLOW, f"[SYSTEM] '{split[0]}' is not recognized as an internal command or an operable program.")
        elif split[0] == 'version' or split[0] == 'VERSION' or split[0] == 'ver' or split[0] == 'VER':
            print(Fore.YELLOW, 'Advanche ZeroOS [Version 1.1.84335.9465]')
        elif split[0] == 'restart' or split[0] == 'RESTART':
            print(colored('[SYSTEM] Restarting Advanche ZeroOS...', 'yellow'))
            directory = f'{os.getcwd()}\\tmp'
            found = os.path.isdir(directory)
            if found == True:
                shutil.rmtree(directory)
            logging.shutdown()
            sleep(3)
            advanche.restart()
        elif split[0] == 'install' or split[0] == 'INSTALL' or split[0] == 'ins' or split[0] == 'INS':
            if 1 < len(split):
                print(Fore.YELLOW, '[SYSTEM] Checking If Application Package Exists...')
                print()
                if split[1].endswith('.zpx') or split[1].endswith('.zppx') or split[1].endswith('.zpp') or split[1].endswith('.ZPX') or split[1].endswith('.ZPPX') or split[1].endswith('.ZPP'):
                    file_exists = exists(split[1])
                    if file_exists == True:
                        print(Fore.YELLOW, '[SYSTEM] Installing Application Package...')
                        try:
                            cmd = f'Add-AppxPackage -Path {split[1]}'
                            subprocess.run(['powershell', '-Command', cmd])
                            print(Fore.YELLOW, '[SYSTEM] Successfully Installed Application Package.')
                        except subprocess.CalledProcessError:
                            a = type(e).__name__.encode()
                            b = hashlib.sha256(a).hexdigest().upper()[:8]

                            exception_type, exception_object, exception_traceback = sys.exc_info()
                            line_number = exception_traceback.tb_lineno

                            print()
                            print(colored(f'[INSTALLATION ERROR] An error has occured while using {split[0]}. Please report this error to the Main Developer.\n', 'yellow'))
                            print(colored(f'[INSTALLATION ERROR] ERROR CODE: 0x{b}', 'yellow'))
                            print(colored(f'[INSTALLATION ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
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
            if readconf["system_conf"]["OfflineMode"] == False and advanche.connect('https://www.google.com') == True:
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

                        exception_type, exception_object, exception_traceback = sys.exc_info()
                        line_number = exception_traceback.tb_lineno

                        print()
                        print(Fore.YELLOW, '[RQSEND ERROR] An error has occured while sending the GET Request. Maybe the URL is invalid or the server is down.')
                        print(Fore.YELLOW, f'[RQSEND ERROR] ERROR CODE: 0x{b}')
                        print(Fore.YELLOW, f'[RQSEND ERROR] ERROR LINE NUMBER: {line_number}')
                        print(Fore.YELLOW, f'[RQSEND ERROR] ERROR MESSAGE: {e}')
                        logger.error('[ERROR] An error has occured while sending the GET Request.')
                        logger.error(f'[ERROR] ERROR CODE: 0x{b}')
                        logger.error(f'[ERROR] ERROR MESSAGE: {e}')
                else:
                    print(Fore.YELLOW, f"[SYSTEM] The syntax of the command '{split[0]}' is incorrect.")
            else:
                print(Fore.YELLOW, f"[SYSTEM] '{split[0]}' is not recognized as an internal command or an operable program.")
        elif split[0] == 'date' or split[0] == 'DATE':
            now = datetime.now()
            date = now.strftime('[SYSTEM] Current Date: %A %m/%d/%Y')
            print(Fore.YELLOW, date)
        elif split[0] == 'time' or split[0] == 'TIME':
            now = datetime.now()
            time = now.strftime('[SYSTEM] Current Time: %H:%M:%S')
            print(Fore.YELLOW, time)
        elif split[0] == 'ip' or split[0] == 'IP' or split[0] == 'ipify' or split[0] == 'IPIFY':
            if readconf["system_conf"]["OfflineMode"] == False and advanche.connect('https://www.google.com') == True:
                if 1 < len(split):
                    if split[1] == 'getlocal' or split[1] == 'GETLOCAL':
                        try:
                            hostname = socket.gethostname()
                            public_ip = requests.get('https://api.ipify.org').text
                            private_ip = socket.gethostbyname(hostname)
                            print(Fore.YELLOW, f'[SYSTEM] Public IP Address: {public_ip}')
                            print(Fore.YELLOW, f'[SYSTEM] Private IP Address: {private_ip}')
                        except requests.RequestException as e:
                            a = type(e).__name__.encode()
                            b = hashlib.sha256(a).hexdigest().upper()[:8]

                            exception_type, exception_object, exception_traceback = sys.exc_info()
                            line_number = exception_traceback.tb_lineno

                            print()
                            print(Fore.YELLOW, '[RQSEND ERROR] An error has occured while sending the GET Request. Maybe the URL is invalid or the server is down.')
                            print(Fore.YELLOW, f'[RQSEND ERROR] ERROR CODE: 0x{b}')
                            print(Fore.YELLOW, f'[RQSEND ERROR] ERROR LINE NUMBER: {line_number}')
                            print(Fore.YELLOW, f'[RQSEND ERROR] ERROR MESSAGE: {e}')
                            logger.error('[ERROR] An error has occured while sending the GET Request.')
                            logger.error(f'[ERROR] ERROR CODE: 0x{b}')
                            logger.error(f'[ERROR] ERROR MESSAGE: {e}')
                    elif split[1] == 'lookup' or split[1] == 'LOOKUP':
                        if 2 < len(split):
                            try:
                                print(Fore.YELLOW, f"[SYSTEM] Checking if IP Address '{split[2]}' exists...")
                                req = requests.get(f'http://ip-api.com/json/{split[2]}')
                                ipdata = req.json()
                                if ipdata["status"] == 'fail':
                                    print(Fore.YELLOW, f"[SYSTEM] The IP Address '{split[2]}' does not exist.")
                                    continue
                                print(Fore.YELLOW, f"[SYSTEM] Searching For Information On '{split[2]}'...")
                                req = requests.get(f'http://ip-api.com/json/{split[2]}')
                                ipdata = req.json()
                                req2 = requests.get(f'https://us1.locationiq.com/v1/reverse.php?key=pk.2436162a8ff5ff42cdfee730392b665e&lat={ipdata["lat"]}&lon={ipdata["lon"]}&format=json')
                                ipdata2 = req2.json()
                                print(Fore.YELLOW, '[SYSTEM] Information Successfully retrieved from IP Database.')
                                print()
                                print(Fore.YELLOW, f'[SYSTEM] IP Address: {split[2]}')
                                print(Fore.YELLOW, f'[SYSTEM] Country: {ipdata["country"]}')
                                print(Fore.YELLOW, f'[SYSTEM] Region: {ipdata["regionName"]}')
                                print(Fore.YELLOW, f'[SYSTEM] City: {ipdata["city"]}')
                                print(Fore.YELLOW, f'[SYSTEM] ZIP Code: {ipdata["zip"]}')
                                print(Fore.YELLOW, f'[SYSTEM] Timezone: {ipdata["timezone"]}')
                                print(Fore.YELLOW, f'[SYSTEM] Internet Service Provider (ISP): {ipdata["isp"]}')
                                try:
                                    if 9 in ipdata2:
                                        print(Fore.YELLOW, f'[SYSTEM] Address: {ipdata2["address"]["house_number"]} {ipdata2["address"]["road"]}')
                                    else:
                                        print(Fore.YELLOW, f'[SYSTEM] Address: {ipdata2["address"]["road"]}')
                                except:
                                    pass
                                try:
                                    if 13 in ipdata2:
                                        print(Fore.YELLOW, f'[SYSTEM] County: {ipdata2["address"]["county"]}')
                                except:
                                    pass
                                try:
                                    if 11 in ipdata2:
                                        print(Fore.YELLOW, f'[SYSTEM] Neighbourhood/Suburb: {ipdata2["address"]["neighbourhood"]}')
                                except:
                                    pass
                                print(Fore.YELLOW, f'[SYSTEM] Latitude: {ipdata["lat"]}')
                                print(Fore.YELLOW, f'[SYSTEM] Longitude: {ipdata["lon"]}')
                            except Exception as e:
                                a = type(e).__name__.encode()
                                b = hashlib.sha256(a).hexdigest().upper()[:8]

                                exception_type, exception_object, exception_traceback = sys.exc_info()
                                line_number = exception_traceback.tb_lineno

                                print()
                                print(Fore.YELLOW, '[RQSEND ERROR] An error has occured while sending the GET Request. Maybe the URL is invalid or the server is down.')
                                print(Fore.YELLOW, f'[RQSEND ERROR] ERROR CODE: 0x{b}')
                                print(Fore.YELLOW, f'[RQSEND ERROR] ERROR LINE NUMBER: {line_number}')
                                print(Fore.YELLOW, f'[RQSEND ERROR] ERROR MESSAGE: {e}')
                                logger.error('[ERROR] An error has occured while sending the GET Request.')
                                logger.error(f'[ERROR] ERROR CODE: 0x{b}')
                                logger.error(f'[ERROR] ERROR MESSAGE: {e}')
                        else:
                            print(Fore.YELLOW, '[SYSTEM] ## IP/IPIFY MODULE ##')
                            print()
                            print(Fore.YELLOW, "[SYSTEM] - getlocal (Get's both Public IP & Private IP Addresses)")
                            print(Fore.YELLOW, "[SYSTEM] - lookup (Look up an IP using this tool for information about the IP Address)")
                    else:
                        print(Fore.YELLOW, '[SYSTEM] ## IP/IPIFY MODULE ##')
                        print()
                        print(Fore.YELLOW, "[SYSTEM] - getlocal (Get's both Public IP & Private IP Addresses)")
                        print(Fore.YELLOW, "[SYSTEM] - lookup (Look up an IP using this tool for information about the IP Address)")
                else:
                    print(Fore.YELLOW, '[SYSTEM] ## IP/IPIFY MODULE ##')
                    print()
                    print(Fore.YELLOW, "[SYSTEM] - getlocal (Get's both Public IP & Private IP Addresses)")
                    print(Fore.YELLOW, "[SYSTEM] - lookup (Look up an IP using this tool for information about the IP Address)")
            else:
                print(Fore.YELLOW, f"[SYSTEM] '{split[0]}' is not recognized as an internal command or an operable program.")
        elif split[0] == 'pswd' or split[0] == 'PSWD' or split[0] == 'password' or split[0] == 'PASSWORD':
            print(Fore.YELLOW, f'[SYSTEM] Current System Password: {readuser["user_conf"]["Password"]}')
            while True:
                new_pswd = pwinput.pwinput(Fore.YELLOW + '[SYSTEM] New System Password: ', '●')
                if new_pswd == '':
                    print(Fore.YELLOW, '[SYSTEM] Please enter a New System Password.')
                else:
                    break
            print()
            print(Fore.YELLOW, '[SYSTEM] Changing Current System Password...')
            logger.info(f'[LOG] Changing Current System Password To {new_pswd}...')
            config = open('config/user.json', 'r+')
            jsondata = config.read()
            modified = jsondata.replace(f'"Password": "{readuser["user_conf"]["Password"]}"', f'"Password": "{new_pswd}"')
            config.seek(0)
            config.truncate()
            config.writelines(modified)
            config.close()
            print(Fore.YELLOW, f"[SYSTEM] Successfully Changed Current System Password To '{new_pswd}'.")
            logger.info(f'[LOG] Successfully Changed Current System Password To {new_pswd}.')
            print()
            print(colored('[SYSTEM] Restarting Advanche ZeroOS...', 'yellow'))
            directory = f'{os.getcwd()}\\tmp'
            found = os.path.isdir(directory)
            if found == True:
                shutil.rmtree(directory)
            logging.shutdown()
            sleep(3)
            advanche.restart()
        elif split[0] == 'user' or split[0] == 'USER' or split[0] == 'username' or split[0] == 'USERNAME':
            print(Fore.YELLOW, f'[SYSTEM] Current System Username: {readuser["user_conf"]["Username"]}')
            while True:
                new_user = input(Fore.YELLOW + '[SYSTEM] New System Username: ')
                if new_user == '':
                    print(Fore.YELLOW, '[SYSTEM] Please enter a New System Username.')
                else:
                    break
            print()
            print(Fore.YELLOW, '[SYSTEM] Changing Current System Username...')
            logger.info(f'[LOG] Changing Current System Username To {new_user}...')
            config = open('config/user.json', 'r+')
            jsondata = config.read()
            modified = jsondata.replace(f'"Username": "{readuser["user_conf"]["Username"]}"', f'"Username": "{new_user}"')
            config.seek(0)
            config.truncate()
            config.writelines(modified)
            config.close()
            print(Fore.YELLOW, f"[SYSTEM] Successfully Changed System Username To '{new_user}'.")
            logger.info(f'[LOG] Successfully Changed System Username To {new_user}.')
            print()
            print(colored('[SYSTEM] Restarting Advanche ZeroOS...', 'yellow'))
            directory = f'{os.getcwd()}\\tmp'
            found = os.path.isdir(directory)
            if found == True:
                shutil.rmtree(directory)
            logging.shutdown()
            sleep(3)
            advanche.restart()
        elif split[0] == 'reset' or split[0] == 'RESET':
            if readconf["system_conf"]["OfflineMode"] == False and advanche.connect('https://www.google.com') == True:
                try:
                    cmd1 = input(Fore.YELLOW + '[SYSTEM] NOTE: This will factory reset Advanche ZeroOS. Are you sure you want to continue? [Y/n] ')
                    if cmd1 == 'y' or cmd1 == 'Y':
                        print()
                        print(Fore.YELLOW, '[SYSTEM] Resetting Advanche ZeroOS...')
                        user.close()
                        os.remove('config/config.json')
                        os.remove('config/user.json')
                        url = 'https://api.github.com/gists/dd6cf700c064b84ba0b40674d138112f'
                        response = urllib.request.urlopen(url)
                        data = response.read()
                        data1 = json.loads(data)
                        config = open('config/config.json', 'w')
                        config.write(data1["files"]["config.json"]["content"])
                        config.close()
                        print(Fore.YELLOW, '[SYSTEM] Successfully Resetted Advanche ZeroOS.')
                        print()
                        print(colored('[SYSTEM] Restarting Advanche ZeroOS...', 'yellow'))
                        directory = f'{os.getcwd()}\\tmp'
                        found = os.path.isdir(directory)
                        if found == True:
                            shutil.rmtree(directory)
                        logging.shutdown()
                        sleep(3)
                        advanche.restart()
                    else:
                        print(Fore.YELLOW, '[SYSTEM] Factory Reset Aborted.')
                except Exception as e:
                    a = type(e).__name__.encode()
                    b = hashlib.sha256(a).hexdigest().upper()[:8]

                    exception_type, exception_object, exception_traceback = sys.exc_info()
                    line_number = exception_traceback.tb_lineno

                    print()
                    print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
                    print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{b}', 'yellow'))
                    print(colored(f'[SYSTEM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
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
            else:
                print(Fore.YELLOW, f"[SYSTEM] '{split[0]}' is not recognized as an internal command or an operable program.")
        elif split[0] == 'about' or split[0] == 'ABOUT' or split[0] == 'system' or split[0] == 'SYSTEM':
            print(Fore.YELLOW, '[SYSTEM] Advanche ZeroOS [Version 1.1.84335.9465]')
            print(Fore.YELLOW, '[SYSTEM] (c) Advanche Corporation. All rights reserved.')
            print()
            print(Fore.YELLOW, f'[SYSTEM] Advanche ZeroOS Platform: {platform.system()}')
            print(Fore.YELLOW, f'[SYSTEM] CPU Processor: {advanche.processor()}')
            mem = psutil.virtual_memory().total
            mem1 = psutil.virtual_memory().available
            print(Fore.YELLOW, f'[SYSTEM] Installed Memory (RAM): {advanche.convert_size(mem)} ({advanche.convert_size(mem1)} usable)')
            if platform.architecture()[0] == '32bit':
                print(Fore.YELLOW, f'[SYSTEM] System Type: 32-bit Operating System, x86-based processor')
            else:
                print(Fore.YELLOW, f'[SYSTEM] System Type: 64-bit Operating System, x64-based processor')
            print(Fore.YELLOW, f'[SYSTEM] Computer Name: {socket.gethostname()}')
            print(Fore.YELLOW, '[SYSTEM] Command Type: A:\>')
            print(Fore.YELLOW, f'[SYSTEM] Username: {username}')
            if cw2 == True or cwa2 == True:
                print(Fore.YELLOW, '[SYSTEM] Administrator Enabled: Yes')
            else:
                print(Fore.YELLOW, '[SYSTEM] Administrator Enabled: No')
            print(Fore.YELLOW, f'[SYSTEM] Product ID: {readuser["user_conf"]["ProductID"]}')
        elif split[0] == 'admin' or split[0] == 'ADMIN' or split[0] == 'administrator' or split[0] == 'ADMINISTRATOR':
            if cw2 == False and cwa2 == False:
                cw1 = input(Fore.YELLOW + '[SYSTEM] NOTE: This will enable Administrator Mode and will enable full access to Advanche ZeroOS. Are you sure you want to continue? [Y/n] ')
                if cw1 == 'y' or cw1 == 'Y':
                    while True:
                        print()
                        password = pwinput.pwinput(Fore.YELLOW + '[SYSTEM] Administrator Login Password: ', '●')
                        if password == readuser["user_conf"]["AdministratorPassword"]:
                            print()
                            print(Fore.YELLOW + '[SYSTEM] Enabling Administrator Mode...')
                            cwcmd = f'(Administrator) A:\{username}>'
                            cw2 = True
                            sleep(0.5)
                            print(Fore.YELLOW + '[SYSTEM] Enabled Administrator Mode Successfully.')
                            break
                        else:
                            print()
                            print(Fore.YELLOW, '[SYSTEM] Administrator Password is Invalid, please try again.')
                else:
                    print(Fore.YELLOW, '[SYSTEM] Administrator Mode Aborted.')
            else:
                cw1 = input(Fore.YELLOW + '[SYSTEM] NOTE: This will disable Administrator Mode and will disable full access to Advanche ZeroOS. Are you sure you want to continue? [Y/n] ')
                if cw1 == 'y' or cw1 == 'Y':
                    while True:
                        print()
                        password = pwinput.pwinput(Fore.YELLOW + '[SYSTEM] Administrator Login Password: ', '●')
                        if password == readuser["user_conf"]["AdministratorPassword"]:
                            print()
                            print(Fore.YELLOW + '[SYSTEM] Disabling Administrator Mode...')
                            cwcmd = f'A:\{username}>'
                            cw2 = False
                            cwa2 = False
                            sleep(0.5)
                            print(Fore.YELLOW + '[SYSTEM] Disabled Administrator Mode Successfully.')
                            break
                        else:
                            print()
                            print(Fore.YELLOW, '[SYSTEM] Administrator Password is Invalid, please try again.')
                else:
                    print(Fore.YELLOW, '[SYSTEM] Administrator Mode Aborted.')
        elif split[0] == 'logoff' or split[0] == 'LOGOFF':
            print(Fore.YELLOW, '[SYSTEM] Logging Off...')
            sleep(0.5)
            if readconf["system_conf"]["LoginRequired"] == True:
                advanche.clear()
                print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
                print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
                print()
                print(colored('[SYSTEM] NOTE: Login Is Required To Boot Advanche ZeroOS.', 'yellow'))
                print(colored("[SYSTEM] NOTE: Forgot your password? Type in 'PSWDFR' to reset your password.", 'yellow'))
                print()
                logger.info('[LOG] Login Required To Boot Advanche ZeroOS.')
                while True:
                    username = input(Fore.YELLOW + '[SYSTEM] Login Username: ')
                    if username == 'pswdfr' or username == 'PSWDFR':
                        reset_password()
                    else:
                        password = pwinput.pwinput(Fore.YELLOW + '[SYSTEM] Login Password: ', '●')
                        if username == '':
                            print()
                            print(colored('[SYSTEM] Username/Password is Invalid, please try again.', 'yellow'))
                        elif username == 'system' or username == 'SYSTEM' or username == 'sys' or username == 'SYS':
                            if password == 'advanche' or password == 'ADVANCHE' or password == 'admin' or password == 'ADMIN':
                                cwcmd = f'(Administrator) A:\{username}>'
                                cw2 = True
                                cwa2 = True
                                break
                            else:
                                print()
                                print(colored('[SYSTEM] Username/Password is Invalid, please try again.', 'yellow'))
                        elif username == 'admin' or username == 'ADMIN' or username == 'administrator' or username == 'ADMINISTRATOR':
                            if password == readuser["user_conf"]["AdministratorPassword"]:
                                cwcmd = f'(Administrator) A:\{username}>'
                                cw2 = True
                                cwa2 = True
                                break
                            else:
                                print()
                                print(colored('[SYSTEM] Username/Password is Invalid, please try again.', 'yellow'))
                        elif username == readuser["user_conf"]["Username"] or username == readuser["user_conf"]["Username"].lower() or readuser["user_conf"]["Username"].upper():
                            if password == readuser["user_conf"]["Password"]:
                                cwcmd = f'A:\{readuser["user_conf"]["Username"]}>'
                                if cw2 == True or cwa2 == True:
                                    cwcmd = f'(Administrator) A:\{readuser["user_conf"]["Username"]}>'
                                else:
                                    cwcmd = f'A:\{readuser["user_conf"]["Username"]}>'
                                break
                            else:
                                print()
                                print(colored('[SYSTEM] Username/Password is Invalid, please try again.', 'yellow'))
                        elif username == readuser["user_conf"]["Username2"] or username == readuser["user_conf"]["Username2"].lower() or readuser["user_conf"]["Username2"].upper():
                            if password == readuser["user_conf"]["Password2"]:
                                cwcmd = f'A:\{readuser["user_conf"]["Username2"]}>'
                                if cw2 == True or cwa2 == True:
                                    cwcmd = f'(Administrator) A:\{readuser["user_conf"]["Username2"]}>'
                                else:
                                    cwcmd = f'A:\{readuser["user_conf"]["Username2"]}>'
                                break
                            else:
                                print()
                                print(colored('[SYSTEM] Username/Password is Invalid, please try again.', 'yellow'))
                        elif username == readuser["user_conf"]["Username3"] or username == readuser["user_conf"]["Username3"].lower() or readuser["user_conf"]["Username3"].upper():
                            if password == readuser["user_conf"]["Password3"]:
                                cwcmd = f'A:\{readuser["user_conf"]["Username3"]}>'
                                if cw2 == True or cwa2 == True:
                                    cwcmd = f'(Administrator) A:\{readuser["user_conf"]["Username3"]}>'
                                else:
                                    cwcmd = f'A:\{readuser["user_conf"]["Username3"]}>'
                                break
                            else:
                                print()
                                print(colored('[SYSTEM] Username/Password is Invalid, please try again.', 'yellow'))
                        else:
                            print()
                            print(colored('[SYSTEM] Username/Password is Invalid, please try again.', 'yellow'))
                advanche.clear()
                print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
                print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
                print()
                print(colored('[SYSTEM] Starting Advanche ZeroOS...', 'yellow'))
                logger.info('[LOG] Successfully Loaded Advanche ZeroOS.')
                print(colored('[SYSTEM] Welcome To Advanche ZeroOS!', 'yellow'))
            else:
                advanche.clear()
                print(colored('Advanche ZeroOS [Version 1.1.84335.9465]', 'yellow'))
                print(colored('(c) Advanche Corporation. All rights reserved.', 'yellow'))
                print()
                print(colored('[SYSTEM] Starting Advanche ZeroOS...', 'yellow'))
                logger.info('[LOG] Successfully Loaded Advanche ZeroOS.')
                print(colored('[SYSTEM] Welcome To Advanche ZeroOS!', 'yellow'))
        elif split[0] == 'cuser' or split[0] == 'CUSER' or split[0] == 'createuser' or split[0] == 'CREATEUSER':
            cmd1 = input(Fore.YELLOW + '[SYSTEM] NOTE: This will create a new user & will allow you to use Advanche ZeroOS as normally for that new user account. Are you sure you want to continue? [Y/n] ')
            if cmd1 == 'y' or cmd1 == 'Y':
                while True:
                    print()
                    password = pwinput.pwinput(Fore.YELLOW + '[SYSTEM] Administrator Login Password: ', '●')
                    if password == readuser["user_conf"]["AdministratorPassword"]:
                        print()
                        user1 = input(Fore.YELLOW + '[SYSTEM] New Login Username: ')
                        pass1 = pwinput.pwinput(Fore.YELLOW + '[SYSTEM] New Login Password: ', '●')
                        print()
                        print(Fore.YELLOW, '[SYSTEM] Creating New User Account...')
                        if readuser["user_conf"]["Username2"] == "" and readuser["user_conf"]["Password2"] == "":
                            config = open('config/user.json', 'r+')
                            jsondata = config.read()
                            modified = jsondata.replace(f'"Username2": ""', f'"Username2": "{user1}"')
                            config.seek(0)
                            config.truncate()
                            config.writelines(modified)
                            config.close()
                            config = open('config/user.json', 'r+')
                            jsondata = config.read()
                            modified = jsondata.replace(f'"Password2": ""', f'"Password2": "{pass1}"')
                            config.seek(0)
                            config.truncate()
                            config.writelines(modified)
                            config.close()
                            readconf = json.loads(x)
                            print(Fore.YELLOW, '[SYSTEM] Successfully Created User Account.')
                            break
                        elif readuser["user_conf"]["Username3"] == "" and readuser["user_conf"]["Password3"] == "":
                            config = open('config/user.json', 'r+')
                            jsondata = config.read()
                            modified = jsondata.replace(f'"Username3": ""', f'"Username3": "{user1}"')
                            config.seek(0)
                            config.truncate()
                            config.writelines(modified)
                            config.close()
                            config = open('config/user.json', 'r+')
                            jsondata = config.read()
                            modified = jsondata.replace(f'"Password3": ""', f'"Password3": "{pass1}"')
                            config.seek(0)
                            config.truncate()
                            config.writelines(modified)
                            config.close()
                            readconf = json.loads(x)
                            print(Fore.YELLOW, '[SYSTEM] Successfully Created User Account.')
                            break
                        else:
                            a = "Couldn't Create New User Account (Maximum Of 3 Users Allowed)."
                            b = a.encode()
                            c = hashlib.sha256(b).hexdigest().upper()[:8]

                            print()
                            print(Fore.YELLOW, '[CUSER ERROR] An error has occured while creating a New User Account. Maybe the URL is invalid or the server is down.')
                            print(Fore.YELLOW, f'[CUSER ERROR] ERROR CODE: 0x{c}')
                            print(Fore.YELLOW, f'[CUSER ERROR] ERROR MESSAGE: {a}')
                            logger.error('[ERROR] An error has occured while creating a New User Account.')
                            logger.error(f'[ERROR] ERROR CODE: 0x{c}')
                            logger.error(f'[ERROR] ERROR MESSAGE: {a}')
                            break
                    else:
                        print(Fore.YELLOW, '[SYSTEM] Administrator Password is Invalid, please try again.')
            else:
                print(Fore.YELLOW, '[SYSTEM] User Account Creation Aborted.')
        elif split[0] == 'duser' or split[0] == 'DUSER' or split[0] == 'deleteuser' or split[0] == 'DELETEUSER':
            cmd1 = input(Fore.YELLOW + '[SYSTEM] NOTE: This will delete an existing user & will delete all personal data associated with the user. Are you sure you want to continue? [Y/n] ')
            if cmd1 == 'y' or cmd1 == 'Y':
                deleted_user = False
                while True:
                    if deleted_user == True:
                        break
                    print()
                    password = pwinput.pwinput(Fore.YELLOW + '[SYSTEM] Administrator Login Password: ', '●')
                    if password == readuser["user_conf"]["AdministratorPassword"]:
                        print()
                        print(Fore.YELLOW, '## USER LIST ##')
                        print()
                        if readuser["user_conf"]["Username"] != "":
                            print(Fore.YELLOW, f'[SYSTEM] #1 {readuser["user_conf"]["Username"]}')
                            if readuser["user_conf"]["Username2"] != "":
                                print(Fore.YELLOW, f'[SYSTEM] #2 {readuser["user_conf"]["Username2"]}')
                                if readuser["user_conf"]["Username3"] != "":
                                    print(Fore.YELLOW, f'[SYSTEM] #3 {readuser["user_conf"]["Username3"]}')
                                    while True:
                                        print()
                                        userdel = input(Fore.YELLOW + f'[SYSTEM] Which user would you like to delete? (ex. {readuser["user_conf"]["Username2"]}) : ')
                                        if userdel == readuser["user_conf"]["Username"]:
                                            print()
                                            print(Fore.YELLOW, f"[SYSTEM] Deleting User '{userdel}'...")
                                            sleep(0.5)
                                            delete_user(userdel)
                                            deleted_user = True
                                            print(Fore.YELLOW, '[SYSTEM] Successfully Deleted User.')
                                            break
                                        elif userdel == readuser["user_conf"]["Username2"]:
                                            print()
                                            print(Fore.YELLOW, f"[SYSTEM] Deleting User '{userdel}'...")
                                            sleep(0.5)
                                            delete_user(userdel)
                                            deleted_user = True
                                            print(Fore.YELLOW, '[SYSTEM] Successfully Deleted User.')
                                            break
                                        elif userdel == readuser["user_conf"]["Username3"]:
                                            print()
                                            print(Fore.YELLOW, f"[SYSTEM] Deleting User '{userdel}'...")
                                            sleep(0.5)
                                            delete_user(userdel)
                                            deleted_user = True
                                            print(Fore.YELLOW, '[SYSTEM] Successfully Deleted User.')
                                            break
                                        else:
                                            print()
                                            print(Fore.YELLOW, f"[SYSTEM] Deleting User '{userdel}'...")
                                            sleep(0.5)
                                            print(Fore.YELLOW, '[SYSTEM] User Deletion Failed (User Not Found).')
                                else:
                                    break
                            elif readuser["user_conf"]["Username3"] != "":
                                print(Fore.YELLOW, f'[SYSTEM] #2 {readuser["user_conf"]["Username3"]}')
                                while True:
                                    print()
                                    userdel = input(Fore.YELLOW + f'[SYSTEM] Which user would you like to delete? (ex. {readuser["user_conf"]["Username3"]}) : ')
                                    if userdel == readuser["user_conf"]["Username"]:
                                        print()
                                        print(Fore.YELLOW, f"[SYSTEM] Deleting User '{userdel}'...")
                                        sleep(0.5)
                                        delete_user(userdel)
                                        print(Fore.YELLOW, '[SYSTEM] Successfully Deleted User.')
                                        break
                                    elif userdel == readuser["user_conf"]["Username3"]:
                                        print()
                                        print(Fore.YELLOW, f"[SYSTEM] Deleting User '{userdel}'...")
                                        sleep(0.5)
                                        delete_user(userdel)
                                        print(Fore.YELLOW, '[SYSTEM] Successfully Deleted User.')
                                        break
                                    else:
                                        print()
                                        print(Fore.YELLOW, f"[SYSTEM] Deleting User '{userdel}'...")
                                        sleep(0.5)
                                        print(Fore.YELLOW, '[SYSTEM] User Deletion Failed (User Not Found).')
                            else:
                                break
                        elif readuser["user_conf"]["Username2"] != "":
                            print(Fore.YELLOW, f'[SYSTEM] #1 {readuser["user_conf"]["Username2"]}')
                            if readuser["user_conf"]["Username3"] != "":
                                print(Fore.YELLOW, f'[SYSTEM] #3 {readuser["user_conf"]["Username3"]}')
                                while True:
                                    print()
                                    userdel = input(Fore.YELLOW + f'[SYSTEM] Which user would you like to delete? (ex. {readuser["user_conf"]["Username2"]}) : ')
                                    if userdel == readuser["user_conf"]["Username2"]:
                                        print()
                                        print(Fore.YELLOW, f"[SYSTEM] Deleting User '{userdel}'...")
                                        sleep(0.5)
                                        delete_user(userdel)
                                        print(Fore.YELLOW, '[SYSTEM] Successfully Deleted User.')
                                        break
                                    elif userdel == readuser["user_conf"]["Username3"]:
                                        print()
                                        print(Fore.YELLOW, f"[SYSTEM] Deleting User '{userdel}'...")
                                        sleep(0.5)
                                        delete_user(userdel)
                                        print(Fore.YELLOW, '[SYSTEM] Successfully Deleted User.')
                                        break
                                    else:
                                        print()
                                        print(Fore.YELLOW, f"[SYSTEM] Deleting User '{userdel}'...")
                                        sleep(0.5)
                                        print(Fore.YELLOW, '[SYSTEM] User Deletion Failed (User Not Found).')
                        elif readuser["user_conf"]["Username3"] != "":
                            print(Fore.YELLOW, f'[SYSTEM] #1 {readuser["user_conf"]["Username3"]}')
                            break
                        else:
                            print(Fore.YELLOW, '[SYSTEM] No Users Found.')
                            break
                    else:
                        print(Fore.YELLOW, '[SYSTEM] Administrator Password is Invalid, please try again.')
            else:
                print(Fore.YELLOW, '[SYSTEM] User Account Deletion Aborted.')
        elif split[0] == 'noncore' or split[0] == 'NONCORE' or split[0] == 'chatbot' or split[0] == 'CHATBOT':
            if readconf["system_conf"]["OfflineMode"] == False and advanche.connect('https://www.google.com') == True:
                if 1 < len(split):
                    print()
                    print(Fore.YELLOW, '[SYSTEM] Advanche NonCore is Thinking...')
                    chat = requests.get(f'http://api.brainshop.ai/get?bid=163511&key=kPwlGenB1kS6n6l9&uid={readuser["user_conf"]["ProductID"]}&msg={split[1]}')
                    chat1 = chat.json()
                    print(Fore.YELLOW, f'[SYSTEM] Advanche NonCore: {chat1["cnt"]}')
                else:
                    print(Fore.YELLOW, f"[SYSTEM] The syntax of the command '{split[0]}' is incorrect.")
            else:
                print(Fore.YELLOW, f"[SYSTEM] '{split[0]}' is not recognized as an internal command or an operable program.")
        elif split[0] == 'scan' or split[0] == 'SCAN' or split[0] == 'vscan' or split[0] == 'VSCAN':
            if readconf["system_conf"]["OfflineMode"] == False and advanche.connect('https://www.google.com') == True:
                print(Fore.YELLOW, f"[SYSTEM] Checking if '{split[1]}' exists...")
                file_exists = exists(split[1])
                if file_exists == False:
                    print(Fore.YELLOW, f'[SYSTEM] File does not exist.')
                    continue
                print(Fore.YELLOW, f"[SYSTEM] Sending '{split[1]}' to Cloud-Based Anti-Virus...")
                url = 'https://www.virustotal.com/vtapi/v2/file/scan'
                params = { 'apikey': 'efe1fb46f42dfa9c974644bb7b1ae40495774d3bda40545266900d79dbc585a4' }
                files = { 'file': (f'{split[1]}', open(f'{split[1]}', 'rb')) }
                vscan = requests.post(url, files=files, params=params)
                if vscan.status_code == 200:
                    vscan1 = vscan.json()
                    if vscan1["response_code"] == 1:
                        print(Fore.YELLOW, '[SYSTEM] Successfully Sent File to Cloud-Based Anti-Virus.')
                        i = 0
                        while True:
                            if i == 25:
                                print(Fore.YELLOW, '[SYSTEM] File Scan Successfully Completed.')
                                break
                            for rod in r'\|/-':
                                print(Fore.YELLOW, f'[SYSTEM] Waiting For File Scan to Complete... {rod}', end='\r')
                                sleep(0.25)
                            i += 1
                        print(Fore.YELLOW, '[SYSTEM] Getting Scan Information from Cloud-Based Anti-Virus...')
                        url = 'https://www.virustotal.com/vtapi/v2/file/report'
                        params = { 'apikey': 'efe1fb46f42dfa9c974644bb7b1ae40495774d3bda40545266900d79dbc585a4', 'resource': f'{vscan1["scan_id"]}' }
                        vscan = requests.get(url, params=params)
                        if vscan.status_code == 200:
                            vscan1 = vscan.json()
                            if vscan1["response_code"] == 1:
                                print(Fore.YELLOW, '[SYSTEM] Successfully Got Scan Information from Cloud-Based Anti-Virus.')
                                print()
                                print(Fore.YELLOW, '## SCAN RESULTS ##')
                                print()
                                print(Fore.YELLOW, f'[1] Bkav: {vscan1["scans"]["Bkav"]["detected"]}                                    [2] Lionic: {vscan1["scans"]["Lionic"]["detected"]}')
                                print(Fore.YELLOW, f'[3] MicroWorld-eScan: {vscan1["scans"]["MicroWorld-eScan"]["detected"]}            [4] FireEye: {vscan1["scans"]["FireEye"]["detected"]}')
                                print(Fore.YELLOW, f'[5] CAT-QuickHeal: {vscan1["scans"]["CAT-QuickHeal"]["detected"]}                  [6] McAfee: {vscan1["scans"]["McAfee"]["detected"]}')
                                print(Fore.YELLOW, f'[7] Malwarebytes: {vscan1["scans"]["Malwarebytes"]["detected"]}                    [8] Zillya: {vscan1["scans"]["Zillya"]["detected"]}')
                                print(Fore.YELLOW, f'[9] Sangfor: {vscan1["scans"]["Sangfor"]["detected"]}                              [10] K7AntiVirus: {vscan1["scans"]["K7AntiVirus"]["detected"]}')
                                print(Fore.YELLOW, f'[11] K7GW: {vscan1["scans"]["K7GW"]["detected"]}                                   [12] Baidu: {vscan1["scans"]["Baidu"]["detected"]}')
                                print(Fore.YELLOW, f'[13] VirIT: {vscan1["scans"]["VirIT"]["detected"]}                                 [14] Cyren: {vscan1["scans"]["Cyren"]["detected"]}')
                                print(Fore.YELLOW, f'[15] Symantec: {vscan1["scans"]["Symantec"]["detected"]}                           [16] ESET-NOD32: {vscan1["scans"]["ESET-NOD32"]["detected"]}')
                                print(Fore.YELLOW, f'[17] TrendMicro-HouseCall: {vscan1["scans"]["TrendMicro-HouseCall"]["detected"]}   [18] Avast: {vscan1["scans"]["Avast"]["detected"]}')
                                print(Fore.YELLOW, f'[19] ClamAV: {vscan1["scans"]["ClamAV"]["detected"]}                               [20] Kaspersky: {vscan1["scans"]["Kaspersky"]["detected"]}')
                                print(Fore.YELLOW, f'[21] BitDefender: {vscan1["scans"]["BitDefender"]["detected"]}                     [22] NANO-Antivirus: {vscan1["scans"]["NANO-Antivirus"]["detected"]}')
                                print(Fore.YELLOW, f'[23] SUPERAntiSpyware: {vscan1["scans"]["SUPERAntiSpyware"]["detected"]}           [24] Tencent: {vscan1["scans"]["Tencent"]["detected"]}')
                                print(Fore.YELLOW, f'[25] Ad-Aware: {vscan1["scans"]["Ad-Aware"]["detected"]}                           [26] TACHYON: {vscan1["scans"]["TACHYON"]["detected"]}')
                                print(Fore.YELLOW, f'[27] Emsisoft: {vscan1["scans"]["Emsisoft"]["detected"]}                           [28] Comodo: {vscan1["scans"]["Comodo"]["detected"]}')
                                print(Fore.YELLOW, f'[29] F-Secure: {vscan1["scans"]["F-Secure"]["detected"]}                           [30] DrWeb: {vscan1["scans"]["DrWeb"]["detected"]}')
                                print(Fore.YELLOW, f'[31] VIPRE: {vscan1["scans"]["VIPRE"]["detected"]}                                 [32] TrendMicro: {vscan1["scans"]["TrendMicro"]["detected"]}')
                                print(Fore.YELLOW, f'[33] McAfee-GW-Edition: {vscan1["scans"]["McAfee-GW-Edition"]["detected"]}         [34] CMC: {vscan1["scans"]["CMC"]["detected"]}')
                                print(Fore.YELLOW, f'[35] Sophos: {vscan1["scans"]["Sophos"]["detected"]}                               [36] Jiangmin: {vscan1["scans"]["Jiangmin"]["detected"]}')
                                print(Fore.YELLOW, f'[37] Avira: {vscan1["scans"]["Avira"]["detected"]}                                 [38] Antiy-AVL: {vscan1["scans"]["Antiy-AVL"]["detected"]}')
                                print(Fore.YELLOW, f'[39] Kingsoft: {vscan1["scans"]["Kingsoft"]["detected"]}                           [40] Microsoft: {vscan1["scans"]["Microsoft"]["detected"]}')
                                print(Fore.YELLOW, f'[41] Gridinsoft: {vscan1["scans"]["Gridinsoft"]["detected"]}                       [42] Arcabit: {vscan1["scans"]["Arcabit"]["detected"]}')
                                print(Fore.YELLOW, f'[43] ViRobot: {vscan1["scans"]["ViRobot"]["detected"]}                             [44] ZoneAlarm: {vscan1["scans"]["ZoneAlarm"]["detected"]}')
                                print(Fore.YELLOW, f'[45] GData: {vscan1["scans"]["GData"]["detected"]}                                 [46] Cynet: {vscan1["scans"]["Cynet"]["detected"]}')
                                print(Fore.YELLOW, f'[47] AhnLab-V3: {vscan1["scans"]["AhnLab-V3"]["detected"]}                         [48] BitDefenderTheta: {vscan1["scans"]["BitDefenderTheta"]["detected"]}')
                                print(Fore.YELLOW, f'[49] ALYac: {vscan1["scans"]["ALYac"]["detected"]}                                 [50] MAX: {vscan1["scans"]["MAX"]["detected"]}')
                                print(Fore.YELLOW, f'[51] VBA32: {vscan1["scans"]["VBA32"]["detected"]}                                 [52] Zoner: {vscan1["scans"]["Zoner"]["detected"]}')
                                print(Fore.YELLOW, f'[53] Rising: {vscan1["scans"]["Rising"]["detected"]}                               [54] Yandex: {vscan1["scans"]["Yandex"]["detected"]}')
                                print(Fore.YELLOW, f'[55] Ikarus: {vscan1["scans"]["Ikarus"]["detected"]}                               [56] MaxSecure: {vscan1["scans"]["MaxSecure"]["detected"]}')
                                print(Fore.YELLOW, f'[57] Fortinet: {vscan1["scans"]["Fortinet"]["detected"]}                           [58] Panda: {vscan1["scans"]["Panda"]["detected"]}')
                                print()
                                print(Fore.YELLOW, f'Scan ID: {vscan1["scan_id"]}')
                                print(Fore.YELLOW, f'Total Anti-Viruses Used: {vscan1["total"]}')
                                print(Fore.YELLOW, f'Positives: {vscan1["positives"]}')
                            else:
                                print(Fore.YELLOW, '[SYSTEM] Failed to Get Scan Information from Cloud-Based Anti-Virus.')
                        else:
                            print(Fore.YELLOW, '[SYSTEM] Failed to Get Scan Information from Cloud-Based Anti-Virus.')
                else:
                    print(Fore.YELLOW, '[SYSTEM] Failed to Send File to Cloud-Based Anti-Virus.')
            else:
                   print(Fore.YELLOW, f"[SYSTEM] '{split[0]}' is not recognized as an internal command or an operable program.") 
        else:
            print(Fore.YELLOW, f"[SYSTEM] '{split[0]}' is not recognized as an internal command or an operable program.")
except Exception as e:
    a = type(e).__name__.encode()
    b = hashlib.sha256(a).hexdigest().upper()[:8]

    exception_type, exception_object, exception_traceback = sys.exc_info()
    line_number = exception_traceback.tb_lineno

    print()
    print(colored('[SYSTEM ERROR] An error has occured while using Advanche ZeroOS. Please report this error to the Main Developer.\n', 'yellow'))
    print(colored(f'[SYSTEM ERROR] ERROR CODE: 0x{b}', 'yellow'))
    print(colored(f'[SYSTEM ERROR] ERROR LINE NUMBER: {line_number}', 'yellow'))
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