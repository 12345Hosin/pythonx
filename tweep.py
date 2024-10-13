import tweepy as tp
import os
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
        self.current_index_file = 'current_index.txt'
        self.repo = '12345Hosin/pythonx'
        self.token = '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'

    def get_current_index(self):
        if os.path.exists(self.current_index_file):
            with open(self.current_index_file, 'r') as file:
                index = int(file.read().strip())
        else:
            index = 0
        return index

    def save_current_index(self, index):
        with open(self.current_index_file, 'w') as file:
            file.write(str(index))
        self.update_github_file(str(index))

    def update_github_file(self, content):
        url = f'https://api.github.com/repos/{self.repo}/contents/{self.current_index_file}'
        response = requests.get(url, headers={'Authorization': f'token {self.token}'})
        
        if response.status_code == 200:
            sha = response.json()['sha']
            encoded_content = base64.b64encode(content.encode()).decode()
            data = {
                'message': 'Update current_index.txt',
                'content': encoded_content,
                'sha': sha
            }
            requests.put(url, json=data, headers={'Authorization': f'token {self.token}'})
        else:
            print("Error retrieving the file:", response.json())

    def generate_attracting_phrase(self):
        index = self.get_current_index()
        if index < len(self.phrases):
            phrase = self.phrases[index]
            self.save_current_index(index + 1)
            return phrase
        else:
            self.save_current_index(0)
            return "تمت طباعة جميع العبارات!"

# مثال على الاستخدام:
ai = HumanPsychologyAI()

# توليد عبارة جديدة
attracting_phrase = ai.generate_attracting_phrase()

api_key = "wYlnU4Tfh9ovNpbOX4IEcDUZk"
apy_sec = "AfdYSuaMmCNc1jsEU7fX1Avp5Txc0ikfaNNIKfeG2KEWBQFvZa"
beare = r"AAAAAAAAAAAAAAAAAAAAAGn1wAEAAAAAaubnNOFva2pC7hLM1OdN7T7Ap4k%3DmRV2HIlEOthLjwFepkhyfwJy8e5XNyKdW7gKpHo5zXTpu4kVYg"
acc_token = "1842421470208700416-R5xgRjrv7R6yQM4d2Cu00Bo66OuY6R"
acc_token_sec = "nJKdH6P3Qn3fQThjzsbVdQLHlFcHx0yEDCrY55r9SACu9"

client = tp.Client(beare, api_key, apy_sec, acc_token, acc_token_sec)
client.create_tweet(text=attracting_phrase + " : https:/up")
