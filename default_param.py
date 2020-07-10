import matplotlib.pyplot as plt
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImExNWE4NjkyLTJiYTktNDk5MC05NjViLTc0NzUzOTFiYzY1ZCIsImlhdCI6MTU5NDM3ODg1OCwic3ViIjoiZGV2ZWxvcGVyLzYzNzY1YzdiLWQzMTctODE0Yy0wZDdkLTVjOWM3M2VlMTgxMiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIzNi45MC4yMTUuMjQ5Il0sInR5cGUiOiJjbGllbnQifV19.UvyeUTuKVeSDJXsx9JS_P1vK3WdYShxVmag6EzBtaJdmRhJgkvHLlObe5Oum9TQsfA2Gjt2w3q4AfKudDNTOwg"
headers = {"Authorization": "Bearer " + token}
base_url = "https://api.clashroyale.com/v1"
hashtag = "/%23"

# Player
players = "/players"
upcomingchest = "/upcomingchests"
battlelog = "/battlelog"

# Clans
clans = "/clans"
clans_member = "/members"
clans_warlog = "/warlog"
clans_currentwar = "/currentwar"

# Cards
cards = "/cards"

# Ingame Cards ID
elixir_1 = ['26000010', '26000030', '28000016']
elixir_1_5 = ['28000006']
elixir_2 = ['26000002', '26000019', '26000031', '26000038', '26000049', '26000058', '28000002', '28000008',
            '28000011', '28000015', '28000017']
elixir_3 = ['26000000', '26000001', '26000005', '26000012', '26000013', '26000023', '26000025', '26000026',
            '26000032', '26000039', '26000040', '26000041', '26000046', '26000050', '26000056', '26000061',
            '26000064', '26000067', '27000000', '27000009', '28000001', '28000004', '28000012', '28000013',
            '28000014', '28000018']
elixir_4 = ['26000011', '26000014', '26000015', '26000018', '26000021', '26000027', '26000035', '26000036',
            '26000037', '26000042', '26000044', '26000048', '26000052', '26000057', '26000062', '26000068',
            '27000002', '27000004', '27000006', '27000010', '27000012', '28000000', '28000005', '28000009']
elixir_5 = ['26000003', '26000006', '26000007', '26000008', '26000016', '26000017', '26000022', '26000034',
            '26000045', '26000051', '26000053', '26000054', '26000059', '26000063', '27000001', '27000003'
            '28000010']
elixir_6 = ['26000020', '26000024', '26000033', '26000043', '26000060', '27000007', '27000008', '28000003',
            '28000007']
elixir_7 = ['26000004', '26000029', '26000047', '26000055', '27000005']
elixir_8 = ['26000009']
elixir_9 = ['26000028']

# Chest Image Link
silver = "https://vignette.wikia.nocookie.net/clashroyale/images/0/07/SilverChest.png/revision/latest/scale-to-width-down/160?cb=20160209231106"
img_silver = plt.imread(silver)
gold = "https://vignette.wikia.nocookie.net/clashroyale/images/8/8b/GoldenChest.png/revision/latest/scale-to-width-down/160?cb=20160209231105"
img_gold = plt.imread(gold)
magical = "https://vignette.wikia.nocookie.net/clashroyale/images/9/93/MagicalChest.png/revision/latest/scale-to-width-down/150?cb=20160312171354"
img_magical = plt.imread(magical)
giant = "https://vignette.wikia.nocookie.net/clashroyale/images/d/da/Giant_chest.png/revision/latest/scale-to-width-down/120?cb=20160306083332"
img_giant = plt.imread(giant)
mega = "https://vignette.wikia.nocookie.net/clashroyale/images/3/3a/MegaLightningChest.png/revision/latest/scale-to-width-down/120?cb=20181205194051"
img_mega = plt.imread(mega)
epic = "https://vignette.wikia.nocookie.net/clashroyale/images/f/f5/EpicChest.png/revision/latest/scale-to-width-down/120?cb=20160923080038"
img_epic = plt.imread(epic)
legendary = "https://vignette.wikia.nocookie.net/clashroyale/images/a/a1/LegendChest.png/revision/latest/scale-to-width-down/120?cb=20161002204147"
img_legendary = plt.imread(legendary)
