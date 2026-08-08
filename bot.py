import random

# 50+ Hindi Proverbs with topics
proverbs = {
    "mehnat": ["Karm karo fal ki chinta mat karo", "Mehnat ka phal meetha hota hai", "Boond boond se sagar bharata hai"],
    "samay": ["Samay bada balwan", "Samay aur lehar kisi ki pratiksha nahi karte"],
    "gyaan": ["Gyaan baantne se badhta hai", "Vidya dhan sarv dhan pradhan"],
    "dosti": ["Dost hi dost ki pehchan hota hai", "Sacha dost mushkil me kaam aata hai"],
    "jhooth": ["Jhooth ke paanv nahi hote", "Sachai chhup nahi sakti"],
    "general": ["Jaisi karni waisi bharni", "Naam bade aur darshan chote", "Ghar ki murgi daal barabar"]
}

def dhoondo_proverb(topic):
    topic = topic.lower()
    for key in proverbs:
        if key in topic:
            return random.choice(proverbs[key])
    return random.choice(proverbs["general"])

print("===== HINDI PROVERB BOT =====")
print("Topic likho: mehnat, samay, gyaan, dosti")
print("Band karne ke liye 'q' likho")
print("=============================")

while True:
    baat = input("\nTu: ")

    if baat == "q":
        print("Bot: Dhanyawad! Phir milte hain")
        break

    ans = dhoondo_proverb(baat)
    print("Bot:", ans)
