class MoveCharacter:
    def move_fwd(self):
        print("Move forward 1 step")

    def move_bwd(self):
        print("Move backward 1 step")

class JumpCharacter:
    def jump_1level(self):
        print("Jump charecter 1 level")

    def jump_2level(self):
        print("Jump charecter 2 level")

class Pokemon(MoveCharacter,JumpCharacter):
    def move_bwd(self):
        print("Pokemon moving" )

p = Pokemon()
p.move_bwd()
p.jump_1level()

