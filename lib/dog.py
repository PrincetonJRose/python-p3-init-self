#!/usr/bin/env python3

class Dog:
    pass
    def __init__( self, name, breed="Mutt" ):
        print( "%s is born!" % name )
        self.name = name
        self.breed = breed

    def bark( self ):
        print( "Woof!" )

    def get_adopted( self, owner_name ):
        self.owner = owner_name