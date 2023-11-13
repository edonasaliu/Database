from faker import Faker
import sqlite3
import random

fake = Faker()

# Connect to the SQLite database
conn = sqlite3.connect('HealthAndFitnessApp.db')
cursor = conn.cursor()

# Define the number of entries to create for each table
num_users = 10
num_workouts_per_user = 5
num_exercises_per_workout = 4
num_logs_per_user = 5
num_meals_per_log = 3
num_records_per_user = 5
num_metrics_per_user = 5

# Inserting randomly generated data into the Users table
for _ in range(num_users):
    name = fake.name()
    age = random.randint(18, 65)
    gender = random.choice(['Male', 'Female', 'Other'])
    height = random.uniform(150.0, 200.0)
    weight_goal = random.uniform(50.0, 100.0)
    cursor.execute('INSERT INTO Users (name, age, gender, height, weight_goal) VALUES (?, ?, ?, ?, ?)',
                   (name, age, gender, height, weight_goal))

conn.commit()

# Fetching user_ids to use as foreign keys in other tables
user_ids = cursor.execute('SELECT user_id FROM Users').fetchall()
for user_id in user_ids:
    user_id = user_id[0]

    try:
        # Start a transaction for each user's data insertion
        conn.execute('BEGIN TRANSACTION;')

        # Inserting workout data for each user
        for _ in range(num_workouts_per_user):
            date = fake.date_between(start_date='-1y', end_date='today')
            duration = random.randint(20, 120)
            workout_type = random.choice(['Cardio', 'Strength', 'Flexibility', 'Balance'])
            cursor.execute('INSERT INTO Workouts (user_id, date, duration, type) VALUES (?, ?, ?, ?)',
                           (user_id, date, duration, workout_type))
            workout_id = cursor.lastrowid

            # Inserting exercise data for each workout
            for _ in range(num_exercises_per_workout):
                exercise_name = fake.word()
                sets = random.randint(1, 5)
                reps = random.randint(5, 15)
                cursor.execute('INSERT INTO Exercises (workout_id, name, sets, reps) VALUES (?, ?, ?, ?)',
                               (workout_id, exercise_name, sets, reps))

        # Inserting nutrition log data for each user
        for _ in range(num_logs_per_user):
            date = fake.date_between(start_date='-1y', end_date='today')
            total_calories = random.randint(1200, 3500)
            cursor.execute('INSERT INTO NutritionLogs (user_id, date, total_calories) VALUES (?, ?, ?)',
                           (user_id, date, total_calories))
            log_id = cursor.lastrowid

            # Inserting meal data for each nutrition log
            for _ in range(num_meals_per_log):
                meal_name = fake.word()
                calories = random.randint(100, 800)
                protein = random.uniform(10.0, 30.0)
                carbs = random.uniform(20.0, 100.0)
                fats = random.uniform(5.0, 50.0)
                cursor.execute('INSERT INTO Meals (log_id, name, calories, protein, carbs, fats) VALUES (?, ?, ?, ?, ?, ?)',
                               (log_id, meal_name, calories, protein, carbs, fats))

        # Inserting sleep record data for each user
        for _ in range(num_records_per_user):
            date = fake.date_between(start_date='-1y', end_date='today')
            duration = random.randint(300, 600)
            quality = random.choice(['Poor', 'Fair', 'Good', 'Excellent'])
            cursor.execute('INSERT INTO SleepRecords (user_id, date, duration, quality) VALUES (?, ?, ?, ?)',
                           (user_id, date, duration, quality))

        # Inserting health metric data for each user
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
        # Rollback the transaction in case of an error
        print(f"An error occurred: {e}")
        conn.rollback()

# Close the database connection
conn.close()
