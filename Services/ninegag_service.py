import json
import html
import random
from urllib.request import Request, urlopen
from datetime import datetime

class ninegag_service():
    def __init__(self):
        pass
    
    async def obter_posts(self):
        
        agora = datetime.now()
        req = Request('https://9gag.com/v1/group-posts/group/funny/type/hot?q=' + agora.strftime("%H-%M-%S"), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        model = json.loads(webpage.decode("utf-8"))

        posts = []

        for post in model["data"]["posts"]:
            if post['type'] == 'Photo':
                posts.append(post)

        numero_aleatorio = random.randint(0,len(posts)-1)
        post = posts[numero_aleatorio]

        return {
            'tipo': post['type'],
            'titulo': html.unescape(post["title"]),
            'url': post["images"]["image700"]["url"],
        }

        