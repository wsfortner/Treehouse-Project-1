import csv

# program must be within if __name__ == '__main__':
if __name__ == '__main__':

    # teams counts the number of experienced and
    # inexprienced players for each team
    teams = [
            'sharks', [0, 0],
            'dragons', [0, 0],
            'raptors', [0, 0],
            ]

    # list of dictionaries that hold the team names and roster for each team
    league = [
              {"Team": "Sharks", "Roster": []},
              {"Team": "Dragons", "Roster": []},
              {"Team": "Raptors", "Roster": []}
             ]

    # import soccer_players.csv file
    with open('soccer_players.csv') as file:
        reader = csv.DictReader(file, delimiter=',')
        players = list(reader)

        # sort players evenly into 3 different teams based on experience
        for player in players:
            if player["Soccer Experience"] == 'YES':
                if teams[1][0] < 3:
                    teams[1][0] += 1
                    league[0]['Roster'].append(player)
                elif teams[3][0] < 3:
                    teams[3][0] += 1
                    league[1]['Roster'].append(player)
                elif teams[5][0] < 3:
                    teams[5][0] += 1
                    league[2]['Roster'].append(player)
            else:
                if teams[1][1] < 3:
                    teams[1][1] += 1
                    league[0]['Roster'].append(player)
                elif teams[3][1] < 3:
                    teams[3][1] += 1
                    league[1]['Roster'].append(player)
                elif teams[5][1] < 3:
                    teams[5][1] += 1
                    league[2]['Roster'].append(player)

    # function for printing league at the specified index
    def print_league_info(league, index, pointer):
        pointer.write(league[index]["Team"] + '\n')
        pointer.write("\n".join([", ".join(player.values()) for player in league[index]["Roster"]]) + "\n""\n")

    # write teams to a csv file
    with open('teams.txt', 'w') as csvfile:
        for index in range(len(league)):
            print_league_info(league, index, csvfile)
