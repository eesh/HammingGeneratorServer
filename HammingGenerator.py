from flask import Flask
from flask import render_template
from hampy import HammingMarker
import matplotlib.pyplot as plt
import cv2
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route("/generator")
def hello():
    return render_template("generator.html")

@app.route("/generateCode/<markerID>")
def generateMarker(markerID):
    marker = HammingMarker(id=int(markerID))
    marker = marker.toimage(size=180)
    imshow(marker, cmap='Greys', interpolation='nearest')
    cnt = cv2.imencode('.png',marker)[1]
    b64 = base64.encodestring(cnt)
    data = 'data:image/png;base64,'+b64
    return data

if __name__ == "__main__":
    app.run()

# generateMarker(112259237)
#
# plt.rcParams['backend'] = "Qt4Agg"
# plt.ion()
# marker = HammingMarker.generate()
# # pil_img = Image.fromarray(marker.toimage(size=128))
# # buff = BytesIO()
# # pil_img.save(buff, format="JPEG")
# # new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
# plt.imshow(marker.toimage(size=128), cmap='Greys', interpolation='nearest')
