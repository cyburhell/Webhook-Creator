# Discord Webhook Creator

This script allows you to create multiple webhooks for a given Discord channel by providing your Discord token, channel ID, and webhook name. It uses the Discord API to generate webhooks, and it's mainly intended for educational purposes.

**⚠️ Disclaimer:**  
This code is made for educational purposes only. The creator is not responsible for any misuse or violation of Discord's Terms of Service. Use this script at your own risk.

## Features

- Create multiple webhooks for a specific Discord channel.
- Customize webhook names.
- Uses Discord's API to create webhooks via a simple Python script.
- Educational demonstration of working with the Discord API.

## Requirements

Before running the script, make sure you have the following installed:

- Python 3.x
- `requests` library
- `pystyle` library for styling terminal output

You can install the required libraries with the following command:

```bash
pip install requests pystyle
```

## How to Use

1. **Obtain your Discord Token**  
   You need to have a Discord  token for authentication. You can get your token by clicking F12 ( make sure your on discord site ) after that go to application tab and there click Local Storage after that search ```TOKEN``` there you will find your token double click and copy paste it , The token will be mixture of numbers and letters.

2. **Obtain your Channel ID**  
   To get the channel ID, enable "Developer Mode" in your Discord settings and right-click the channel to copy its ID.

3. **Run the Script**  
   Run the script in your terminal/command prompt:

   ```bash
   python main.py
   ```

4. **Input the Required Information**  
   The script will ask for:
   - Your Discord token.
   - The channel ID where the webhooks will be created.
   - The name of the webhooks.
   - The number of webhooks to create.

5. **Webhook Creation**  
   The script will send requests to Discord's API and attempt to create the webhooks. Once the webhooks are created, it will display the success message with the webhook URL.

## Example Output

```
 █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀    ▄████▄   ██▀███  ▓█████ ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒    ▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░    ▒▓█    ▄ ▓██ ░▄█ ▒▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄    ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄   ▒ ▓███▀ ░░██▓ ▒██▒░▒████▒▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒   ░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░     ░  ▒     ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
  ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░    ░          ░░   ░    ░    ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
    ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░      ░ ░         ░        ░  ░     ░  ░            ░ ░     ░     
 
...
Enter your token : <your-token>
Channel ID : 123456789012345678
Enter the webhook name : My Webhook
How many webhooks do you want to create ? : 3
Creating webhook 1...
Creating webhook 2...
Creating webhook 3...
Webhook 3 created successfully.
```

## Notes

- This script does not handle rate-limiting from the Discord API. Be mindful of API restrictions when creating large numbers of webhooks.
- Ensure that you use this script responsibly and within the guidelines of Discord's Terms of Service.

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

- **Discord**: `arandomguyin2024`

---

**Warning:** Always be cautious when using scripts that interact with external services such as Discord, especially for creating and managing resources like webhooks.
