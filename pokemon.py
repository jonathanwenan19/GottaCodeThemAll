import random as r

def splitone(data):
        finaldata= data.split(' ')
        newlist = []
        counter = 0
        for i in range(0,len(finaldata)):
            #firstelementonlist
            if len(newlist)==0:
                random_select = r.randint(0, 70)
                erased = finaldata.pop(random_select)
                newlist.append(erased)
                finalletter= erased[len(erased)-1]
            else: continue
            #newinsert
            for word1 in finaldata:
                if word1.startswith(finalletter):
                    newlist.append(word1)
                    counter+=1
                    finalletter=word1[len(word1)-1]
                    finaldata.remove(word1)
                else:continue
        return str(newlist)+'The maximum words in this list is {}'.format(counter+1)

print(splitone('audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask'))
