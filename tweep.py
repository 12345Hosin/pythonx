import tweepy as tp
import requests
import base64

class HumanPsychologyAI:
    def __init__(self):
        # العبارات كقائمة ثابتة داخل الكود
        self.phrases = [
            "عبارة 1: القوة في الصبر.",
            "عبارة 2: الحياة قصيرة، لذا استمتع بكل لحظة.",
            "عبارة 3: كل يوم هو فرصة جديدة.",
            "عبارة 4: التغيير يبدأ من الداخل.",
            "عبارة 5: التفاؤل هو الإيمان الذي يؤدي إلى الإنجاز."
        ]
        self.current_index = 0  # تخزين الفهرس كمتغير داخلي

    def generate_attracting_phrase(self):
        if self.current_index < len(self.phrases):
            phrase = self.phrases[self.current_index]
            self.current_index += 1  # زيادة الفهرس
            return phrase
        else:
            # إعادة تعيين الفهرس إلى 0
            self.current_index = 0
            return "تمت طباعة جميع العبارات!"

# مثال على الاستخدام:
ai = HumanPsychologyAI()

# توليد عبارة جديدة
attracting_phrase = ai.generate_attracting_phrase()

# نشر العبارة على تويتر
if attracting_phrase != "تمت طباعة جميع العبارات!":
    api_key = "wYlnU4Tfh9ovNpbOX4IEcDUZk"
    apy_sec = "AfdYSuaMmCNc1jsEU7fX1Avp5Txc0ikfaNNIKfeG2KEWBQFvZa"
    beare = r"AAAAAAAAAAAAAAAAAAAAAGn1wAEAAAAAaubnNOFva2pC7hLM1OdN7T7Ap4k%3DmRV2HIlEOthLjwFepkhyfwJy8e5XNyKdW7gKpHo5zXTpu4kVYg"
    acc_token = "1842421470208700416-R5xgRjrv7R6yQM4d2Cu00Bo66OuY6R"
    acc_token_sec = "nJKdH6P3Qn3fQThjzsbVdQLHlFcHx0yEDCrY55r9SACu9"

    client = tp.Client(beare, api_key, apy_sec, acc_token, acc_token_sec)
    client.create_tweet(text=attracting_phrase + " : https:/up")
else:
    print(attracting_phrase)
