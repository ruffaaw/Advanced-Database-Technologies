import redis
import random
from datetime import datetime, timedelta

# Połączenie z serwerem Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Przygotowanie danych
exercise_descriptions = {
    "Squats": "Squats are a strength training exercise where an individual stands in an upright position then lowers their body down while maintaining balance and control until the thighs are parallel to the floor and then returns to the upright position, engaging the muscles of the legs, glutes, and back",
    "Bench Press": "Bench press is a popular strength training exercise where an individual lies on a bench and lifts a weighted barbell or dumbbells upward from the chest until the arms are fully extended and then lowers the weight back down to the chest, primarily targeting the muscles of the chest, shoulders, and arms",
    "Deadlifts": "Deadlifts involve lifting a barbell or weights from the floor to a standing position using a hip hinge movement pattern, targeting multiple muscle groups including the back, glutes, hamstrings, and core, effective for building overall strength and power",
    "Pull-ups": "Pull-ups are a bodyweight exercise where an individual hangs from a bar with an overhand grip and pulls their body upward until the chin is above the bar and then lowers back down with control, primarily working the muscles of the back, arms, and shoulders, effective for improving upper body strength and endurance",
    "Lunges": "Lunges are a lower body exercise where an individual steps forward with one leg and lowers their body until both knees are bent at a 90-degree angle and then returns to the starting position, targeting the muscles of the legs including the quadriceps, hamstrings, and glutes, also engaging the core for stability",
    "Planks": "Planks are a core-strengthening exercise where an individual holds a push-up position with the body in a straight line from head to heels supporting their weight on their forearms and toes, engaging the muscles of the core including the abdominals, obliques, and lower back, helping improve overall stability and posture"
}

# Funkcja do generowania danych sesji treningowych
def generate_session_data(user_id):
    sessions = []
    for _ in range(200):  # Zmiana na 200 sesji treningowych dla każdego użytkownika
        exercises = []
        for _ in range(1,7):  # Losowa liczba ćwiczeń w sesji
            sets = random.randint(1, 5)  # Losowa liczba serii
            reps = random.randint(5, 15)  # Losowa liczba powtórzeń
            weight = random.randint(20, 100)  # Losowa waga
            date = datetime.now() - timedelta(days=random.randint(0, 365))  # Losowa data w ciągu ostatniego roku
            date_str = date.strftime("%Y-%m-%d")
            exercises.append({
                "date": date_str,
                "sets": sets,
                "reps": reps,
                "weight": weight
            })
        sessions.append(exercises)
    return sessions

# Dodawanie danych sesji treningowych do Redis
for user_id in range(1, 1001):
    session_data = generate_session_data(user_id)
    for i, session in enumerate(session_data):
        session_key = f"session:{user_id}:{i+1}"  # Unikalny klucz sesji
        for j, exercise in enumerate(session):
            r.hmset(f"{session_key}:exercise:{j+1}", exercise)
    if user_id % 10 == 0:
        print(user_id)

print("Dane sesji treningowych zostały dodane do Redis.")
