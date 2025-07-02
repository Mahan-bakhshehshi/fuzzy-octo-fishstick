class Person :
    def __init__(self , id , health , interest , Authority_Role , mobility):
        self.id = id
        self.health = health  #healthy  , sick , COVID suspect    
        self.interest = interest    #math, AI, art, economey
        self.Authority_Role = Authority_Role    #True, False
        self.mobility = mobility #0 , 1 , 2 (integers)
class Seat :
    def __init__(self , row , col):
        self.row = row
        self.col = col
        self.is_occupied = False

#The hall with 100 seats
NUM_ROWS = 10
NUM_COLS = 10

hall = [[Seat(r , c) for c in range(NUM_COLS)] for r in range(NUM_ROWS)]
