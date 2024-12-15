class obj:

    def __init__(self, elo, name, imgDataType):
        self.elo = int(elo)
        self.name = name
        self.imgDataType = imgDataType

brawl = obj(1000,"brawlhalla",".gif")
smash = obj(1000,"smash bros",".gif")

def eloCompare(obj1,obj2,obj1Wins,K = 32):
    ExpectedRatingObj1 = 1 / (1 + 10 ** ((obj2.elo - obj1.elo) / 400))
    ExpectedRatingObj2 = 1 / (1 + 10 ** ((obj1.elo - obj2.elo) / 400))
    if obj1Wins:
        obj1.elo = obj1.elo + K * (1 - ExpectedRatingObj1)
        obj2.elo = obj2.elo + K * (0 - ExpectedRatingObj2)
    else:
        obj1.elo = obj1.elo + K * (0 - ExpectedRatingObj1)
        obj2.elo = obj2.elo + K * (1 - ExpectedRatingObj2)
    print(obj1.elo, obj2.elo)