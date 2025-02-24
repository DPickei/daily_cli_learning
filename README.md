## Usage

1. Clone this repo: 
```bash
git clone https://github.com/DPickei/daily_cli_learning.git
```

2. Setup and activate virtual environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies: `pip install -r requirements.txt`
4. Create a `questions.yaml` file and fill it with questions / answers
    * see `example_questions.yaml` for reference
5. Run the quiz: `python main.py`

## Run it daily

I think the best way to use this is as something to do everyday, so I recommend adding it to your daily startup applications. Here's how you do that

### windows
1. hit "win + r"
2. type in "shell:startup" and hit enter
3. Right click anywhere in the folder, click 'new', then 'Shortcut'
4. Enter your repository path (enter 'pwd' into your command line to get the current directory)

### mac
1. Open System Preferences
2. Go to Users & Groups
3. Select your user and click Login Items
4. Click the '+' button to add a new item
5. Navigate to your repository and select the `main.py` file
