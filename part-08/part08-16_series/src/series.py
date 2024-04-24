class Series:

    def __init__(self, title:str, seasonsNo:int, genres:list):
        self.title = title
        self.seasonsNo = seasonsNo
        self.genres = genres
        self.ratingSum = 0
        self.numOfRatings = 0
        self.ratingsAvg = 0

    def __str__(self):
        if self.numOfRatings == 0:
            return (f"{self.title} ({self.seasonsNo} seasons)\ngenres: {", ".join(self.genres)}\nno ratings")
        return(f"{self.title} ({self.seasonsNo} seasons)\ngenres: {", ".join(self.genres)}\n{self.numOfRatings} ratings, average {self.ratingsAvg:.1f} points")

    def rate(self, rating:int):
        if(rating >= 0) and (rating <= 5):
            self.ratingSum += rating
            self.numOfRatings += 1
        self.ratingsAvg = self.ratingSum/self.numOfRatings
    
def minimum_grade(rating: float, series_list: list):
    min_grade_list = []
    for s in series_list:
        if s.ratingsAvg >= rating:
            min_grade_list.append(s)
    return(min_grade_list)

def includes_genre(genre: str, series_list: list):
    series_result = []
    for s in series_list:
        if genre in s.genres:
            series_result.append(s)
    return(series_result)


if __name__ == "main":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
