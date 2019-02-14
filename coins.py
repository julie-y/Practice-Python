import random

class Coin:
    def __init__ (self, rare = False, clean =True, heads = True, **kwargs):
        for key, value in kwargs. items():
            setattr (self, key, value)
            
            self.is_rare = rare
            self.is_clean = clean
            self.heads = heads

        if self.is_rare:
            self.value = self. original_value *1.25
        else:
            self. value = self. original_value

        if self.is_clean:
            self.colour = self. clean_colour
        else:
            self.colour = self.original_value

    def rust(self):
          self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def flip(self):
        heads_options = [True, False]
        choice = random. choice(heads_options)
        self.heads = choice

    def __str__ (self):
        if self.original_value >= 1.00:
            return'{}'.format(int(self.original_value))
        else:
            return '{} p Coin'.format(int(self.original_value))
        
class one_pence (Coin): # create a class called Pound, and will inherit the parent class (coin)
    
    def __init__(self):
        data = {
            'original_value' : 0.01,
            'clean_colour': 'bronze',
            'rusty_colour': 'borwnish',
            'num_edges': 1,
            'diameter': 20.3,
            'thickness': 1.52,
            'mass': 3.56
            }
        super ().__init__(**data) 

class five_pence (Coin): # create a class called Pound, and will inherit the parent class (coin)
    
    def __init__(self):
        data = {
            'original_value' : 0.05,
            'clean_colour': 'silver',
            'rusty_colour': 'None',
            'num_edges': 1,
            'diameter': 18.0,
            'thickness': 1.77,
            'mass': 3.25
            }
        super ().__init__(**data)
        def rust(self):
            self.colour = self.clean_colour
        def clean(self):
            self.colour = self. clean_colour

class Pound (Coin): # create a class called Pound, and will inherit the parent class (coin)
    
    def __init__(self):
        data = {
            'original_value' : 1.00,
            'clean_colour': 'gold',
            'rusty_colour': 'greenish',
            'num_edges': 1,
            'diameter': 22.5,
            'thickness': 3.15,
            'mass': 9.5
            }
        super ().__init__(**data) #unpack data for key world arguments

#inside the init function, then get the parent constructor for the rest of the setup.
        
