## Usage

0. Clone this repo `git clone https://github.com/<YOURUSERNAME>/daily_cli_learning.git`
1. Setup virtual environment: `python -m venv .venv`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the quiz: `python main.py`

Also: I think the best way to use this is as something to do everyday, so I recommend adding it to your daily startup applications. Here's how you do that

### windows
0. hit "win + r"
1. type in "shell:startup" and hit enter
2. Right click anywhere in the folder, click 'new', then 'Shortcut'
3. Enter your repository path (enter 'pwd' into your command line to get the current directory)

### mac
0. Open System Preferences
1. Go to Users & Groups
2. Select your user and click Login Items
3. Click the '+' button to add a new item
4. Navigate to your repository and select the `main.py` file

### linux
0. Open your terminal
1. Create a desktop entry file: `nano ~/.config/autostart/cli_quiz.desktop`
2. Add the following content:
