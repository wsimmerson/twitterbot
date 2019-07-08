import env


class TwitterBot():
    def __init__(self, username, password):
        self.username = username
        self.password = password


if __name__ == '__main__':
    bot = new TwitterBot(env.USERNAME, env.PASSWORD)