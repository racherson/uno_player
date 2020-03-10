# Companions Uno AI
This Uno AI uses Companions to track a game of Uno between 4 players and provide move suggestions for one player.

## Setup
Run generate_uno_player.py.
In Companions, load uno.krf and NextMove.krf.

## Card Entities
See Cards.krf for card entities. Example card entities include blue2 and redreverse. 

## Opponents
See OpponentsState.krf to see opponent entities and properties. Example opponent entities include opponent1, opponent2, opponent3. 

## Colors
See Cards.krf for color collections. Example color collections include RedPlayingCard, BluePlayingCard. 

## Instructions for Playing a Game
**1. Initialize Game**

Initialize the game state with the top card in the discard pile and the cards in your hand. To do this, go to the commands tab in Companions and run the following command (InitializeGame ?topCard ?card1 ?card2 ?card3 ?card4 ?card5 ?card6 ?card7) where topCard is the top card in the discard pile and ?card1 through ?card7 are the seven cards you start with in your hand. Here is an example of the InitializeGame command with real entities: (InitializeGame blue2 bluedraw2 blue1 blue3 bluereverse blueskip blue8 blue0) 

**2. Your Turn**

When it is your turn, you can either draw or play a card. Both outcomes will involve commands in the commands tab in Companions. 

If you draw a card, run the following command (selfDrewCard ?card) with the card entity you drew. Here is an example of the selfDrewCard command with real entities: (selfDrewCard red7)

If you play a card, run the following command (selfPlayedCard ?card) with the card entity you played. Here is an example of the selfPlayedCard command with real entities: (selfPlayedCard blue8)

See instruction #4 for how to get recommendations for what card to play on your turn.

**3. Opponents' Turns**

When it is an opponents turn, they can either draw or play a card. Both outcomes will involve commands in the commands tab in Companions. 

If an opponent draws and then plays a card (e.g. they had no playable cards in their hand and the card they drew was playable), run the following command (opponentDrewAndPlayed ?opponent ?card) with the respective opponent and card entities. Here is an example of the opponentDrewAndPlayed command with real entities:  (opponentDrewAndPlayed opponent1 green5)

If an opponent drew card(s), run the following command (opponentDrewCard ?opponent ?quantity) with the respective opponent and number of cards drawn. Here is an example of the opponentDrewCard command with real entities when the previous player played a draw 2: (opponentDrewCard opponent2 2)

If an opponent played a wild card, run the following command (opponentPlayedWildCard ?opponent ?color) with the respective opponent and switched-to color entities. Here is an example of the opponentPlayedWildCard command with real entities: (opponentPlayedWildCard opponent1 RedPlayingCard)

If an opponent plays a card that isn't a wild card, run the following command (opponentPlayedCard ?opponent ?card) with the respective opponent and card entities. Here is an example of the opponentPlayedCard command with real entities: (opponentPlayedCard opponent1 blue3)

**4. Recommendations**

This is the primary purpose of our system.

If it is your turn and you want to know your best move, run the following command (cardToPlay). Then, go back to the status tab in Companions, right-click session-reasoner and select Browse KB. Search "MyNextMoveMt" in the search bar, and open up facts in mt. You will see a fact of the form (nextMove ?card) where ?card is the recommended card to play. Here is what the fact looks like with real entities: (nextMove blue8)

If you are recommended to play a wild card, the entity's name will reflect a wild card and a color to change to. For example, if you should play a wild card and change the color to red, your next move would look like (nextMove wildRed). 
         
## Notes

Some commands and queries may take some time to run. If it looks like the KB isn't updated immediately, wait a minute just in case and give the system time to run. The status tab will tell you the states of the different agents; here you can see if the session-reasoner is still planning. 