shows = ['Pokemon', 'Looney Tunes', 'Popeye', 'Big City Greens']
##for i in range(len(shows)):
##    print(shows[i])
for show in shows:
    print(show)    
show = input('Enter another show. ')
index = int(input('Enter an index 0-4. '))
shows.insert(index, show)
##for i in range(len(shows)):
##    print(shows[i])
for show in shows:
    print(show)     

