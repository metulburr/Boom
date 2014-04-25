data = {
#roles
    'fbi':{
        'info':'Kill all the Mobsters and the Snitch.',
        'max':1,
    },
    'mobster':{
        'info':'Kill the FBI agent.',
        'max':3,
    },
    'police':{
        'info':'Protect the FBI agent. Kill all the Mobsters and the Snitch.',
        'max':2,
    },
    'snitch':{
        'info':'Be the last one in play. You must kill the FBI agent after all the mobsters and police are dead.',
        'max':1,
    },
#actions
    'panic':{
        'info':'Draw a card from a player at distance 1. This distance is not modified by weapons, but by cards such as Vehicle and/or Scope.',
        'max':5,
        'action':'player',
    },
    'store':{
        'info':'When played, as many cards as there are players still playing are turned face down on the table. Starting with the player that played it, proceeding clockwise, each player chooses one of the cards and adds it to their hand',
        'max':3,
        'action':'all_players',
    },
    'miss':{
        'info':'May be played immediately to cancel the effect of a BOOM card, or any card with a BOOM symbol.',
        'max':17,
        'action':'self',
    },
    'pawn':{
        'info':'Draw 3 cards from the deck at time of play.',
        'max':2,
        'action':'self',
    },
    'shop':{
        'info':'Draw 2 cards from the deck at time of play.',
        'max':2,
        'action':'self',
    },
    'boom':{
        'info':'Deal a BOOM to target player. Target must play a MISS, otherwise the target loses one life point. Each player can only play one BOOM per turn.',
        'max':29,
        'action':'player',
    },
    'bar':{
        'info':'One life point to every player.',
        'max':2,
        'action':'all_players',
    },
    'beer':{
        'info':'Discard this and gain one life point.',
        'max':9,
        'action':'self',
    },
    'duel':{
        'info':'Target player must discard a BOOM card, then you, etc. First player failing to discard a BOOM card loses one life point. A MISS or KEG card is not accepted. This card does not use your turns BOOM.',
        'max':3,
        'action':'player',
    },
    'raid':{
        'info':'All other players discard a BOOM card or lose one life point. A MISS or KEG card is not accepted.',
        'max':3,
        'action':'all_players',
    },
    'thief':{
        'info':'Force a player to discard a card. This card can be random from their hand, or a card they have on the table in play.',
        'max':6,
        'action':'player',
    },
    'tommygun':{
        'info':'Deals a BOOM card to every other player regardless of distance. This card does not use your turns BOOM.',
        'max':2,
        'action':'all_players',
    },
    'whiskey':{
        'info':'Discard this and a card of your choice from your hand and get two life points',
        'max':1,
        'action':'self',
    },
#effects
    'vehicle':{
        'info':'When you have the vehicle in play, the distance at which other players see you is increased by one. However you still see the other players at normal distance.',
        'max':4,
        'action':'self_table',
    },
    'scope':{
        'info':'When you have the scope in play, you see all other players at a distance decreased by one. However, other players still see you at the normal distance. ',
        'max':1,
        'action':'self_table',
    },
    'binoculars':{
        'info':'When you have the binoculars in play, you see all other players at a distance decreased by one. However, other players still see you at the normal distance. ',
        'max':1,
        'action':'self_table',
    },
    'dynamite':{
        'info':'Before you play your turn, draw a card for the dynamite. If the card is a spades, you lose three life points, otherwise pass the dynamite to your left. The dynamite stays in play rotating around the table until it explodes on a player. Player putting the card down puts it on themself first, and draws for it on their next turn.',
        'max':2,
        'action':'self_table',
    },
    'jail':{
        'info':'Either draw a card and get a heart to discard the jail, or skip your turn and discard the jail. If you draw a card, and do not get a heart, the jail is still in play, and you must choose again on your next turn. If in hand, play on a player to put them in jail.', 
        'max':3,
        'action':'player',
    },
    'keg':{
        'info':'Draw a heart and it acts as a MISS card played. Keg stays in play after.',
        'max':3,
        'action':'self_table',
    },
#characters
    'capone':{
        'info':'Each time another player is eliminated, he regains 2 life points',
        'life':4,
        'max':1,
    },
    'costello':{
        'info':'He may use any card as a Miss card',
        'life':3,
        'max':1,
    },
    'gillis':{
        'info':'During his turn he may choose to lose one life to draw two cards',
        'life':4,
        'max':1,
    },
    'gotti':{
        'info':'For onr whole round, he gains the same ability of another character in play of his choice',
        'life':4,
        'max':1,
    },
    'backend':{
        'info':'Cards back side',
        'max':0
    }
}

if __name__ == '__main__':
    for k,v in data.items():
        print(k,v['info'])
        print(k,v.get('life', 'life none'))
        print(k,v.get('action', 'action none'))
        
    print('\nCard Types: {}'.format(len(data.values())))
    print('Card Instances: {}'.format( sum([v['max'] for v in data.values()]) ))

