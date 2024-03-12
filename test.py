import pandas as pd
import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier
import os
os.chdir('/CK_IOT')
label_map = {'Backdoor_Malware': 1, 'BenignTraffic': 2, 'BrowserHijacking': 3, 'CommandInjection': 4, 'DDoS-ACK_Fragmentation': 5, 'DDoS-HTTP_Flood': 6, 'DDoS-ICMP_Flood': 7, 'DDoS-ICMP_Fragmentation': 8, 'DDoS-PSHACK_Flood': 9, 'DDoS-RSTFINFlood': 10, 'DDoS-SYN_Flood': 11, 'DDoS-SlowLoris': 12, 'DDoS-SynonymousIP_Flood': 13, 'DDoS-TCP_Flood': 14, 'DDoS-UDP_Flood': 15, 'DDoS-UDP_Fragmentation': 16, 'DNS_Spoofing': 17, 'DictionaryBruteForce': 18, 'DoS-HTTP_Flood': 19, 'DoS-SYN_Flood': 20, 'DoS-TCP_Flood': 21, 'DoS-UDP_Flood': 22, 'MITM-ArpSpoofing': 23, 'Mirai-greeth_flood': 24, 'Mirai-greip_flood': 25, 'Mirai-udpplain': 26, 'Recon-HostDiscovery': 27, 'Recon-OSScan': 28, 'Recon-PingSweep': 29, 'Recon-PortScan': 30, 'SqlInjection': 31, 'Uploading_Attack': 32, 'VulnerabilityScan': 33, 'XSS': 34}
top_n_attributes = ['Protocol Type',
 'UDP',
 'Min',
 'Magnitue',
 'AVG',
 'Tot size',
 'Tot sum',
 'Header_Length',
 'flow_duration',
 'syn_flag_number',
 'Rate',
 'Srate',
 'SSH',
 'syn_count',
 'ARP',
 'DNS',
 'DHCP',
 'cwr_flag_number',
 'ece_flag_number',
 'Drate',
 'Weight',
 'Number',
 'IAT',
 'urg_count',
 'Max',
 'IPv',
 'LLC',
 'HTTP',
 'Variance',
 'Duration',
 'Covariance',
 'rst_count',
 'HTTPS',
 'TCP',
 'Radius',
 'Std',
 'fin_count',
 'rst_flag_number',
 'ack_count',
 'fin_flag_number',
 'psh_flag_number',
 'ack_flag_number',
 'ICMP',
 'Telnet',
 'SMTP',
 'IRC']
datatest = pd.read_csv("test.csv")
test = datatest[top_n_attributes]
# load
with open('model.pkl', 'rb') as f:
    clf2 = pickle.load(f)
new_pred = clf2.predict(test)
value = {
    'true_label' : datatest['label'],
    'actual_label' : datatest['label'].map(label_map),
    'predicted_label' : new_pred,
}

compare = pd.DataFrame(value)
print(compare.head(40))