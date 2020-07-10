from default_param import *
import urllib.request
import json
import string
import decimal
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table
from matplotlib.backends.backend_pdf import PdfPages
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def check_code(code):
    if code[0:4] == '/%23':
        new_code = code.replace('/%23', '')
        return new_code
    elif code[0] == '#':
        new_code = code.replace('#', '/%23')
        return new_code
    elif code[0] != '#':
        return hashtag + code
    else:
        return('ID is not valid')


def players_info(playerscode):
    code = check_code(playerscode)
    request = urllib.request.Request(
        base_url+players+code, None, headers=headers)
    response = urllib.request.urlopen(request).read().decode("utf-8")
    info_players = json.loads(response)
    ply_nama, ply_tag, ply_level, ply_trophies, ply_PBtrophies, ply_wins, ply_losses, ply_battlecount, ply_totaldonations, ply_wardaywins = [
    ], [], [], [], [], [], [], [], [], []
    ply_nama.append(info_players['name'])
    ply_tag.append(info_players['tag'])
    ply_level.append(info_players['expLevel'])
    ply_trophies.append(info_players['trophies'])
    ply_PBtrophies.append(info_players['bestTrophies'])
    ply_wins.append(info_players['wins'])
    ply_losses.append(info_players['losses'])
    ply_battlecount.append(info_players['battleCount'])
    ply_totaldonations.append(info_players['totalDonations'])
    ply_wardaywins.append(info_players['warDayWins'])
    players_info = {'Nama': ply_nama, 'Tag': ply_tag, 'Level': ply_level, 'Trophies': ply_trophies,
                    'PB Trophies': ply_PBtrophies, 'Total Wins': ply_wins, 'Total Losses': ply_losses,
                    'Total Battle': ply_battlecount, 'Total Donations': ply_totaldonations,
                    'War Day Wins': ply_wardaywins}
    df = pd.DataFrame(players_info)
    return players_info, df


def see_players_info(playerscode):
    code = check_code(playerscode)
    request = urllib.request.Request(
        base_url+players+code, None, headers=headers)
    response = urllib.request.urlopen(request).read().decode("utf-8")
    info_players = json.loads(response)
    print("Nama : " + info_players['name'])
    print("Tag : " + info_players['tag'])
    print("Level : " + str(info_players['expLevel']))
    print("Trophies : " + str(info_players['trophies']))
    print("PB Trophies : " + str(info_players['bestTrophies']))
    print("Wins : " + str(info_players['wins']))
    print("Losses : " + str(info_players['losses']))
    print("Total Battle : " + str(info_players['battleCount']))
    print("Total Donations : " + str(info_players['totalDonations']))
    print("War Day Wins : " + str(info_players['warDayWins']))


def deck_average_elix(cardlist):
    num_elixir = 0
    for id_card in cardlist:
        if(id_card in elixir_1):
            num_elixir += 1
        elif(id_card in elixir_1_5):
            num_elixir += 1.5
        elif(id_card in elixir_2):
            num_elixir += 2
        elif(id_card in elixir_3):
            num_elixir += 3
        elif(id_card in elixir_4):
            num_elixir += 4
        elif(id_card in elixir_5):
            num_elixir += 5
        elif(id_card in elixir_6):
            num_elixir += 6
        elif(id_card in elixir_7):
            num_elixir += 7
        elif(id_card in elixir_8):
            num_elixir += 8
        elif(id_card in elixir_9):
            num_elixir += 9
    return float(round(decimal.Decimal(str(num_elixir/8)), ndigits=1))


