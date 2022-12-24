# Helen's Helper
Minecraft Mod Manager and Advisor, powered by OpenAI

### MUM: If you are reading this, just complete the four steps under Quickstart. Don't worry about the rest. Just download the .exe file in the folder "dist" and it'll do all the work for you :)

## Setup and Installation

### Quickstart

1. navigate to ./dist
2. download the file helenshelper.exe
3. once download is complete, open helenshelper.exe
4. enjoy!

### Installation and Full Setup (optional: for editing src files)

#### Requirements
* [Python 3.10.6](https://www.python.org/downloads/)
* [PIP Package Manager](https://pypi.org/project/pip/)
* [Git Bash](https://git-scm.com/downloads)

#### Setup
1. Open your desired project location
2. Clone this repo and move into the dev dir
```
git clone https://www.github.com/emmy-bradfield/helens-helper
cd dev
```
3. Install requirements with PIP
```
python -m pip install -r requirements.txt
```
4. From the terminal, you can run the app with
```
python app.py
```
5. To access OpenAI's Davinici you will need a API key. This is included in the .exe dist, but if you're rebuilding you can aquire one from [OpenAI's Website](https://openai.com/api/) for free
6. Once you have the API key, simply create '.env' file in the dev directory, with
```
OPENAI_API_KEY="<your-API-key>"
```
7. Congrats; you're ready to go!


## Testing
don't

## Build as Exe
Following any changes you have made, there are two ways you can package the file into an executable for windows

**Build with PyInstaller**
```
pyinstaller --noconfirm --onefile --console --name "helenshelper" --log-level "WARN" --debug "noarchive"  "path/to/file/app.py"
```

## About

### Built With
* [OpenAi's Davinci](https://www.github.com/openai)
* [SpaCy](https://github.com/explosion/spaCy)

### Contributors
* [DarkbyteAT](https://www.github.com/darkbyteAT)
* [emmy-bradfield](https://www.github.com/emmy-bradfield)

### Licensing
Licenced with MIT. See [Licencing Page](https://github.com/emmy-bradfield/helens-helper/blob/master/LICENSE)
