from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains
import typer


def main(url: str):
    downloader_url = "https://www.soundcloudme.com/"

    browser = webdriver.ChromiumEdge()

    browser.get(url)

    time.sleep(2)

    # Cookie Banner
    browser.find_element("id", "onetrust-accept-btn-handler").click()

    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    tracklist = browser.find_element(By.CLASS_NAME, "trackList__list")

    track_items = tracklist.find_elements(By.CLASS_NAME, "trackItem")

    url_list = []

    # Iterate through all Track Items and gather their button, hover over the track item and then click the button
    # To gather the link that gets appended to the url list
    for track_item in track_items:
        browser.execute_script(f"window.scrollTo({track_item.location['x'] - 30},{track_item.location['y'] - 30});")
        ActionChains(browser).move_to_element(track_item).perform()

        try:
            button = track_item.find_element(By.CLASS_NAME, "sc-button-copylink")
            time.sleep(0.25)
            button.click()
            time.sleep(1)
            url_list.append(pyperclip.paste())
        except Exception:
            next

    # Switch to Downloader
    browser.get(downloader_url)
    time.sleep(1.95)
    # Cookie Banner
    browser.find_element(By.CLASS_NAME, "fc-cta-consent").click()

    # Iterate through all gathered URLs and download the respective songs
    for url in url_list:
        input = browser.find_element(By.CLASS_NAME, "form-control")

        input.send_keys(url)

        button_submit = browser.find_element(By.CLASS_NAME, "btn-secondary")

        button_submit.click()

        time.sleep(5)

        download_buttons = browser.find_elements(By.CLASS_NAME, "custom-download")

        button_download = download_buttons[-1]

        browser.execute_script(
            f"window.scrollTo({button_download.location['x'] - 30},{button_download.location['y'] - 30});")

        button_download.click()

        time.sleep(5)

        browser.get(downloader_url)

    time.sleep(120)

    browser.close()


if __name__ == '__main__':
    typer.run(main)
