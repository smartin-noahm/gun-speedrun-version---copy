@namespace
class SpriteKind:
    Hud = SpriteKind.create()
    Health = SpriteKind.create()
    Mana = SpriteKind.create()
    Placeholder = SpriteKind.create()
    Boxx = SpriteKind.create()
mySprite = sprites.create(img("""
        . . . . . . e e c c e e . . . . 
            . . . . . e 2 2 2 2 2 2 e . . . 
            . . . . 2 c 2 2 2 2 2 2 c 2 . . 
            . . . e 2 c 4 2 2 2 2 2 c 2 e . 
            . . . f 2 2 4 2 2 2 2 2 c 2 f . 
            . . . f 2 2 4 2 2 2 2 2 2 2 f . 
            . . . f 2 2 4 2 2 2 2 2 2 2 f . 
            . . . f 2 c 2 4 4 2 2 2 c 2 f . 
            . . . e 2 c e c c c c e c 2 e . 
            . . . e 2 e c b b b b c e 2 e . 
            . . . e 2 e b b b b b b e 2 e . 
            . . . e e e e e e e e e e e e . 
            . . . f e d e e e e e e d e f . 
            . . . f e 2 d e e e e d 2 e f . 
            . . . f f e e e e e e e e f f . 
            . . . . f f . . . . . . f f . .
    """),
    SpriteKind.player)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
tiles.place_on_random_tile(mySprite, assets.tile("""
    myTile9
"""))
scene.camera_follow_sprite(mySprite)
controller.move_sprite(mySprite)
Render.set_view_mode(ViewMode.TILEMAP_VIEW)