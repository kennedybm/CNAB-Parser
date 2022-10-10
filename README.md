# INSTRUCTIONS

Make sure to have installed pyhton 3.10 or above - [https://www.python.org/downloads/source/](https://www.python.org/downloads/source/)

also the package installer for python pip - [https://pypi.org/project/pip/](https://pypi.org/project/pip/)

---

- **After cloning the repository run this commands in order:**

  python -m venv venv --upgrade-deps

  source venv/bin/activate

  pip install -r requirements.txt

---

- **Project has two options to run localy, the default with Sqlite3 and Docker:**

  **1 - Sqlite3 :**

       ./manage.py migrate

       ./manage.py generate_types

       ./manage.py runserver

      Access on - [http://localhost:8000/upload/](http://localhost:8000/upload/) or in a diferent port

      At the root of the project theres a CNAB file, simply copy and upload

      To access routes documentation [http://localhost:8000/api/](http://localhost:8000/upload/)docs/

  **2 - Docker:**

      Set the variables on .env, following the instructions on .env.example

      In project_base/settings.py: comment out lines 87 through 92 and uncomment lines 87 to 92



      run: docker compose up or docker-compose up

      Access on - [http://localhost:8000/upload/](http://localhost:8000/upload/) or in a diferent port

      At the root of the project theres a CNAB file, simply copy and upload

      To access routes documentation [http://localhost:8000/api/](http://localhost:8000/upload/)docs/
