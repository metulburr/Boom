

import pygame as pg
from .. import tools, data
from ..GUI import button
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
        self.database = data.data
        
        button_config = {
            "hover_color"        : (150,150,150),
            "clicked_color"      : (255,255,255),
            "clicked_font_color" : (0,0,0),
            "hover_font_color"   : (0,0,0),
            'font'               : tools.Font.load('impact.ttf', 12)
        }
        self.next_button = button.Button((475,150,100,25),(100,100,100), 
            lambda x=1:self.switch_card(x), text='Next', **button_config
        )
        self.prev_button = button.Button((225,150,100,25),(100,100,100), 
            lambda x=-1:self.switch_card(x), text='Previous', **button_config
        )
    def callback_test(self):
        print('callback')
        
    def update_category(self, text):
        self.category, self.category_rect = self.make_text(text, (255,255,255), (self.screen_rect.centerx, 162), 15, fonttype='impact.ttf')
        
    def update_image(self, val):
        self.image = self.cards[val].surf
        self.image_rect = self.image.get_rect(centerx=self.screen_rect.centerx-125, centery=self.screen_rect.centery + self.card_offsetY)
        self.path = self.cards[val].path
        category = tools.get_category(self.path)
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
        self.next_button.check_event(event)
        self.prev_button.check_event(event)

    def update(self, now, keys):
        pg.mouse.set_visible(True)
        self.mouse_hover_sound()
        self.change_selected_option()
        
        filename = tools.get_filename(self.path)
        self.help_overlay_title, self.help_overlay_title_rect = self.make_text(filename.title(),
            (255,255,255), (self.screen_rect.centerx, 100), 60, fonttype='impact.ttf')
        
        string = self.database[filename]['info']
        my_font = tools.Font.load('impact.ttf', 20)
        self.help_overlay_text_rect = pg.Rect((425, 200, 300, 300))
        self.help_overlay_text = tools.render_textrect(string, my_font, self.help_overlay_text_rect, (216, 216, 216), self.bg_color, 0)

    def render(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.title,self.title_rect)
        screen.blit(self.category, self.category_rect)
        screen.blit(self.image ,self.image_rect)
        #screen.blit(self.help_overlay_title, self.help_overlay_title_rect)
        screen.blit(self.help_overlay_text, self.help_overlay_text_rect)
        for i,opt in enumerate(self.rendered["des"]):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom+i*self.spacer)
            if i == self.selected_index:
                rend_img,rend_rect = self.rendered["sel"][i]
                rend_rect.center = opt[1].center
                screen.blit(rend_img,rend_rect)
            else:
                screen.blit(opt[0],opt[1])
        self.next_button.render(screen)
        self.prev_button.render(screen)
        
    def cleanup(self):
        pg.display.set_caption("Boom")
        
    def entry(self):
        pass
