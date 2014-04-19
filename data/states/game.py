

import pygame as pg
from .. import tools, card, data
import os
import random

class Game(tools.States):
    def __init__(self, screen_rect): 
        tools.States.__init__(self)
        self.screen_rect = screen_rect
        #self.score_text, self.score_rect = self.make_text("SCOREBOARD_PLACEHOLDER",
        #    (255,255,255), (screen_rect.centerx,100), 50)
        #self.help_overlay_title, self.help_overlay_title_rect = self.make_text("help_overlay",
        #    (255,255,255), screen_rect.center, 50)
        #self.help_overlay_text, self.help_overlay_text_rect = self.make_text("help_overlay",
        #    (255,255,255), screen_rect.center, 50)
            
        self.overlay_bg = pg.Surface((screen_rect.width, screen_rect.height))
        self.overlay_bg.fill(0)
        self.overlay_bg.set_alpha(200)
        self.overlay_card_position = (100,200)
        
        self.deck = []
        self.database = data.data
        self.create_deck()
        #self.make_deck()
        self.bg_color = (255,255,255)
        self.help_overlay = False
        self.card_bufferX = 100
        self.card_bufferY = 25
        
        self.bg = tools.Image.load('greenbg.png')
        self.bg_rect = self.bg.get_rect()
        self.is_hand_set = False
        
        self.help_btn_image = tools.Image.load('info.png')
        #self.help_btn_image = pg.transform.scale(self.help_btn_image, (20,25))
        self.help_btn_image_rect = self.help_btn_image.get_rect(topleft=(0,0))
        
        self.settings = tools.Image.load('gear.png')
        self.settings = pg.transform.scale(self.settings, (25,25))
        self.settings_rect = self.settings.get_rect(topleft=(25,0))
        
        
    
    def get_event(self, event, keys):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYDOWN:
            if event.key == self.keybinding['back']:
                if not self.help_overlay:
                    self.button_sound.sound.play()
                    self.done = True
                    self.next = 'MENU'
                else:
                    self.help_overlay = not self.help_overlay
                
        elif event.type == self.background_music.track_end:
            self.background_music.track = (self.background_music.track+1) % len(self.background_music.tracks)
            pg.mixer.music.load(self.background_music.tracks[self.background_music.track]) 
            pg.mixer.music.play()
            
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if not self.help_overlay:
                self.select_left_side_of_card()
            if self.help_btn_image_rect.collidepoint(pg.mouse.get_pos()):
                if self.selected_card():
                    self.help_overlay = not self.help_overlay
            
    def select_left_side_of_card(self):
       for card in self.hand:
            #if card != self.hand[-1]:
            half_width = int(card.rect.width/2)
            card_left_side = card.rect.inflate(-half_width, 0)
            card_left_side.x -= int(half_width/2)
            if card_left_side.collidepoint(pg.mouse.get_pos()):
                if self.same_bool(self.hand_selected()) or card.selected:
                    card.selected = not card.selected
                else: #select new card, and deselect current card
                    self.set_all_cards_select_to_false()
                    card.selected = True
                    
    def set_all_cards_select_to_false(self):
        for card in self.hand:
            card.selected = False
                    
    def selected_card(self):
        for card in self.hand:
            if card.selected:
                return card
                    
    def hand_selected(self):
        c = []
        for card in self.hand:
            c.append(card.selected)
        return c
                
    def same_bool(self, lister):
        return all(lister) or not any(lister)

    def update(self, now, keys):
        if not self.help_overlay:
            self.update_hand_position()
        else:
            filename = tools.get_filename(self.selected_card().path)
            self.help_overlay_title, self.help_overlay_title_rect = self.make_text(filename.title(),
                (255,255,255), (self.screen_rect.centerx, 100), 60, fonttype='impact.ttf')
            
            string = self.database[filename]['info']
            my_font = tools.Font.load('impact.ttf', 20)
            self.help_overlay_text_rect = pg.Rect((400, 200, 300, 300))
            self.help_overlay_text = tools.render_textrect(string, my_font, self.help_overlay_text_rect, (216, 216, 216), (48, 48, 48, 255), 0)
            
            #self.help_overlay_text, self.help_overlay_text_rect = self.make_text(self.database[filename]['info'],
            #    (255,255,255), (self.screen_rect.centerx + 100, 200), 20, fonttype='impact.ttf')

    def render(self, screen):
        screen.blit(self.bg, self.bg_rect)
        
        selected_card = None
        for card in self.hand:
            if card.selected:
                selected_card = card
            else:
                screen.blit(card.surf, (card.rect.x, card.rect.y))
        if selected_card:
            screen.blit(selected_card.surf, (selected_card.rect.x, selected_card.rect.y))
            
        if self.help_overlay:
            screen.blit(self.overlay_bg,(0,0))
            screen.blit(self.help_overlay_title, self.help_overlay_title_rect)
            screen.blit(self.help_overlay_text, self.help_overlay_text_rect)
            sel = self.selected_card()
            screen.blit(sel.surf, self.overlay_card_position)
        if self.selected_card():
            screen.blit(self.help_btn_image, self.help_btn_image_rect)
        #screen.blit(self.settings, self.settings_rect)

    def update_hand_position(self):
        for i, card in enumerate(self.hand):
            card.rect.y = self.screen_rect.bottom - card.surf.get_height()
            if card.selected:
                card.rect.y -= self.card_bufferY
            card.rect.x = i * self.card_bufferX 
            
    def get_hand_cards(self):
        hand_cards = []
        for card in self.deck:
            if tools.get_category(card.path) not in ['roles', 'characters']:
                hand_cards.append(card)
        return hand_cards
        
    def set_hand(self, card_num):
        return random.sample(self.get_hand_cards(), card_num)
        
    def create_deck(self):
        path = os.path.join(tools.Image.path, 'cards')
        for root, dirs, files in os.walk(path):
            for f in files:
                if f.endswith('.png'):
                    path = os.path.abspath(os.path.join(root, f))
                    image = pg.image.load(path)
                    filename = tools.get_filename(path)
                    for i in range(self.database[filename]['max']):  
                        self.deck.append(card.Card(path, image))
        #for c in self.deck:
        #    print('{} at {}'.format(c.path, c))
        #print(len(self.deck))
            
    def cleanup(self):
        pg.mixer.music.unpause()
        #pg.mixer.music.stop()
        #self.background_music.setup(self.background_music_volume)
        
    def entry(self):
        if not self.is_hand_set:
            self.is_hand_set = True
            self.hand = self.set_hand(4)
        pg.mixer.music.pause()
        #pg.mixer.music.play()
