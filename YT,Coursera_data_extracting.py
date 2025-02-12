import yt_dlp

def download_video_and_captions(url):
    # Set options to download video and captions with verbose logging
    ydl_opts = {
        'format': 'best',  # Download the best quality video
        'writesubtitles': True,  # Download subtitles if available
        'writeautomaticsub': True,  # Download auto-generated captions
        'subtitleslangs': ['en'],  # Specify the language (English in this case)
        'outtmpl': '%(title)s.%(ext)s',  # Save the file with the video title
        'verbose': True,  # Enable verbose output for debugging
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

video_urls = ["https://youtu.be/2-JV8UxegWE?si=97fGy6BtQagyGmdg",
"https://youtu.be/EUey9L9sgzE?si=Wt2WNbT97YDgwbGt",
"https://youtu.be/HZZVKGPsBfs?si=zu6GFYmlBO_CFYLP",
"https://youtu.be/cDm5vPXVln8?si=HtvVZrDwsTzvxVCe",
"https://youtu.be/L3cFbMK3eRI?si=Pm7DF9vuAck0Dt3h",
"https://youtu.be/ViwX3-ajytA?si=nIflYF6BGtSE3Loz",
"https://youtu.be/VM3I_aq8AMI?si=NatIgwvaKbmAX_Dp",
"https://youtu.be/_e8tDxB4eG4?si=Wv9AjGvimVkWSDCw",
"https://youtu.be/wUc6sVXHtAU?si=izv1x1Z0wHtTARAR",
"https://youtu.be/KVIrAXXR3Xk?si=3cC5MMl1ZdO89tSz",
"https://youtu.be/tlEZGfF9CYc?si=Ivx3yJMYlcktdM60",
"https://youtu.be/Yl3UlGkDaDE?si=0m8qTeYE6dJhGyH9",
"https://youtu.be/gfmxRFywWzQ?si=hP31unCMBqcWut1u",
"https://youtu.be/RIHegYl79cI?si=lYeBFRarwoNAf2KK",
"https://youtu.be/h_j1FIqnHrE?si=EFqC02KRNHVdzoAF",
"https://youtu.be/W_1oY2vkxUU?si=VBKe5ImtRYUKt94B",
"https://youtu.be/YkMdiz8--t8?si=ehX5pEeRzw49sajZ",
"https://youtu.be/TTLZmGzi_R8?si=oWftVAnCvB9xAIx",
"https://youtu.be/vWc9yNSmqqc?si=9a98rmdqMRPC4P3e",
"https://youtu.be/b-EJDC5y20I?si=ceiV7k_c0JFhQviU",
"https://youtu.be/2Xto420YebA?si=j2UIKeZS8R1PiAy8",
"https://youtu.be/VsjP2m3Y_A8?si=KImcgYUOtOr5cLH0",
"https://youtu.be/rCkBQhVIj0g?si=f-FwBpt2O9c3EsD4",
"https://youtu.be/WtWo1iXK8HQ?si=WbSZlGOHCS4uGNUZ",
"https://youtu.be/ONKOXwucLvE?si=_tgS7fGa88qPz0Bk",
"https://youtu.be/kBXYFaZ0EN0?si=luSw1guwIf06fMzd",
"https://www.youtube.com/live/lLCck9FH6z4?si=63M0AM-eICgCZpcL",
"https://youtu.be/sPzc6hMg7So?si=gJXdMeEAG48hArMm",
"https://youtu.be/8PtGcNE01yo?si=dmtFHgU7UwT2u5jn",
]

for url in video_urls:
    download_video_and_captions(url)