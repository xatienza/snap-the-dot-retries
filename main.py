def on_button_pressed_a():
    global intentos
    if sprite.get(LedSpriteProperty.X) == 2:
        game.add_score(1)
    else:
        intentos = intentos - 1
        if intentos == 0:
            game.game_over()
        else:
            basic.show_string("Quedan: " + str(intentos))
input.on_button_pressed(Button.A, on_button_pressed_a)

sprite: game.LedSprite = None
intentos = 0
intentos = 3
sprite = game.create_sprite(2, 2)

def on_forever():
    sprite.move(1)
    sprite.if_on_edge_bounce()
    basic.pause(200)
basic.forever(on_forever)
