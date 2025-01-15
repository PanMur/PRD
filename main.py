import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

# Функция для генерации данных акселерометра и гироскопа с учетом шумов
def generate_sensor_data(activity, duration, sampling_rate, accel_noise, gyro_noise, baro_noise):
    time = np.arange(0, duration, 1/sampling_rate)
    if activity == "Покой":
        accel_x = np.random.normal(0, accel_noise, len(time))
        accel_y = np.random.normal(0, accel_noise, len(time))
        accel_z = 1 + np.random.normal(0, accel_noise, len(time))  # Ось Z: сила тяжести
        gyro_x = np.random.normal(0, gyro_noise, len(time))
        gyro_y = np.random.normal(0, gyro_noise, len(time))
        gyro_z = np.random.normal(0, gyro_noise, len(time))
        baro = np.random.normal(1013.25, baro_noise, len(time))  # Нормальное атмосферное давление
    elif activity == "Ходьба":
        accel_x = 0.3 * np.sin(2 * np.pi * 1 * time) + np.random.normal(0, accel_noise, len(time))
        accel_y = 0.3 * np.sin(2 * np.pi * 1 * time + np.pi/2) + np.random.normal(0, accel_noise, len(time))
        accel_z = 1 + 0.1 * np.sin(2 * np.pi * 1 * time) + np.random.normal(0, accel_noise, len(time))
        gyro_x = 30 * np.sin(2 * np.pi * 1 * time) + np.random.normal(0, gyro_noise, len(time))
        gyro_y = 30 * np.sin(2 * np.pi * 1 * time + np.pi/2) + np.random.normal(0, gyro_noise, len(time))
        gyro_z = np.random.normal(0, gyro_noise, len(time))
        baro = np.random.normal(1013.25, baro_noise, len(time))
    elif activity == "Бег":
        accel_x = 0.8 * np.sin(2 * np.pi * 2 * time) + np.random.normal(0, accel_noise, len(time))
        accel_y = 0.8 * np.sin(2 * np.pi * 2 * time + np.pi/2) + np.random.normal(0, accel_noise, len(time))
        accel_z = 1 + 0.3 * np.sin(2 * np.pi * 2 * time) + np.random.normal(0, accel_noise, len(time))
        gyro_x = 100 * np.sin(2 * np.pi * 2 * time) + np.random.normal(0, gyro_noise, len(time))
        gyro_y = 100 * np.sin(2 * np.pi * 2 * time + np.pi/2) + np.random.normal(0, gyro_noise, len(time))
        gyro_z = np.random.normal(0, gyro_noise, len(time))
        baro = np.random.normal(1013.25, baro_noise, len(time))
    elif activity == "Прыжки":
        accel_x = np.random.normal(0, 0.5, len(time)) + np.random.normal(0, accel_noise, len(time))
        accel_y = np.random.normal(0, 0.5, len(time)) + np.random.normal(0, accel_noise, len(time))
        accel_z = 1 + 2 * np.sin(2 * np.pi * 0.5 * time) + np.random.normal(0, accel_noise, len(time))
        gyro_x = np.random.normal(0, 50, len(time)) + np.random.normal(0, gyro_noise, len(time))
        gyro_y = np.random.normal(0, 50, len(time)) + np.random.normal(0, gyro_noise, len(time))
        gyro_z = 200 * np.sin(2 * np.pi * 0.5 * time) + np.random.normal(0, gyro_noise, len(time))
        baro = np.random.normal(1013.25, baro_noise, len(time))
    elif activity == "Подъем по лестнице":
        accel_x = 0.5 * np.sin(2 * np.pi * 1 * time) + np.random.normal(0, accel_noise, len(time))
        accel_y = 0.5 * np.sin(2 * np.pi * 1 * time + np.pi / 2) + np.random.normal(0, accel_noise, len(time))
        accel_z = 1 + 0.2 * np.sin(2 * np.pi * 2 * time) + np.random.normal(0, accel_noise, len(time))
        gyro_x = 50 * np.sin(2 * np.pi * 1 * time) + np.random.normal(0, gyro_noise, len(time))
        gyro_y = 50 * np.sin(2 * np.pi * 1 * time + np.pi / 2) + np.random.normal(0, gyro_noise, len(time))
        gyro_z = np.random.normal(0, gyro_noise, len(time))
        baro = 1013.25 - 0.1 * time + np.random.normal(0, baro_noise, len(time))  # Постепенное уменьшение давления
    elif activity == "Спуск по лестнице":
        accel_x = 0.5 * np.sin(2 * np.pi * 1 * time) + np.random.normal(0, accel_noise, len(time))
        accel_y = 0.5 * np.sin(2 * np.pi * 1 * time + np.pi / 2) + np.random.normal(0, accel_noise, len(time))
        accel_z = 1 + 0.2 * np.sin(2 * np.pi * 2 * time) + np.random.normal(0, accel_noise, len(time))
        gyro_x = 50 * np.sin(2 * np.pi * 1 * time) + np.random.normal(0, gyro_noise, len(time))
        gyro_y = 50 * np.sin(2 * np.pi * 1 * time + np.pi / 2) + np.random.normal(0, gyro_noise, len(time))
        gyro_z = np.random.normal(0, gyro_noise, len(time))
        baro = 1013.25 + 0.1 * time + np.random.normal(0, baro_noise, len(time))  # Постепенное увеличение давления
    elif activity == "Подъем на лифте":
        accel_x = np.random.normal(0, 0.1, len(time)) + np.random.normal(0, accel_noise, len(time))
        accel_y = np.random.normal(0, 0.1, len(time)) + np.random.normal(0, accel_noise, len(time))
        accel_z = 1 + 0.1 * np.sin(2 * np.pi * 0.5 * time) + np.random.normal(0, accel_noise, len(time))
        gyro_x = np.random.normal(0, 10, len(time)) + np.random.normal(0, gyro_noise, len(time))
        gyro_y = np.random.normal(0, 10, len(time)) + np.random.normal(0, gyro_noise, len(time))
        gyro_z = np.random.normal(0, gyro_noise, len(time))
        baro = 1013.25 - 0.2 * time + np.random.normal(0, baro_noise, len(time))  # Быстрое уменьшение давления
    elif activity == "Спуск на лифте":
        accel_x = np.random.normal(0, 0.1, len(time)) + np.random.normal(0, accel_noise, len(time))
        accel_y = np.random.normal(0, 0.1, len(time)) + np.random.normal(0, accel_noise, len(time))
        accel_z = 1 + 0.1 * np.sin(2 * np.pi * 0.5 * time) + np.random.normal(0, accel_noise, len(time))
        gyro_x = np.random.normal(0, 10, len(time)) + np.random.normal(0, gyro_noise, len(time))
        gyro_y = np.random.normal(0, 10, len(time)) + np.random.normal(0, gyro_noise, len(time))
        gyro_z = np.random.normal(0, gyro_noise, len(time))
        baro = 1013.25 + 0.2 * time + np.random.normal(0, baro_noise, len(time))  # Быстрое увеличение давления
    elif activity == "Падение с высоты роста человека":
        accel_x = np.random.normal(0, 2, len(time)) + np.random.normal(0, accel_noise, len(time))
        accel_y = np.random.normal(0, 2, len(time)) + np.random.normal(0, accel_noise, len(time))
        accel_z = 1 + 5 * np.sin(2 * np.pi * 0.5 * time) + np.random.normal(0, accel_noise, len(time))
        gyro_x = np.random.normal(0, 200, len(time)) + np.random.normal(0, gyro_noise, len(time))
        gyro_y = np.random.normal(0, 200, len(time)) + np.random.normal(0, gyro_noise, len(time))
        gyro_z = np.random.normal(0, 200, len(time)) + np.random.normal(0, gyro_noise, len(time))
        baro = 1013.25 + np.random.normal(0, baro_noise, len(time))  # Резкое изменение давления
    elif activity == "Падение с большой высоты":
        accel_x = np.random.normal(0, 5, len(time)) + np.random.normal(0, accel_noise, len(time))
        accel_y = np.random.normal(0, 5, len(time)) + np.random.normal(0, accel_noise, len(time))
        accel_z = 1 + 10 * np.sin(2 * np.pi * 0.5 * time) + np.random.normal(0, accel_noise, len(time))
        gyro_x = np.random.normal(0, 500, len(time)) + np.random.normal(0, gyro_noise, len(time))
        gyro_y = np.random.normal(0, 500, len(time)) + np.random.normal(0, gyro_noise, len(time))
        gyro_z = np.random.normal(0, 500, len(time)) + np.random.normal(0, gyro_noise, len(time))
        baro = 1013.25 + np.random.normal(0, baro_noise, len(time))  # Резкое изменение давления
    else:
        raise ValueError("Неизвестный тип активности")

    data = pd.DataFrame({
        "time": time,
        "accel_x": accel_x,
        "accel_y": accel_y,
        "accel_z": accel_z,
        "gyro_x": gyro_x,
        "gyro_y": gyro_y,
        "gyro_z": gyro_z,
        "baro": baro
    })
    return data

