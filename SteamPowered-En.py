import requests
from bs4 import BeautifulSoup
import os
from pystyle import Write, Colors, Colorate

#┌──────────────────────────COPYRIGHT──────────────────────────────────┐
#│ ┌────────────────────┐                                              │                                   
#│ │     _   _ ____     │                                              │
#│ │    | | | / ___|    │                                              │
#│ │    | |_| \___ \    │                                              │
#│ │    |  _  |___) |   │                                              │
#│ │    |_| |_|____/    │                                              │
#│ │                    │                                              │  
#│ └────────────────────┘                                              │
#│ ┌────────────────────────────────────────────────┐                  │
#│ │Copyright © BY Hexa - Educetional Purposes Only!|                  │
#│ └────────────────────────────────────────────────┘                  │
#└──────────────────────────COPYRIGHT──────────────────────────────────┘


#─────────────────────────────CODE──────────────────────────────────────

# Steam oyunlar sayfasının urlsi
url = 'https://store.steampowered.com/search/?filter=topsellers&os=win'


#KATEGORİ EKLENECEK STEAMS.DB GAME TAGS


banner = r"""
 ____  _                       ____                                _ 
/ ___|| |_ ___  __ _ _ __ ___ |  _ \ _____      _____ _ __ ___  __| |
\___ \| __/ _ \/ _` | '_ ` _ \| |_) / _ \ \ /\ / / _ \ '__/ _ \/ _` |
 ___) | ||  __/ (_| | | | | | |  __/ (_) \ V  V /  __/ | |  __/ (_| |
|____/ \__\___|\__,_|_| |_| |_|_|   \___/ \_/\_/ \___|_|  \___|\__,_|

                                        Discord - [Hexadzn#hexa]

    [0] - Quit
    [1] - Discounted Games
    [2] - Search Game
    [3] - TopSellers
    [4] - Free Games
                                                                            
"""

def showbanner():
    print("")
    Write.Print(banner, Colors.blue_to_cyan, interval=0.0005)

def discountPrices():
    os.system("cls")
    showbanner()

    #───────STEAM URL────────
    url = "https://store.steampowered.com/search/?specials=1"
    response = requests.get(url)
    #──────STEAM URL────────

    soup = BeautifulSoup(response.text, 'html.parser')

    #───────────────────OYUN İSİMLERİ────────────────────────────
    game_titles = soup.find_all('span', class_='title')
    #───────────────────OYUN İSİMLERİ────────────────────────────

    #─────────────────İNDİRİMLİ FİYATLARI────────────────────────────
    discount_prices = soup.find_all('div', class_='discount_final_price')
    #─────────────────İNDİRİMLİ FİYATLARI────────────────────────────


    #─────────────────OYUN - FİYAT LİSTESİ────────────────────────────
    count = 0
    for title, price in zip(game_titles, discount_prices):
        count += 1
        #OYUN ISMI
        Write.Print(f'Game: ', Colors.blue_to_cyan,0.0001)
        Write.Print(f'{title.text} ', Colors.purple_to_blue,0.0001)
        #İNDİRİMLİ FİYAT
        Write.Print(f'- Discounted Price: ', Colors.blue_to_green,0.0001)
        Write.Print(f'{price.text}\n', Colors.green_to_blue,0.0001)

    print("")
    Write.Print(f"{count} Game are on discounted price",Colors.green_to_red,0.001)

    #─────────────────OYUN - FİYAT LİSTESİ────────────────────────────

    input("\nPress Enter For Continue...")


