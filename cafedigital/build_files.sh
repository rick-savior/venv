python3.9 -m venv venv
source venv/scripts/activate
pip install -r requirements.txt
python3.9 manage.py collectstatic
