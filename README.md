# PRODIGY_CS_03


This Python script is a password complexity checker that evaluates the strength of a given password based on several criteria. Here's a breakdown of its functionality:

1. Password Strength Assessment
The function assess_password_strength(password) evaluates the password based on:

Length (≥12 characters)
At least one uppercase letter
At least one lowercase letter
At least one digit
At least one special character (e.g., !@#$%^&*)
Each criterion is checked using regular expressions (re.search()).

2. Scoring System
The password is scored from 1 to 5, based on how many criteria it meets:

1 → Very Weak
2 → Weak
3 → Moderate
4 → Strong
5 → Very Strong
3. Feedback for Improvement
If the password is weak, the script provides suggestions such as:

"Increase length to at least 12 characters."
"Add at least one uppercase letter."
"Include at least one number."
4. Continuous Input Loop
The script continuously asks for a password until a strong or very strong password is entered. If the password meets the criteria, it exits with:

"Your password is secure! ✅"

