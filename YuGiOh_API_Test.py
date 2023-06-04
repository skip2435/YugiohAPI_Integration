import requests
import json

# Get data from the API
response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?cardset=Metal%20Raiders&attribute=Light")
data = response.json()

# Iterate through the cards
for card in data['data']:
    print("ID:", card['id'])
    print("Name:", card['name'])
    print("Type:", card['type'])
    print("Description:", card['desc'])
    if 'atk' in card:
        print("ATK:", card['atk'])
    if 'def' in card:
        print("DEF:", card['def'])
    if 'level' in card:
        print("Level:", card['level'])
    print("Race:", card['race'])
    print("Attribute:", card['attribute'])
    if 'archetype' in card:
        print("Archetype:", card['archetype'])
    if 'card_sets' in card:
        print("Card Sets:")
        for card_set in card['card_sets']:
            print("  Set Name:", card_set['set_name'])
            print("  Set Code:", card_set['set_code'])
            print("  Set Rarity:", card_set['set_rarity'])
            print("  Set Price:", card_set['set_price'])
    if 'card_images' in card:
        print("Card Images:")
        for card_image in card['card_images']:
            print("  Image URL:", card_image['image_url'])
    if 'card_prices' in card:
        print("Card Prices:")
        for card_price in card['card_prices']:
            print("  Card Market Price:", card_price['cardmarket_price'])
            print("  TCG Player Price:", card_price['tcgplayer_price'])
            print("  eBay Price:", card_price['ebay_price'])
            print("  Amazon Price:", card_price['amazon_price'])
    print("\n")
