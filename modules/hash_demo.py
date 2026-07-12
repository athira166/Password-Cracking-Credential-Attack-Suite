import hashlib
import os


def generate_hash(password, algorithm="sha256"):
    """
    Generate hash using the selected algorithm.
    Supported: md5, sha1, sha256, sha512
    """

    password = password.encode()

    if algorithm == "md5":
        return hashlib.md5(password).hexdigest()

    elif algorithm == "sha1":
        return hashlib.sha1(password).hexdigest()

    elif algorithm == "sha256":
        return hashlib.sha256(password).hexdigest()

    elif algorithm == "sha512":
        return hashlib.sha512(password).hexdigest()

    else:
        return None


def create_hash_file():

    os.makedirs("sample_data", exist_ok=True)

    input_file = "sample_data/passwords.txt"
    output_file = "sample_data/hashes.txt"

    if not os.path.exists(input_file):
        print("Error: passwords.txt not found!")
        return

    algorithm = input(
        "Choose Hash Algorithm (md5 / sha1 / sha256 / sha512): "
    ).lower()

    if algorithm not in ["md5", "sha1", "sha256", "sha512"]:
        print("Invalid algorithm selected!")
        return

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:

        outfile.write("=" * 70 + "\n")
        outfile.write(f"Hash Algorithm : {algorithm.upper()}\n")
        outfile.write("=" * 70 + "\n\n")

        for password in infile:

            password = password.strip()

            if password == "":
                continue

            hash_value = generate_hash(password, algorithm)

            outfile.write(f"Password : {password}\n")
            outfile.write(f"Hash     : {hash_value}\n")
            outfile.write("-" * 70 + "\n")

    print("\nHash generation completed successfully!")
    print("Output saved to:", output_file)

def verify_hash(password, target_hash, algorithm="sha256"):

    generated = generate_hash(password, algorithm)

    if generated == target_hash:
        return True

    return False

if __name__ == "__main__":
    create_hash_file()