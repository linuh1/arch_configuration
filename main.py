import platform
import constants
import subprocess


def check_system_compatibility():
    print('Checking system compatibility...')
    if not(constants.DISTRO.lower() in platform.release()):
        print('Your system is not suitable')
    else:
        print('Your system is suitable')


check_system_compatibility()


def get_password():
    res = input('Please enter your user password:\n')
    subprocess.run(f'echo {res} | sudo -S ls /', shell=True)
    return res


user_password = get_password()
