-- Users Table
-- Stores basic user information, essential for personalizing the app experience.
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    height REAL,
    weight_goal REAL
);

-- Workouts Table
-- Tracks user workouts, including type and duration, linked to Users via user_id.
CREATE TABLE IF NOT EXISTS Workouts (
    workout_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    date DATE,
    duration INTEGER, -- in minutes
    type TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Exercises Table
-- Details specific exercises within a workout, linked to Workouts via workout_id.
CREATE TABLE IF NOT EXISTS Exercises (
    exercise_id INTEGER PRIMARY KEY,
    workout_id INTEGER,
    name TEXT,
    sets INTEGER,
    reps INTEGER,
    FOREIGN KEY (workout_id) REFERENCES Workouts(workout_id)
);

-- Nutrition Logs Table
-- Logs daily nutritional intake of users, linked to Users via user_id.
CREATE TABLE IF NOT EXISTS NutritionLogs (
    log_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    date DATE,
    total_calories INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Meals Table
-- Records specific meal details within a nutrition log, linked to NutritionLogs via log_id.
CREATE TABLE IF NOT EXISTS Meals (
    meal_id INTEGER PRIMARY KEY,
    log_id INTEGER,
    name TEXT,
    calories INTEGER,
    protein REAL,
    carbs REAL,
    fats REAL,
    FOREIGN KEY (log_id) REFERENCES NutritionLogs(log_id)
);

-- Sleep Records Table
-- Tracks user sleep patterns, including duration and quality, linked to Users via user_id.
CREATE TABLE IF NOT EXISTS SleepRecords (
    record_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    date DATE,
    duration INTEGER, -- in minutes
    quality TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Health Metrics Table
-- Records various health metrics like weight, BMI, heart rate, and blood pressure, linked to Users via user_id.
CREATE TABLE IF NOT EXISTS HealthMetrics (
    metric_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    date DATE,
    weight REAL,
    BMI REAL,
    heart_rate INTEGER,
    blood_pressure TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Add indexes to foreign key columns for faster joins
-- These indexes are created after all tables to improve the performance of queries involving joins.
CREATE INDEX idx_user_id_workouts ON Workouts(user_id);
CREATE INDEX idx_user_id_nutrition_logs ON NutritionLogs(user_id);
CREATE INDEX idx_log_id_meals ON Meals(log_id);
CREATE INDEX idx_user_id_sleep_records ON SleepRecords(user_id);
CREATE INDEX idx_user_id_health_metrics ON HealthMetrics(user_id);