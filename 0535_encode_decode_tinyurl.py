# use of hash table memoi, though it might not be realistic
class Codec:
    f = {}
    b = {}
    n = 0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        i = str(Codec.n)
        Codec.f[longUrl] = i
        Codec.b[i] = longUrl
        
        Codec.n += 1
        return i

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return Codec.b[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))