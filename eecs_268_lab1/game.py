class BoardGame:
    def __init__(self, name, year, gibbons_rating, public_rating, min_players, max_playtime):
        self._name = name
        self._year = year
        self._gibbons_rating = gibbons_rating
        self._public_rating = public_rating
        self._min_players = min_players
        self._max_playtime = max_playtime

    def __str__(self):
        return f'{self._name} ({self._year}) [GR={self._gibbons_rating}, PR={self._public_rating}, MP={self._min_players}, MT={self._max_playtime}]'
        # NAME (YEAR) [GR=Gibbons Rating, PR=Public Rating, MP=Min Players, MT=Max Playtime]

    def __repr__(self):
        return f'Game({self._name}, {self._year}, {self._gibbons_rating}, {self._public_rating}, {self._min_players}, {self._max_playtime})'

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getYear(self):
        return self._year

    def setYear(self, year):
        self._year = year

    def getGibbonsRating(self):
        return self._gibbons_rating

    def setGibbonsRating(self, gibbons_rating):
        self._gibbons_rating = gibbons_rating

    def getPublicRating(self):
        return self._public_rating

    def setPublicRating(self, public_rating):
        self._public_rating = public_rating

    def getMinPlayers(self):
        return self._min_players

    def setMinPlayers(self, min_players):
        self._min_players = min_players

    def getMaxPlaytime(self):
        return self._max_playtime

    def setMaxPlaytime(self, max_playtime):
        self._max_playtime = max_playtime

    def __lt__(self, other):
        return self._gibbons_rating < other.getGibbonsRating()

    def __gt__(self, other):
        return self._gibbons_rating > other.getGibbonsRating()

    def __eq__(self, other):
        return self._gibbons_rating == other.getGibbonsRating()

    def __le__(self, other):
        return self._gibbons_rating <= other.getGibbonsRating()

    def __ge__(self, other):
        return self._gibbons_rating >= other.getGibbonsRating()

    def __ne__(self, other):
        return self._gibbons_rating != other.getGibbonsRating()
