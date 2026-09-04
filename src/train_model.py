from pathlib import Path
import pandas as pd,joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,roc_auc_score,classification_report
root=Path(__file__).resolve().parents[1]; df=pd.read_csv(root/'data/network_logs.csv')
features=['protocol','src_bytes','dst_bytes','duration','src_packets','dst_packets','dst_port','failed_connections','login_attempts','connection_rate']
X=df[features]; y=df.label.map({'Normal':0,'Suspicious':1})
pre=ColumnTransformer([('cat',OneHotEncoder(handle_unknown='ignore'),['protocol']),('num',StandardScaler(),features[1:])])
pipe=Pipeline([('preprocess',pre),('model',RandomForestClassifier(n_estimators=250,class_weight='balanced',random_state=42))])
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,stratify=y,random_state=42); pipe.fit(Xtr,ytr)
p=pipe.predict(Xte); pr=pipe.predict_proba(Xte)[:,1]
print('Accuracy:',round(accuracy_score(yte,p),4)); print('ROC-AUC:',round(roc_auc_score(yte,pr),4)); print(classification_report(yte,p))
(root/'models').mkdir(exist_ok=True); joblib.dump(pipe,root/'models/threat_detector.joblib')
