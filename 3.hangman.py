word=['abruptly','absurd','abyss','affix','askew','avenue','awkward','axiom','azure','bagpipes','bandwagon','banjo','bayou'
,'beekeeper','bikini','blitz','blizzard','boggle','bookworm','boxcar','boxful','buckaroo','buffalo','buffoon','buxom','buzzard','buzzing','buzzwords'
,'caliph','cobweb','cockiness','croquet','crypt','curacao','cycle','daiquiri','dirndl','disavow','dizzying','duplex','dwarves','embezzle','equip'
,'espionage','euouae','exodus','faking','fishhook','fixable','fjord','flapjack','flopping','fluffiness','flyby','foxglove','frazzled','frizzled','fuchsia'
,'funny','gabby','galaxy','galvanize','gazebo','giaour','gizmo','glowworm','glyph','gnarly','gnostic','gossip','grogginess','haiku'
,'haphazard','hyphen','iatrogenic','icebox','injury','ivory','ivy','jackpot','jaundice','jawbreaker','jaywalk','jazziest','jazzy'
,'jelly','jigsaw','jinx','jiujitsu','jockey','jogging','joking','jovial','joyful','juicy','jukebox','jumbo','kayak','kazoo','keyhole','khaki'
,'kilobyte','kiosk','kitsch','kiwifruit','klutz','knapsack','larynx','lengths','lucky','luxury','lymph','marquis','matrix','megahertz'
,'microwave',',mnemonic','mystify','naphtha','nightclub','nowadays','numbskull','nymph','onyx','ovary','oxidize','oxygen','pajama','peekaboo','phlegm'
,'pixel','pizazz','pneumonia','polka','pshaw','psyche','puppy','puzzling','quartz','queue','quips','quixotic','quiz','quizzes','quorum'
,'razzmatazz','rhubarb','rhythm','rickshaw','schnapps','snazzy','sphinx','spritz','squawk','staff','strength','strengths','stretch','stronghold'
,'stymied','subway','swivel','syndrome','thriftless','thumbscrew','topaz','transcript','transgress','transplant','triphthong','twelfth','twelfths'
,'unknown','unworthy','unzip','uptown','vaporize','vixen','vodka','voodoo','vortex','voyeurism','walkway','waltz','wave','wavy','waxy'
,'wellspring','wheezy','whiskey','whizzing','whomever','wimpy','witchcraft','wizard','woozy','wristwatch','wyvern','xylophone','yachtsman','yippee'
,'yoked','youthful','yummy','zephyr','zigzag','zigzagging','zilch','zipper','zodiac','zombie']

import random
life=12
computer_guess=random.choice(word)

print("Welcome to hangman let's play you have 12 chance")
lettersofchoice=[]
for i in range(len(computer_guess)):
    lettersofchoice.append(computer_guess[i])
    print("_",end='')

trueletters = []

for j in range(len(computer_guess)):
    trueletters.append("-")

selected=[]
while True:

    guess=input("\nplz enter your guess:")
    guess=guess.lower()






    if guess not in lettersofchoice :
        life-=1
        selected.append(guess)
        print("\nwrong answer life:",life,"your selected word:")
        for n in range(len(selected)):
            print( selected[n], ",", end='')
        print("\n")


    for i in range(len(computer_guess)):

        if guess in lettersofchoice[i]:
            trueletters[i]=str(guess)


    for j in range(len(trueletters)):
        print(trueletters[j],end='')
    if trueletters == lettersofchoice:
        print("\tcongratulation you win")
        break
    if life==0:
        print( "You lost, Do you want to try again?")
        break









