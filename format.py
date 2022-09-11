import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

TMC_FOLDER = os.getenv('TMC_FOLDER')

def clang_format(input: str) -> None:
    '''
    Write the code into a temporary file, run clang-format on it and then read the code back.
    '''

    # Format input
    TMP_FILE ='/tmp/ghidra_code.c'
    FORMAT_FILE = '/tmp/.clang-format'

    with open(TMP_FILE, 'w') as f:
        f.write(input)

    if not os.path.isfile(FORMAT_FILE):
        # Need to copy the .clang-format file due to https://stackoverflow.com/a/46374122
        subprocess.call(['cp', os.path.join(TMC_FOLDER, '.clang-format'), FORMAT_FILE])

    subprocess.call(['clang-format', '--style=file', '-i', TMP_FILE])

    with open(TMP_FILE, 'r') as f:
        input = f.read()
    return input