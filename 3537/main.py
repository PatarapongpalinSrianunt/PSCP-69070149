"""[LEARNING LOGS] Impostor"""
from ast import literal_eval
def main():
    """[LEARNING LOGS] Impostor"""
    alive_roles = {}
    while True:
        line = input().strip()
        if line == "Start":
            break
        if line:
            alive_roles.update(literal_eval(line))
    dead_roles = {}
    while True:
        voted_name = input().strip()
        if voted_name == "End":
            break
        if voted_name in alive_roles:
            dead_roles[voted_name] = alive_roles.pop(voted_name)
    impostor_remaining = list(alive_roles.values()).count("Impostor")

    print(f"{impostor_remaining} Impostor Remains")

    print("***Alive***")
    for name in sorted(alive_roles):
        print(f"{name} : {alive_roles[name]}")

    print("***Dead***")
    for name in sorted(dead_roles):
        print(f"{name} : {dead_roles[name]}")

main()
