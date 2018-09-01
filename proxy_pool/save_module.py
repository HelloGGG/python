import redis
from random import choice

MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCROE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = 'foobared'
REDIS_KEY = 'proxies'

# 存储模块
class RedisCilent(object):

    def __init__(self):
        self.db = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)
    

    # 添加proxy
    def add(self, proxy, score=INITIAL_SCROE):
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, score, proxy)

    # 获取随机可用代理   
    def random(self):

        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        # 有最高分数，取最高分数中随机代理
        if len(result):
            return choice(result)
        # 没有最高分数，取分数前100个随机选取
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                print('代理池为空')

    # 代理测试不通过不可用减分
    def decrease(self, proxy):

        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理', proxy, '当前分数', score, '减1')
            return self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            print('代理', proxy, '当前分数', '移除')
            return self.db.zrem(REDIS_KEY, proxy)
        

    def exists(self, proxy):
        return not self.db.zscore(REDIS_KEY, proxy) == None
    
    # 将可用代理设为MAX_SCORE
    def max(self, proxy):
        print('代理', proxy, '可用，设置为', MAX_SCORE)
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    # 返回可用代理数量
    def count(self):
        return self.db.zcard(REDIS_KEY)

    # 返回可用代理列表
    def all(self):
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)

