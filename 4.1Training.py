extramans = ['Alan','Green','Gries','Raymend']
for extraman in extramans:
    if 'Alan' in extramans:
        extramans.remove('Green') 
        extramans.insert(0,'Superalan'.upper())
        extramans.sort(reverse=True)
        print(sorted(extramans))
        print(extramans)
        extramans.pop()
        extramans.pop()
    print(extramans)

  