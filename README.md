# Flask Word Manager

This project provides a Flask-based API for managing words in a database. It includes two API endpoints: one for inserting a word into the database and another for fetching the word from the database. Additionally, there is a website endpoint with an admin portal form that allows updating the word in the database.

## Installation

1. Clone the repository:

```bash
   git clone <repository_url>
```

2. Change into the project directory:

```bash
   cd flask-word-manager
```

3. Create a virtual environment:

```bash
   python3 -m venv venv
```

4. Activate the virtual environment:

```bash
   # For Linux/Mac
source venv/bin/activate

# For Windows
venv\Scripts\activate

```

5. Install the dependencies:

```bash
   pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root directory.

2. Add the following environment variables to the `.env` file:


```makefile
DB_HOST = 
DB_PORT = 
DB_USER = 
DB_PASSWORD = 
DB_NAME = 
TABLE_NAME = 
```

### Setting Up MySQL Database

If you need to set up a MySQL database for this project, you can use the included docker-compose file to quickly create a MySQL instance. Follow the steps below:

1. Make sure you have Docker installed on your machine.

2. Open a terminal or command prompt and navigate to the project's root directory.

3. Run the following command to start the MySQL container:

```
docker-compose up -d
```

This command will pull the necessary Docker image and start a MySQL container running in the background.

4. The MySQL instance will be accessible at `localhost` with the default port `3306`. You can configure the connection parameters in your code or use a tool like phpMyAdmin or MySQL Workbench to interact with the database.

**Note:** By default, the docker-compose file sets up the MySQL container with the `root` user and `rootpassword` as the password. You can modify these values in the `docker-compose.yml` file if needed.

5. When you're finished with the MySQL instance, you can stop and remove the container by running:

```
docker-compose down
```


## Usage

To run the Flask application, execute the following command:

```bash
flask run
```


The code block above represents the command to run the Flask application, and the URL `http://localhost:8000/` specifies the location where the development server will be accessible.


## API Endpoints

### Insert a Word

- **Endpoint:** `/api/insert-word`
- **Method:** POST
- **Parameters:**
  - `word` (string): The word to be inserted into the database.
- **Example:**

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"word": "example"}' http://localhost:8000/api/insert-word
  ```


### Fetch the Word

- **Endpoint:** `/api/get-word`
- **Method:** GET
- **Example:**

  ```bash
  curl http://localhost:8000/api/get-word
```

## Website Endpoint

### Admin Portal

- **URL:** `http://localhost:8000/admin`
- **Description:** This endpoint provides a form for updating the word in the database.

  Visit `http://localhost:8000/admin` in a web browser and fill out the form to update the word.


## License

This project is licensed under the [MIT License](LICENSE).
