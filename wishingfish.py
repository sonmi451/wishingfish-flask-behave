from flask import Flask, render_template
import random

################################################################################
# CONSTANTS

WISHINGFISH = Flask(__name__)

IMAGES = {
        "Hello": "/static/Hello.jpg",
        "Thankyou": "/static/Thankyou.jpg",
        "Gday": "/static/Gday.jpg"
        }

################################################################################
# FUNCTIONS

def random_image(d):
    choice = random.choice(list(d))
    image_path = d[choice]
    return image_path

################################################################################
# FLASK APP

@WISHINGFISH.route('/')
def hello_world():
    return render_template('index.html', picture=random_image(IMAGES))
