input.onButtonPressed(Button.A, function () {
    if (sprite.get(LedSpriteProperty.X) == 2) {
        game.addScore(1)
    } else {
        intentos = intentos - 1
        if (intentos == 0) {
            game.gameOver()
        } else {
            basic.showString("Quedan: " + intentos)
        }
    }
})
let sprite: game.LedSprite = null
let intentos = 0
intentos = 3
sprite = game.createSprite(2, 2)
basic.forever(function () {
    sprite.move(1)
    sprite.ifOnEdgeBounce()
    basic.pause(200)
})
