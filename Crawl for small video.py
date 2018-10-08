""" 
爬取小视频
Author          : liuliunx 
Created         : 2018-7-16

"""  

import os
import requests

def do_load_media(url, path):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.3.2.1000 Chrome/30.0.1599.101 Safari/537.36"}
        pre_content_length = 0
        # 循环接收视频数据
        while True:
            # 若文件已经存在，则断点续传，设置接收来需接收数据的位置
            if os.path.exists(path):
                headers['Range'] = 'bytes=%d-' % os.path.getsize(path)
            res = requests.get(url, stream=True, headers=headers)

            content_length = int(res.headers['content-length'])
            # 若当前报文长度小于前次报文长度，或者已接收文件等于当前报文长度，则可以认为视频接收完成
            if content_length < pre_content_length or (
                    os.path.exists(path) and os.path.getsize(path) == content_length):
                break
            pre_content_length = content_length

            # 写入收到的视频数据
            with open(path, 'ab') as file:
                file.write(res.content)
                file.flush()
                print('receive data，file size : %d   total size:%d' % (os.path.getsize(path), content_length))
    except Exception as e:
        print(e)


def load_media():
    url = 'type=feedvideo&objectid=1034:eecb401c04274821ff372bf0962d028b&mid=4253997924048834&fnick=%E4%B8%8A%E6%B5%B7%E8%BF%AA%E5%A3%AB%E5%B0%BC%E5%BA%A6%E5%81%87%E5%8C%BA&uid=5200478600&video_src=%2F%2Ff.us.sinaimg.cn%2F002I2o7Flx07lnDEnjJK010402006K0E0k010.mp4%3Flabel%3Dmp4_hd%26template%3D852x480.28%26Expires%3D1530072460%26ssig%3DSlp14Jy%252FFD%26KID%3Dunistore%2Cvideo&playerType=proto&cover_img=https%3A%2F%2Fwx4.sinaimg.cn%2Flarge%2F005FWG36ly1fsgf90x2jcj30ru0fon07.jpg&card_height=564&card_width=1002&keys=4252614605687746&short_url=http%3A%2F%2Ft.cn%2FRBBJF9j&play_count=4万&duration=15&encode_mode=&bitrate=831'
    #小视频下载地址
	path = r'd:\video\Batorusp.mp4'
	#可修改电脑本地存放路径和文件名
    do_load_media(url, path)
    pass


def main():
    load_media()
    pass


if __name__ == '__main__':
    main()