import itertools
import time


def brute_force_simulation(target, charset):

    start_time = time.time()
    attempts = 0

    total_combinations = len(charset) ** len(target)

    for guess in itertools.product(charset, repeat=len(target)):

        guess = "".join(guess)
        attempts += 1

        if guess == target:

            end_time = time.time()

            return {
                "target": target,
                "charset": charset,
                "attempts": attempts,
                "total_combinations": total_combinations,
                "time_taken": round(end_time - start_time, 6),
                "status": "Password Found (Simulation)"
            }

    return {
        "target": target,
        "charset": charset,
        "attempts": attempts,
        "total_combinations": total_combinations,
        "time_taken": 0,
        "status": "Password Not Found"
    }


if __name__ == "__main__":

    print("=" * 50)
    print("        BRUTE-FORCE ATTACK SIMULATOR")
    print("=" * 50)

    target = input("Enter sample password: ")
    charset = input("Enter character set (Example: abc123): ")

    result = brute_force_simulation(target, charset)

    print("\n========== SIMULATION REPORT ==========")
    print(f"Target Password      : {result['target']}")
    print(f"Password Length      : {len(result['target'])}")
    print(f"Character Set        : {result['charset']}")
    print(f"Character Set Size   : {len(result['charset'])}")
    print(f"Total Combinations   : {result['total_combinations']}")
    print(f"Attempts Made        : {result['attempts']}")
    print(f"Time Taken           : {result['time_taken']} seconds")
    print(f"Result               : {result['status']}")

    print("\nSecurity Recommendation:")

    if len(result["target"]) < 8:
        print("- Use a password of at least 8 characters.")

    if len(result["charset"]) < 10:
        print("- Increase password complexity by using uppercase, lowercase, numbers, and special characters.")

    print("- Enable Multi-Factor Authentication (MFA).")
    print("- Avoid dictionary-based passwords.")
    print("- Change passwords periodically.")

    print("\nSimulation Completed Successfully!")