# ClashRoyaleInfoBot
A simple Clash Royale bot to gather players/clans information and statistics that are not visible in the game.

## Prerequisites
Multiple library are needed to be installed in order for this program to run:
* Matplotlib
* Urllib
* Json
* Pandas
* Decimal
* PdfPages from matplotlib
* Table from pandas
* Inquirer

An API token to access the game json data:
* [Clash Royale Developer](https://developer.clashroyale.com/#/)

## Run
* Run test.py using a code editor or command prompt
* Input Clash Royale Player Code or Clash Royale Clan Code 
* Pick the command that you want to run

## Note
* Public IP address are required to get the game API token, so you need to register with your own computer public ip address and change manually the API token or else it isnt going to run. 
* Public IP address keep changing because of expired ISP, etc. So we need to keep updating the registered public ip address at the game developer website for the game token to work.

## Example
* **Player Current Deck** in the command choice, the output will be :
![Current_Deck_Example](https://github.com/yoshualukash/ClashRoyaleInfoBot/blob/master/output_example/current_deck_example.jpg)
* **Player Upcoming Chest** in the command choice, the output will be :
![Upcoming_Chest_Example](https://github.com/yoshualukash/ClashRoyaleInfoBot/blob/master/output_example/upcoming_chest_example.jpg)
* **Clan Members Info(Save as PDF)** in the command choice, the output will be :

https://github.com/yoshualukash/ClashRoyaleInfoBot/blob/master/output_example/Champion_members_list.pdf

* **Clan Top 10 Donation(Save as PDF)** in the command choice, the output will be :

https://github.com/yoshualukash/ClashRoyaleInfoBot/blob/master/output_example/Champion_top_donation_list.pdf

* **Clan Top 10 Lowest(Save as PDF)** in the command choice, the output will be :

https://github.com/yoshualukash/ClashRoyaleInfoBot/blob/master/output_example/Champion_lowest_donation_list.pdf

* **Clan War Log(Save as PDF)** in the command choice, the output will be :

https://github.com/yoshualukash/ClashRoyaleInfoBot/blob/master/output_example/Champion_warlog.pdf

## Author

[Yoshua Lukas](https://github.com/yoshualukash)

These code are made by myself by looking at the game API's documentation

Contact me: yoshua.hutabarat@gmail.com

## Source
* [Clash Royale Developer](https://developer.clashroyale.com/#/) for the API token
* [Clash Royale Documentation](https://developer.clashroyale.com/#/documentation) for the game json documentation
* [Clash Royale Fandom](https://clashroyale.fandom.com/wiki/Chests) for the chest images.
