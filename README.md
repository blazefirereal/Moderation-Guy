# Discord Bot - Moderation Guy

**Welcome to Moderation Guy!** This bot provides moderation and fun features for your Discord server. Follow these steps to get it up and running.

## Prerequisites

Before you start, make sure you have the following:

- **Python 3.8 or higher**: Needed to run the bot.

## Getting Started

### 1. Download the Repository

1. Click the green "Code" button.
2. Select "Download ZIP" to download the repository to your computer.

### 2. Extract the ZIP File

1. Locate the downloaded ZIP file on your computer.
2. Extract the contents of the ZIP file to a folder.

### 3. Install Python

1. **Download and Install Python**:
   - Go to the [Python Downloads page](https://www.python.org/downloads/).
   - Download and install Python (version 3.8 or higher).
   - During installation, make sure to check the box that says "Add Python to PATH".

### 4. Install Dependencies

1. **Open Command Prompt**:
   - Press `Win + R`, type `cmd`, and press Enter to open Command Prompt.

2. **Navigate to the Folder**:
   - Use the `cd` command to change to the directory where you extracted the ZIP file. For example:

     ```bash
     cd path\to\Moderation-Guy
     ```

   - Replace `path\to\Moderation-Guy` with the actual path to your folder.

3. **Install `discord.py`**:
   - Run the following command to install the necessary Python library:

     ```bash
     pip install discord.py
     ```

### 5. Configure Your Bot

1. **Create a Bot on Discord**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Click "New Application" and give it a name.
   - Go to the "Bot" section on the left sidebar and click "Add Bot".
   - Copy the "Token" from the bot section (you’ll need this for your script).

2. **Edit `bot.py`**:
   - Open the `bot.py` file in your preferred code editor.
   - Find the line with `'YOUR_BOT_TOKEN'` and replace it with the token you copied from the Discord Developer Portal.

### 6. Run the Bot

1. **Run the Bot**:
   - In Command Prompt, make sure you're in the folder where `bot.py` is located.
   - Run the bot with:

     ```bash
     python bot.py
     ```

   - You should see messages indicating that the bot is online.

### Troubleshooting

- **If the bot isn’t running**: Ensure Python and `discord.py` are properly installed. Double-check that your bot token is correctly added to the `bot.py` file.

- **If you see errors**: Look up the error message online or consult the [discord.py documentation](https://discordpy.readthedocs.io/) for help.

For more information, refer to the [discord.py documentation](https://discordpy.readthedocs.io/).
