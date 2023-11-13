import unittest
import sqlite3

class TestCreateTables(unittest.TestCase):
    def setUp(self):
        # Connect to the SQLite database
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

        # Import the SQL script to create the tables
        with open('sql_scripts/create_tables.sql', 'r') as f:
            create_tables_sql = f.read()

        # Create the tables
        self.cursor.executescript(create_tables_sql)

    def tearDown(self):
        # Close the database connection
        self.conn.close()

    def test_users_table(self):
        # Check that the Users table was created with the correct columns
        self.assertEqual(self.cursor.execute('PRAGMA table_info(Users)').fetchall(), [(0, 'user_id', 'INTEGER', 0, None, 1), (1, 'name', 'TEXT', 1, None, 0), (2, 'age', 'INTEGER', 1, None, 0), (3, 'gender', 'TEXT', 1, None, 0), (4, 'height', 'REAL', 0, None, 0), (5, 'weight_goal', 'REAL', 0, None, 0)])

    def test_workouts_table(self):
        # Check that the Workouts table was created with the correct columns and foreign key
        self.assertEqual(self.cursor.execute('PRAGMA table_info(Workouts)').fetchall(), [(0, 'workout_id', 'INTEGER', 0, None, 1), (1, 'user_id', 'INTEGER', 0, None, 0), (2, 'date', 'DATE', 0, None, 0), (3, 'duration', 'INTEGER', 0, None, 0), (4, 'type', 'TEXT', 0, None, 0)])
        self.assertEqual(self.cursor.execute('PRAGMA foreign_key_list(Workouts)').fetchall(), [(0, 0, 'Users', 'user_id', 'user_id', 'NO ACTION', 'NO ACTION', 'NONE')])

    def test_exercises_table(self):
        # Check that the Exercises table was created with the correct columns and foreign key
        self.assertEqual(self.cursor.execute('PRAGMA table_info(Exercises)').fetchall(), [(0, 'exercise_id', 'INTEGER', 0, None, 1), (1, 'workout_id', 'INTEGER', 0, None, 0), (2, 'name', 'TEXT', 0, None, 0), (3, 'sets', 'INTEGER', 0, None, 0), (4, 'reps', 'INTEGER', 0, None, 0)])
        self.assertEqual(self.cursor.execute('PRAGMA foreign_key_list(Exercises)').fetchall(), [(0, 0, 'Workouts', 'workout_id', 'workout_id', 'NO ACTION', 'NO ACTION', 'NONE')])

    def test_nutrition_logs_table(self):
        # Check that the NutritionLogs table was created with the correct columns and foreign key
        self.assertEqual(self.cursor.execute('PRAGMA table_info(NutritionLogs)').fetchall(), [(0, 'log_id', 'INTEGER', 0, None, 1), (1, 'user_id', 'INTEGER', 0, None, 0), (2, 'date', 'DATE', 0, None, 0), (3, 'total_calories', 'INTEGER', 0, None, 0)])
        self.assertEqual(self.cursor.execute('PRAGMA foreign_key_list(NutritionLogs)').fetchall(), [(0, 0, 'Users', 'user_id', 'user_id', 'NO ACTION', 'NO ACTION', 'NONE')])

    def test_meals_table(self):
        # Check that the Meals table was created with the correct columns and foreign key
        self.assertEqual(self.cursor.execute('PRAGMA table_info(Meals)').fetchall(), [(0, 'meal_id', 'INTEGER', 0, None, 1), (1, 'log_id', 'INTEGER', 0, None, 0), (2, 'name', 'TEXT', 0, None, 0), (3, 'calories', 'INTEGER', 0, None, 0), (4, 'protein', 'REAL', 0, None, 0), (5, 'carbs', 'REAL', 0, None, 0), (6, 'fats', 'REAL', 0, None, 0)])
        self.assertEqual(self.cursor.execute('PRAGMA foreign_key_list(Meals)').fetchall(), [(0, 0, 'NutritionLogs', 'log_id', 'log_id', 'NO ACTION', 'NO ACTION', 'NONE')])

    def test_sleep_records_table(self):
        # Check that the SleepRecords table was created with the correct columns and foreign key
        self.assertEqual(self.cursor.execute('PRAGMA table_info(SleepRecords)').fetchall(), [(0, 'record_id', 'INTEGER', 0, None, 1), (1, 'user_id', 'INTEGER', 0, None, 0), (2, 'date', 'DATE', 0, None, 0), (3, 'duration', 'INTEGER', 0, None, 0), (4, 'quality', 'TEXT', 0, None, 0)])
        self.assertEqual(self.cursor.execute('PRAGMA foreign_key_list(SleepRecords)').fetchall(), [(0, 0, 'Users', 'user_id', 'user_id', 'NO ACTION', 'NO ACTION', 'NONE')])

    def test_health_metrics_table(self):
        # Check that the HealthMetrics table was created with the correct columns and foreign key
        self.assertEqual(self.cursor.execute('PRAGMA table_info(HealthMetrics)').fetchall(), [(0, 'metric_id', 'INTEGER', 0, None, 1), (1, 'user_id', 'INTEGER', 0, None, 0), (2, 'date', 'DATE', 0, None, 0), (3, 'weight', 'REAL', 0, None, 0), (4, 'BMI', 'REAL', 0, None, 0), (5, 'heart_rate', 'INTEGER', 0, None, 0), (6, 'blood_pressure', 'TEXT', 0, None, 0)])
        self.assertEqual(self.cursor.execute('PRAGMA foreign_key_list(HealthMetrics)').fetchall(), [(0, 0, 'Users', 'user_id', 'user_id', 'NO ACTION', 'NO ACTION', 'NONE')])

if __name__ == '__main__':
    unittest.main()