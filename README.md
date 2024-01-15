# Installation

### Make sure you have Python 3.11 installed on your system. If `YES` then follow along the instructions given below.

#### • Create a virtual environment using python.
```bash
> python -m venv env
```

#### • Activate the virtual environment based on your terminal. For me it's Git Bash, so search online on how to activate on your terminal.
```bash
> source env/Script/activate
```

#### • Now install all the required libraries using pip.
```bash
> pip install -r requirements.txt
```

#### • Create a `.env` file and copy the code from below.
```http
API_KEY=
DISCORD_API_KEY=
```

#### • Get OCR API key and Discord bot API token from the given link.
Signup and get your free API key from [OCR API](https://ocr.space/ocrapi)

Create a bot and use the token from [Discord Bot API](https://discord.com/developers/applications/)

#### • Now copy both the keys accordingly in the `.env` file. Replace `<ocr_key>` with your key from OCR.Space and replace `<bot_token>` with your bot token from Discord developers portal.
```http
API_KEY=<ocr_key>
DISCORD_API_KEY=<bot_token>
```

#### • Save the `.env` file.

#### • Now create a `qna_kfm.json` file that holds every question(lowercased and no space) and every answer(no changes) as key and value. An example has been given below.
```bash
{
"ahumanfingernailismadeofwhichmaterial?": "Alpha-keratin",
}
```
#### `N.B:` Enter every question and answer with a comma.

#### • Now run the `main.py` file using python.
```bash
> python main.py
```

### Enjoy the bot on your server.
