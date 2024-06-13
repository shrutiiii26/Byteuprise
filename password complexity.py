import re

def password_strength(password):
    # Define the criteria for a strong password
    criteria = {
        'length': len(password) >= 12,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digits': bool(re.search(r'[0-9]', password)),
        'special': bool(re.search(r'[\W_]', password))
    }
    
    # Calculate the score based on how many criteria are met
    score = sum(criteria.values())
    
    # Generate feedback based on unmet criteria
    feedback = []
    if not criteria['length']:
        feedback.append("Password should be at least 12 characters long.")
    if not criteria['uppercase']:
        feedback.append("Password should include at least one uppercase letter.")
    if not criteria['lowercase']:
        feedback.append("Password should include at least one lowercase letter.")
    if not criteria['digits']:
        feedback.append("Password should include at least one numeric digit.")
    if not criteria['special']:
        feedback.append("Password should include at least one special character (e.g., !, @, #, $, etc.).")
    
    # Determine the strength of the password based on the score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return {
        'score': score,
        'strength': strength,
        'feedback': feedback
    }

def main():
    password = input("Enter your password to check its strength: ")
    result = password_strength(password)
    print(f"Score: {result['score']}/5")
    print(f"Strength: {result['strength']}")
    print("Feedback:")
    for feedback in result['feedback']:
        print(f"- {feedback}")

if __name__ == "__main__":
    main()
