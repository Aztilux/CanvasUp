from datetime import datetime, timedelta
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import datetime

icon_dict = {
"vip": "<:vip:1070865933540802590>",
"snowball": "<:snowball:1070865913076793385>",
"partner": "<:partner:1070865878956126308>",
"painting-owner": "<:paintingowner:1070865855765819422>",
"painting-moderator": "<:paintingmoderator:1070865835356328056>",
"nitro": "<:nitro:1070865804427534437>",
"moderator": "<:moderator:1070865779198795777>",
"gifter": "<:gifter:1070865753412223077>",
"former-global-moderator": "<:formerglobalmoderator:1070865723565547590>",
"chat-moderator": "<:chatmoderator:1070865697757999226>",
"bread": "<:bread:1070865671426150410>",
"booster": "<:booster:1070865655601057842>",
"admin": "<:admin:1070865607102300222>",
"3-months": "<:3months:1070865562537820170>",
"3-days": "<:3days:1070865451799822467>",
"1-month": "<:1month:1070865395814244422>",
"1-year": "<:1year:1070865387593420901>"
}

# Webhooks #
with open('secrets.json') as f:
    secrets = json.load(f)
bombsWH = secrets['bombs']
islandsWH = secrets['islands']
giftsWH = secrets['gifts']
mutesWH = secrets['mutes']
statsWH = secrets['stats']
connectionsWH = secrets['connections']
globalWH = secrets['global']
nonenglishWH = secrets['nonenglish']
toxicWH = secrets['toxicalert']
warWH = secrets['wars']
mvpWH = secrets['mvp']

