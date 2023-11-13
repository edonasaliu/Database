-- Scenario 1: Retrieve all workouts for a specific user
SELECT * FROM Workouts WHERE user_id = 1;

-- Scenario 2: Calculate the average calories consumed per day for a user
SELECT AVG(total_calories) AS average_daily_calories FROM NutritionLogs WHERE user_id = 1;

-- Scenario 3: Find the total duration of sleep for a user over the last week
SELECT SUM(duration) AS total_sleep_last_week FROM SleepRecords
WHERE user_id = 1 AND date >= date('now', '-7 days');

-- Scenario 4: List all users who have not met their weight goal according to the latest health metrics
SELECT u.user_id, u.name, u.weight_goal, hm.weight AS latest_weight
FROM Users u
JOIN (
    SELECT user_id, weight, MAX(date) AS latest_date
    FROM HealthMetrics
    GROUP BY user_id
) hm ON u.user_id = hm.user_id
WHERE hm.weight > u.weight_goal;

-- Scenario 5: Get the top 3 most frequent workout types for a user
SELECT type, COUNT(*) AS frequency
FROM Workouts
WHERE user_id = 1
GROUP BY type
ORDER BY frequency DESC
LIMIT 3;

-- Scenario 6: Retrieve last month's nutrition logs for a user
SELECT * FROM NutritionLogs
WHERE user_id = 1 AND date BETWEEN date('now', 'start of month', '-1 month') AND date('now', 'start of month', '-1 day');

-- Scenario 7: Find users with an average sleep duration less than 7 hours in the past month
SELECT user_id, AVG(duration) AS avg_sleep_duration
FROM SleepRecords
WHERE date BETWEEN date('now', 'start of month', '-1 month') AND date('now', 'start of month', '-1 day')
GROUP BY user_id
HAVING avg_sleep_duration < 420; -- 7 hours * 60 minutes

-- Scenario 8: List workouts and corresponding exercises for a user on a specific date
SELECT w.date, w.type, e.name, e.sets, e.reps
FROM Workouts w
JOIN Exercises e ON w.workout_id = e.workout_id
WHERE w.user_id = 1 AND w.date = '2023-01-01';

-- Scenario 9: Calculate the total protein intake for a user on a specific day
SELECT SUM(m.protein) AS total_protein
FROM NutritionLogs n
JOIN Meals m ON n.log_id = m.log_id
WHERE n.user_id = 1 AND n.date = '2023-01-01';

-- Scenario 10: Identify users who have consistently worked out more than 3 times a week for the past month
SELECT user_id, COUNT(*) AS workout_count
FROM Workouts
WHERE date BETWEEN date('now', 'start of month', '-1 month') AND date('now', 'start of month', '-1 day')
GROUP BY user_id
HAVING workout_count >= 12; -- 3 times a week * 4 weeks