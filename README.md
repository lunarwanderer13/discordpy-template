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
$ ./start.sh
```
Note: change the name of `discordpy-template.sh` to the name of your discord bot.  
This will be used to locate and terminate the process when `stop.sh` is ran, so make sure to avoid generic or conflicting names.  
If you have zero ideas for a name the best choice is to smash your head on your keyboard, that way you won't name two files the same name.
