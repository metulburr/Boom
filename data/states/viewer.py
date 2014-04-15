

import pygame as pg
from .. import tools
import os

class Viewer(tools.States):
    def __init__(self, screen_rect):
        tools.States.__init__(self)
        self.screen_rect = screen_rect
        self.options = ['Back']
        self.next_list = ['MENU']
        self.title, self.title_rect = self.make_text('Card Viewer', self.title_color, (self.screen_rect.centerx, 75), 150)
        
        self.pre_render_options()
        self.from_bottom = 550
        self.spacer = 75
        self.card_offsetY = 55
        
        self.create_deck()
        self.update_image(0)
        #self.update_category('placeholder')
        
    def update_category(self, text):
        self.category, self.category_rect = self.make_text(text, (255,255,255), (self.screen_rect.centerx, 175), 15, fonttype='impact.ttf')
        
    def update_image(self, val):
        self.image = self.cards[val].surf
        self.image_rect = self.image.get_rect(centerx=self.screen_rect.centerx, centery=self.screen_rect.centery + self.card_offsetY)
        path = self.cards[val].path
        category = tools.get_category(path)
        self.update_category(category.title())
        
    def switch_card(self, num):
        for i, obj in enumerate(self.cards):
            if obj.surf == self.image:
                ind = i
        ind += num
        if ind < 0:
            ind = len(self.cards)-1
        elif ind > len(self.cards)-1:
            ind = 0
            
        self.update_image(ind)
        #pg.display.set_caption(self.cards[ind].path)
        self.button_sound.sound.play()

    def get_event(self, event, keys):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYDOWN:
            if event.key in self.keybinding['left']:
                self.switch_card(-1)
            elif event.key in self.keybinding['right']:
                self.switch_card(1)
            
            elif event.key in self.keybinding['up']:
                self.change_selected_option(-1)
            elif event.key in self.keybinding['down']:
                self.change_selected_option(1)
                
            elif event.key == self.keybinding['select']:
                self.select_option(self.selected_index)
        self.mouse_menu_click(event)

    def update(self, now, keys):
        pg.mouse.set_visible(True)
        self.mouse_hover_sound()
        self.change_selected_option()

    def render(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.title,self.title_rect)
        screen.blit(self.category, self.category_rect)
        screen.blit(self.image ,self.image_rect)
        for i,opt in enumerate(self.rendered["des"]):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom+i*self.spacer)
            if i == self.selected_index:
                rend_img,rend_rect = self.rendered["sel"][i]
                rend_rect.center = opt[1].center
                screen.blit(rend_img,rend_rect)
            else:
                screen.blit(opt[0],opt[1])
        
    def cleanup(self):
        pg.display.set_caption("Boom")
        
    def entry(self):
        pass