def players_current_deck(playerscode):
    code = check_code(playerscode)
    request = urllib.request.Request(
        base_url+players+code, None, headers=headers)
    response = urllib.request.urlopen(request).read().decode("utf-8")
    info_players = json.loads(response)
    card_image = []
    card_id = []
    player_name = info_players['name']
    for card_item in info_players['currentDeck']:
        card_id.append(str(card_item['id']))
        card_image.append(card_item['iconUrls']['medium'])
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # imread declaration
    for iter in range(len(alpha)):
        alpha[iter] = plt.imread(card_image[iter])
    image_1 = [alpha[0], alpha[1], alpha[2], alpha[3]]
    image_2 = [alpha[4], alpha[5], alpha[6], alpha[7]]
    # Deck average elixir
    deck_elixir = deck_average_elix(card_id)
    # Plotting
    fig, ax = plt.subplots(nrows=2, ncols=4, figsize=(6, 4))
    fig.suptitle(player_name + " current Deck (" + str(deck_elixir) +
                 " Average Elixir)", fontsize=10, fontweight='bold', color="purple")
    fig.patch.set_facecolor('xkcd:white')
    for j in range(4):
        ax[0][j].imshow(image_1[j])
        ax[0][j].axis('off')
        ax[1][j].imshow(image_2[j])
        ax[1][j].axis('off')
    fig.tight_layout()
    plt.show()
    return plt.show()


def check_chest_image(chest):
    if(chest == "Silver Chest"):
        return img_silver
    elif(chest == "Golden Chest"):
        return img_gold
    elif(chest == "Magical Chest"):
        return img_magical
    elif(chest == "Giant Chest"):
        return img_giant
    elif(chest == "Mega Lightning Chest"):
        return img_mega
    elif(chest == "Epic Chest"):
        return img_epic
    elif(chest == "Legendary Chest"):
        return img_legendary


def see_player_upcoming_chests(playercode):
    code = check_code(playercode)
    request = urllib.request.Request(
        base_url+players+code+upcomingchest, None, headers=headers)
    response = urllib.request.urlopen(request).read().decode("utf-8")
    player_json = json.loads(response)
    chest_index, chest_name = [], []
    for item in player_json['items']:
        chest_index.append(item['index'])
        chest_name.append(item['name'])
    chest_image = []
    for name_chest in chest_name:
        chest_image.append(check_chest_image(name_chest))
    # Plotting
    fig, ax = plt.subplots(nrows=1, ncols=7, figsize=(10, 5))
    fig.suptitle("Upcoming Chest", fontsize=10,
                 fontweight='bold', color="purple")
    fig.patch.set_facecolor('xkcd:white')
    chest_pick = [0, 1, 9, 10, 11, 12, 13]
    for i in range(7):
        ax[i].imshow(chest_image[chest_pick[i]])
        ax[i].axis('off')
        ax[i].title.set_text(
            '+' + (str(chest_index[chest_pick[i]]+1)) + ' Chest')
    fig.tight_layout()
    return plt.show()


def get_members_pb(clancode):
    code = check_code(clancode)
    request = urllib.request.Request(
        base_url+clans+code, None, headers=headers)
    response = urllib.request.urlopen(request).read().decode("utf-8")
    clan = json.loads(response)
    membersPB, tag = [], []
    for members in clan['memberList']:
        tag.append(members['tag'])
    for tags in tag:
        clan_members = players_info(tags)[0]
        membersPB.append(clan_members['PB Trophies'])
    members_PB = []
    for sublist in membersPB:
        for item in sublist:
            members_PB.append(item)
    return members_PB


def see_clan_members_info(clancode):
    code = check_code(clancode)
    request = urllib.request.Request(
        base_url+clans+code, None, headers=headers)
    response = urllib.request.urlopen(request).read().decode("utf-8")
    clan = json.loads(response)
    clan_name = clan['name']
    nama, tag, trophies, role, donations, received = [], [], [], [], [], []
    personal_best = get_members_pb(clancode)
    for members in clan['memberList']:
        nama.append(members['name'])
        tag.append(members['tag'])
        trophies.append(members['trophies'])
        role.append(members['role'])
        donations.append(members['donations'])
        received.append(members['donationsReceived'])
    members_info = {'Nama': nama, 'Tag': tag, 'Trophies': trophies,
                    'PB Trophies': personal_best, 'Role': role, 'Donations': donations, 'Received': received}
    df = pd.DataFrame(members_info)
    return df, clan_name