def on_messagews1(ws, message):
    if 'item.notification.use' in message:
        start = message.index('{"')
        end = message.rindex("}") + 1
        data = json.loads(message[start:end])
        from_user = data["from"]
        item_name = data["itemName"]
        item = data["item"]
        x = data["x"]
        y = data["y"]
        webhook = DiscordWebhook(
        url=bombsWH
        )
        embed = DiscordEmbed(
        title=f"[💥] Dropped {item_name}",
        description=f"{from_user} dropped a {item_name} on {x}, {y}\nhttps://pixelplace.io/7-pixels-world-war#x={x}&y={y}&s=2",
        color="30D5C8",
            )
        embed.set_thumbnail(url=f"https://pixelplace.io/img/item-{item}.png?v=3")            
        webhook.add_embed(embed)
        embed.set_timestamp()
        response = webhook.execute()
        print(f'{from_user} has dropped a {item_name} on {x}, {y}')
    elif '42["coin_island_owner_change",' in message:
        webhook = DiscordWebhook(
            url=islandsWH
        )
        start = message.index('{"')
        end = message.rindex("}") + 1
        data = json.loads(message[start:end])
        user = data["from"]
        amount = data["amount"]
        island = data["island"]
        if island == 0:
            print(f"{user} cap won {amount} coins on the big island")
            embed.set_thumbnail(url=f"https://pixelplace.io/img/coin-island-t.gif")
            embed = DiscordEmbed(
                title="[🏁] Someone captured the BIG island.",
                description=f"{user} captured the BIG island winning {amount} coins!",
                color="2B339E",
            )
            webhook.add_embed(embed)
            embed.set_timestamp()
            response = webhook.execute()
        elif island == 1:
            print("test")
            embed = DiscordEmbed(
                title="[🚩] Someone captured a small island.",
                description=f"{user} captured the north-east island winning {amount} coins!",
                color="30D5C8",
            )
            webhook.add_embed(embed)
            embed.set_thumbnail(url=f"https://pixelplace.io/img/coin-island-t.gif")
            embed.set_timestamp()
            response = webhook.execute()
        elif island == 2:
            print("test")
            embed = DiscordEmbed(
                title="[🚩] Someone captured a small island.",
                description=f"{user} captured the east island winning {amount} coins!",
                color="30D5C8",
            )
            webhook.add_embed(embed)
            embed.set_thumbnail(url=f"https://pixelplace.io/img/coin-island-t.gif")
            embed.set_timestamp()
            response = webhook.execute()
        elif island == 3:
            print("test")
            embed = DiscordEmbed(
                title="[🚩] Someone captured a small island.",
                description=f"{user} captured the south-east island winning {amount} coins!",
                color="30D5C8",
            )
            webhook.add_embed(embed)
            embed.set_thumbnail(url=f"https://pixelplace.io/img/coin-island-t.gif")
            embed.set_timestamp()
            response = webhook.execute()

    elif '42["item.notification.gift",' in message:
        start = message.index('{"')
        end = message.rindex("}") + 1
        data = json.loads(message[start:end])
        sender = data["from"]
        receiver = data["to"]
        item = data["item"]
        item_names = {
            1: "Pixel Missile",
            2: "Pixel Bomb",
            3: "Atomic Bomb",
            4: "One Month Premium",
            5: "One Year Premium",
            6: "Rainbow Username",
            7: "Guild Bomb",
            8: "Avatar Bomb",
            9: "Name Change",
            10: "XMas Username",
            11: "3 Days Premium",
        }
        item_name = item_names.get(item, "Unknown Item")
        print(f"Gift from {sender} to {receiver} [item {item_name}]")
        webhook = DiscordWebhook(
            url=giftsWH,
            content=f"{sender} sent a gift to {receiver} item: {item_name}",
        )
        embed = DiscordEmbed(
            title="[🎁] New Gift!",
            description=f"{sender} sent a __{item_name}__ to {receiver}\nLet's hope he enjoys it...",
            color="FFC0CB",
        )
        embed.set_thumbnail(url=f"https://pixelplace.io/img/item-{item}.png?v=3")
        webhook.add_embed(embed)
        embed.set_timestamp()
        response = webhook.execute()

    # done
    elif message.startswith('42["chat.system.delete",'):
        start = message.index(',"') + 2
        end = message.rindex('"]')
        username = message.split(',"')[-1][:-2]
        print(f"User Muted: {username}")
        webhook = DiscordWebhook(
            url=mutesWH)
        embed = DiscordEmbed(
            title="[❌] User Muted.",
            description=f"{username} has been muted.",
            color="8B0000",
        )
        webhook.add_embed(embed)
        embed.set_timestamp()
        response = webhook.execute()

    # done
    elif message.startswith('42["chat.stats",'):
        data = json.loads(message[2:])
        players = data[1][0]
        print("Total players:", players)
        # py_dt = datetime.now()
        # epoch = round(py_dt.timestamp())
        # disc_dt = f"<t:{epoch}:R>"
        webhook = DiscordWebhook(
            url=statsWH
        )
        embed = DiscordEmbed(
            title="[👥] Stat Update",
            description=f"Total Players: {players}",
            color="000000",
        )
        webhook.add_embed(embed)
        embed.set_timestamp()
        response = webhook.execute()

    # Done
    elif message.startswith('42["j","') or message.startswith('42["l","'):
        user = message[8:-2]
        if not user:
            pass
        webhook = DiscordWebhook(
            url=connectionsWH
        )
        if message.startswith('42["j","'):
            print(f"User joined:", user)
            embed = DiscordEmbed(
                title="[+] User Joined!", description=f"{user}", color="03ff00"
            )
            webhook.add_embed(embed)
            embed.set_timestamp()
            response = webhook.execute()
        else:
            print(f"User left:", user)
            embed = DiscordEmbed(
                title="[-] User Left!", description=f"{user}", color="FF0000"
            )
            webhook.add_embed(embed)
            embed.set_timestamp()
            response = webhook.execute()


    # Todo Icons, Guild, etc.
    elif '42["chat.user.message",' in message:
        start = message.index('{"')
        end = message.rindex("}") + 1
        data = json.loads(message[start:end])
        username = data["username"]
        text = data["message"].strip()
        channel = data["channel"].strip()
        mention = data["mention"]
        guild = data["guild"] if data["guild"] != "" else ""
        formatted_username = f"{guild}" + (f" • {username}" if guild else f"{username}")
        pos_x = data.get("posX")
        pos_y = data.get("posY")
        pos_s = data.get("posS")
        icons = data.get("icons")
        created_at = data["createdAt"]
        created_at = datetime.datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
        if created_at + datetime.timedelta(seconds=10) > datetime.datetime.utcnow() - datetime.timedelta(seconds=10):
            icon_str = ""
            for icon in icons:
                if icon in icon_dict:
                    icon_str += icon_dict[icon]
            formatted_username = f"{icon_str} {formatted_username}"
            response = requests.get("https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en")
            bad_words = response.text.splitlines()
            if pos_x is not None and pos_y is not None and pos_s is not None:
                if text != '':
                    text = f"Message: {text}\n"
                if mention != '':
                    mention = f"Mention: __@{mention}__\n"
                if channel == "nonenglish":
                    webhook = DiscordWebhook(
                        url=nonenglishWH
                        )
                    embed = DiscordEmbed(
                    title="[📍] New Coordinate (/here)! [Non-English]",
                    description=f"**User: {formatted_username}\n{mention}{text}/here [X={pos_x}, Y={pos_y}, S={pos_s}]\nhttps://pixelplace.io/7-pixels-world-war#x={pos_x}&y={pos_y}&s={pos_s}**",
                    color="d1ebf7",
                    )
                    webhook.add_embed(embed)
                    embed.set_timestamp()
                    response = webhook.execute()
                elif channel == "global":
                    webhook = DiscordWebhook(
                        url=globalWH
                        )
                    embed = DiscordEmbed(
                    title="[📍] New Coordinate (/here)! [Global]",
                    description=f"**User: {formatted_username}\n{mention}{text}/here [X={pos_x}, Y={pos_y}, S={pos_s}]\nhttps://pixelplace.io/7-pixels-world-war#x={pos_x}&y={pos_y}&s={pos_s}**",
                    color="d1ebf7",
                    )
                    webhook.add_embed(embed)
                    embed.set_timestamp()
                    response = webhook.execute()

            else:
                if mention != '':
                    mention = f"__@{mention}__"
                if channel == "nonenglish":
                    webhook = DiscordWebhook(
                        url=nonenglishWH
                    )
                    embed = DiscordEmbed(
                        title="[💬] New Message! [Non-English]",
                        description=f"**{formatted_username}: {mention} {data['message']}**",
                        color="d1ebf7",
                    )
                    webhook.add_embed(embed)
                    embed.set_timestamp()
                    response = webhook.execute()
                elif channel == "global":
                    webhook = DiscordWebhook(
                        url=globalWH
                    )
                    embed = DiscordEmbed(
                        title="[🌐] New Message! [Global]",
                        description=f"**{formatted_username}: {mention} {data['message']}**",
                        color="d1ebf7",
                    )
                    webhook.add_embed(embed)
                    embed.set_timestamp()
                    response = webhook.execute()
                print(
                    f"Received message from {formatted_username} in #{channel}: {data['message']}"
                )
            if any(word in text for word in bad_words):
                    if mention != '':
                        mention = f"{mention}"                            
                    webhook = DiscordWebhook(
                        url=toxicWH
                    )
                    embed = DiscordEmbed(
                        title=f"[⚠] Toxicity detected in #{channel}",
                        description=f"**{formatted_username}: {mention} {data['message']}**",
                        color="ffa590",
                    )
                    webhook.add_embed(embed)
                    embed.set_timestamp()
                    response = webhook.execute()

    elif '42["area_fight_start",' in message:
        start = message.index('{"')
        end = message.rindex("}") + 1
        data = json.loads(message[start:end])
        id = data["id"]
        fight_type = data.get("fightType", None)
        name_mapping = {
            "0": "Australian",
            "1": "Russian",
            "2": "African",
            "3": "Antarctica",
            "4": "Canadian",
            "5": "Brazilian",
            "6": "Chinese",
            "7": "Greenland",
            "8": "United States"
        }
        webhook = DiscordWebhook(
        url=warWH
        )
        if fight_type == 1:
            print(f"Player War started with id {id}, corresponding to {name_mapping.get(id)}")
            embed = DiscordEmbed(

                title=f"[⚔] __{name_mapping.get(id)}__ **Player** War Started!",
                description=f"Be the fastest player to win!",
                color="0000FF",
            )
            webhook.add_embed(embed)
            embed.set_timestamp()
            response = webhook.execute()        
        elif fight_type == 0:
            embed = DiscordEmbed(

                title=f"[⚔] __{name_mapping.get(id)}__ **Guild** War Started!",
                description=f"Be the fastest guild to win!",
                color="0000FF",
            )
            py_dt = datetime.datetime.now() + timedelta(minutes=15)
            epoch = round(py_dt.timestamp())
            disc_dt = f"<t:{epoch}:R>"
            embed.add_embed_field(
                name=f"Time Remaining",
                value=f"{disc_dt}",
                inline=False
            )
            webhook.add_embed(embed)
            embed.set_timestamp()
            response = webhook.execute()

    elif '42["area_fight_end",' in message:
        start = message.index('{"')
        end = message.rindex("}") + 1
        data = json.loads(message[start:end])
        id = data["id"]
        owned_by = data["ownedBy"]
        owned_by_guild = data["ownedByGuild"]
        previous_owner = data["previousOwner"]
        fight_type = data["fightType"]
        points = data["points"]
        total = data["total"]
        guilds = total["guilds"]
        pixels = total["pixels"]
        users = total["users"]
        webhook = DiscordWebhook(
            url=warWH
        )
        name_mapping = {
            "0": "Australian",
            "1": "Russian",
            "2": "African",
            "3": "Antarctica",
            "4": "Canadian",
            "5": "Brazilian",
            "6": "Chinese",
            "7": "Greenland",
            "8": "United States"
        }
        stats = data.get("stats", [])
        location = name_mapping.get(id)
        if fight_type == 0:
            print(f"---------------------------------------------")
            print(f"Fight ended with id {id}, corresponding to {location}")
            print(f"Owned by: {owned_by}")
            print(f"Previous owner: {previous_owner}")
            print(f"Fight type: {fight_type}")
            print(f"Points: {points}")
            print(f"Top 3:")
            if stats:
                stats = sorted(stats, key=lambda x: x["pixels"], reverse=True)
                for i, stat in enumerate(stats[:3]):
                    place = "🥇" if i == 0 else "🥈" if i == 1 else "🥉"
                    print(f"{place} {stat['guild']}: {stat['pixels']} pixels with {stat['users']} users")
            print(f"Total: {total}")
            embed = DiscordEmbed(

                title=f"[🏆] __{location}__ **Guild** War Ended!",
                description=f"Owned by: {owned_by}\nPrevious owner: {previous_owner}\nPoints: {points}\n\n**Top 3:**\n",
                color="ece75f",
            )
            if stats:
                stats = sorted(stats, key=lambda x: x["pixels"], reverse=True)
                for i, stat in enumerate(stats[:3]):
                    place = "🥇" if i == 0 else "🥈" if i == 1 else "🥉"
                    embed.add_embed_field(
                        name=f"{place} {stat['guild']}:",
                        value=f"{stat['pixels']} pixels with {stat['users']} users",
                        inline=False
                    )
            embed.add_embed_field(
                name=f"\nTotal:",
                value=f"Guilds: {guilds}\nPixels: {pixels}\nUsers: {users}",
                inline=False
            )
            webhook.add_embed(embed)
            embed.set_timestamp()
            response = webhook.execute()
            print(f"---------------------------------------------")
        elif fight_type == 1: #Player War End
            if owned_by_guild != '':
                mention = f"[{owned_by_guild}]"
            ores = data["ores"]
            print(f"---------------------------------------------")
            print(f"Fight ended with id {id}, corresponding to {location}")
            print(f"Owned by: {owned_by} [{owned_by_guild}]")
            print(f"Previous owner: {previous_owner}")
            print(f"Fight type: {fight_type}")
            print(f"Points: {points}")
            print(f"Ores: {ores}")
            print(f"Top 3:")
            if stats:
                stats = sorted(stats, key=lambda x: x["pixels"], reverse=True)
                for i, stat in enumerate(stats[:3]):
                    place = "🥇" if i == 0 else "🥈" if i == 1 else "🥉"
                    print(f"{place} {stat['username']}: {stat['pixels']} pixels")
            print(f"Total: {total}")
            embed = DiscordEmbed(

                title=f"[🏆] __{location}__ **Player** War Ended!",
                description=f"Owned by: {owned_by} {owned_by_guild}\nPrevious owner: {previous_owner}\nPoints: {points}\nGold: {ores}\n\n**Top 3:**\n",
                color="ece75f",
            )
            if stats:
                stats = sorted(stats, key=lambda x: x["pixels"], reverse=True)
                for i, stat in enumerate(stats[:3]):
                    place = "🥇" if i == 0 else "🥈" if i == 1 else "🥉"
                    userguild = stat['guild']
                    if stat['guild'] != '':
                        userguild = f" [{userguild}]"
                    embed.add_embed_field(
                        name=f"{place} {stat['username']}{userguild}:",
                        value=f"{stat['pixels']} pixels",
                        inline=False
                    )
            embed.add_embed_field(
                name=f"\nTotal:",
                value=f"Pixels: {pixels}\nUsers: {users}",
                inline=False
            )
            py_dt = datetime.datetime.now() + timedelta(minutes=15)
            epoch = round(py_dt.timestamp())
            disc_dt = f"<t:{epoch}:R>"
            embed.add_embed_field(
                name=f"Next War:",
                value=f"{disc_dt}",
                inline=False
            )
            webhook.add_embed(embed)
            embed.set_timestamp()
            response = webhook.execute()
            print(f"---------------------------------------------")

    elif not message.startswith('42["p",') and not message.startswith('42["canvas",') and not message.startswith('42["chat.user.message"') and not message.startswith('42["areas",'):
        print("Received XTra: ", message)


