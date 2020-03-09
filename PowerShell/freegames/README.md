# freegames

This is a free game plugin with the purpose on teaching programming through games. It is a python plugin ran entirely through powershell. It is better to run these commands seperate and not in the single file that is also included.


### Prerequisites
You need to have pip and Python installed to use this plugin.

### Usage
To install, type in PowerShell:
``` powershell
pip install freegames
```

There are many different games available to play. To view to full list tpye in PowerShell:
``` powershell
python -m freegames list
```

To play a game type in PowerShell with [memory] being the game you want to play:
``` powershell
python -m freegames.memory
```

Because this is an educational plugin, you can download the games to make changes.
To download the .py file to the working directory, type in PowerShell:
``` powershell
python -m freegames copy memory
```

You can edit this .py file in PowerShell by using a Python text editor called IDLE.
To do this type in PowerShell with [memory.py] being the file path:

``` powershell
python -m idlelib.idle memory.py
```
