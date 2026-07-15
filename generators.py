import random

def generate_email():
    return f"bulat_gabaev_46_{random.randint(100, 999)}@ya.ru"


def generate_password():
    return str(random.randint(100000, 999999999))