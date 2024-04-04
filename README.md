# Mass-Telegram-Scrapper-and-Adder
This Python application allows you to manage Telegram groups by scraping members from one group and adding them to another.
It consists of three main files: `scrapall.py`, `join.py`, and `add.py`.
## Requirements

- Python 3.7.1 or later. You can download Python 3.7.1 from [here](https://www.python.org/downloads/release/python-371/).
- [Telethon](https://github.com/LonamiWebs/Telethon) library. Install it using `pip`:

    ```sh
    # For Linux
    pip install telethon

    # For Windows
    python -m pip install telethon
    ```

## Usage

1. **Scraping Members:**
   - Run `scrapall.py` by typing `python scrapall.py`.
   - Choose the group from which you want to scrape members.
   - Select the users you want to scrape.

2. **Joining Groups/Channels:**
   - Use `join.py` to automatically join a group or channel.
   - Replace `GROUP_ID` with the ID of the group/channel you want to join.

3. **Adding Users:**
   - `add.py` allows you to add users from a CSV file.
   - Ensure the CSV file is properly formatted and contains the required information.

## Note
- **Important:** Be cautious when scraping or adding users to groups. Ensure you have the necessary permissions and follow Telegram's guidelines and terms of service.

---
