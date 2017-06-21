from flask import Flask, render_template, jsonify, request, session
from datetime import datetime
from pytz import timezone
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'RWpPwNz1KPObtJYqgNa40HUKaufHWDayCKjRnxHqmE6Mq3xiWGa5gNYIQKHTtiihKvwP4T3TEFdYPK8wJor1J0g2NZuzp5lAH9xvjfSJZqtsuYLZDO0bNbR9SHf0tRAciwgq1rK9DmSZ24nL0OwlVxBtb2E3eoTVuE0WMSJXK6hRA6lceD0oGKLkxK5fb3soBHMCRZzK0eUAvDPWvjZWbIBlIh4QefMYs46Xf3pZOq9UkZqnJyH3hptubK8MvRM5'

@app.route('/')
def index():
    circuits = {
        1: {'id': 1, 'name': '南西', 'bgcolor': '#8C8'},
        2: {'id': 2, 'name': '喜沢', 'bgcolor': '#FAAC58'},
        3: {'id': 3, 'name': '川岸', 'bgcolor': '#F5A9A9'},
        4: {'id': 4, 'name': '西',   'bgcolor': '#2E64FE'},
        5: {'id': 5, 'name': '美笹', 'bgcolor': '#F5A9F2'},
    }
    time_tables = {
        1: {
        	 1: {"id": 1, 'arrived_at': '00', 'station': '0 下笹目'},
        	 2: {"id": 2, 'arrived_at': '01', 'station': '1 下町橋'},
        	 3: {"id": 3, 'arrived_at': '02', 'station': '2 笹目公園'},
        	 4: {"id": 4, 'arrived_at': '03', 'station': '3 笹目七丁目'},
        	 5: {"id": 5, 'arrived_at': '04', 'station': '4 早瀬公園'},
        	 5: {"id": 5, 'arrived_at': '04', 'station': '5 早瀬二丁目'},
        	 6: {"id": 6, 'arrived_at': '05', 'station': '6 早瀬会館'},
        	 8: {"id": 8, 'arrived_at': '11', 'station': '7 戸田公園大橋'},
        	 9: {"id": 9, 'arrived_at': '12', 'station': '8 下町さくら西ひろば'},
        	10: {"id":10, 'arrived_at': '13', 'station': '9 金森橋'},
        	11: {"id":11, 'arrived_at': '14', 'station': '10 新曽南三丁目'},
        	12: {"id":12, 'arrived_at': '15', 'station': '11 南町'},
        	13: {"id":13, 'arrived_at': '16', 'station': '12 上戸田南保育園'},
        	14: {"id":14, 'arrived_at': '18', 'station': '13 戸田公園駅西口'},
        	15: {"id":15, 'arrived_at': '27', 'station': '14 本町五丁目'},
        	16: {"id":16, 'arrived_at': '28', 'station': '15 ボートコース入口'},
        	17: {"id":17, 'arrived_at': '32', 'station': '16 県営戸田公園'},
        	18: {"id":18, 'arrived_at': '33', 'station': '17 旭ヶ丘'},
        	19: {"id":19, 'arrived_at': '34', 'station': '18 ボートコース入口'},
        	20: {"id":20, 'arrived_at': '36', 'station': '19 戸田公園駅南'},
        	21: {"id":21, 'arrived_at': '37', 'station': '20 上戸田南保育園'},
        	22: {"id":22, 'arrived_at': '38', 'station': '21 南町'},
        	23: {"id":23, 'arrived_at': '39', 'station': '22 新曽南三丁目'},
        	24: {"id":24, 'arrived_at': '40', 'station': '23 給食センター入り口'},
        	25: {"id":25, 'arrived_at': '41', 'station': '24 戸田公園大橋'},
        	26: {"id":26, 'arrived_at': '44', 'station': '25 笹目川排水機場'},
        	27: {"id":27, 'arrived_at': '46', 'station': '26 早瀬二丁目'},
        	28: {"id":28, 'arrived_at': '48', 'station': '27 聖橋'},
        },
        2: {
        	 1: {"id": 1, 'arrived_at': '40', 'station': '0 戸田公園駅西口'},
        	 2: {"id": 2, 'arrived_at': '41', 'station': '1 こどもの国'},
        	 3: {"id": 3, 'arrived_at': '42', 'station': '2 戸田中央総合病院'},
        	 4: {"id": 4, 'arrived_at': '43', 'station': '3 上戸田二丁目'},
        	 5: {"id": 5, 'arrived_at': '45', 'station': '4 戸田市役所南'},
        	 5: {"id": 5, 'arrived_at': '47', 'station': '5 上戸田稲荷'},
        	 6: {"id": 6, 'arrived_at': '49', 'station': '6 中島病院'},
        	 8: {"id": 8, 'arrived_at': '50', 'station': '7 戸田東中学校北'},
        	 9: {"id": 9, 'arrived_at': '51', 'station': '8 中町一丁目北'},
        	10: {"id":10, 'arrived_at': '52', 'station': '9 中町公園'},
        	11: {"id":11, 'arrived_at': '54', 'station': '10 カリン通り'},
        	12: {"id":12, 'arrived_at': '55', 'station': '11 とだ小林医院'},
        	13: {"id":13, 'arrived_at': '56', 'station': '12 喜沢一丁目'},
        	14: {"id":14, 'arrived_at': '57', 'station': '13 喜沢記念会館'},
        	15: {"id":15, 'arrived_at': '58', 'station': '14 喜沢小学校南'},
        	16: {"id":16, 'arrived_at': '59', 'station': '15 アリスの広場東'},
        	17: {"id":17, 'arrived_at': '32', 'station': '16 喜沢橋'},
        	18: {"id":18, 'arrived_at': '33', 'station': '17 喜沢南一丁目'},
        	19: {"id":19, 'arrived_at': '34', 'station': '18 喜沢中学校'},
        	20: {"id":20, 'arrived_at': '36', 'station': '19 喜沢南二丁目'},
        	21: {"id":21, 'arrived_at': '37', 'station': '20 中町多目的広場'},
        	22: {"id":22, 'arrived_at': '38', 'station': '21 こぶし公園前'},
        	23: {"id":23, 'arrived_at': '39', 'station': '22 障害者福祉会館北'},
        	24: {"id":24, 'arrived_at': '40', 'station': '23 戸田南小学校南'},
        	25: {"id":25, 'arrived_at': '41', 'station': '24 戸田公園駅西口'},
        }
    }
    defaults = {
        'circuit_id':    1,     # 循環ID
        'station_id':    12,    # 停留所ID
        'exclude_hours': {16},  # 排除時間 (2017年6月現在 16時台は運行していない)
        'start_hour':    8,     # 開始時間
        'final_hour':    19,    # 最終時間
    }

    circuit_id    = session.get('circuit_id', defaults['circuit_id'])
    session['circuit_id'] = circuit_id
    circuit_flickity_index = list(circuits.keys()).index(circuit_id)
    logging.warning(circuit_flickity_index)
    station_id    = session.get('station_id', defaults['station_id'])
    exclude_hours = defaults['exclude_hours']
    start_hour    = defaults['start_hour']
    final_hour    = defaults['final_hour']

    arrived_at = time_tables[circuit_id][station_id]['arrived_at']
    arrived_at = int(arrived_at)

    current_datetime = datetime.now(timezone('Asia/Tokyo'))
    current_year  = current_datetime.year
    current_month = current_datetime.month
    current_day   = current_datetime.day
    current_hour  = int(current_datetime.hour)
    current_min   = int(current_datetime.minute)

    next_hour = current_hour if current_min < arrived_at else current_hour + 1
    if next_hour in exclude_hours:
        next_hour = next_hour + 1

    # 次回候補が 開始時間よりも前の場合、開始時間に設定
    if next_hour < start_hour:
        next_hour = start_hour

    # 次にバスがくる時刻
    next_time_tables = []
    for i in range(next_hour, final_hour-1):
        if i in exclude_hours:
            continue
        d = datetime(
            current_year,
            current_month,
            current_day,
            i,
            arrived_at,
            0
        ).strftime('%Y-%m-%d %H:%M:%S')
        next_time_tables.append(d)

    return render_template(
        "index.html",
        circuits=circuits,
        circuit_flickity_index=circuit_flickity_index,
        time_tables=time_tables,
        defaults=defaults,
        circuit_id=circuit_id,
        station_id=station_id,
        next_time_tables=next_time_tables
    )

@app.route('/circuit', methods=['POST'])
def set_circuit():
    # get circuit_id from post data.
    circuit_id = request.json['circuit_id']
    # save circuit_id to session.
    session['circuit_id'] = circuit_id
    # variable for api response
    r = {
        "circuit_id": circuit_id
    }
    # jsonify
    res = jsonify(r)
    res.status_code = 200
    return res

@app.route('/station', methods=['POST'])
def set_station():
    station_id = request.json['station_id']
    session['station_id'] = station_id
    r = {
        "station_id": station_id
    }
    res = jsonify(r)
    res.status_code = 200
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0')
