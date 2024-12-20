schema.md

---

# **Database Schema for "What's for Dinner" Application**

This document outlines the database schema for the "What's for Dinner" application. The schema is designed to store meals, their attributes, ingredients, and historical usage efficiently while allowing flexibility for future extensions.

---

## **1. Meals Table**

### **Purpose**
Stores the core details about each meal.

### **Schema**
| Column Name  | Type      | Description                            |
|--------------|-----------|----------------------------------------|
| meal_id      | INTEGER   | Unique identifier for each meal (Primary Key). |
| meal_name    | TEXT      | Name of the meal (Unique).             |
| cuisine      | TEXT      | Cuisine type (e.g., Italian, Mexican). |
| protein      | TEXT      | Protein type (e.g., Chicken, Beef).    |
| prep_time    | INTEGER   | Time in minutes for preparation.       |
| cook_time    | INTEGER   | Time in minutes for cooking.           |

### **SQL**
```sql
CREATE TABLE meals (
    meal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    meal_name TEXT NOT NULL UNIQUE,
    cuisine TEXT NOT NULL,
    protein TEXT NOT NULL,
    prep_time INTEGER NOT NULL,
    cook_time INTEGER NOT NULL
);
```

---

## **2. Meal Attributes Table**

### **Purpose**
Captures additional properties for meals, such as difficulty or dietary preferences, in a flexible format.

### **Schema**
| Column Name      | Type      | Description                                   |
|------------------|-----------|-----------------------------------------------|
| attribute_id     | INTEGER   | Unique identifier for each attribute (Primary Key). |
| meal_id          | INTEGER   | Links to the `meals` table (Foreign Key).     |
| attribute_name   | TEXT      | Name of the attribute (e.g., "Difficulty").   |
| attribute_value  | TEXT      | Value of the attribute (e.g., "Medium").      |
| attribute_type   | TEXT      | Optional: Groups attributes by type (e.g., Difficulty). |

### **SQL**
```sql
CREATE TABLE meal_attributes (
    attribute_id INTEGER PRIMARY KEY AUTOINCREMENT,
    meal_id INTEGER NOT NULL,
    attribute_name TEXT NOT NULL,
    attribute_value TEXT NOT NULL,
    attribute_type TEXT DEFAULT NULL,
    FOREIGN KEY (meal_id) REFERENCES meals(meal_id)
);
```

---

## **3. Meal Ingredients Tables**

### **Purpose**
Normalizes ingredients to avoid duplication and allows dynamic filtering based on ingredients.

### **Schema**
**`meal_ingredients` Table**
| Column Name     | Type      | Description                           |
|-----------------|-----------|---------------------------------------|
| ingredient_id   | INTEGER   | Unique identifier for each ingredient (Primary Key). |
| ingredient_name | TEXT      | Name of the ingredient (e.g., Tomato).|

**`meal_ingredients_link` Table**
| Column Name     | Type      | Description                           |
|-----------------|-----------|---------------------------------------|
| meal_id         | INTEGER   | Links to the `meals` table (Foreign Key). |
| ingredient_id   | INTEGER   | Links to the `meal_ingredients` table (Foreign Key).|

### **SQL**
**`meal_ingredients` Table**
```sql
CREATE TABLE meal_ingredients (
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_name TEXT NOT NULL UNIQUE
);
```

**`meal_ingredients_link` Table**
```sql
CREATE TABLE meal_ingredients_link (
    meal_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    FOREIGN KEY (meal_id) REFERENCES meals(meal_id),
    FOREIGN KEY (ingredient_id) REFERENCES meal_ingredients(ingredient_id),
    PRIMARY KEY (meal_id, ingredient_id)
);
```

---

## **4. Meal History Table**

### **Purpose**
Tracks when meals were used and includes optional user feedback.

### **Schema**
| Column Name  | Type      | Description                              |
|--------------|-----------|------------------------------------------|
| history_id   | INTEGER   | Unique identifier for each history entry (Primary Key). |
| meal_id      | INTEGER   | Links to the `meals` table (Foreign Key). |
| used_date    | DATE      | Date the meal was used.                  |
| notes        | TEXT      | Optional user feedback or notes.         |

### **SQL**
```sql
CREATE TABLE meal_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    meal_id INTEGER NOT NULL,
    used_date DATE NOT NULL,
    notes TEXT,
    FOREIGN KEY (meal_id) REFERENCES meals(meal_id)
);
```

---

## **Relationships**

- **`meals` Table**:
  - Primary table containing core meal information.
  - Linked to:
    - `meal_attributes` via `meal_id`
    - `meal_ingredients_link` via `meal_id`
    - `meal_history` via `meal_id`

- **`meal_attributes` Table**:
  - Flexible attributes for meals, such as difficulty or dietary restrictions.

- **`meal_ingredients` and `meal_ingredients_link` Tables**:
  - Normalized structure for ingredients, avoiding duplication and enabling dynamic queries.

- **`meal_history` Table**:
  - Tracks when meals were used and allows for user feedback.

---

## **Example Queries**

### 1. Retrieve Meals by Cuisine and Protein
```sql
SELECT meal_name, prep_time, cook_time
FROM meals
WHERE cuisine = 'Italian' AND protein = 'Chicken';
```

### 2. List Ingredients for a Meal
```sql
SELECT ingredient_name
FROM meal_ingredients mi
JOIN meal_ingredients_link mil ON mi.ingredient_id = mil.ingredient_id
WHERE mil.meal_id = 1;
```

### 3. Get Recently Used Meals
```sql
SELECT meal_name, used_date, notes
FROM meal_history mh
JOIN meals m ON mh.meal_id = m.meal_id
WHERE mh.used_date > DATE('now', '-21 days');
```

---

This schema is designed to be efficient, scalable, and adaptable to future features. If you have further questions or need adjustments, feel free to reach out!