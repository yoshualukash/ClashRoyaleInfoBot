## Motives and Background

So i've been playing a mobile game called 'Clash Royale' since 2016. Quick explanation, Clash Royale is a freemium real-time strategy video game developed and published by Supercell. The game combines elements from collectible card games, tower defense, and multiplayer online battle arena. This game also is the most popular esport mobile game besides Fortnite(obviously) hence why im still playing this game because of the competitive aspect. I'm also a co-Leader at my clan and basically the ones that monitor the member activities while being in the clan, like the donations/request and war strategies. The leader is so strictly about the clan trophies and clan members qualities. So i had the idea to make a simple clash royale bot that could ease my job as a co-Leader. 

The one job that is hard to track as a co-Leader is the Donations/Request balance per member, because the game only shows the number of donations. While im playing around with the game JSON, i find that the json actually stores the number of 'Request' per member in the clan. So the first thing that i do is to make a table/pandas that stores the clan members statistics like 'name', 'tag', 'trophies', 'donations', 'request'. And because of that i continue to make other function in this bot. 

## Project Duration

I started to playing around with the json at 3 June 2020. The features completed at 10 July 2020. Roughly took me 3 days of coding if i shrink the total time. 

## Structure Code

```
ClashRoyaleInfoBot
┣ Function.py
┃ ┣ check_code
┃ ┣ players_info
┃ ┣ see_players_info
┃ ┣ deck_average_elix
┃ ┣ players_current_deck
┃ ┣ check_chest_image
┃ ┣ see_player_upcoming_chests
┃ ┣ get_members_pb 
┃ ┣ see_clan_members_info
┃ ┣ save_clan_members_info_pdf
┃ ┣ sort_clan_members_byPB
┃ ┣ clan_high_donation
┃ ┣ save_clan_members_high_donation_pdf
┃ ┣ clan_low_donation
┃ ┣ save_clan_members_low_donation_pdf
┃ ┣ see_clan_warlog
┃ ┣ save_clan_warlog_pdf
┣ Command.py
┃ ┣ cmd_player_info
┃ ┣ cmd_clan_info
┃ ┣ cmd_loop
┃ ┣ cmd_loop_clan
┃ ┣ cmd_input
┃ ┣ cmd_exit
┣ default_param.py
┣ test.py
```

## Class and Function
File: Function.py
Function | Access Level | Parameter | Return
-------- | ------------ | --------- | ------
check_code | public | code : str | new code after checked
players_info | public | players code : str | players info and its dataframe
see_players_info | public | players code : str | None
deck_average_elix | public | card list : list | deck average elixir
players_current_deck | public | players code : str | plot the current deck
check_chest_image | public | chest : list | plt.imread version of the image
see_player_upcoming_chests | public | players code : str | plot the upcoming chest
get_members_pb | public | clan code : str | list of members PB trophies
see_clan_members_info | public | clan code : str | data frame of clan members info table
save_clan_members_info_pdf | public | clan code : str | pdf file version of the clan members info table
sort_clan_members_byPB | public | clan code : str | data frame of clan members info table sorted by its PB
clan_high_donation | public | clan code : str | data frame table of Top 10 Donation of the clan
save_clan_members_high_donation_pdf | public | clan code : str | pdf file version of top 10 donation
clan_low_donation | public | clan code : str | data frame table of Top 10 Lowest Donation of the clan
save_clan_members_low_donation_pdf | public | clan code : str | pdf file version of top 10 lowest donation
see_clan_warlog | public | clan code : str | data frame table of latest war log table
save_clan_warlog_pdf | public | clan code : str | pdf file version of latest war log table

File: Command.py
Function | Access Level | Parameter | Return
-------- | ------------ | --------- | ------
cmd_player_info | public | None | run a command that the user pick
cmd_clan_info | public | None | run a command that the user pick
cmd_loop | public | None | None | run a loop command
cmd_loop_clan | public | None | run a loop command
cmd_input | public | None | run welcome command
cmd_exit | public | None | exit the command
## Statistics
The line that i made in all these files are **519** lines
