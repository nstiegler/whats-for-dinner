# What's for Dinner App

A Python-based meal planning application that helps select weekly dinners using a database of Freshly meal cards.

## Project Overview

A Python-based meal planning application that helps you select weekly dinners using a database of Freshly meal cards. After two years of enjoying Freshly’s meal deliveries, my wife and I decided to save money by cooking at home. We kept the meal cards from those deliveries—complete with the ingredients and cooking instructions—and this app transforms that collection into a personalized tool to simplify meal planning.

### Purpose

This application aims to solve the common challenge of meal planning by:

- Managing a database of Freshly meal cards
- Providing automated meal suggestions for weekly dinner planning
- Tracking meal history to prevent frequent repetition
- Offering ingredient lists and cooking instructions when needed

## Features

### Core Features

- Freshly meals database
- Criteria-based meal selection
- Multiple meal suggestions based on user preferences
- Ingredient and cooking instruction display
- Meal usage history tracking

### Non-Core Features

- Meal difficulty level display
- Customizable selection criteria (cuisine type, protein, etc.)
- Configurable number of meal suggestions
- Random meal selection from filtered groups
- Option to request new suggestions

## Technical Specifications

### Architecture

The application follows a three-layer architecture:

- Presentation Layer (CLI initially, desktop GUI planned)
- Business Logic Layer (Meal services)
- Data Layer (SQLite database)

### Database Schema

```
meals
  - meal_id (PK)
  - meal_name
  - ingredients
  - instructions
  - prep_time
  - cook_time
  - created_date
  - is_active

meal_attributes
  - meal_id (FK)
  - attribute_name
  - value

meal_history
  - history_id (PK)
  - meal_id (FK)
  - used_date
  - notes
```

### Dependencies

- Python 3.x
- SQLite3
- Required Python packages:
  - sqlite3 (built-in)
  - datetime (built-in)
  - argparse (built-in)
  - random (built-in)

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/whats-for-dinner.git
cd whats-for-dinner
```

2. Set up a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Initialize the database:

```
python database.py --init
```

## Project Structure

```
WHATS-FOR-DINNER/
├── data/
│   ├── mock_data/   # Sample data for testing
│   ├── db_functions.py    # Database utility functions
│   ├── initialize_db.py   # Database initialization script
│   └── schema.md    # Database schema documentation
├── test/
│   └── view_db.py   # Database viewing utility for testing
├── .gitignore       # Git ignore file
├── database.py      # Core database operations
├── main.py          # Application entry point
├── README.md
├── requirements.md  # Project dependencies list
└── whats_for_dinner.db  # SQLite database file
```

## Development Roadmap

1. **MVP (Current Focus)**

   - Command Line Interface
   - Basic meal suggestion functionality
   - Core database operations

2. **Future Enhancements**
   - Desktop GUI application
   - Enhanced filtering capabilities
   - Meal rating system
   - Weekly meal plan export
   - Grocery list generation

## Contributing

This is a personal project, but suggestions and feedback are welcome. Please feel free to open an issue or contact the project owner with ideas.

## License

This project is for personal use only.

## Author

Created by Norman Stiegler for personal meal planning purposes.
