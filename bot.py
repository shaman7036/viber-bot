from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
	name='weather data',
	avatar='http://viber.com/avatar.jpg',
	auth_token='46d62887e527d0c3-1bfc4106b385f2a3-4168ccefcfd50c4b'
)
viber = Api(bot_configuration)

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/incoming', methods=['POST'])
def incoming():
	logger.debug("received request. post data: {0}".format(request.get_data()))
	# handle the request here
	return Response(status=200)
#XREIAZETAI DHMIOYRGEIA SSL CERT APO TA APP TOY HEROKU - DHMIOYRGEIA APO TOPIKO openssl KAI APOSTOLH STO APP TOY HEROKU 20USD/MONTH
context = ('server.crt', 'server.key')
app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)

viber.set_webhook('https://viber-bot-meteokav.herokuapp.com:443/')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

from viberbot.api.messages import (
    TextMessage,
    ContactMessage,
    PictureMessage,
    VideoMessage
)
from viberbot.api.messages.data_types.contact import Contact

# creation of text message
text_message = TextMessage(text="sample text message!")

# creation of contact message
contact = Contact(name="Viber user", phone_number="0123456789")
contact_message = ContactMessage(contact=contact)

# creation of picture message
picture_message = PictureMessage(text="Check this", media="http://site.com/img.jpg")

# creation of video message
video_message = VideoMessage(media="http://mediaserver.com/video.mp4", size=4324)

from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages.text_message import TextMessage
import logging

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

app = Flask(__name__)
viber = Api(BotConfiguration(
    name='PythonSampleBot',
    avatar='http://site.com/avatar.jpg',
    auth_token='445da6az1s345z78-dazcczb2542zv51a-e0vc5fva17480im9'
))


@app.route('/', methods=['POST'])
def incoming():
    logger.debug("received request. post data: {0}".format(request.get_data()))
    # every viber message is signed, you can verify the signature using this method
    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)

    # this library supplies a simple way to receive a request object
    viber_request = viber.parse_request(request.get_data())

    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        # lets echo back
        viber.send_messages(viber_request.sender.id, [
            message
        ])
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!")
        ])
    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return Response(status=200)

if __name__ == "__main__":
    context = ('server.crt', 'server.key')
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)
