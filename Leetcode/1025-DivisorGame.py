class Solution:
    def divisorGame(self, n: int) -> bool:
        # So, if Bob has no more moves, Alice wins (person who made first move)
        # Since Alice always starts, she wins if she gets an even number, and loses if she gets an odd one. 
        bob_score = 0
        alice_score = 0

        while(n!=1):
            alice_score+=1
            n-=1
            if(n == 1):
                break
            bob_score+=1
            n-=1

        if(alice_score > bob_score):
            return True
        else:
            return False
