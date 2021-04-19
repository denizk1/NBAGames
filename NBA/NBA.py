from termcolor import colored


class NBA:
    def __init__(self, T, G):
        self.T = T  # list holding the teams' abbreviations and long software ["TOR", "Toronto Raptors"]
        self.G = G  # played matches
        self.NBAdict = dict()  # Dictionary holding team abbreviations {"TOR": "Toronto Raptors"}
        for i in self.T:
            self.NBAdict[i[0]] = i[1]

    def total_game(self):  # For each team find and print total number of games played.
        self.total_game = dict()
        for i in self.NBAdict:
            count = 0  # counter of how many matches a team has played
            for j in self.G:
                if (i == j[0]) or (i == j[1]):  # if the team is on the match list it will increment the counter by 1
                    count += 1
            self.total_game[self.NBAdict[i]] = int(count)
        print(colored("Number of Games:", "green"))
        for key, value in self.total_game.items():
            print(value, '  ', key)

    def home_away(self):  # For each team find and print total number of home games and away games played.
        self.home_away = dict()
        for i in self.NBAdict:
            home = 0
            away = 0
            for j in self.G:
                if (i == j[0]):  # If the team is the first member of the match list, the team hosts the match.
                    home += 1
                elif (i == j[1]):  # if not the first case the team is away
                    away += 1
            self.home_away[self.NBAdict[i]] = [home, away]
        print(colored("Number of Home & Away Games:", "green"))
        for key, value in self.home_away.items():
            print(value[0], ' ', value[1], '    ', key)

    def won_loss(self):  # For each team find and print total number of wins and losses.
        self.won_loss = dict()
        for i in self.NBAdict:
            won = 0
            loss = 0
            for j in G:
                if (i == j[0]):  # If the match is in the team's own court, it is the number of baskets scored in the second index of the match list.
                    if j[2] < j[3]:  # If the 2nd index is small, the team lost the match
                        loss += 1
                    else:
                        won += 1
                if (i == j[
                    1]):  # If the match is away, the 3rd index of the match list is the number of baskets scored.
                    if j[2] > j[3]:  # If the 2nd index is greater, the team lost the match
                        loss += 1
                    else:
                        won += 1
            self.won_loss[self.NBAdict[i]] = [won, loss]
        print(colored("Number of Wins & Losses:", "green"))
        for key, value in self.won_loss.items():
            print(value[0], ' ', value[1], '    ', key)

    def team_game(self):  # For each team list all games (names of teams played against)
        self.team_game = dict()
        for i in self.NBAdict:
            teams = list()
            for j in G:
                if (i == j[0]):  # If the match is in the team's own court, we add the away team to the list.
                    teams.append(self.NBAdict[j[1]])
                elif (i == j[1]):  # If the team is away, the home team is added to the list.
                    teams.append(self.NBAdict[j[0]])
            self.team_game[self.NBAdict[i]] = teams
        print(colored("List of Games:", "green"))
        for key, value in self.team_game.items():
            print(key)
            for item in value:
                print("\t", item)

    def display(self):  # show on screen
        print(colored("\nOptional (H/A) info format (fancy):", "blue"))
        for i in self.NBAdict:
            print("{} ".format(self.NBAdict[i]))
            for k in self.G:
                if (i == k[1]):
                    print("\t(A){}".format(self.NBAdict[k[0]]))
                elif (i == k[0]):
                    print("\t(H){}".format(self.NBAdict[k[1]]))
        print(colored("\nOptional full info format (very very fancy):", "blue"))
        for i in self.NBAdict:
            print("{} ".format(self.NBAdict[i]))
            for k in G:
                if (i == k[1]):
                    if (k[2] < k[3]):
                        print("\taway loss to {}-{} to {}".format(k[2], k[3], self.NBAdict[k[0]]))
                    elif k[3] < k[2]:
                        print("\taway won to {}-{} to {}".format(k[2], k[3], self.NBAdict[k[0]]))
                elif (i == k[0]):
                    if (k[2] < k[3]):
                        print("\thome loss to {}-{} to {}".format(k[2], k[3], self.NBAdict[k[1]]))
                    elif k[3] < k[2]:
                        print("\thome won to {}-{} to {}".format(k[2], k[3], self.NBAdict[k[1]]))
        print(colored("Optional compact format (quite fancy):", "blue"))
        print("\t\t\t\t\t\t{} {} {} {} {}".format("N", "H", "A", "W", "L"))
        for i in self.NBAdict:
            print("{:>22}\t{} {} {} {} {}".format(self.NBAdict[i], self.total_game[self.NBAdict[i]],
                                                  self.home_away[self.NBAdict[i]][0],
                                                  self.home_away[self.NBAdict[i]][1], self.won_loss[self.NBAdict[i]][0],
                                                  self.won_loss[self.NBAdict[i]][1]))


T = [['TOR', 'Toronto Raptors'],
     ['BOS', 'Boston Celtics'],
     ['CHI', 'Chicago Bulls'],
     ['MIL', 'Milwaukee Bucks'],
     ['MIN', 'Minnesota Timberwolves']]
G = [['CHI', 'TOR', 119, 123],
     ['CHI', 'MIN', 122, 123],
     ['MIL', 'TOR', 129, 111],
     ['MIL', 'MIN', 105, 118],
     ['MIL', 'BOS', 101, 105],
     ['MIN', 'CHI', 112, 125],
     ['BOS', 'CHI', 123, 103]]

nba = NBA(T, G)
nba.total_game()
nba.home_away()
nba.won_loss()
nba.team_game()
nba.display()
