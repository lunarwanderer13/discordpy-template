# Discord.py Template
## Prefix Commands Version

### Dependencies
```
Python 3.14.7
pip 26.3
Discord.py 2.7.1
```

### Installation
Create a python virtual environment and activate it (may differ depending on the OS).
```
$ python -m venv .venv
$ source .venv/bin/activate
```

Install all packages listed in `requirements.txt`
```
$ pip install -r requirements.txt
```

### Usage
Rename `.envtemplate` to `.env` and fill it out with bot's variables.
```
$ mv .envtemplate .env
```
```
TOKEN - your discord bot's token, grab it from the discord developers portal and make sure to keep it private
PREFIX - the symbol used to trigger the bot's commands, use the command name after the prefix
```

Run the bot in the activated virtual environment.
```
$ python main.py
```
