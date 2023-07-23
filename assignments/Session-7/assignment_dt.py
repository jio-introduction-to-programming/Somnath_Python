from datetime import *

# datetime to string
def datetime_to_str_1(dt):
    # Convert to format "2023-07-19"
    return (dt.strftime('%Y-%m-%d'))

def datetime_to_str_2(dt):
    # Convert to format "23-07-19"
    return (dt.strftime('%y-%m-%d'))

def datetime_to_str_3(dt):
    # Convert to format "July 19, 2023"
    return (dt.strftime('%B %d, %Y'))

def datetime_to_str_4(dt):
    # Convert to format "Jul 19, 2023"
    return (dt.strftime('%b %d, %Y'))

def datetime_to_str_5(dt):
    # Convert to format "19 July 2023"
    return (dt.strftime('%d %B %Y'))

def datetime_to_str_6(dt):
    # Convert to format "Wednesday July 19, 2023"
    return (dt.strftime('%A %B %d, %Y'))

def datetime_to_str_7(dt):
    # Convert to format "Wed July 19, 2023"
    return (dt.strftime('%a %B %d, %Y'))

def datetime_to_str_8(dt):
    # Convert to format "2023-07-19 10:30:45"
    return (dt.strftime('%Y-%m-%d %H:%M:%S'))

def datetime_to_str_9(dt):
    # Convert to format "10:30:45"
    return (dt.strftime('%H:%M:%S'))

def datetime_to_str_10(dt):
    # Convert to format "10:30 AM"
    return (dt.strftime('%H:%M %p'))

# string to datetime
def str_to_datetime_1(s):
    # Convert from format "2023-07-19"
    return (datetime.strptime(s, '%Y-%m-%d'))

def str_to_datetime_2(s):
    # Convert from format "23-07-19"
    return (datetime.strptime(s, '%y-%m-%d'))

def str_to_datetime_3(s):
    # Convert from format "July 19, 2023"
    return (datetime.strptime(s, '%B %d, %Y'))

def str_to_datetime_4(s):
    # Convert from format "Jul 19, 2023"
    return (datetime.strptime(s, '%b %d, %Y'))

def str_to_datetime_5(s):
    # Convert from format "19 July 2023"
    return (datetime.strptime(s, '%d %B %Y'))

def str_to_datetime_6(s):
    # Convert from format "Wednesday July 19, 2023"
    return (datetime.strptime(s, '%A %B %d, %Y'))

def str_to_datetime_7(s):
    # Convert from format "Wed July 19, 2023"
    return (datetime.strptime(s, '%a %B %d, %Y'))

def str_to_datetime_8(s):
    # Convert from format "2023-07-19 10:30:45"
    return (datetime.strptime(s, '%Y-%m-%d %H:%M:%S'))

def str_to_datetime_9(s):
    # Convert from format "10:30:45"
    return (datetime.strptime(s, '%H:%M:%S'))

def str_to_datetime_10(s):
    # Convert from format "10:30 AM"
    return (datetime.strptime(s, '%H:%M %p'))
