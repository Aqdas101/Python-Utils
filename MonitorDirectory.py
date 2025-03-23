from time import sleep 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class myHandler(FileSystemEventHandler):
    def on_created(self, event):

        src_path = event.src_path
        print(f'NEW FILE IS CREATED {src_path}')
        
        # perform operation on source file here

MONITOR_DIR = '.'    
observer = Observer()
event_handler = myHandler()
observer.schedule(event_handler, path=MONITOR_DIR, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
