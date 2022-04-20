from instagrapi import Client
from instagrapi.types import Location
import json, os, time
cl = Client()
auth:list = ["basarn.mss", "#Mb03012005#"];
auth = ["bxbxbx77", "onureda123"]
auth = ["theonemitchl", "onureda123"]
target:str = "bsndjdnnsnsndnsndndnd";

cl.login(auth[0], auth[1])

user_id = cl.user_id_from_username(target)
medias = cl.user_medias(user_id, 90)[55:];
for media,counter in zip(medias, range(len(medias))):
    # media = media.dict();
    # media.location
    # Location()
    os.system("rmdir /Q /S ./media/*" if os.name == "nt" else "rm -r ./media/*");
    # for item in media.dict():
        
    print(f"{len(medias)-counter} gönderi kaldı.")
    print(media.dict(), "\n");
    if (not os.path.exists(f"./media/{counter}")):
        os.mkdir(f"./media/{counter}");
    run = True;
    while run:
        data = {
            "description": "#istanbul #bahcelievler #maslak #kadiköy #Bakırköy #Pendik #kartal #beşiktaş #şişli #mecidiyekoy #florya #bostanci #ataköy #bakirköymarina #kurtköy #ümraniye #nişantaşi #istanbul #facebook #tiktok #twitter #tumblr #İstanbul",
            # "description": media.caption_text,
            "location": media.location,
            "isImage": not media.video_url
        }
        try:
            if (data["isImage"]):
                data["imagePath"] = cl.photo_download(media.pk, f"./media/{counter}").absolute();
                cl.photo_upload(data["imagePath"], caption= data["description"], location=media.location);
            else:
                data["videoPath"] = cl.video_download(media.pk, f"./media/{counter}").absolute();
                cl.video_upload(data["videoPath"], data["description"], location=media.location);
        except Exception as e:
            print(f"Hatalı deneme! {e}")
            time.sleep(3);
            continue;
        run = False;
    # with open(f"./media/{counter}/data.json", "w+", encoding="utf-8") as f:
    #     f.write(json.dumps({
    #         "description": data["caption_text"],
    #         "imagePath": cl.photo_download(data["pk"], f"./media/{counter}").absolute()
    #     }, indent=4))
# cl.download