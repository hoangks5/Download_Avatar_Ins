from fastapi import FastAPI
import instaloader
import os
import shutil
import threading
import time



app = FastAPI()

@app.get("/{url}")
async def root(url):
        ig = instaloader.Instaloader(dirname_pattern='Image',title_pattern=url)  
        ig.download_profile(url ,profile_pic_only=True)
        def dell():
            os.chdir('Image')
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
        time.sleep(10)
        dell()
        return {"message": "Hello World"}