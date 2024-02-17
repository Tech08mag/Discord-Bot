import inspect

def info(*msg):
    print(f"\033[92m[INFO]:\033[00m {''.join([str(m) for m in msg])}")

def error(err):
    # for line and fileinfo see: 
    # https://stackoverflow.com/questions/6810999/how-to-determine-file-function-and-line-number
    frame = inspect.stack()[1][0]
    info = inspect.getframeinfo(frame)
    print(f"\n\033[91m[ERROR]:\033[00m Error occurred in "
          f"line {info.lineno} from script {info.filename}"
          f"\n   -->  {err}")

def warn(msg: str):
    print(f"\033[93m[WARN]:\033[00m {msg}")