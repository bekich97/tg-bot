## Telegram bot with selenium

### Prerequisites

* python3.8+
* pyTelegramBotAPI==4.8.0
* python-dotenv==0.21.0
* selenium==4.7.2

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/bekich97/tg-bot.git
   ```
2. Create virtual environment with:
   ```sh
   virtualenv venv
   ```
3. Select virtualenv which you created recently, with (in Ubuntu)
   ```sh
   source venv/bin/activate
   ```
4. Install  packages
   ```sh
   pip install -r requirements.txt
   ```
5. Run main.py file
   ```sh
   python main.py
   ```

### Crontab configuration for checking web form availability
1. install crontab on OS (in my case, OS is Ubuntu):
   ```sh
   sudo apt update
   sudo apt install cron
   sudo systemctl enable cron
   ```
2. Edit your crontab with the following command:
   ```sh
   crontab -e
   ```
3. If this is the first time you’re running the crontab command under this user profile, it will prompt you to select a default text editor to use when editing your crontab:
   ```sh
   Output
    no crontab for username - using an empty one

    Select an editor.  To change later, run 'select-editor'.
    1. /bin/nano        <---- easiest
    2. /usr/bin/vim.basic
    3. /usr/bin/vim.tiny
    4. /bin/ed

    Choose 1-4 [1]: 
   ```
4. After making your selection, you’ll be taken to a new crontab containing some commented-out instructions on how to use it:
   ```sh
    # Edit this file to introduce tasks to be run by cron.
    # 
    # Each task to run has to be defined through a single line
    # indicating with different fields when the task will be run
    # and what command to run for the task
    # 
    # To define the time you can provide concrete values for
    # minute (m), hour (h), day of month (dom), month (mon),
    # and day of week (dow) or use '*' in these fields (for 'any').# 
    # Notice that tasks will be started based on the cron's system
    # daemon's notion of time and timezones.
    # 
    # Output of the crontab jobs (including errors) is sent through
    # email to the user the crontab file belongs to (unless redirected).
    # 
    # For example, you can run a backup of all your user accounts
    # at 5 a.m every week with:
    # 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
    # 
    # For more information see the manual pages of crontab(5) and cron(8)
    # 
    # m h  dom mon dow   command
   ```
3. Then write following command at the end of file
   ```sh
   */10 * * * * /home/<your_username>/Desktop/projects/python/tg-bot/venv/bin/python /home/<your_username>/Desktop/projects/python/tg-bot/cronjob.py >/tmp/cronlog.txt 2>&1
   ```
   if your crontab config fails, it saves them to ```/tmp/cronlog.txt```.

I think, that's all.