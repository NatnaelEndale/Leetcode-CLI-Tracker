import json
import argparse
from datetime import date

DATA_FILE = "tracker.json"

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent= 2)

def add_problem(problem):
    data = load_data()

    for p in data:
        if p["id"] == problem["id"]:
            print("❌ Problem already exists.")
            return

    data.append(problem)
    save_data(data)
    print("✅ Problem added successfully.")

def list_problems():
    data = load_data()

    if not data:
        print("No problems solved yet.")
        return

    for p in data:
        print(f'{p["id"]} | {p["title"]} | {p["difficulty"]} | {p["topic"]}')

def show_stats():
    data = load_data()

    if not data:
        print("No problems solved yet.")
        return

    stats = {
        "Easy": 0,
        "Medium": 0,
        "Hard": 0
    }

    for p in data:
        difficulty = p["difficulty"]
        if difficulty in stats:
            stats[difficulty] += 1

    print(f"Total solved: {len(data)}")
    for level, count in stats.items():
        print(f"{level}: {count}")

def main():
    parser = argparse.ArgumentParser(description="Leetcode Tracker")
    parser.add_argument("command", choices=["add", "list", "stats"])

    args = parser.parse_args()

    if args.command == "add":
        problem = {
            "id": int(input("Problem ID: ")),
            "title": input("Title: "),
            "difficulty": input("Difficulty (Easy/Medium/Hard): "),
            "topic": input("Topic: "),
            "time_spent": int(input("Time spent (minutes): ")),
            "date_solved": date.today().isoformat()
        }
        add_problem(problem)

    elif args.command == "list":
        list_problems()

    elif args.command == "stats":
        show_stats()

if __name__ == "__main__":
    main()

