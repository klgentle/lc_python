class Codec:
    def __init__(self):
        self.hashDict = {}
        self.tinyPrefix = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Use hash method to encodes a URL to a shortened URL.
        """
        shortUrl = self.tinyPrefix + str(hash(longUrl))
        self.hashDict[shortUrl] = longUrl
        return shortUrl
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hashDict.get(shortUrl)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
