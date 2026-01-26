# EVR

pip install adafruit-circuitpython-ads1x15 numpy scipy matplotlib

---

# ELF / VLF RESEARCH (Extremely Low Frequency | Very Low Frequency)

dedicado só a sinais industriais até 100 Hz...

não é gambiarra nn, é projeto com menor custo

<img width="671" height="546" alt="image" src="https://github.com/user-attachments/assets/76a9d8dc-f9e7-40d0-8255-227f568902ed" />

---

1 - Sinais ELF/VLF

0Hz (DC) não funciona.

Faixa: 3 Hz–30 Hz (ELF), 3 kHz–30 kHz (VLF)

Sensor: Antena magnética de baixa frequência ou magnetômetro sensível

Setup amador: Loop de fio com ferrite + LNA + ADC (Arduino/Raspberry Pi)

Observação: Apenas monitoramento; sinais abaixo de 1 Hz exigem equipamento grande/caro

---

2 - Sinais industriais / alta frequência (1Hz até 100 Hz)

Sensor: Acelerômetro ou sensor elétrico (corrente/tensão)

Função: Captura vibrações ou sinais elétricos industriais

---

como utilizar o sistema

CABO P2 (FORMA SEGURA)

- Cabo

- P2 TRS

- Tip → sinal

- Sleeve → GND

- Ring → não usar (ou segundo canal)

🔒 Proteção (OBRIGATÓRIA)

Nunca ligue direto em equipamento industrial.

Usar:

<img width="246" height="126" alt="image" src="https://github.com/user-attachments/assets/3136af80-8645-4765-af62-9cc29484513a" />

capacitor bloqueia DC, resistor limita corrente e protege a placa de som...

Não substitui ADC dedicado (ADS1115)

Só montar e rodar

by k

mit
