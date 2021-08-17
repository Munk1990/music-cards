import math
import time

from PIL import Image

from imager.cardcreator import generate_card_front, generate_card_back
from metadata.albumdetails import search_songlink_album


#album_list = [698763515,880709749, 1103770960,1569562341, 1557647242, 1545009134, 1340749725, 1127721796 ]
#album_list = [1413202153, 528436018, 269572838, 1566113914, 1537030727, 1529529901, 302390919, 1103770960]
#album_list = [184335550, 283567119, 300388319, 1139142272, 1376027367,1161539183,  269572838, 215738269]
album_list = [155658405,1499378108 , 1440870373, 1557647242, 698763515, 1452141648, 1452571880, 1476076148]
page_dimension = [203, 277]
dpi = 300
mmtoinch = 0.0393700787
print_margin_left = int(1.5 * 300 * mmtoinch)
print_margin_right = 0

widthpixel = int(page_dimension[0] * mmtoinch * dpi)
heightpixel = int(page_dimension[1] * mmtoinch * dpi)
cardwidth = int(heightpixel/4)
cardheight = int((widthpixel - print_margin_left - print_margin_right)/2)

print("card dimensions are Width [%d] Height [%d]" % (int(cardwidth/dpi/mmtoinch), int(cardheight/dpi/mmtoinch)))

front_page = Image.new('RGB', (widthpixel, heightpixel), (255, 255, 255))
back_page = Image.new('RGB', (widthpixel, heightpixel), (255, 255, 255))

for counter in range(len(album_list)):
    album_details = search_songlink_album(album_list[counter])
    album_front_image = generate_card_front(album_details, cardwidth, cardheight)
    album_front_image = album_front_image.rotate(90, expand=True)
    x = (counter % 2) * cardheight
    y = math.floor(counter/2) * cardwidth
    front_page.paste(album_front_image, (x + print_margin_left ,y))

    album_back_image = generate_card_back(album_details, cardwidth, cardheight)
    album_back_image = album_back_image.rotate(270, expand=True)
    x = ((counter + 1) % 2) * cardheight
    y = math.floor(counter/2) * cardwidth
    back_page.paste(album_back_image, (x,y))


