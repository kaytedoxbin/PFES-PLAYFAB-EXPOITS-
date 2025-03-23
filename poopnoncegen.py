import string
import uuid
import random
import hashlib

def save_to_file(game_id, nonce_id, oculus_id, custom_id):
    with open("generatednonce.txt", "w") as file:
       file.write(f"App ID: {game_id}\n")
       file.write(f"Nonce ID: {nonce_id}\n")
       file.write(f"OculusId: {oculus_id}\n")
       file.write(f"Org Scope: {custom_id}\n")
    print("\nnonce gen saved!")
def generate_ids(game_id):
    org_scope_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, game_id))

    player_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

    nonce_id = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=64))

    custom_id = "OCULUS" + ''.join([str(random.randint(0, 9)) for _ in range(10)])

    oculus_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))

    return org_scope_id, player_id, nonce_id, custom_id, oculus_id

def main():
    game_id = input("game ID: ")

    org_scope_id, player_id, nonce_id, custom_id, oculus_id = generate_ids(game_id)

    print("\nshitty generator:")
    print(f"Org Scope: {custom_id}")
    print(f"Nonce: {nonce_id}")
    print(f"OculusId: {oculus_id}")
    
    save_to_file(game_id, nonce_id, oculus_id, custom_id)

if __name__ == "__main__":
    main()
