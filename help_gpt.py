import tkinter as tk
from tkinter import ttk
import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 시리얼 포트 설정 (아두이노와 연결된 포트로 변경)
ser = serial.Serial('COM3', 9600)

# GUI 설정
root = tk.Tk()
root.title("서보모터 데이터 시각화")

# 그래프 초기화
fig, ax = plt.subplots()
line, = ax.plot([], [], label='서보모터 데이터')
ax.set_ylim(0, 1023)
ax.set_xlim(0, 100)
ax.legend()

# 데이터 저장을 위한 리스트
data = [] # 외부에서 선언해서 데이터 넘겨받음


# 그래프 업데이트 함수
def update(frame):
    try:
        # 시리얼 데이터 읽기
        # 데이터 읽어와서 데이터에 append
        value = int(ser.readline().decode('utf-8').strip())
        data.append(value)

        # 최대 100개까지의 데이터만 표시
        if len(data) > 100:
            # 100개넘으면 pop 해서 삭제
            data.pop(0)

        # 그래프 업데이트
        line.set_data(range(len(data)), data)
        ax.relim()
        ax.autoscale_view()
    except Exception as e:
        print(f"Error: {e}")

# 애니메이션 설정
ani = FuncAnimation(fig, update, frames=None, blit=False, interval=100)

# GUI 시작
root.mainloop()
