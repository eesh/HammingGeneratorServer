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

@app.route("/generateCode/<int:m_id>")
def generateMarker(m_id):
    marker = HammingMarker(id=m_id)
    marker = marker.toimage(size=128)
    for row in range(len(marker)):
        for column in range(len(marker[0])):
            print(marker[row][column])
    # cnt = cv2.imencode('.jpg',marker)[1]
    # b64 = base64.encodestring(cnt)
    print("test 1")
    try:
        pil_img = Image.fromarray(marker, 'RGB')
    except Exception as e:
        print(e)
        print("test 1.5")
    print("test 2")
    buff = BytesIO()
    print("test 3")
    pil_img.save(buff, format="JPEG")
    print("test 4")
    new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
    print("test 5")
    data = 'data:image/jpeg;base64,'+new_image_string
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

# generateMarker(112259237)
#
# plt.rcParams['backend'] = "Qt4Agg"
# plt.ion()
# marker = HammingMarker.generate()
# pil_img = Image.fromarray(marker.toimage(size=128))
# buff = BytesIO()
# pil_img.save(buff, format="JPEG")
# new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
# plt.imshow(marker.toimage(size=128), cmap='Greys', interpolation='nearest')
