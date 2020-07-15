# UCSI Sanity Check Dashboard

### How to install dependencies and run the project on Windows localhost

Prerequisite dependencies: Python v3.7+ , Nodejs 6.0+ , Npm 3.0+ 
Check confluence UCSI Automation documentation for more details.
This project uses Django 3.0.4 and Vue 2.5.2

- Navigate to any desired path in your command line and create a new directory using `mkdir <name of folder>`
- Pull the project files into this directory and navigate to the project root (Check confluence for more GitLab documentation)
- Create a new python virtual environment using
    ``` 
    python -m venv \venv 
    ```

- Activate your environment 
     ```
    \venv\scripts\activate.bat
    ```
- Install backend dependencies through the Bell proxy 
     ```
    pip install --proxy=http://fastweb.int.bell.ca:8083 -r requirements.txt
     ```
- Install backend dependencies without proxy 
     ```
    pip install -r requirements.txt
     ```
- Navigate to the frontend `cd djangovue/frontend`
- Configure npm settings if behind a proxy:
     ```
    npm config set strict-ssl false
     ```
     ```
     npm config set registry http://registry.npmjs.org
     ```
     ```
     npm config set proxy http://fastweb.int.bell.ca:8083
     ```
- Install frontend dependencies `npm install`

##### Note
- You do not need to migrate as the database is read-only.
- If you encounter proxy issues to install backend dependencies, create a configuration file for pip.

##### Running the Project
- Activate virtual environment 
     ```
    \venv\scripts\activate.bat
     ```
- In the project root directory run the backend server 
     ```
    python manage.py runserver
     ```
- In another console navigate to project root then  
     ```
    cd djangovue/frontend
     ```
- Run the frontend 
     ```
    npm run dev
     ```

##### Testing
- In the project root directory run unit tests 
     ```
    python manage.py test
     ```
- In another console navigate to project root then   
     ```
    cd djangovue/frontend
     ```
- Run cypress UI 
    ```
    npx cypress open
     ```
- Or run cypress tests 
     ```
    npx cypress run
     ```

##### Documentation
- Confluence link: https://confluence.wnst.int.bell.ca/display/I3A/Service+Monitoring+Dashboard

##### Project Authors
- Karl-Joey Chami
- Hassan Mansour



