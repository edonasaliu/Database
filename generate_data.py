from faker import Faker
import sqlite3
import random

# Initialize Faker for generating fake data
fake = Faker()

# Connect to the SQLite database
conn = sqlite3.connect('HealthAndFitnessApp.db')
cursor = conn.cursor()

# Define the number of records to generate for each entity
num_users = 10
num_workouts_per_user = 5
num_exercises_per_workout = 4
num_logs_per_user = 5
num_meals_per_log = 3
num_records_per_user = 5
num_metrics_per_user = 5

try:
    # Generate data for each user
    for _ in range(num_users):
        # Start a new transaction for each user
        conn.execute('BEGIN TRANSACTION;')

        # Generate and insert user data
        name = fake.name()
        age = random.randint(18, 65)
        gender = random.choice(['Male', 'Female', 'Other'])
        height = random.uniform(150.0, 200.0)
        weight_goal = random.uniform(50.0, 100.0)
        cursor.execute('INSERT INTO Users (name, age, gender, height, weight_goal) VALUES (?, ?, ?, ?, ?)',
                       (name, age, gender, height, weight_goal))

        # Get the last inserted user_id
        user_id = cursor.lastrowid

        # Generate and insert workout data for each user
        for _ in range(num_workouts_per_user):
            date = fake.date_between(start_date='-1y', end_date='today')
            duration = random.randint(20, 120)
            workout_type = random.choice(['Cardio', 'Strength', 'Flexibility', 'Balance'])
            cursor.execute('INSERT INTO Workouts (user_id, date, duration, type) VALUES (?, ?, ?, ?)',
                           (user_id, date, duration, workout_type))
            workout_id = cursor.lastrowid

            # Generate and insert exercise data for each workout
            for _ in range(num_exercises_per_workout):
                exercise_name = fake.word()
                sets = random.randint(1, 5)
                reps = random.randint(5, 15)
                cursor.execute('INSERT INTO Exercises (workout_id, name, sets, reps) VALUES (?, ?, ?, ?)',
                               (workout_id, exercise_name, sets, reps))

        # Generate and insert nutrition log data for each user
        for _ in range(num_logs_per_user):
            date = fake.date_between(start_date='-1y', end_date='today')
            total_calories = random.randint(1200, 3500)
            cursor.execute('INSERT INTO NutritionLogs (user_id, date, total_calories) VALUES (?, ?, ?)',
                           (user_id, date, total_calories))
            log_id = cursor.lastrowid

            # Generate and insert meal data for each nutrition log
            for _ in range(num_meals_per_log):
                meal_name = fake.word()
                calories = random.randint(100, 800)
                protein = random.uniform(10.0, 30.0)
                carbs = random.uniform(20.0, 100.0)
                fats = random.uniform(5.0, 50.0)
                cursor.execute('INSERT INTO Meals (log_id, name, calories, protein, carbs, fats) VALUES (?, ?, ?, ?, ?, ?)',
                               (log_id, meal_name, calories, protein, carbs, fats))

        # Generate and insert sleep record data for each user
        for _ in range(num_records_per_user):
            date = fake.date_between(start_date='-1y', end_date='today')
            duration = random.randint(300, 600)
            quality = random.choice(['Poor', 'Fair', 'Good', 'Excellent'])
            cursor.execute('INSERT INTO SleepRecords (user_id, date, duration, quality) VALUES (?, ?, ?, ?)',
                           (user_id, date, duration, quality))

        # Generate and insert health metric data for each user
        for _ in range(num_metrics_per_user):
            date = fake.date_between(start_date='-1y', end_date='today')
            weight = random.uniform(50.0, 100.0)
            bmi = random.uniform(18.5, 30.0)
            heart_rate = random.randint(60, 100)
            blood_pressure = f"{random.randint(90, 140)}/{random.randint(60, 90)}"
            cursor.execute('INSERT INTO HealthMetrics (user_id, date, weight, BMI, heart_rate, blood_pressure) VALUES (?, ?, ?, ?, ?, ?)',
                           (user_id, date, weight, bmi, heart_rate, blood_pressure))

        # Commit the transaction after successfully inserting all data for a user
        conn.commit()

except sqlite3.Error as e:
    # Print any error that occurs and rollback the transaction
    print(f"An error occurred: {e}")
    conn.rollback()
finally:
    # Close the database connection
    conn.close()
