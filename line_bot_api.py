
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, 
    StickerSendMessage, ImageSendMessage, LocationSendMessage,FlexSendMessage,
    TemplateSendMessage,ImageCarouselTemplate,ImageCarouselColumn,PostbackAction,
    PostbackEvent,QuickReply,QuickReplyButton,ConfirmTemplate,MessageAction,ButtonsTemplate
)

line_bot_api = LineBotApi('N44yZEfmA3bq6c/FGbOu2CfLZ13p0sO9nFcSuymeArXSc7uF8qOIhA6eZaATEu1K9RCVkV+6GmJBJouIH2NotgsPXjCvUwsgAKd5pATaHUtlaR0hg7R8+IzpJ7nsl1gcZW914FKo67sd5246tqrG8gdB04t89/1O/w1cDnyilFU=')
# Channel access token
handler = WebhookHandler('b3b067df5cd7d0d0496b8ed94a1dd873') 
#Channel secret