# Pinkham Supercollider!

A spot for Pinkhams to work on Supercollider stuff!

## Windows Setup from 0
- Install supercollider
    - https://supercollider.github.io/
- Download and install [VS Code](https://code.visualstudio.com/)
    - A good and free general purpose IDE
    - Install Extensions (left hand side there is an extension button, or click the links to install from browser):
        - Choose a cool theme (optional): [Catpuccin](https://marketplace.visualstudio.com/items/?itemName=Catppuccin.catppuccin-vsc) and [Catpuccin Icons](https://marketplace.visualstudio.com/items/?itemName=Catppuccin.catppuccin-vsc-icons) is what I'm using right now, but there are loads of cool ones, [Tokyo Midnight](https://marketplace.visualstudio.com/items/?itemName=nacholaciar.tokyo-midnight) is another fav.
        - [Python](https://marketplace.visualstudio.com/items/?itemName=ms-python.python)
        - [Ruff](https://marketplace.visualstudio.com/items/?itemName=charliermarsh.ruff)
            - I guess ***technically*** optional, but I highly recommend. Having these settings enabled makes collaboration much better. Add the following settings, press `ctrl + ,` or click the links (which only work if you are looking at this in vs code)
            - [files.insertFinalNewline](vscode://settings/files.insertFinalNewline)
            - [editor.formatOnSave](vscode://settings/editor.formatOnSave), click it
            - [editor.codeActionsOnSAve](vscode://settings/editor.codeActionsOnSave)
                - Enter this json:
                ```
                "editor.codeActionsOnSave": {
                    "source.organizeImports.ruff": "explicit"
                }
                ```
                your `settings.json` file should look something like this:
                ```
                {
                    "workbench.colorTheme": "Catppuccin Frappé",
                    "workbench.iconTheme": "catppuccin-frappe",
                    "editor.formatOnSave": true,
                    "editor.codeActionsOnSave": {
                        "source.organizeImports.ruff": "explicit"
                    },
                    "files.insertFinalNewline": true
                }
                ```
- Create a directory to store your code
    - Just somewhere to keep your code, I keep all of my coding projects in a `src` directory `C:\Users\erica\src\`
- Install [UV](https://docs.astral.sh/uv/), the latest and greatest python package manager.
    - Press (in vs code) ```ctrl + shift + ` ``` to open a terminal
    - Type: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- Install Git
    - [Create a github account](https://github.com/)
    - Install git for windows, download and run the [file from here](https://git-scm.com/downloads/win).
- Restart your computer
    - UV and GIT added stuff that needs a restart to take effect
- Set global git config settings:
    - in the terminal again run:
        - ```git config --global user.name "Your name!"```
        - ```git config --global user.email "your email"``` (your github account email)
- Clone the github repository (in vs code):
    - On the left hand side there's a source control button, click that, then `clone repository`
    - Enter this `https://github.com/ericapinkham/pinkham-supercollider.git`
    - It should prompt you to open your browser and log in
    - It might also ask you where to clone it to, whatever directory you made above.
- Install Python
    - open the integrated terminal again (```ctrl + shift + ` ```)
    - run `uv sync` to install all the stuff we want, like Python 3.12, [Supriya](https://supriya-project.github.io/supriya/) (the python implementation of supercollider) etc.
- Test it out!
    - Open `src\main.py` in the editor and click `run` at the top middle of your screen.
    - `src\main.py` is a slightly modifed version of what I found here https://supriya-project.github.io/supriya/index.html

## Next Steps
Based on what I've seen so far, we probably want to build "=", like the "play_chord" function I wrote that just get the effects we want and make the whole deal simpler. Or find what other people have done and use that. We'd customize them to meet the needs of whatever you want to do.
