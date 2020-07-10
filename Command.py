from Function import *
import inquirer


def cmd_player_info():
    while True:
        try:
            code_player = input("Insert your player ID! : ")
        except ValueError:
            print("Error Input")
            continue
        if(code_player == ''):
            print("There's no input!")
            continue
        else:
            break
    questions_player = [
        inquirer.List('cmd_player',
                      message="Choose your player command: ",
                      choices=['Player Upcoming Chest', 'Player Profile',
                               'Player Current Deck', 'Go Back', 'Exit'],
                      ),
    ]
    ans_player = inquirer.prompt(questions_player)
    if(ans_player["cmd_player"] == 'Player Upcoming Chest'):
        print("Please Wait...")
        see_player_upcoming_chests(code_player)
        return cmd_loop()
    elif(ans_player["cmd_player"] == 'Player Profile'):
        print("Please Wait...")
        see_players_info(code_player)
        return cmd_loop()
    elif(ans_player["cmd_player"] == 'Player Current Deck'):
        print("Please Wait...")
        players_current_deck(code_player)
        return cmd_loop()
    elif(ans_player["cmd_player"] == 'Go Back'):
        return cmd_input()
    elif(ans_player["cmd_player"] == 'Exit'):
        return cmd_exit()


def cmd_clan_info():
    while True:
        try:
            code_clan = input("Insert your clan ID! : ")
        except ValueError:
            print("Error Input")
            continue
        if(code_clan == ''):
            print("There's no input!")
            continue
        else:
            break
    question_clan = [
        inquirer.List('cmd_clan',
                      message="Choose your clan command: ",
                      choices=['Clan Members Info', 'Clan Members Info(Save as PDF)',
                               'Clan Members PB', 'Clan Top 10 Donation', 'Clan Top 10 Donation(Save as PDF)',
                               'Clan Top 10 Lowest Donation', 'Clan Top 10 Lowest(Save as PDF)',
                               'Clan War Log', 'Clan War Log(Save as PDF)', 'Go Back', 'Exit'],
                      ),
    ]
    ans_clan = inquirer.prompt(question_clan)
    if(ans_clan["cmd_clan"] == 'Clan Members Info'):
        print("Please Wait...")
        clan_members = see_clan_members_info(str(code_clan))[0]
        print(clan_members)
        return cmd_loop_clan()
    elif(ans_clan["cmd_clan"] == 'Clan Members Info(Save as PDF)'):
        print("Please Wait...")
        save_clan_members_info_pdf(str(code_clan))
        return cmd_loop_clan()
    elif(ans_clan["cmd_clan"] == 'Clan Members PB'):
        print("Please Wait...")
        clan_members_byPB = sort_clan_members_byPB(str(code_clan))
        print(clan_members_byPB)
        return cmd_loop_clan()
    elif(ans_clan["cmd_clan"] == 'Clan Top 10 Donation'):
        print("Please Wait...")
        high_donation = clan_high_donation(str(code_clan))
        print(high_donation)
        return cmd_loop_clan()
    elif(ans_clan["cmd_clan"] == 'Clan Top 10 Donation(Save as PDF)'):
        print("Please Wait...")
        save_clan_members_high_donation_pdf(str(code_clan))
        return cmd_loop_clan()
    elif(ans_clan["cmd_clan"] == 'Clan Top 10 Lowest Donation'):
        print("Please Wait...")
        lowest_donation = clan_low_donation(str(code_clan))
        print(lowest_donation)
        return cmd_loop_clan()
    elif(ans_clan["cmd_clan"] == 'Clan Top 10 Lowest(Save as PDF)'):
        print("Please Wait...")
        save_clan_members_low_donation_pdf(str(code_clan))
        return cmd_loop_clan()
    elif(ans_clan["cmd_clan"] == 'Clan War Log'):
        print("Please Wait...")
        warlog = see_clan_warlog(str(code_clan))
        print(warlog)
        return cmd_loop_clan()
    elif(ans_clan["cmd_clan"] == 'Clan War Log(Save as PDF)'):
        print("Please Wait...")
        save_clan_warlog_pdf(str(code_clan))
        return cmd_loop_clan()
    elif(ans_clan["cmd_clan"] == 'Go Back'):
        return cmd_input()
    elif(ans_clan["cmd_clan"] == 'Exit'):
        return cmd_exit()


def cmd_loop():
    questions_loop = [
        inquirer.List('cmd_loop',
                      message="Try Different Command?: ",
                      choices=['Yes', 'No/Exit'],
                      ),
    ]
    ans_loop = inquirer.prompt(questions_loop)
    if(ans_loop["cmd_loop"] == 'Yes'):
        return cmd_input()
    elif(ans_loop["cmd_loop"] == 'No/Exit'):
        return cmd_exit()


def cmd_loop_clan():
    questions_loop_clan = [
        inquirer.List('cmd_loop_clan',
                      message="Try Different Clan Command?: ",
                      choices=['Yes', 'No'],
                      ),
    ]
    ans_loop = inquirer.prompt(questions_loop_clan)
    if(ans_loop["cmd_loop_clan"] == 'Yes'):
        return cmd_clan_info()
    elif(ans_loop["cmd_loop_clan"] == 'No'):
        return cmd_loop()


def cmd_input():
    print("Welcome to CR_API Bot!")
    questions1 = [
        inquirer.List('command1',
                      message="Choose your command: ",
                      choices=['Player Info', 'Clan Info', 'Exit'],
                      ),
    ]
    answers1 = inquirer.prompt(questions1)
    if(answers1["command1"] == 'Player Info'):
        return cmd_player_info()
    elif(answers1["command1"] == 'Clan Info'):
        return cmd_clan_info()
    elif(answers1["command1"] == 'Exit'):
        return cmd_exit()


def cmd_exit():
    print("Thanks for using CR_Bot!")
    exit
