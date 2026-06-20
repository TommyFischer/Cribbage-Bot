
## Overview ##

# Each card represent as number from 0-51 
# Will use default rules except deal 5 discard 1 instead of deal 6 discard 2
# Optimising for biggest point differential \Delta X (My points - opponents points)
    # Considering your hand, crib, and pegging
# At this stage assuming opponent cards are random, in the future will maybe account for opponent playing optimally 


# Crib_bot will make two decisions:
    # What card to discard at the start of each round

        # For each of your 5 cards calculate expected points if you discard it 

            # How many points will my hand give me on average

                # Iterate through possible flip cards + number of points

                    # Count points in a hand 

            # How many points will the crib give me (+ or - depending on if its your crib or opponents)

                # Is it my crib or opponents (do i maximise or minimise crib)

                # What 3 cards might already be in the crib (2 random from deck + 1 from opponent discarding)

                # Given 3 cards in a crib, calculate expected points for each card i could add to it

            # How many points will I get from pegging  

                # Use pegging functions below 
            

    # What order to play cards for pegging

        # Given known cards, what cards produce best average point difference

            # Given known cards (+ how many my opponent has played) what possible cards could my opponent have
                # Deck = (0,52) - known cards, n = # of cards opponent has left, iterate through n-card combinations from deck

            # For a given set of opponent cards, what is best of all possible outcomes
                # Map out pegging outcomes 


    