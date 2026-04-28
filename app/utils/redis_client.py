import redis

#连接本地Redis(默认端口6379）
redis_client = redis.Redis(host='localhost',
                           port=6379,
                           db=0,
                           decode_responses=True
)