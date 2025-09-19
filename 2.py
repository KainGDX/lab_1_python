import re

log_text = """
2023-10-15 12:30:45 User ADMIN logged in from 192.168.1.1
2023-10-15 12:31:02 ERROR: Connection failed from 10.0.0.5
2023-10-15 12:32:15 User TESTER accessed system from 172.16.0.8
Contact support at help@example.com or admin@company.org
"""

#находим IPv4 адреса
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
ip_addresses = re.findall(ip_pattern, log_text)
print("IP адреса:", ip_addresses)

#находим временные метки
time_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
timestamps = re.findall(time_pattern, log_text)
print("Временные метки:", timestamps)

#находим слова в UPPERCASE
uppercase_pattern = r'\b[A-Z]{2,}\b'
uppercase_words = re.findall(uppercase_pattern, log_text)
print("UPPERCASE слова:", uppercase_words)

#заменяем email адреса
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
protected_text = re.sub(email_pattern, '[EMAIL PROTECTED]', log_text)
print("Текст с защищенными email:")
print(protected_text)