def on_messagews2(ws, message):
    if '42["chat.user.message",' in message:
        start = message.index('{"')
        end = message.rindex("}") + 1
        data = json.loads(message[start:end])
        username = data["username"]
        text = data["message"].strip()
        channel = data["channel"].strip()
        mention = data["mention"]
        guild = data["guild"] if data["guild"] != "" else ""
        formatted_username = f"{guild}" + (f" • {username}" if guild else f"{username}")
        pos_x = data.get("posX")
        pos_y = data.get("posY")
        pos_s = data.get("posS")
        icons = data.get("icons")
        created_at = data["createdAt"]
        created_at = datetime.datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
        if created_at + datetime.timedelta(seconds=10) > datetime.datetime.utcnow() - datetime.timedelta(seconds=10):
            icon_str = ""
            for icon in icons:
                if icon in icon_dict:
                    icon_str += icon_dict[icon]
            formatted_username = f"{icon_str} {formatted_username}"
            response = requests.get("https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en")
            bad_words = response.text.splitlines()
            webhook = DiscordWebhook(
                url=mvpWH
            )
            if channel == "painting":
                if pos_x is not None and pos_y is not None and pos_s is not None:
                    if text != '':
                        text = f"Message: {text}\n"
                    if mention != '':
                        mention = f"Mention: __@{mention}__\n"
                    if channel == "painting":
                        embed = DiscordEmbed(
                        title="[📍] New Coordinate (/here)! [MVP]",
                        description=f"**User: {formatted_username}\n{mention}{text}/here [X={pos_x}, Y={pos_y}, S={pos_s}]\nhttps://pixelplace.io/7-pixels-world-war#x={pos_x}&y={pos_y}&s={pos_s}**",
                        color="d1ebf7",
                        )
                        webhook.add_embed(embed)
                        embed.set_timestamp()
                        response = webhook.execute()
                else:
                    if mention != '':
                        mention = f"__@{mention}__"
                    embed = DiscordEmbed(
                        title="[💬] New Message! [MVP]",
                        description=f"**{formatted_username}: {mention} {data['message']}**",
                        color="d1ebf7",
                    )
                    webhook.add_embed(embed)
                    embed.set_timestamp()
                    response = webhook.execute()
                    print(
                        f"Received message from {formatted_username} in #{channel}: {data['message']}"
                    )
                    if any(word in text for word in bad_words):
                            if mention != '':
                                mention = f"{mention}"                            
                            webhook = DiscordWebhook(
                                url=toxicWH
                            )
                            embed = DiscordEmbed(
                                title=f"[⚠] Toxicity detected in #{channel}",
                                description=f"**{formatted_username}: {mention} {data['message']}**",
                                color="ffa590",
                            )
                            webhook.add_embed(embed)
                            embed.set_timestamp()
                            response = webhook.execute()
