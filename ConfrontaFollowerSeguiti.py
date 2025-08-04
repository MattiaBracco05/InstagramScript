import json

def estrai_usernames(nome_file, chiave_principale=None):
    with open(nome_file, "r", encoding="utf-8") as f:
        dati = json.load(f)

    if chiave_principale:
        dati = dati.get(chiave_principale, [])

    usernames = []
    for item in dati:
        try:
            value = item["string_list_data"][0]["value"]
            usernames.append(value)
        except (KeyError, IndexError, TypeError):
            print(f"⚠️ Voce non valida o malformata in {nome_file}: {item}")
    return usernames

# Estrai username
followers = estrai_usernames("followers.json")
following = estrai_usernames("following.json", "relationships_following")

# Confronto
non_followback = sorted(set(following) - set(followers))

# Stampa
print(f"\n❌ Persone che segui ma che non ti seguono: {len(non_followback)}")
for user in non_followback:
    print(user)

# Salva su file
with open("non_followback.txt", "w", encoding="utf-8") as f:
    for user in non_followback:
        f.write(user + "\n")

print("\n💾 Lista salvata nel file: non_followback.txt")
