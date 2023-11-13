-- Users Table
-- This table stores information about the users of the Health and Fitness Tracking App.
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT, -- A unique identifier for each user.
    name TEXT NOT NULL, -- The name of the user.
    age INTEGER, -- The age of the user.
    gender TEXT, -- The gender of the user.
    height REAL, -- The height of the user in centimeters.
    weight_goal REAL -- The weight goal of the user in kilograms.
);

-- Workouts Table
-- This table stores information about the workouts logged by users.
CREATE TABLE Workouts (
    workout_id INTEGER PRIMARY KEY AUTOINCREMENT, -- A unique identifier for each workout.
    user_id INTEGER, -- The identifier of the user who performed the workout.
    date DATE, -- The date when the workout was performed.
    duration INTEGER, -- The duration of the workout in minutes.
    type TEXT, -- The type of workout (e.g., Cardio, Strength, Flexibility, Balance).
    FOREIGN KEY (user_id) REFERENCES Users(user_id) -- A foreign key linking to the Users table.
);
