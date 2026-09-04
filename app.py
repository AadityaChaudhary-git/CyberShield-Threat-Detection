from pathlib import Path
import joblib,pandas as pd
from flask import Flask,render_template,request,jsonify
root=Path(__file__).resolve().parent; model=joblib.load(root/'models/threat_detector.joblib'); data=pd.read_csv(root/'data/network_logs.csv')
app=Flask(__name__); FEATURES=['protocol','src_bytes','dst_bytes','duration','src_packets','dst_packets','dst_port','failed_connections','login_attempts','connection_rate']
@app.route('/')
def home():
 return render_template('index.html',total=len(data),suspicious=int((data.label=='Suspicious').sum()),normal=int((data.label=='Normal').sum()),recent=data.tail(12).to_dict('records'))
@app.route('/predict',methods=['POST'])
def predict():
 x=request.get_json(); row=pd.DataFrame([x])[FEATURES]; prob=float(model.predict_proba(row)[0,1]); return jsonify(prediction='Suspicious' if prob>=.5 else 'Normal',risk_score=round(prob*100,2))
if __name__=='__main__': app.run(debug=True)
