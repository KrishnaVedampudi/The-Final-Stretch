from flask import Flask, render_template

from paho.mqtt import client as mqtt_client

app = Flask(__name__)

broker = "broker.emqx.io"
port = 1883
topic = "topicName/iot"

client_id = 'test'
username = 'emqx'
password = ''

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main', methods=['POST'])
def main():
    return render_template('main.html')

def on(number):
    client = connect_mqtt()
    client.loop_start()
    send_data(client, number)

@app.route('/1', methods=['POST'])
def release():
    on(1)
    return render_template('1.html')

@app.route('/2', methods=['POST'])
def test():
    on(2)
    return render_template('2.html')

@app.route('/3', methods=['POST'])
def activate():
    on(3)
    return render_template('3.html')

@app.route('/4', methods=['POST'])
def ignite():
    on(4)
    return render_template('4.html')

@app.route('/5', methods=['POST'])
def vent():
    on(5)
    return render_template('5.html')

@app.route('/6', methods=['POST'])
def srb():
    on(6)
    return render_template('6.html')

def send_data(client,number):
    msg=str(number)
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print("Send `{msg}` to topic `{topic}`")

if __name__ == "__main__":
    app.run(port=5001)