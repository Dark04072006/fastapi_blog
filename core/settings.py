import os
import dotenv

dotenv.load_dotenv()


SECRET_KEY = os.getenv('SECRET_KEY')

DATABASE = {
    'url': os.getenv('DB_URL')
}