def searchGame():
    os.system("cls")
    showbanner()

    Write.Print("🔍 Which Game are you looking?: ",Colors.green_to_blue)
    search = input()

    #----------------GİRİLEN İNPUT SİTEDE SEARCH EDİLİYOR---------------
    search = search.replace(" ", "+")
    search_url = f"https://store.steampowered.com/search/?term={search}"
    #----------------GİRİLEN İNPUT SİTEDE SEARCH EDİLİYOR---------------

    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    game_titles = soup.find_all('span', class_='title')
    discount_prices = soup.find_all('div', class_='discount_final_price')
    original_prices = soup.find_all('div', class_='discount_original_price')

    if not game_titles:
        Write.Print("😔 Cannot found any game.\n", Colors.red_to_blue)
        return

    count = 0
    for title, orig, discount in zip(game_titles, original_prices, discount_prices):
        count += 1
        #Oyun ismi
        Write.Print(f'Game: ', Colors.blue_to_cyan, 0.001)
        Write.Print(f'{title.text}\n', Colors.purple_to_blue, 0.001)
        #Orj Fiyat
        Write.Print(f'Original Price: ', Colors.red_to_blue, 0.001)
        Write.Print(f'{orig.text}\n', Colors.blue_to_red, 0.001)
        #İndirimli Fiyat
        Write.Print(f'Discounted Price: ', Colors.yellow_to_green, 0.001)
        Write.Print(f'{discount.text}\n\n', Colors.green_to_blue, 0.001)

    print("")
    Write.Print(f"Founded Games {count}",Colors.green_to_red,0.001)

    input("\nPress Enter For Continue...")


def topSellers():
    os.system("cls")
    showbanner()

    #--------STEAM URL----------
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    #-----------------OYUN İSİMLERİ--------------------
    game_titles = soup.find_all('span', class_='title')

    #------------------İNDİRİMLİ FİYATLARI-------------------------------
    original_prices = soup.find_all('div', class_='discount_final_price')

    count = 0
    for title, orig in zip(game_titles, original_prices):
        count += 1
        #OYUN ISMI
        Write.Print(f'Game: ', Colors.blue_to_cyan,0.0001)
        Write.Print(f'{title.text} ', Colors.purple_to_blue,0.0001)

        Write.Print(f'- Original Price: ', Colors.green_to_cyan, 0.001)
        Write.Print(f'{orig.text}\n', Colors.cyan_to_green, 0.001)
    
    print("")
    Write.Print(f"{count} Game are TopSeller",Colors.green_to_red,0.001)

    input("\nPress Enter For Continue...")

def freeGames():
    os.system("cls")
    showbanner()
    url = "https://store.steampowered.com/search/?filter=free"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    game_titles = soup.find_all('span', class_='title')
    discount_prices = soup.find_all('div', class_='discount_final_price')

    print("")
    count = 0
    for title, price in zip(game_titles, discount_prices):
        if "Free" in price.text or "Ücretsiz" in price.text:
            count += 1
            Write.Print(f'Game: ', Colors.blue_to_cyan, 0.001)
            Write.Print(f'{title.text} ', Colors.purple_to_blue, 0.001)
            Write.Print(f'- Price: ', Colors.blue_to_green, 0.001)
            Write.Print(f'{price.text}\n', Colors.green_to_blue, 0.001)
    
    print("")
    Write.Print(f"{count} Game are free",Colors.green_to_red,0.001)

    if count == 0:
        Write.Print("\ncannot find any free games.", Colors.red_to_blue)

    input("\nPress Enter For Continue...")

def Menu():
    os.system("cls")
    showbanner()

while True:
    Menu()
    Write.Print("   Enter Choice: ", Colors.green_to_blue,0.001 )
    choice = input()
    
    #quit
    if choice == "0":
        Write.Print("   Quitting...",Colors.red_to_blue,0.001)
        os._exit(0)

    #indirimdekiler - discount prices
    elif choice == '1':
        discountPrices()

    #search game
    elif choice == "2":
        searchGame()  

    #topsellers
    elif choice == '3':
        topSellers()
        
    #free games
    elif choice == "4":
        freeGames()

    #else
    else:
        Write.Print("   Invalid Option.",Colors.red_to_blue)
        continue  # Geçerli bir seçenek girene kadar menü devam eder
