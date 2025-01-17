
---

# 🔥 **Discord Webhook Creator** 🔥

✨ This Python script allows you to create **multiple webhooks** for a specific Discord channel by providing your **Discord token**, **channel ID**, and **webhook name**. It uses the **Discord API** to generate webhooks, and it's mainly intended for **educational purposes**. 🚀

⚠️ **Disclaimer**:  
This script is made for **educational purposes only**. The creator is **not responsible** for any misuse or violation of Discord's Terms of Service. **Use this script at your own risk!** 🔥

---

## 🚀 **Features**

- 🌐 **Create multiple webhooks** for a specific Discord channel.
- 🖊️ **Customize webhook names** to fit your needs.
- 🔧 Uses **Discord's API** to create webhooks with just a few lines of Python code.
- 🎓 **Educational tool** for learning how to interact with APIs.
- ✨ **Stylish terminal output** with `pystyle` to make it fun!

---

## 📦 **Requirements**

Before running the script, make sure you have the following installed:

- **Python 3.x** 🐍
- **`requests` library** 📦 (for making HTTP requests)
- **`pystyle` library** ✨ (for styling the terminal output)

You can install the required libraries using this command:

```bash
pip install requests pystyle
```

---

## 💡 **How to Use**

### 1. **Obtain your Discord Token** 🔑  
To authenticate the script with Discord, you’ll need your **Discord token**. Here’s how to get it:

- Open **Discord** in your browser (make sure you’re logged in).
- Press **F12** to open Developer Tools.
- Go to the **Application** tab.
- Under **Local Storage**, search for **TOKEN**.
- Copy the token (a mix of numbers and letters) from there.

### 2. **Get Your Channel ID** 📝  
To get the **Channel ID** where you want the webhooks created:

- Enable **Developer Mode** in your Discord settings.
- Right-click the channel you want and click **Copy ID**.

### 3. **Run the Script** 🎬  
Now, you’re ready to go! Run the script in your terminal/command prompt:

```bash
python main.py
```

### 4. **Input the Required Information**  
The script will ask you to provide:

- 🔑 Your **Discord token**.
- 🏙️ The **Channel ID** where the webhooks will be created.
- ✨ The **Webhook name** you want to use.
- 🔢 The **number of webhooks** you wish to create.

### 5. **Webhook Creation** 🖥️  
The script will then use Discord’s API to create the webhooks. Once the webhooks are successfully created, you’ll see a success message along with the webhook URL. 🥳

---

## 🎬 **Example Output**

```bash
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
Webhook 3 created successfully. 🎉
```

---

## 📝 **Notes**

- 🚨 **Rate Limiting:**  
  This script does **not** handle **rate-limiting** from Discord’s API. Be cautious if you plan to create a large number of webhooks in a short period.
  
- 📜 **Responsible Use:**  
  Always ensure that you use this script responsibly and within the boundaries of [Discord's Terms of Service](https://discord.com/terms).

---

## 📜 **License**

This project is open-source and available under the **MIT License**. 📝  
See the `LICENSE` file for more details.

---

## 🙋‍♂️ **Author**

- **Discord**: [arandomguyin2024](https://discord.com/users/arandomguyin2024)

---

## ⚠️ **Warning**

🔐 Always be cautious when using scripts that interact with external services such as Discord, especially when creating and managing webhooks. **Misuse can lead to account suspension.**

---

