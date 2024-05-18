#In the world of Dota2, there are two parties: the Radiant and the Dire.
#The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:
#Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
#Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
#Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.
#The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.
#Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

#exercise 649

#this is a more efficient solution if a senator can ban a senator that's not neccesary next to him

from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dSentaros= deque() #this type of lists is more efficient for poping elements from the left
        rSenators = deque()

        for i, element in enumerate(senate):
            if element == "D":
                dSentaros.append(i)
            else:
                rSenators.append(i)
        n = len(senate)

        while len(rSenators) != 0 and len(dSentaros) != 0:
            if dSentaros[0] > rSenators[0]: #let's see who is the next senator to vote
                dSentaros.popleft() # we remove the banned senator
                rSenators.popleft() # we remove the senator to give to him a new turn to vote
                rSenators.append(n) #we put the senator at the end of the list, with his new turn to vote
            else:
                dSentaros.popleft()
                rSenators.popleft()
                dSentaros.append(n)
            n += 1
            
        if len(rSenators) == 0:
            return "Dire"
        else:
            return "Radiant"