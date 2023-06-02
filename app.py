from flask import Flask, request, jsonify, render_template, abort, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
alarmId = 0

# 임시로 데이터를 저장할 리스트
alarm_data = []

@app.route('/')
def main():
    return render_template('main.html', alarm_data=alarm_data)

@app.route('/your-endpoint', methods=['GET', 'POST'])
def your_endpoint():
    global alarmId

    if request.method == 'GET':
        # GET 방식으로 요청이 들어왔을 
        idValue = alarmId
        nameValue = request.args.get('name')
        timeValue = request.args.get('time')

        try:
            # 받은 데이터를 alarm_data에 저장
            data = {
                'id': idValue,
                'name': nameValue,
                'time': timeValue,
            }
            alarm_data.append(data)
            alarmId += 1

            response_data = {'result': 'success', 'id': idValue, 'name': nameValue, 'time': timeValue}
            return jsonify(response_data)
        except Exception as e:
            traceback.print_exc()  # 오류 메시지 출력
            
            return jsonify({'result': 'error', 'message': str(e)}), 500
    else:
        return jsonify({'result': 'error', 'message': 'Invalid request method.'}), 400

@app.route('/read')
def read():
    return render_template('read.html', alarm_data=alarm_data)

if __name__ == '__main__':
    app.run()
    app.config['TEMPLATES_AUTO_RELOAD'] = True
