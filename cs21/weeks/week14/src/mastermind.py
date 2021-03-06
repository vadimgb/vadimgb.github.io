from logic import *

цвета = ["красный", "голубой", "зелёный", "жёлтый"]
символы = []
for i in range(4):
    for цвет in цвета:
        символы.append(Символ(f"{цвет}{i}"))

знания = И()

# Каждый цвет занимает место.
for цвет in цвета:
    знания.добавить(Или(
        Символ(f"{цвет}0"),
        Символ(f"{цвет}1"),
        Символ(f"{цвет}2"),
        Символ(f"{цвет}3")
    ))

# Цвет занимает только одно положение.
for цвет in цвета:
    for i in range(4):
        for j in range(4):
            if i != j:
                знания.добавить(Импликация(
                    Символ(f"{цвет}{i}"), Не(Символ(f"{цвет}{j}"))
                ))

# Одно место занимает только один цвет.
for i in range(4):
    for ц1 in цвета:
        for ц2 in цвета:
            if ц1 != ц2:
                знания.добавить(Импликация(
                    Символ(f"{ц1}{i}"), Не(Символ(f"{ц2}{i}"))
                ))

знания.добавить(Или(
    И(Символ("красный0"), Символ("голубой1"), Не(Символ("зелёный2")), Не(Символ("жёлтый3"))),
    И(Символ("красный0"), Символ("зелёный2"), Не(Символ("голубой1")), Не(Символ("жёлтый3"))),
    И(Символ("красный0"), Символ("жёлтый3"), Не(Символ("голубой1")), Не(Символ("зелёный2"))),
    И(Символ("голубой1"), Символ("зелёный2"), Не(Символ("красный0")), Не(Символ("жёлтый3"))),
    И(Символ("голубой1"), Символ("жёлтый3"), Не(Символ("красный0")), Не(Символ("зелёный2"))),
    И(Символ("зелёный2"), Символ("жёлтый3"), Не(Символ("красный0")), Не(Символ("голубой1")))
))

знания.добавить(И(
    Не(Символ("голубой0")),
    Не(Символ("красный1")),
    Не(Символ("зелёный2")),
    Не(Символ("жёлтый3"))
))

for символ in символы:
    if проверка_моделей(знания, символ):
        print(символ)
