
# ================================ 1

from datetime import datetime



class SmartphoneMixin:
    def call(self, number):
        return f'Calling to number +{number}'
    def where_to_wear(self):
        return 'You can keep me anywhere'


class WatchMixin:
    def see_time(self):
        time = datetime.now()
        return f'{time.hour}:{time.minute}:{time.second}'
    def where_to_wear(self):
        return 'You should wear me on your hand'



class SmartWatch(WatchMixin, SmartphoneMixin):
    pass


smwatch = SmartWatch()
print(smwatch.call(996_909_898_434))
print(smwatch.see_time())
print(smwatch.where_to_wear())




# =============================== 2

class CreateMixin:
    def post_post(self, post, password, user_name):
        for k,v in self.data_base.items():
            if password == k and user_name == v:
                self.data_base_post[user_name].append(post)
                return 'Successfully created'
        return 'Incorrect password or user_name'
    
    def post_video(self, post, password, user_name):
        for k,v in self.data_base.items():
            if password == k and user_name == v:
                self.data_base_video[user_name].append(post)
                return 'Successfully created'
        return 'Incorrect password or user_name'

class Instagram(CreateMixin):
    data_base = {'Rysa9801': 'RyuDzaky'}
    data_base_post = {'RyuDzaky':[]}
    


class TikTok(CreateMixin):
    data_base = {'Zaky9900': 'Zaky'}
    data_base_video = {}


instagram = Instagram()
tiktok = TikTok()

print(instagram.post_post('I bout New Sock', 'Rysa9801', 'RyuDzaky'))
print(instagram.post_post('lol', 'lol', 'lol'))

print(tiktok.post_video('I bout New Sock', 'Zaky9900', 'Zaky'))   
print(instagram.post_video('lol', 'lol', 'lol'))