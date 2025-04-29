"""
Challenge #025  [Easy] Election.

Description

In an election, the person with the majority of the votes is the winner. 
Sometimes due to similar number of votes, there are no winners.

Your challenge is to write a program that determines the winner of a vote, 
or shows that there are no winners due to a lack of majority.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

votes = {"libdem":230, "labour":40, "conservative":400}

total = votes['libdem'] + votes['labour'] + votes['conservative']
total = int(total)
majority = (total/2)+1

if int(votes['libdem']) < majority and int(votes['labour']) < majority and int(votes['conservative']) < majority :
    print "No clear majority"

else:
    print "The winner is " + max(votes, key=votes.get)
