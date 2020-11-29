from flask import Blueprint, render_template, request
import cv2 as cv
from werkzeug.utils import secure_filename
import os
import uuid

from app.home.helpers import resize, image_weight

home = Blueprint('home', __name__,
                template_folder='templates',
                static_folder='static')

@home.route('/', methods=["GET", "POST"])
def index():
    if request.method=="POST":

        files = request.files.getlist('file')

        image_list = []
        for f in files:
            filename = secure_filename(f.filename)
            f.save(os.path.join('./uploads/', filename))
            image_list.append(os.path.join('./uploads/', filename))
            
        dim = (500, 500)

        def transform(image_list):
            for index, image in enumerate(image_list):
                img = cv.imread(image, cv.IMREAD_UNCHANGED)
                img = resize(img, dim)
                img = img * weight
                yield img

        weight = image_weight(image_list)
        image_generator = transform(image_list)
        new_image = 0
        for image in image_generator:
            new_image += image
        combined_image = new_image.astype("uint8")
        filename = str(uuid.uuid4())
        cv.imwrite(f'app/static/{filename}.jpg', combined_image)
        
        return render_template('home/image.html', image=f'{filename}.jpg')

    return render_template('home/index.html')

@home.route('/out', methods=["GET"])
def show():
    return render_template('home/image.html')
        
