import argparse
import os
import time
import schedule
from organizer.core import FileOrganizer
from organizer.config import load_config
from organizer.logger import setup_logging

def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer")
    parser.add_argument("--path", type=str, default=os.path.expanduser("~/Downloads"),
                        help="Path to the directory to organize. Defaults to ~/Downloads.")
    parser.add_argument("--config", type=str, default=None,
                        help="Path to a custom configuration file (JSON or YAML). Defaults to built-in rules.")
    parser.add_argument("--interval", type=int, default=0,
                        help="Interval in minutes to automatically run the organizer. Set to 0 for a single run. Defaults to 0.")

    args = parser.parse_args()

    logger = setup_logging(log_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'file_organizer.log'))

    try:
        rules = load_config(args.config)
        organizer = FileOrganizer(rules)
    except (FileNotFoundError, ValueError) as e:
        logger.error(f"Configuration error: {e}")
        return

    def job():
        logger.info(f"Running file organization job for path: {args.path}")
        organizer.organize_files(args.path, logger)

    if args.interval > 0:
        logger.info(f"Scheduling file organization to run every {args.interval} minutes in {args.path}")
        schedule.every(args.interval).minutes.do(job)
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        logger.info(f"Performing a single file organization run for path: {args.path}")
        job()

if __name__ == "__main__":
    main()


