import tweepy as tp
import os
import requests
import base64

class HumanPsychologyAI:
    def __init__(self, phrases_file):
        self.phrases = self.load_phrases(phrases_file)
        self.current_index_file = 'current_index.txt'  # ملف لتخزين الفهرس الحالي
        self.repo = '12345Hosin/pythonx'  # استبدل بـ اسم مستخدم GitHub واسم المستودع
        self.token = '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'  # ضع توكن الوصول الخاص بك هنا

    def load_phrases(self, phrases_file):
        if os.path.exists(phrases_file):
            with open(phrases_file, 'r', encoding='utf-8') as file:
                return [line.strip() for line in file.readlines() if line.strip()]
        else:
            return []

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

    def update_github_file(self, content):
        url = f'https://api.github.com/repos/{self.repo}/contents/{self.current_index_file}'
        response = requests.get(url, headers={'Authorization': f'token {self.token}'})
        
        if response.status_code == 200:
            sha = response.json()['sha']  # احصل على SHA الحالي للملف
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
phrases_file_path = r'jml2.txt'  # مسار ملف الجمل
ai = HumanPsychologyAI(phrases_file_path)

# توليد عبارة جديدة
attracting_phrase = ai.generate_attracting_phrase()

# تحديث الملف في GitHub
ai.update_github_file(str(ai.get_current_index()))
