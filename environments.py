import environ

env = environ.Env(
    SECRET_KEY = (str, 'D7WND473HF7384F38J8943JF'),
    DEBUG = (bool, True),
    ALLOWED_HOSTS = (list, ['valenn2.pythonanywhere.com', '127.0.0.1', 'localhost'])
)