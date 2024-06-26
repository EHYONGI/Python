import random

people = [
    "강지승",
    "김민수",
    "김수현",
    # "김아영",
    "김정아",
    "김주미",
    "김태주",
    "김현호",
    "박진경",
    "성찬렬",
    "이시운",
    "이현주",
    "이후석",
    "조은수",
    "최지원",
    "최진욱"
]

random.shuffle(people)

for i in range(0, len(people), 4):
    print(people[i:i+4])