import re

def assess_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 12
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    number_criteria = bool(re.search(r"\d", password))
    special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    # Calculate score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Feedback messages
    feedback = []
    if not length_criteria:
        feedback.append("Increase length to at least 12 characters.")
    if not uppercase_criteria:
        feedback.append("Add at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Add at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Include at least one number.")
    if not special_char_criteria:
        feedback.append("Use at least one special character (e.g., !@#$%^&*).")

    # Strength classification
    strength_levels = {
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }
    strength = strength_levels.get(score, "Very Weak")

    return strength,feedback
"""
# Example usage
password = input("Enter your password: ")
result = assess_password_strength(password)

print("\nPassword Strength:", result["strength"])
if result["feedback"]:
    print("Suggestions to improve:")
    for tip in result["feedback"]:
        print("-", tip)"""
while True:
    password = input("Enter your password: ")
    strength, feedback = assess_password_strength(password)

    print("\nPassword Strength:", strength)
    
    if strength in ["Strong", "Very Strong"]:
        print("Your password is secure! ✅")
        break  # Exit loop if password is strong
    else:
        print("Suggestions to improve:")
        for tip in feedback:
            print("-", tip)
        print("\nPlease try again.\n")







