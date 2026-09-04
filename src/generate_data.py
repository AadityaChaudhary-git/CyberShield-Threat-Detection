from pathlib import Path
import random,pandas as pd
random.seed(42); root=Path(__file__).resolve().parents[1]
rows=[]
for _ in range(3000):
 s=random.random()<.24; proto=random.choice(['TCP','UDP','HTTP','HTTPS','DNS'])
 if s:
  vals=[random.randint(3000,50000),random.randint(100,8000),random.randint(1,30),random.randint(80,500),random.randint(1,80),random.choice([21,22,23,25,445,3389,8080]),random.randint(3,20),random.randint(2,15),random.uniform(10,80)]
 else:
  vals=[random.randint(100,10000),random.randint(200,30000),random.randint(5,300),random.randint(1,100),random.randint(1,150),random.choice([53,80,443,8080]),random.randint(0,2),random.randint(0,2),random.uniform(.1,9)]
 rows.append([f'10.0.{random.randint(0,5)}.{random.randint(2,254)}',f'192.168.{random.randint(0,5)}.{random.randint(2,254)}',proto,*vals,'Suspicious' if s else 'Normal'])
cols=['src_ip','dst_ip','protocol','src_bytes','dst_bytes','duration','src_packets','dst_packets','dst_port','failed_connections','login_attempts','connection_rate','label']
pd.DataFrame(rows,columns=cols).to_csv(root/'data/network_logs.csv',index=False)
print('Generated',len(rows),'records')
