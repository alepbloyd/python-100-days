class Article():
    def __init__(self, article_dict):
        self.source = article_dict['source']['name']
        self.author = article_dict['author']
        self.title = article_dict['title']
        self.description = article_dict['description']
        self.url = article_dict['url']
        self.url_to_image = article_dict['urlToImage']
        self.published_at = article_dict['publishedAt']
        self.content = article_dict['content']