

import pygame as pg
from .. import tools
import os
import random
import copy
from ..card import Card

class Testing(tools.States):
    def __init__(self, screen_rect): 
        tools.States.__init__(self)
        self.screen_rect = screen_rect
        self.score_text, self.score_rect = self.make_text("SCOREBOARD_PLACEHOLDER",
            (255,255,255), (screen_rect.centerx,100), 50)
        self.pause_text, self.pause_rect = self.make_text("PAUSED",
            (255,255,255), screen_rect.center, 50)
            
        self.overlay_bg = pg.Surface((screen_rect.width, screen_rect.height))
        self.overlay_bg.fill(0)
        self.overlay_bg.set_alpha(200)
        
        self.set_cards()
        self.bg_color = (255,255,255)
        self.pause = False
        self.card_bufferX = 100
        self.card_bufferY = 25
    
    def get_event(self, event, keys):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYDOWN:
            if event.key == self.keybinding['back']:
                self.button_sound.sound.play()
                self.done = True
                self.next = 'MENU'

            elif event.key == self.keybinding['pause']:
                self.pause = not self.pause
                
        elif event.type == self.background_music.track_end:
            self.background_music.track = (self.background_music.track+1) % len(self.background_music.tracks)
            pg.mixer.music.load(self.background_music.tracks[self.background_music.track]) 
            pg.mixer.music.play()
            
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.select_left_side_of_card()
            
    def select_left_side_of_card(self):
       for card in self.hand:
            #if card != self.hand[-1]:
            half_width = int(card.rect.width/2)
            card_left_side = card.rect.inflate(-half_width, 0)
            card_left_side.x -= int(half_width/2)
            if card_left_side.collidepoint(pg.mouse.get_pos()):
                if self.same_bool(self.hand_selected()) or card.selected:
                    card.selected = not card.selected
                    
    def hand_selected(self):
        c = []
        for card in self.hand:
            c.append(card.selected)
        return c
                
    def same_bool(self, lister):
        return all(lister) or not any(lister)

    def update(self, now, keys):
        if not self.pause:
            self.update_hand_position()
        else:
            self.pause_text, self.pause_rect = self.make_text("Menu",
                (255,255,255), self.screen_rect.center, 50)

    def render(self, screen):
        screen.fill(self.bg_color)
        selected_card = None
        for card in self.hand:
            if card.selected:
                selected_card = card
            else:
                screen.blit(card.surf, (card.rect.x, card.rect.y))
        if selected_card:
            screen.blit(selected_card.surf, (selected_card.rect.x, selected_card.rect.y))
        if self.pause:
            screen.blit(self.overlay_bg,(0,0))
            screen.blit(self.pause_text, self.pause_rect)

    def update_hand_position(self):
        for i, card in enumerate(self.hand):
            card.rect.y = self.screen_rect.bottom - card.surf.get_height()
            if card.selected:
                card.rect.y -= self.card_bufferY
            card.rect.x = i * self.card_bufferX 
            
    def get_hand_cards(self):
        hand_cards = []
        for card in self.cards:
            if tools.get_category(card.path) not in ['roles', 'characters']:
                hand_cards.append(card)
        return hand_cards
        
    def set_hand(self):
        '''BUGFIX need to get any number of types of cards'''
        return random.sample(self.get_hand_cards(), 7)
        '''
        c = self.get_hand_cards()
        hand = []
        for i in range(7):
            card = random.choice(c)
            hand.append(copy.copy(card))
        return hand
        '''
    def set_cards(self):
        self.cards = []
        path = os.path.join(tools.Image.path, 'cards')
        for root, dirs, files in os.walk(path):
            for f in files:
                if f.endswith('.png'):
                    path = os.path.abspath(os.path.join(root, f))
                    image = pg.image.load(path)
                    self.cards.append(Card(path, image))
            
    def cleanup(self):
        pg.mixer.music.unpause()
        #pg.mixer.music.stop()
        #self.background_music.setup(self.background_music_volume)
        
    def entry(self):
        self.hand = self.set_hand()
        pg.mixer.music.pause()
        #pg.mixer.music.play()
