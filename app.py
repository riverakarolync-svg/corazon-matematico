import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# --------------------------------------------------
# CONFIGURACIÓN GENERAL DE LA PÁGINA
# --------------------------------------------------

st.set_page_config(
    page_title="Mi cariño en coordenadas",
    page_icon="❤️",
    layout="centered"
)

# --------------------------------------------------
# TÍTULO Y MENSAJE PRINCIPAL
# --------------------------------------------------

st.title("❤️ Mi cariño en coordenadas")

st.markdown(
    """
    <div style="
        background-color: #fff0f5;
        padding: 24px;
        border-radius: 18px;
        text-align: center;
        border: 2px solid #ff4b6e;
        margin-bottom: 25px;
        box-shadow: 0px 4px 15px rgba(255, 75, 110, 0.18);
    ">
        <h2 style="color:#c9184a; margin-bottom: 12px;">
            Siempre encontraré la forma de demostrarte que te quiero ❤️
        </h2>
        <p style="font-size:20px; color:#590d22; margin: 0;">
            Incluso si es tan complejo como una función, una gráfica o un código hecho solo para ti.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(
    "Este regalo fue creado con una función matemática en Python. "
    "El programa calcula puntos en el plano cartesiano y los va uniendo "
    "hasta formar un corazón."
)

# --------------------------------------------------
# FUNCIÓN MATEMÁTICA
# --------------------------------------------------

st.subheader("Función matemática utilizada")

st.write("El corazón se construye usando una función paramétrica:")

st.latex(r"""
x(t)=16\sin^3(t)
""")

st.latex(r"""
y(t)=13\cos(t)-5\cos(2t)-2\cos(3t)-\cos(4t)
""")

st.write("El parámetro utilizado es:")

st.latex(r"""
0 \leq t \leq 2\pi
""")

st.write(
    "Esto significa que el programa va cambiando el valor de **t**, "
    "calcula un punto **(x, y)** y lo dibuja en el plano cartesiano. "
    "Al unir todos los puntos, aparece el corazón."
)

# --------------------------------------------------
# CÁLCULO DEL CORAZÓN
# --------------------------------------------------

def corazon(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

# Valores del parámetro t
t = np.linspace(0, 2*np.pi, 500)

# Puntos del corazón
x, y = corazon(t)

# Espacio donde se actualizará la gráfica
grafica = st.empty()

# --------------------------------------------------
# FUNCIÓN PARA DIBUJAR EL CORAZÓN POCO A POCO
# --------------------------------------------------

def dibujar_corazon(hasta):
    fig, ax = plt.subplots(figsize=(6, 6))

    # Límites del plano cartesiano
    ax.set_xlim(min(x)-2, max(x)+2)
    ax.set_ylim(min(y)-2, max(y)+2)

    # Ejes X y Y
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)

    # Cuadrícula
    ax.grid(True, linestyle="--", alpha=0.3)

    # Etiquetas
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")

    # Título de la gráfica mientras se dibuja
    ax.set_title("Tienes una ingenierita que te quiere ❤️", fontsize=14)

    # Mantener la proporción correcta
    ax.set_aspect("equal")

    # Dibujar el corazón progresivamente
    ax.plot(x[:hasta], y[:hasta], color="red", linewidth=3)

    # Punto que muestra por dónde va la animación
    if hasta > 1:
        ax.scatter(x[hasta-1], y[hasta-1], color="crimson", s=70)

    return fig

# --------------------------------------------------
# ANIMACIÓN AUTOMÁTICA
# --------------------------------------------------

st.subheader("El corazón se va formando...")

# Mostrar el plano inicial
fig_inicial = dibujar_corazon(1)
grafica.pyplot(fig_inicial)
plt.close(fig_inicial)

# Animación automática al abrir la página
for i in range(1, len(t), 6):
    fig = dibujar_corazon(i)
    grafica.pyplot(fig)
    plt.close(fig)
    time.sleep(0.03)

# --------------------------------------------------
# CORAZÓN COMPLETO AL FINAL
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(6, 6))

ax.set_xlim(min(x)-2, max(x)+2)
ax.set_ylim(min(y)-2, max(y)+2)

ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)
ax.grid(True, linestyle="--", alpha=0.3)

ax.plot(x, y, color="red", linewidth=3)
ax.fill(x, y, color="pink", alpha=0.55)

ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")

# Título final arriba del corazón
ax.set_title("Tienes una ingenierita que te quiere ❤️", fontsize=14)

ax.set_aspect("equal")

grafica.pyplot(fig)
plt.close(fig)

st.success("Listo ❤️ El corazón se formó usando matemáticas.")

# --------------------------------------------------
# EXPLICACIÓN DEL PROGRAMA
# --------------------------------------------------

st.subheader("Cómo funciona el programa")

st.write(
    "Primero se crea un conjunto de valores de **t** entre 0 y 2π. "
    "Después, para cada valor de **t**, la función calcula una coordenada **x** "
    "y una coordenada **y**. Finalmente, el programa grafica esos puntos en orden. "
    "Por eso parece que el corazón se va dibujando como un video."
)

with st.expander("Ver el código principal de la función"):
    st.code("""
import numpy as np

def corazon(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

t = np.linspace(0, 2*np.pi, 500)
x, y = corazon(t)
""", language="python")

# --------------------------------------------------
# MENSAJE FINAL
# --------------------------------------------------

st.markdown(
    """
    <div style="
        background-color: #ffe5ec;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 25px;
        border: 1px solid #ff8fab;
    ">
        <h3 style="color:#c9184a;">
            Porque hasta las matemáticas saben formar algo bonito para ti ❤️
        </h3>
    </div>
    """,
    unsafe_allow_html=True
)
