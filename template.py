import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name= 'AI_agent'

List_of_files=[
    '.github/workflows/.gitkeep',
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/main.py",
    f"src/{project_name}/config.py",
    f"src/{project_name}/prompts/",
    f"src/{project_name}/prompts/main_prompt.txt",
    f"src/{project_name}/tools/__init__.py",
    f"src/{project_name}/tools/get_afcon_matches.py",
    f"src/{project_name}/tools/check_city_airports.py",
    f"src/{project_name}/tools/get_hotels_or_distance.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/logging_config.py",
    f"src/{project_name}/utils/api_client.py",
    f"src{project_name}/agent.py",
    'tests/test_agent.py',
    'setup.py',
    "requirements.txt",
    ".env"


]

for filepath in List_of_files:
    filepath= Path(filepath)
    filedir, filename= os.path.split(filepath)


    if filedir !='':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            logging.info(f"creating empty file : {filepath}")

    else:
        logging.info(f"{filename} already exists")