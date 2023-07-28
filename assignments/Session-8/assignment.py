
def persist_data(data, filename):
    # Use Python built-in functions to write 'data' to 'filename'
    file = open(filename, 'w')
    file.write(data)
    file.close()

def read_file(filename):
    # Use Python built-in functions to read contents of 'filename' and print them to screen
    file = open(filename, 'r')
    print(file.read())
    file.close()

def write_file(filename, data):
    # Use Python built-in functions to write 'data' to 'filename'
    file = open(filename, 'w')
    file.write(data)
    file.close()

def delete_file(filename):
    # Use Python built-in functions to delete 'filename'
    import os
    os.remove(filename)

def overwrite_file(filename, data):
    # Use Python built-in functions to write 'data' to 'filename'
    file = open(filename, 'w')
    file.write(data)
    file.close()

def append_file(filename, data):
    # Use Python built-in functions to append 'data' to 'filename'
    file = open(filename, 'a')
    file.write(data)
    file.close()

def write_binary_file(filename, data):
    # Use Python built-in functions to write 'data' as binary to 'filename'
    file = open(filename, 'wb')
    file.write(data)
    file.close()


def read_image_file(filename):
    # Use OpenCV to read 'filename' as an image
    import cv2
    img = cv2.imread(filename)
    cv2.imshow(img)
    return img

def read_csv_file(filename):
    # Use Pandas to read 'filename' as a csv
    import pandas as pd
    df = pd.read_csv(filename)
    print(df.head())
    return df

def write_csv_file(filename, df):
    # Use Pandas to write dataframe 'df' to 'filename'
    import pandas as pd
    df.to_csv(filename, index = False)

def read_json_file(filename):
    # Use json to read 'filename' as a json
    import json
    file = open(filename, 'r')
    data = json.load(file)
    return data

def write_json_file(filename, data):
    # Use json to write 'data' to 'filename'
    import json
    file = open(filename, 'w')
    data = json.dump(file)
    print(data)

def write_pickle_file(filename, data):
    # Use pickle to write 'data' to 'filename'
    import pickle
    file = open(filename, 'wb')
    pickle.dump(data,file)


def read_pickle_file(filename):
    # Use pickle to read 'filename'
    import pickle
    file = open(filename, 'rb')
    return pickle.load(file)
