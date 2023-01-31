from game import BoardGame

class Executive:
    def __init__(self, filename):
        self._filename = filename  # Stores the name of the file given by the user earlier
        self._games = self.parseData()  # Gets a list of BoardGame objects from file

    def parseData(self):
        inputFile = open(self._filename, 'r') # Opens file of filename
        games = []  # List that will hold BoardGame objects later

        for line in inputFile:  # Goes through each line and converts them into BoardGame objects
            splitLine = line.split()
            games.append(BoardGame(splitLine[0],          # Name
                                   int(splitLine[3]),     # Year
                                   float(splitLine[1]),   # Gibbons Rating
                                   float(splitLine[2]),   # Public Rating
                                   int(splitLine[4]),     # Min Players
                                   int(splitLine[5])))    # Max Playtime

            # BoardGame(Name, Year, gibbons_rating, public_rating, # min_players, max_playtime)

        return games


    def menu(self):
        print('\nChoices:\n1. Print all games highest Gibbons range to lowest\n2. Print all games from a year\n3. Time '
              'for a game?\n4. The People VS Dr. Gibbons\n5. Print based on ranking\n6. Exit the program')
        userChoice = input('\nEnter Choice Number:  ')  # Gets user choice, keeps as string for now
        return userChoice


    def allGamesGibbonRanked(self):
        self._games.sort()  # Sorts list using .sort which looks at Gibbon's Rating
        for game in self._games[::-1]:  # Inverts order of list to make it descend
            print(game)


    def allGamesFromYear(self):
        desiredYear = int(input('Choose a Year: '))  # Gets user input for year, converts to int
        gamesFromYear = []  # Empty list that will store only game objects from the given year
        for game in self._games:  # Goes through each game in the list of all games
            if game.getYear() == desiredYear:
                gamesFromYear.append(game)  # Adds the game to gamesFromYear if it is from the desired year
        if len(gamesFromYear) == 0:  # Checks to makes sure at least one game was found
            print('No games found')
        else:
            for game in gamesFromYear:  # Prints each game on its own line
                print(game)


    def timeForGame(self):
        desiredTime = int(input('How Much Time Do You Have?: '))  # Gets time a person has, and converts to int
        gamesInTime = []  # Empty list that will store only game objects with a max playtime less than the desired time
        for game in self._games: # Goes through each game in the list of all games
            if game.getMaxPlaytime() < desiredTime:  # Checks to see if they have less max playtime than playtime desired
                gamesInTime.append(game)
        if len(gamesInTime) == 0:  # Checks to make sure at least one game was found
            print('No games found')
        else:
            for game in gamesInTime:  # Prints each game on its own line
                print(game)


    def thePeopleVSGibbons(self):
        differenceThreshold = 11.0  # Sets a default score outside of range (0, 10)
        while differenceThreshold > 10 or differenceThreshold < 0: # Keeps asking the user for the difference they want
            # until its within the proper range
            differenceThreshold = float(input('How Much of A Difference Are You Looking For? (between 0 and 10): '))
        gamesWithDifference = []  # An empty list that will contain all game objects that match our search criteria
        for game in self._games:  # Goes through each game in the stored games list
            rating_difference = abs(game.getGibbonsRating() - game.getPublicRating())  # Gets the range between the two
            # values (and absolute values them) to get the difference no matter which dirrection
            if rating_difference >= differenceThreshold:
                gamesWithDifference.append(game)  # Adds items to the list of sucessful hits
        if len(gamesWithDifference) != 0:  # Makes sure at least one result is found
            for game in gamesWithDifference:
                print(game)
        else:
            print('No games found')


    def printBasedOnRanked(self):
        desiredScore = float(input('What Score Are You Looking For?: '))  # Gets desired score from user
        gamesWithScore = []  # Empty list that will eventually contain game objects that match our search
        for game in self._games:
            if game.getGibbonsRating() >= desiredScore:  # Checks if the games Gibbons Score is greater or equal to
                # the wanted score
                gamesWithScore.append(game)
        if len(gamesWithScore) != 0:  # Makes sure at least one result is found
            for game in gamesWithScore:
                print(game)
        else:
            print('No games found')


    def run(self):
        wantExit = False
        while not wantExit:
            userChoice = self.menu()
            if userChoice == '1':  # Prints all games ranked by Gibbon's score
                self.allGamesGibbonRanked()
            if userChoice == '2':  # Asks user for a year, then prints all games from that year
                self.allGamesFromYear()
            if userChoice == '3':  # Asks user for a time, and then prints all games that can be played in that time
                self.timeForGame()
            if userChoice == '4':  # Asks the user for a difference threshold and prints all games where Gibbon's score
                # and the people's core differ by at least that much
                self.thePeopleVSGibbons()
            if userChoice == '5':  # Asks the user for a ranking and shows all games with at least that much of a
                # Gibbon's rating
                self.printBasedOnRanked()
            if userChoice == '6':  # Quits the program
                wantExit = True
