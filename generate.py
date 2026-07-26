import os

channels = [
    # beIN Sports
    {"name": "beIN Sports News", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917225.ts", "group": "beIN Sports"},
    {"name": "beIN Sports 1", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917215.ts", "group": "beIN Sports"},
    {"name": "beIN Sports 2", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917214.ts", "group": "beIN Sports"},
    {"name": "beIN Sports 3", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917213.ts", "group": "beIN Sports"},
    {"name": "beIN Sports 4", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917212.ts", "group": "beIN Sports"},
    {"name": "beIN Sports 5", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917211.ts", "group": "beIN Sports"},
    {"name": "beIN Sports 6", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917210.ts", "group": "beIN Sports"},
    {"name": "beIN Sports 7", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917209.ts", "group": "beIN Sports"},
    {"name": "beIN Sports 8", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917208.ts", "group": "beIN Sports"},
    
    # الثمانية
    {"name": "الثمانية 1", "url": "http://line.vpntxvpn.ru/live/1508358b7d/7b13892f97dc/1898976.ts", "group": "Thamanya"},
    {"name": "الثمانية 2", "url": "http://line.vpntxvpn.ru/live/1508358b7d/7b13892f97dc/1898975.ts", "group": "Thamanya"},
    {"name": "الثمانية 3", "url": "http://line.vpntxvpn.ru/live/1508358b7d/7b13892f97dc/1899054.ts", "group": "Thamanya"},
    
    # MBC
    {"name": "MBC 2", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/7746.ts", "group": "MBC"},
    {"name": "MBC 3", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/7745.ts", "group": "MBC"},
    {"name": "MBC 4", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/7744.ts", "group": "MBC"},
    {"name": "MBC 5", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/90929.ts", "group": "MBC"},
    
    # القنوات المغربية والوثائقية والإسلامية
    {"name": "Al Aoula HD", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/891367.ts", "group": "Moroccan"},
    {"name": "2M Maroc", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/6736.ts", "group": "Moroccan"},
    {"name": "Arryadia HD", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/969051.ts", "group": "Moroccan"},
    {"name": "National Geographic", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/880186.ts", "group": "Documentary"},
    {"name": "القرآن الكريم", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/2112498.ts", "group": "Islamic"}
]

def build_playlist():
    content = "#EXTM3U\n"
    for ch in channels:
        content += f'#EXTINF:-1 group-title="{ch["group"]}", {ch["name"]}\n{ch["url"]}\n'
    
    # حفظ النسختين .m3u و .m3u8
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(content)
        
    with open("playlist.m3u8", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    build_playlist()
