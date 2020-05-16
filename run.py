from data_structures.types import Coordinates

# Challenge for end of chapter 1
projectile = {
    "position": Coordinates.point(0, 1, 0),
    "velocity": Coordinates.vector(4, 1, 0).normalize(),
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

for projectile in projectiles:
    pos = projectile["position"]
    print(f"x: {round(pos.x, 4)} y: {round(pos.y, 4)}")
