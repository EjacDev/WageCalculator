import argparse
from app.run import Main

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Wage calculator for employees schedule")
    parser.add_argument('--filename', '-f', type=str, default="data.txt", help="Name of the file containig schedule data")
    args = parser.parse_args()
    main = Main(args.filename)
    main.load_file()
    main.calculate_all_schedules()
    main.print_total()





