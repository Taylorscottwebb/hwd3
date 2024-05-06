import random
moods = ["Energetic", "Happy", "Sad", "Calm"] 
print(random.choice(moods))
weekdays =["monday","tuesday", "wednesday","thursday"]
for i in range(len(weekdays)) :
    print(weekdays[i],random.choice(moods))



import random
moods = ["Energetic", "Happy", "Sad", "Calm"] 
print(random.choice(moods))
weekdays =["monday","tuesday", "wednesday","thursday"]
for i in range(len(weekdays)) :
    times = ["morning", "night", "afternoon"]
    print(weekdays[i],(random.choice(times)), "You were", (random.choice(moods)))