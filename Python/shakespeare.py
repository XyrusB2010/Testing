import random

nouns = ["bugbear", "clot pole", "cur", "foot-licker", "gudgeon", "jolthead", "mammet", "minnow", "moldwarp", "ninny", "penury", "umbrage", "base-court", "caitiff", "coxcomb", "fustilarian", "harpy", "loggerhead", "meed", "miscreant", "morrow", "noddle", "prolixity", "termagant", "varlet", "braggert", "carrion", "cuckold", "flirt-gill", "giglet", "horn-beast", "lout", "moiety", "mumble-news", "paramour", "ratsbane", "vassal"]

adjectives = ["artless", "churlish", "currish", "fawning", "impertinent", "roguish", "spleeny", "villainous", "bawdy", "cockered", "dissembling", "forward", "lumpish", "ruttish", "surly", "warped", "bootless", "craven", "dulcet", "gorbellied", "rank", "saucy", "unmuzzled", "beef-witted", "clay-brained", "earth-vexing", "fat-kidneyed", "folly-fallen", "full-gorged", "horn-mad", "ill-breeding", "knotty-pated", "motley-minded", "plume-plucked", "shard-borne", "swag-bellied", "toad-spotted", "beetle-headed", "dizzy-eyed", "elf-skinned", "flap-mouthed", "fool-born", "hasty-witted", "idle-headed", "ill-nurtured", "milk-livered", "onion-eyed", "rude-growing", "sheep-biting", "tardy-gaited", "whey-face"]

myName = "Xyrus"
nameInput = input('Prithee, what is thy nameth? ').strip().title()

if nameInput == myName:
    print(f"{myName}, thou art a wond'rful p'rson.")
else:
    numInsults = int(input("How many times shouldst i fig thee? "))
    insults = random.sample(adjectives, numInsults - 1)
    insults.append(random.choice(nouns))
    message = ', '.join(insults)

    print(f'{nameInput}, thou art a {message}!')

    if numInsults < 10:
        print(f"{nameInput}, thee has't been did praise.")
    else:
        print(f"{nameInput}, doth thee wanteth to beest did insult some m're?")