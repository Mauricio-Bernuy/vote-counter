# my_path = "D:\Folder1\SampleDir\\" ##Where your csv files are - all files there should be csv only
# for my_path in pathlist:
    # for filename in os.listdir(my_path):
    #     df = pd.read_csv(os.path.join(my_path, filename)) #Read each file
    #     df.to_excel(os.path.join(currdir, my_path, filename.split(".")[0]+".xlsx"), index=False) #Write to xlsx in locl dir


import os
import pandas as pd
from time import sleep, perf_counter
from threading import Thread

# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

def task(pathlist,currdir):
    for my_path in pathlist:
        print(f'Starting path {my_path}')
        for filename in os.listdir(my_path):
            print(f'Starting {my_path}/{filename}')
            df = pd.read_csv(os.path.join(currdir, my_path, filename)) #Read each file
            if not os.path.exists(os.path.join(currdir, my_path + '_xlsx')):
                os.mkdir(os.path.join(currdir, my_path + '_xlsx'))
            df.to_excel(os.path.join(currdir, my_path + '_xlsx', filename.split(".")[0]+".xlsx"), index=False) 
        print(f'Path {my_path} completed')

start_time = perf_counter()

# create and start 10 threads
threads = []

pathlist = next(os.walk('./'))[1]
pathlist = [x for x in pathlist if len(x) == 2]
pathchunks = list(divide_chunks(pathlist, 2))
print(pathchunks)
currdir = os.getcwd()
for chunk in pathchunks: 
    task(chunk, currdir)
    # t = Thread(target=task, args=(chunk,currdir,))
    # threads.append(t)
    # t.start()

# wait for the threads to complete
# for t in threads:
#     t.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')