# Bash file should be located with the python files. this is probably fine
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit
echo "Executing in directory: $SCRIPT_DIR"

# Remove files to avoid conflicts
rm no_town_clean.csv
rm original_db.db

# Execute python files in order
python3 task1.py
python3 task2.py
python3 summary.py