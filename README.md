# Модульний контроль 1: Охоронна система приватного будинку (Варіант 3)

**Посилання на відеодемонстрацію:** [https://drive.google.com/file/d/1nz1WsxRmq7hYiezQuk63kdPA50JyTta2/view?usp=drive_link]

## Архітектура та протоколи
Для зв'язку обрано **MQTT**, оскільки він легкий, підтримує Pub/Sub архітектуру та забезпечує сповіщення про аварійне вимкнення пристроїв через механізм **Last Will & Testament**.

## Структура MQTT-топіків
- `my_house_variant3_test/doors/door1/telemetry` (QoS 0) — Стан дверей
- `my_house_variant3_test/smoke/telemetry` (QoS 0) — Датчик диму
- `my_house_variant3_test/yard/motion/telemetry` (QoS 0) — Датчик руху
- `my_house_variant3_test/doors/door1/status` (QoS 1, retain=True) — Стан пристрою (online/offline)

## Інструкція запуску
1. Відкрити термінал у папці проєкту.
2. Встановити залежності: `pip install paho-mqtt`
3. Запустити симулятор: `python devices.py --scenario door_open`
