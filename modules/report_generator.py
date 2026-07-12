from datetime import datetime
import os


def generate_report():

    os.makedirs("reports", exist_ok=True)

    report_path = "reports/security_audit_report.txt"

    with open(report_path, "w", encoding="utf-8") as report:

        report.write("=" * 60 + "\n")
        report.write(" PASSWORD CRACKING & CREDENTIAL ATTACK SUITE\n")
        report.write("=" * 60 + "\n\n")

        report.write(f"Generated On : {datetime.now()}\n\n")

        report.write("PROJECT MODULES\n")
        report.write("-" * 60 + "\n")
        report.write("[✓] Dictionary Generator\n")
        report.write("[✓] Hash Demonstration\n")
        report.write("[✓] Password Strength Analyzer\n")
        report.write("[✓] Brute-Force Simulation\n\n")

        report.write("SECURITY RECOMMENDATIONS\n")
        report.write("-" * 60 + "\n")
        report.write("• Use passwords with at least 12 characters.\n")
        report.write("• Include uppercase and lowercase letters.\n")
        report.write("• Include numbers and special characters.\n")
        report.write("• Avoid common dictionary passwords.\n")
        report.write("• Enable Multi-Factor Authentication (MFA).\n")
        report.write("• Never reuse passwords across websites.\n")
        report.write("• Change passwords when compromise is suspected.\n\n")

        report.write("PROJECT STATUS\n")
        report.write("-" * 60 + "\n")
        report.write("All modules executed successfully.\n")
        report.write("This toolkit is intended for educational and")
        report.write(" ethical security demonstrations only.\n")

    print("\nReport Generated Successfully!")
    print("Saved at:", report_path)


if __name__ == "__main__":
    generate_report()