# lee
import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get('YOUR_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.environ.get('YOUR_CHANNEL_SECRET'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    foo == event.message.text
        if foo[0] == '?':
            pass
            print('WTF')
            
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

    message = TextSendMessage(text='Hello, world')
    line_bot_api.reply_message(event.reply_token, message)

    message = ImageSendMessage(
    original_content_url='https://example.com/original.jpg',
    preview_image_url='https://example.com/preview.jpg'
    )
    line_bot_api.reply_message(event.reply_token, message)

    message = StickerSendMessage(
    package_id='1',
    sticker_id='1'
    )
    line_bot_api.reply_message(event.reply_token, message)