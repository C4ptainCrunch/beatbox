# beatbox

Crossbar and React swag for a useless Beatbox in your kitchen.

# Warning !
At the moment, this app is **VULNERABLE TO SHELL INJECTION**. Do **NOT** run in untrusted environments.

# Install

    virtualenv ve
    source ve/bin/activate
    pip install -r requirements.txt
    crossbar run & python app.py

Fill `samples/` with mp3 files then go to `http://localhost:8080`` and have fun !

# Screenshot

![](https://github.com/C4ptainCrunch/beatbox/raw/master/.screenshot.png)