def save_clan_members_info_pdf(clancode):
    clan_members, clan_name = see_clan_members_info(clancode)
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=clan_members.values,
                         colLabels=clan_members.columns, loc='center')
    pdfname = clan_name + "_members_list"
    pp = PdfPages(pdfname + ".pdf")
    pp.savefig(fig, bbox_inches='tight')
    print("file saved as " + pdfname + ".pdf")
    return pp.close()


def sort_clan_members_byPB(clancode):
    clan_members_byPB = see_clan_members_info(clancode)[0]
    return clan_members_byPB.sort_values(by='PB Trophies', ascending=False)


def clan_high_donation(clancode):
    members_info = see_clan_members_info(clancode)[0]
    # Highest Donation
    highest_donation_row = members_info['Donations'].argmax()
    nama = members_info.iloc[highest_donation_row, 0]

    # Top 10 Donation
    number_of_people = 10
    top_donation = members_info.nlargest(number_of_people, ['Donations'])

    print('Highest Donation -> "' + nama + '"')
    print('\n')
    print('Top ' + str(number_of_people) + ' Donation in this clan')
    return top_donation


def save_clan_members_high_donation_pdf(clancode):
    clan_name = see_clan_members_info(clancode)[1]
    high_donation = clan_high_donation(clancode)
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=high_donation.values,
                         colLabels=high_donation.columns, loc='center')
    pdfname = clan_name + "_top_donation_list"
    pp = PdfPages(pdfname + ".pdf")
    pp.savefig(fig, bbox_inches='tight')
    print("file saved as " + pdfname + ".pdf")
    return pp.close()


def clan_low_donation(clancode):
    members_info = see_clan_members_info(clancode)[0]
    number_of_people = 10
    lowest_donation = members_info.nsmallest(number_of_people, ['Donations'])
    print('Top 10 Lowest Donation')
    return lowest_donation


def save_clan_members_low_donation_pdf(clancode):
    clan_name = see_clan_members_info(clancode)[1]
    low_donation = clan_low_donation(clancode)
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=low_donation.values,
                         colLabels=low_donation.columns, loc='center')
    pdfname = clan_name + "_lowest_donation_list"
    pp = PdfPages(pdfname + ".pdf")
    pp.savefig(fig, bbox_inches='tight')
    print("file saved as " + pdfname + ".pdf")
    return pp.close()


def see_clan_warlog(clancode):
    code = check_code(clancode)
    request = urllib.request.Request(
        base_url+clans+code+clans_warlog, None, headers=headers)
    response = urllib.request.urlopen(request).read().decode("utf-8")
    warlog = json.loads(response)
    nama, tag, cardsEarned, battlesPlayed, wins, collectionDayBattle, numberOfBattles = [
    ], [], [], [], [], [], []
    for participant in warlog['items'][0]['participants']:
        nama.append(participant['name'])
        tag.append(participant['tag'])
        cardsEarned.append(participant['cardsEarned'])
        battlesPlayed.append(participant['battlesPlayed'])
        wins.append(participant['wins'])
        collectionDayBattle.append(participant['collectionDayBattlesPlayed'])
        numberOfBattles.append(participant['numberOfBattles'])
    participant_info = {'Nama': nama, 'Tag': tag, 'Cards Earned': cardsEarned, 'Col. Day Battle': collectionDayBattle,
                        'War Battles': numberOfBattles, 'Battles Played': battlesPlayed, 'Wins': wins}
    df = pd.DataFrame(participant_info).sort_values(
        by=['Cards Earned', 'Wins'], ascending=False)
    return df


def save_clan_warlog_pdf(clancode):
    clan_name = see_clan_members_info(clancode)[1]
    war_log = see_clan_warlog(clancode)
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=war_log.values,
                         colLabels=war_log.columns, loc='center')
    pdfname = clan_name + "_warlog"
    pp = PdfPages(pdfname + ".pdf")
    pp.savefig(fig, bbox_inches='tight')
    print("file saved as " + pdfname + ".pdf")
    return pp.close()
