class Sources:
    '''
    Class that defines the sources objects
    '''
    def __init__(self, id, name):
        '''
        Function that initiates the source class
        '''
        self.id = id
        self.name = name
        


class Articles:
    '''
    Class that defines the article objects
    '''
    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt