import re
import math

COMMON_PASSWORDS = [
    "password",
    "123456",
    "123456789",
    "admin",
    "qwerty",
    "abc123",
    "password123"
]


def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26

    if re.search(r"[A-Z]", password):
        charset += 26

    if re.search(r"[0-9]", password):
        charset += 10

    if re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/\\|]", password):
        charset += 32

    if charset == 0:
        return 0

    return round(len(password) * math.log2(charset), 2)


def analyze_password(password):

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase password length to at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include at least one number.")

    if re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/\\|]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character.")

    entropy = calculate_entropy(password)

    if password.lower() in COMMON_PASSWORDS:
        strength = "Very Weak"
        suggestions.append("This password is commonly used. Avoid dictionary passwords.")
    else:
        if score <= 2:
            strength = "Weak"
        elif score <= 4:
            strength = "Medium"
        else:
            strength = "Strong"

    return score, strength, entropy, suggestions


if __name__ == "__main__":

    password = input("Enter Password: ")

    score, strength, entropy, suggestions = analyze_password(password)

    print("\n========== PASSWORD SECURITY REPORT ==========")
    print(f"Password        : {password}")
    print(f"Score           : {score}/5")
    print(f"Strength        : {strength}")
    print(f"Entropy         : {entropy} bits")

    if suggestions:
        print("\nRecommendations:")
        for item in suggestions:
            print(f"- {item}")
    else:
        print("\nExcellent! Your password follows recommended security practices.")