curtime = time.strftime("%m%d%H%M")
front_page.save("C:/Users/mayan/Workspace/music-cards/outputs/front_%s.jpg" % curtime)
front_page.show()
back_page.save("C:/Users/mayan/Workspace/music-cards/outputs/back_%s.jpg" % curtime)
back_page.show()
{'entityUniqueId': 'ITUNES_ALBUM::344562307', 'userCountry': 'US', 'pageUrl': 'https://album.link/us/i/344562307', 'entitiesByUniqueId': {'AMAZON_ALBUM::B003BG4KHE': {'id': 'B003BG4KHE', 'type': 'album', 'title': 'Axis: Bold As Love', 'artistName': 'The Jimi Hendrix Experience', 'thumbnailUrl': 'https://m.media-amazon.com/images/I/61YL3ZocTrL._AA500.jpg', 'thumbnailWidth': 500, 'thumbnailHeight': 500, 'apiProvider': 'amazon', 'platforms': ['amazonMusic', 'amazonStore']}, 'ITUNES_ALBUM::357222341': {'id': '357222341', 'type': 'album', 'title': 'Axis: Bold As Love', 'artistName': 'The Jimi Hendrix Experience', 'thumbnailUrl': 'https://is3-ssl.mzstatic.com/image/thumb/Music3/v4/02/8e/b0/028eb02e-58f3-f02c-bbfb-5087b2dc6253/source/512x512bb.jpg', 'thumbnailWidth': 512, 'thumbnailHeight': 512, 'apiProvider': 'itunes', 'platforms': ['appleMusic', 'itunes']}, 'PANDORA_ALBUM::AL:2261': {'id': 'AL:2261', 'type': 'album', 'title': 'Axis: Bold As Love', 'artistName': 'The Jimi Hendrix Experience', 'thumbnailUrl': 'https://content-images.p-cdn.com/images/public/int/8/2/1/0/008811160128_500W_500H.jpg', 'thumbnailWidth': 500, 'thumbnailHeight': 500, 'apiProvider': 'pandora', 'platforms': ['pandora']}, 'SOUNDCLOUD_PLAYLIST::1088254327': {'id': '1088254327', 'type': 'album', 'title': 'The Jimi Hendrix Experience – Axis: Bold As Love', 'artistName': 'djsammie', 'apiProvider': 'soundcloud', 'platforms': ['soundcloud']}, 'YANDEX_ALBUM::80056': {'id': '80056', 'type': 'album', 'title': 'Axis: Bold As Love', 'artistName': 'The Jimi Hendrix Experience', 'thumbnailUrl': 'https://avatars.yandex.net/get-music-content/42108/72477fc1.a.80056-1/600x600', 'thumbnailWidth': 600, 'thumbnailHeight': 600, 'apiProvider': 'yandex', 'platforms': ['yandex']}, 'ITUNES_ALBUM::344562307': {'id': '344562307', 'type': 'album', 'title': 'Axis: Bold As Love', 'artistName': 'The Jimi Hendrix Experience', 'thumbnailUrl': 'https://is2-ssl.mzstatic.com/image/thumb/Music18/v4/23/a8/02/23a80279-2d39-fcd8-ff53-1d62d8a68052/source/512x512bb.jpg', 'thumbnailWidth': 512, 'thumbnailHeight': 512, 'apiProvider': 'itunes', 'platforms': ['appleMusic', 'itunes']}}, 'linksByPlatform': {'amazonMusic': {'country': 'US', 'url': 'https://music.amazon.com/albums/B003BG4KHE?do=play', 'entityUniqueId': 'AMAZON_ALBUM::B003BG4KHE'}, 'amazonStore': {'country': 'US', 'url': 'https://amazon.com/dp/B003BG4KHE', 'entityUniqueId': 'AMAZON_ALBUM::B003BG4KHE'}, 'appleMusic': {'country': 'US', 'url': 'https://geo.music.apple.com/us/album/_/357222341?mt=1&app=music&ls=1&at=1000lHKX', 'nativeAppUriMobile': 'music://itunes.apple.com/us/album/_/357222341?mt=1&app=music&ls=1&at=1000lHKX', 'nativeAppUriDesktop': 'itmss://itunes.apple.com/us/album/_/357222341?mt=1&app=music&ls=1&at=1000lHKX', 'entityUniqueId': 'ITUNES_ALBUM::357222341'}, 'itunes': {'country': 'US', 'url': 'https://geo.music.apple.com/us/album/_/357222341?mt=1&app=itunes&ls=1&at=1000lHKX', 'nativeAppUriMobile': 'itmss://itunes.apple.com/us/album/_/357222341?mt=1&app=itunes&ls=1&at=1000lHKX', 'nativeAppUriDesktop': 'itmss://itunes.apple.com/us/album/_/357222341?mt=1&app=itunes&ls=1&at=1000lHKX', 'entityUniqueId': 'ITUNES_ALBUM::357222341'}, 'pandora': {'country': 'US', 'url': 'https://pandora.app.link/?$desktop_url=https%3A%2F%2Fwww.pandora.com%2FAL%3A2261&$ios_deeplink_path=pandorav4%3A%2F%2Fbackstage%2Falbum%3Ftoken%3DAL%3A2261&$android_deeplink_path=pandorav4%3A%2F%2Fbackstage%2Falbum%3Ftoken%3DAL%3A2261', 'entityUniqueId': 'PANDORA_ALBUM::AL:2261'}, 'soundcloud': {'country': 'US', 'url': 'https://soundcloud.com/user-619405357/sets/the-jimi-hendrix-experience-1', 'entityUniqueId': 'SOUNDCLOUD_PLAYLIST::1088254327'}, 'yandex': {'country': 'RU', 'url': 'https://music.yandex.ru/album/80056', 'entityUniqueId': 'YANDEX_ALBUM::80056'}}}