import requests
from bs4 import BeautifulSoup
import pyautogui
import time
import keyboard

# Function to scrape a webpage
def scrape_webpage(url):
    # Send an HTTP request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all article titles
        articles = soup.find_all('span')
        
        # Extract the text of each article title and store it in a list
        titles = [article.get_text() for article in articles]
        
        return titles
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return []

# Function to simulate typing
def typing_bot(messages, delay):
    time.sleep(delay)  # Delay to give you time to switch to the typing field
    for message in messages:
        pyautogui.typewrite(message + '\n', interval=0.1)  # Type each message with a slight delay between keystrokes

# Function to start the bot on hotkey press
def start_bot_on_hotkey(url, delay, hotkey):
    print(f"Press {hotkey} to start the typing bot.")
    
    def on_hotkey():
        # Scrape the webpage and get the article titles
        titles = scrape_webpage(url)
        
        # Call the typing bot function with the scraped titles
        typing_bot(titles, delay)

    # Register the hotkey
    keyboard.add_hotkey(hotkey, on_hotkey)
    
    # Keep the script running
    keyboard.wait('esc')  # Press 'esc' to exit

# Define the URL to scrape and the delay for typing
url = input("Enter webpage: ")
delay = 5  # 5-second delay
hotkey = 'ctrl+alt+r'  # Hotkey to start the bot

# Start the bot on hotkey press
start_bot_on_hotkey(url, delay, hotkey)