SELECT COUNT(*) AS total_records FROM network_logs;
SELECT label, COUNT(*) AS records FROM network_logs GROUP BY label;
SELECT protocol, COUNT(*) AS total, SUM(CASE WHEN label='Suspicious' THEN 1 ELSE 0 END) AS suspicious FROM network_logs GROUP BY protocol ORDER BY suspicious DESC;
SELECT src_ip, COUNT(*) AS total_events, SUM(CASE WHEN label='Suspicious' THEN 1 ELSE 0 END) AS suspicious_events FROM network_logs GROUP BY src_ip HAVING suspicious_events>0 ORDER BY suspicious_events DESC;
SELECT dst_port, COUNT(*) AS suspicious_events FROM network_logs WHERE label='Suspicious' GROUP BY dst_port ORDER BY suspicious_events DESC LIMIT 10;
