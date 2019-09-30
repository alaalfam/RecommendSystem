class Recommend:
    def manhattan(self, rating1, rating2):
        manhattanDistance = 0
        for key in rating1:
            if key in rating2:
                manhattanDistance += abs(rating1[key] - rating2[key])

        return manhattanDistance

    def findNearest(self, username, users):
        distanceList = []
        for user in users:
            if user != username:
                distance = self.manhattan(users[user], users[username])
                distanceList.append((distance, user))
        distanceList.sort()
        return distanceList

    def recommend(self, username, users):
        nearestKey = self.findNearest(username, users)[0][1]
        recommendation = []
        nearRating = users[nearestKey]
        userRating = users[username]
        for artist in nearRating:
            if not artist in userRating:
                recommendation.append((artist, nearRating[artist]))
        return sorted(recommendation, key=lambda artistTuple :artistTuple[1], reverse=True)
