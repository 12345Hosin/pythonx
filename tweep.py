import tweepy as tp
import random
import os


class HumanPsychologyAI:
    def __init__(self, phrases_file):
        self.phrases = self.load_phrases(phrases_file)
        self.current_index_file = 'current_index.txt'  # ملف لتخزين الفهرس الحالي

    def load_phrases(self, phrases_file):
        # قراءة الجمل من الملف
        if os.path.exists(phrases_file):
            with open(phrases_file, 'r', encoding='utf-8') as file:
                return [line.strip() for line in file.readlines() if line.strip()]
        else:
            return []  # إرجاع قائمة فارغة إذا لم يكن الملف موجودًا

    def get_current_index(self):
        # قراءة الفهرس الحالي من الملف
        if os.path.exists(self.current_index_file):
            with open(self.current_index_file, 'r') as file:
                index = int(file.read().strip())
        else:
            index = 0
        return index

    def save_current_index(self, index):
        # حفظ الفهرس الحالي في الملف
        with open(self.current_index_file, 'w') as file:
            file.write(str(index))

    def generate_attracting_phrase(self):
        index = self.get_current_index()
        if index < len(self.phrases):
            phrase = self.phrases[index]
            self.save_current_index(index + 1)  # زيادة الفهرس ليتجه للجملة التالية
            return phrase
        else:
            self.save_current_index(0)  # إعادة الفهرس إلى الصفر
            return "تمت طباعة جميع العبارات!"

# مثال على الاستخدام:
phrases_file_path = r'jml2.txt'  # مسار ملف الجمل
ai = HumanPsychologyAI(phrases_file_path)

# توليد عبارة جديدة
attracting_phrase = ai.generate_attracting_phrase()







api_key = "wYlnU4Tfh9ovNpbOX4IEcDUZk"
apy_sec = "AfdYSuaMmCNc1jsEU7fX1Avp5Txc0ikfaNNIKfeG2KEWBQFvZa"
beare = r"AAAAAAAAAAAAAAAAAAAAAGn1wAEAAAAAaubnNOFva2pC7hLM1OdN7T7Ap4k%3DmRV2HIlEOthLjwFepkhyfwJy8e5XNyKdW7gKpHo5zXTpu4kVYg"
acc_token = "1842421470208700416-R5xgRjrv7R6yQM4d2Cu00Bo66OuY6R"
acc_token_sec = "nJKdH6P3Qn3fQThjzsbVdQLHlFcHx0yEDCrY55r9SACu9"


client = tp.Client(beare,api_key,apy_sec,acc_token,acc_token_sec)
auth = tp.OAuthHandler(api_key,apy_sec,acc_token,acc_token_sec)
api = tp.API(auth)


client.create_tweet(text=attracting_phrase+" : https://t.me/TAE_group")


