import requests
import shutil


def download(url):
    filename = url.split("/")[-1]
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print("image successfully downloaded: ", filename)
    else:
        print("image can not be retrieved")


if __name__ == '__main__':
    download('https://utqyvml.hkilfcvzghgc.hath.network:32715/h/ee8073c94616796dd106fb7190360330eced172a-474124-1280-1807-jpg/keystamp=1609689600-6622358ff5;fileindex=88065694;xres=1280/001.jpg')