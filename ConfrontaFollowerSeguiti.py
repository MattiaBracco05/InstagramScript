import json

def estrai_followers(nome_file):
    with open(nome_file, "r", encoding="utf-8") as f:
        dati = json.load(f)

    usernames = []
    for item in dati:
        try:
            usernames.append(item["string_list_data"][0]["value"])
        except (KeyError, IndexError, TypeError):
            print(f"⚠️ Voce non valida in followers: {item}")

    return usernames


def estrai_following(nome_file):
    with open(nome_file, "r", encoding="utf-8") as f:
        dati = json.load(f)

    usernames = []
    for item in dati["relationships_following"]:
        try:
            usernames.append(item["title"])
        except KeyError:
            print(f"⚠️ Voce non valida in following: {item}")

    return usernames


followers = estrai_followers("followers.json")
following = estrai_following("following.json")

non_followback = sorted(set(following) - set(followers))

print(f"\n❌ Persone che segui ma che non ti seguono: {len(non_followback)}")
for user in non_followback:
    print(user)

with open("non_followback.txt", "w", encoding="utf-8") as f:
    for user in non_followback:
        f.write(user + "\n")

print("\n💾 Lista salvata nel file: non_followback.txt")