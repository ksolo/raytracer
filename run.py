from data_structures import Coordinates
from data_structures import Color
from drawing import Canvas
from drawing.formats import PPMFormat

# Challenge for end of chapter 1
projectile = {
    "position": Coordinates.point(0, 1, 0),
    "velocity": Coordinates.vector(1, 1.8, 0).normalize() * 11.25,
}

environment = {
    "gravity": Coordinates.vector(0, -0.1, 0),
    "wind": Coordinates.vector(-0.01, 0, 0),
}


def tick(projectile, environment):
    position = projectile["position"] + projectile["velocity"]
    velocity = projectile["velocity"] + environment["gravity"] + environment["wind"]

    return {"position": position, "velocity": velocity}


projectiles = [projectile]

while projectile["position"].y > 0:
    projectile = tick(projectile, environment)
    projectiles.append(projectile)

red = Color(1, 0, 0)

canvas = Canvas(900, 550)
for projectile in projectiles:
    position = projectile["position"]
    if (  # position inbounds of canvas
        position.x > 0
        and position.x <= canvas.width
        and position.y > 0
        and position.y <= canvas.height
    ):
        canvas.write_pixel(int(position.x), int(canvas.height - position.y), red)

PPMFormat(canvas).write()
