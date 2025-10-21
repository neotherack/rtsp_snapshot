from flask import Flask, Response
import cv2
import time

app = Flask(__name__)

@app.route('/snapshot')
def snapshot():
    try:
        rtsp_url = "rtsp://192.168.1.12:554"
        cap = cv2.VideoCapture(rtsp_url)
        
        if not cap.isOpened():
            return "Error: No se puede conectar a la cámara RTSP", 500
            
        success, frame = cap.read()
        cap.release()
        
        if not success:
            return "Error: No se pudo capturar imagen", 500
        
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            return "Error: No se pudo codificar imagen", 500

        return Response(buffer.tobytes(), mimetype='image/jpeg')
    
    except Exception as e:
        return f"Error: {str(e)}", 500

def generate_frames():
    rtsp_url = "rtsp://192.168.1.12:554"
    cap = cv2.VideoCapture(rtsp_url)
    
    try:
        while True:
            success, frame = cap.read()
            if not success:
                break
            
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
                
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
            
    finally:
        cap.release()

@app.route('/video')
def video():
    return Response(generate_frames(), 
                   mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8087)
