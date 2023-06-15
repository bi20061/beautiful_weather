import random

sun = ['晴朗', '好天', '日本晴れ', '澄晴', '蒼穹', '碧空', '青天井', ]

rain = ['片時雨','霧雨','小糠雨','糸雨', '驟雨','滝落とし','村雨','村時雨']

cloud = ['曇天', '雨曇り', '時化空']

snow = ['餅雪', '小米雪']


def generateSun():
    print(sun[random.randint(0, 6)])

def generateRain():
    print(rain[random.randint(0, 7)])

def generateCloud():
    print(cloud[random.randint(0, 2)])

def generateSnow():
    print(snow[random.randint(0, 1)])