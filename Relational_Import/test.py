import sys
import socket
from pathlib import Path
home = str(Path.home())
def rel_import(file=__file__):
    """

    Help with relational imports if doesn't work properly send arg as __file__.
    
    """
    sys.path.insert(0,f'{home}')
    
    name = file.replace('/','.').replace(f'.{home.split("/")[1]}.{home.split("/")[2]}.','')
    
    name = name[:len(name)-3]
    
    return name
