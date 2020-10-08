#!c:\users\thevenel\documents\project\flask\shipping\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'us==2.0.2','console_scripts','states'
__requires__ = 'us==2.0.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('us==2.0.2', 'console_scripts', 'states')()
    )
