data = {
#roles
    'fbi':{
        'info':'Kill all the Mobsters and the Snitch',
    },
    'mobster':{
        'info':'Kill the FBI agent',
    },
    'police':{
        'info':'Protect the FBI agent. Kill all the Mobsters and the Snitch',
    },
    'snitch':{
        'info':'Be the last one in play. You must kill the FBI agent after all the mobsters and police are dead',
    },
#actions
    'bar':{
        'info':'One life point to every player',
    },
    'beer':{
        'info':'Discard this card and gain one life point',
    },
    'duel':{
        'info':'Target player must discard a BOOM card, then you, etc. First player failing to discard a BOOM card loses 1 life point',
    },
    'raid':{
        'info':'All other players discard a BOOM card or lose one life point',
    },
    'thief':{
        'info':'Force a player to discard a card',
    },
    'tommygun':{
        'info':'Deals a BOOM card to every other player except the person who played it',
    },
    'whiskey':{
        'info':'discard this card and a card of your choice from your hand and get two life points',
    },
#effects
    'dynamite':{
        'info':'Before you play your turn, draw a card for the dynamite. A spades and lose 3 life points. Otherwise pass the Dynamite to your left.',
    },
    'jail':{
        'info':'Either draw a card and get a heart to discard the jail, or skip your turn and discard the jail. If you draw a card, and do not get a heart, the jail is still in play, and you mujst choose again your next turn.', 
    },
    'keg':{
        'info':'Draw a heart and it acts as a Miss card played. Keg stays in play after.',
    },
#characters
    'capone':{
        'info':'Each time another player is eliminated, he regains 2 life points',
        'life':4,
    },
    'costello':{
        'info':'He may use any card as a Miss card',
        'life':3,
    },
    'gillis':{
        'info':'During his turn he may choose to lose one life to draw two cards',
        'life':4,
    },
    'gotti':{
        'info':'For onr whole round, he gains the same ability of another character in play of his choice',
        'life':4,
    },
}

if __name__ == '__main__':
    for k,v in data.items():
        print(k,v['info'])
        print(k,v.get('life', 'No "life"'))

