# Cribbage-Bot
Making a bot that plays crib statistically perfectly. Will keep track of the remaining cards in the deck and iterate through all possible outcomes to make optimal decisions. 

## Update 1:
After some more thought, the script will specifically maximise for putting you ahead of your opponent (expected points you get from a move minus opponents expected points), rather than just maximising your own points. Initially this will only be based off the points in your hand + crib, but later on will also take into account the pegging phase of crib. Another feature I'm wanting to add later on is rather than assuming the cards already in the crib and the opponents cards are random, assuming the opponent discards optimally. This will then result in the possible opponents hands and cribs will be different to just a random combination of the cards we don't already know, slightly tweaking the weighting of different decisions. 
