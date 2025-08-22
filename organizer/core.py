import os
import shutil
from collections import defaultdict

class FileOrganizer:
    def __init__(self, rules):
        self.rules = self._process_rules(rules)

    def _process_rules(self, rules):
        processed_rules = defaultdict(list)
        for category, extensions in rules.items():
            for ext in extensions:
                processed_rules[ext.lower().lstrip('.')].append(category)
        return processed_rules

    def organize_files(self, source_path, logger):
        if not os.path.isdir(source_path):
            logger.error(f"Source path does not exist or is not a directory: {source_path}")
            return

        logger.info(f"Starting file organization in: {source_path}")
        moved_files_count = 0

        for filename in os.listdir(source_path):
            file_path = os.path.join(source_path, filename)

            if os.path.isfile(file_path):
                _, file_extension = os.path.splitext(filename)
                file_extension = file_extension.lower().lstrip('.')

                destination_categories = self.rules.get(file_extension)

                if destination_categories:
                    # Use the first category found for simplicity, or implement more complex logic
                    destination_category = destination_categories[0]
                    destination_folder = os.path.join(source_path, destination_category)

                    os.makedirs(destination_folder, exist_ok=True)
                    destination_path = os.path.join(destination_folder, filename)

                    try:
                        shutil.move(file_path, destination_path)
                        logger.info(f"Moved: {filename} -> {destination_category}/")
                        moved_files_count += 1
                    except Exception as e:
                        logger.error(f"Error moving {filename}: {e}")
                else:
                    logger.debug(f"No rule for extension {file_extension}: {filename}")

        logger.info(f"Finished organizing files. Moved {moved_files_count} files.")
        return moved_files_count


