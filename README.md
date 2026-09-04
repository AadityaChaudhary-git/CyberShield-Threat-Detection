# CyberShield Threat Detection

MCA major group project for network threat detection using Machine Learning, SQL and a Flask web application.

**Workflow:** Network Logs → Feature Engineering → ML Model → Threat Prediction → Security Alert

## Run
```bash
pip install -r requirements.txt
python src/generate_data.py
python src/train_model.py
python app.py
```
Open `http://127.0.0.1:5000`.

> The included dataset is synthetic and intended for academic demonstration.
