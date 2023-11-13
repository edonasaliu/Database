import unittest
import sqlite3
from insert_data import num_users, num_workouts_per_user, num_exercises_per_workout, num_logs_per_user, num_meals_per_log, num_records_per_user, num_metrics_per_user

class TestInsertData(unittest.TestCase):
    def setUp(self):
        # Connect to the SQLite database
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

        # Create the tables
        self.cursor.execute('CREATE TABLE Users (user_id INTEGER PRIMARY KEY, name TEXT, age INTEGER, gender TEXT, height REAL, weight_goal REAL)')
        self.cursor.execute('CREATE TABLE Workouts (workout_id INTEGER PRIMARY KEY, user_id INTEGER, date TEXT, duration INTEGER, type TEXT)')
        self.cursor.execute('CREATE TABLE Exercises (exercise_id INTEGER PRIMARY KEY, workout_id INTEGER, name TEXT, sets INTEGER, reps INTEGER)')
        self.cursor.execute('CREATE TABLE NutritionLogs (log_id INTEGER PRIMARY KEY, user_id INTEGER, date TEXT, total_calories INTEGER)')
        self.cursor.execute('CREATE TABLE Meals (meal_id INTEGER PRIMARY KEY, log_id INTEGER, name TEXT, calories INTEGER, protein REAL, carbs REAL, fats REAL)')
        self.cursor.execute('CREATE TABLE SleepRecords (record_id INTEGER PRIMARY KEY, user_id INTEGER, date TEXT, duration INTEGER, quality TEXT)')
        self.cursor.execute('CREATE TABLE HealthMetrics (metric_id INTEGER PRIMARY KEY, user_id INTEGER, date TEXT, weight REAL, BMI REAL, heart_rate INTEGER, blood_pressure TEXT)')

    def tearDown(self):
        # Close the database connection
        self.conn.close()

    def test_insert_data(self):
        # Import the function to be tested
        from insert_data import fake, conn, cursor

        # Call the function to insert data into the database
        exec(open('insert_data.py').read())

        # Check that the correct number of entries were created for each table
        self.assertEqual(len(cursor.execute('SELECT * FROM Users').fetchall()), num_users)
        self.assertEqual(len(cursor.execute('SELECT * FROM Workouts').fetchall()), num_users * num_workouts_per_user)
        self.assertEqual(len(cursor.execute('SELECT * FROM Exercises').fetchall()), num_users * num_workouts_per_user * num_exercises_per_workout)
        self.assertEqual(len(cursor.execute('SELECT * FROM NutritionLogs').fetchall()), num_users * num_logs_per_user)
        self.assertEqual(len(cursor.execute('SELECT * FROM Meals').fetchall()), num_users * num_logs_per_user * num_meals_per_log)
        self.assertEqual(len(cursor.execute('SELECT * FROM SleepRecords').fetchall()), num_users * num_records_per_user)
        self.assertEqual(len(cursor.execute('SELECT * FROM HealthMetrics').fetchall()), num_users * num_metrics_per_user)

if __name__ == '__main__':
    unittest.main()