import tweepy as tp
import requests
import base64
import os

class HumanPsychologyAI:
    def __init__(self, phrases_file):
        self.phrases = self.load_phrases(phrases_file)
        self.current_index_file = 'current_index.txt'  # ملف لتخزين الفهرس الحالي
        self.repo = '12345Hosin/pythonx'  # استبدل بـ اسم مستخدم GitHub واسم المستودع
        self.token = os.getenv('GITHUB_TOKEN')  # احصل على التوكن من متغيرات البيئة في GitHub Actions

    def load_phrases(self, phrases_file):
        if os.path.exists(phrases_file):
            with open(phrases_file, 'r', encoding='utf-8') as file:
                return [line.strip() for line in file.readlines() if line.strip()]
        else:
            return []

    def get_current_index(self):
        url = f'https://api.github.com/repos/{self.repo}/contents/{self.current_index_file}'
        response = requests.get(url, headers={'Authorization': f'token {self.token}'})
        
        if response.status_code == 200:
            content = response.json()['content']
            return int(base64.b64decode(content).decode())
        else:
            return 0  # افتراضي إذا لم يوجد

    def save_current_index(self, index):
        encoded_content = base64.b64encode(str(index).encode()).decode()
        url = f'https://api.github.com/repos/{self.repo}/contents/{self.current_index_file}'
        
        # الحصول على SHA للملف الحالي
        sha = requests.get(url, headers={'Authorization': f'token {self.token}'}).json()['sha']
        
        response = requests.put(url, json={
            'message': 'Update current_index.txt',
            'content': encoded_content,
            'sha': sha
        }, headers={'Authorization': f'token {self.token}'})
        
        return response.status_code == 200

    def generate_attracting_phrase(self):
        index = self.get_current_index()
        if index < len(self.phrases):
            phrase = self.phrases[index]
            self.save_current_index(index + 1)  # زيادة الفهرس
            return phrase
        else:
            self.save_current_index(0)  # إعادة تعيين الفهرس
            return "تمت طباعة جميع العبارات!"

# مثال على الاستخدام:
phrases_file_path = r'jml2.txt'  # مسار ملف الجمل
ai = HumanPsychologyAI(phrases_file_path)

# إعدادات تويتر
api_key = "wYlnU4Tfh9ovNpbOX4IEcDUZk"
api_secret = "AfdYSuaMmCNc1jsEU7fX1Avp5Txc0ikfaNNIKfeG2KEWBQFvZa"
bearer = "AAAAAAAAAAAAAAAAAAAAAGn1wAEAAAAAaubnNOFva2pC7hLM1OdN7T7Ap4k%3DmRV2HIlEOthLjwFepkhyfwJy8e5XNyKdW7gKpHo5zXTpu4kVYg"
access_token = "1842421470208700416-R5xgRjrv7R6yQM4d2Cu00Bo66OuY6R"
access_token_secret = "nJKdH6P3Qn3fQThjzsbVdQLHlFcHx0yEDCrY55r9SACu9"

client = tp.Client(bearer, api_key, api_secret, access_token, access_token_secret)

# توليد عبارة جديدة
attracting_phrase = ai.generate_attracting_phrase()

# نشر العبارة على تويتر
if attracting_phrase != "تمت طباعة جميع العبارات!":
    client.create_tweet(text=attracting_phrase + " : https://up")
    print(attracting_phrase)
else:
    print(attracting_phrase)
