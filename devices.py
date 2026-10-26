import time
import json
import argparse
import paho.mqtt.client as mqtt

parser = argparse.ArgumentParser()
parser.add_argument('--scenario', type=str, default='normal')
args = parser.parse_args()

# Використовуємо стабільний публічний брокер EMQX
BROKER = "broker.emqx.io"
PORT = 1883
TOPIC_BASE = "my_house_variant3_test"

# Явно вказуємо CallbackAPIVersion.VERSION2
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="HouseSensors_Student")
client.will_set(f"{TOPIC_BASE}/doors/door1/status", payload="offline", qos=1, retain=True)

try:
    client.connect(BROKER, PORT, 60)
    client.loop_start()
    client.publish(f"{TOPIC_BASE}/doors/door1/status", "online", qos=1, retain=True)

    print(f"=== Симуляцію запущено! Сценарій: {args.scenario} ===")
    print("Натисніть Ctrl+C для зупинки.\n")

    while True:
        door_state = "OPEN" if args.scenario == 'door_open' else "CLOSED"
        smoke_val = True if args.scenario == 'smoke' else False
        motion_val = True if args.scenario == 'night_motion' else False

        client.publish(f"{TOPIC_BASE}/doors/door1/telemetry", json.dumps({"state": door_state, "ts": int(time.time())}), qos=0)
        client.publish(f"{TOPIC_BASE}/smoke/telemetry", json.dumps({"smoke": smoke_val, "ts": int(time.time())}), qos=0)
        client.publish(f"{TOPIC_BASE}/yard/motion/telemetry", json.dumps({"motion": motion_val, "ts": int(time.time())}), qos=0)

        print(f"[Дані відправлено] Двері: {door_state} | Дим: {smoke_val} | Рух: {motion_val}")
        time.sleep(3)
except Exception as e:
    print(f"Помилка: {e}")