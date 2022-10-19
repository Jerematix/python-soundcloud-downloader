This Package allows downloading Soundcloud playlists via browser automation.

Selenium requires the respective browser driver to be downloaded and in PATH, in this case it's [msedgedriver.exe](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

# How it works

It first gathers all the links via Soundcloud itself and then pastes them to a Soundcloud downloader and downloads them in your download folder. 

# Setup

    pip install -r requirements.txt

# Usage

    python main.py [playlist_url]