# Функция для визуализации данных
def plot_data(data):
    st.subheader("Данные акселерометра")
    fig_accel = px.line(data, x="time", y=["accel_x", "accel_y", "accel_z"], title="Акселерометр")
    st.plotly_chart(fig_accel)

    st.subheader("Данные гироскопа")
    fig_gyro = px.line(data, x="time", y=["gyro_x", "gyro_y", "gyro_z"], title="Гироскоп")
    st.plotly_chart(fig_gyro)

    st.subheader("Данные барометра")
    fig_baro = px.line(data, x="time", y=["baro"], title="Барометр")
    st.plotly_chart(fig_baro)

# Основное приложение
def main():
    st.title("Генератор и визуализатор данных акселерометра и гироскопа")
    st.write("Это приложение имитирует данные с носимого устройства для различных видов активности.")

    # Выбор активности
    activity = st.selectbox("Выберите активность", ["Покой", "Ходьба", "Бег", "Прыжки", "Подъем по лестнице", "Спуск по лестнице", "Подъем на лифте", "Спуск на лифте", "Падение с высоты роста человека", "Падение с большой высоты"])
    duration = st.slider("Длительность (секунды)", 1, 3600, 10)
    sampling_rate = st.slider("Частота дискретизации (Гц)", 1, 100, 50)
    accel_noise = st.slider("Уровень шума акселерометра", 0.0, 0.5, 0.05)
    gyro_noise = st.slider("Уровень шума гироскопа", 0.0, 1.0, 0.01)
    baro_noise = st.slider("Уровень шума барометра", 0.0, 1.0, 0.1)


    # Генерация данных
    data = generate_sensor_data(activity, duration, sampling_rate, accel_noise, gyro_noise, baro_noise)

    # Визуализация данных
    plot_data(data)

    # Показать сырые данные
    if st.checkbox("Показать сырые данные"):
        st.write(data)

    # Сохранение данных в CSV
    if st.button("Сохранить данные в CSV"):
        csv = data.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Скачать CSV",
            data=csv,
            file_name="sensor_data.csv",
            mime="text/csv",
        )

if __name__ == "__main__":
    main()