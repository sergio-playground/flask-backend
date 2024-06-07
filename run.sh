if [ ! -d "./env" ]; then
    python3.11 -m venv ./env
fi

source env/bin/activate
pip install -r requirements.txt

python3 main.py