import wikipedia
def wiki(query,lines):
    return wikipedia.summary(query,lines)
if __name__=="__main__":
    print(wikipedia.suggest("leo Messi"))
    print(wikipedia.summary("leo Messi",10))
