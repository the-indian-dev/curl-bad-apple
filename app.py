from flask import Flask, Response, request
import time

app = Flask(__name__)

@app.route('/')
def bad_apple():
    def generate():
        i = 1
        while True:
            yield "\033[2J\033[H"
            frame_num = "{:0>4}".format(i)
            i = i + 1
            try:
                ascii_frame = open(f'ascii_frames/frame_{frame_num}.txt')
                yield ascii_frame.read()
                time.sleep(0.1)
            except:
                yield "END"
                break
    
    return Response(generate(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port='10000')
