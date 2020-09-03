# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self,name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = [ ]

    def __str__(self):
        return f"{self.name} \nyou are at the {self.current_room}"

    def move(self, room):
        self.current_room = room

    def take_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)
    
    def list_inventory(self):
        print(f"{self.name} you have {len(self.inventory)} items in your inventory")
        for item in self.inventory:
            print(item)

    def location(self):
        print(f"\nyou are at the {self.current_room}")