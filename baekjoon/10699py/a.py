from datetime import datetime
now = datetime.now()
print('%04d-%02d-%02d' %(now.year, now.month, now.day))
