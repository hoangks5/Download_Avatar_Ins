import instaloader
import os
import shutil
import threading
import time

while True:
    def download(dp):
        ig = instaloader.Instaloader(dirname_pattern='Image',title_pattern=dp)  
        ig.download_profile(dp ,profile_pic_only=True)
    list_acc = open('username.txt','r',encoding='utf-8').read().splitlines()
    autotool = []
    for dp in list_acc:
        autotool.append(threading.Thread(target=download,args={dp,}))
    for threadd in autotool:
        threadd.start()
    for threadd in autotool:
        threadd.join()


    def dell():
        os.chdir('./Image')
        list = os.listdir()
        for accs in list:
            try:
                if accs.split('.')[-1] == 'jpg':
                    pass
                else:
                    os.remove(accs)
            except:
                try:
                    os.remove(accs)
                except:
                    pass
        os.chdir('..')
    dell()
    time.sleep((10))