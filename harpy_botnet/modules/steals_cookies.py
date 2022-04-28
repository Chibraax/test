from os import path
import tempfile

def steal_firefox_cookies() : 

    user_path = path.expanduser('~')
    print(tempfile.gettempdir())


steal_firefox_cookies()