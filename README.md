# 🌎 selenium_test_funcional — Tests Funcionales con Selenium

Suite de **pruebas funcionales automatizadas** con Selenium WebDriver y Python. Automatiza la interacción con navegador real (Chrome) para validar flujos de búsqueda web de extremo a extremo.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) ![Selenium](https://img.shields.io/badge/Selenium-4.33-green?logo=selenium) ![Chrome](https://img.shields.io/badge/ChromeDriver-Linux64-yellow?logo=googlechrome) ![License](https://img.shields.io/badge/License-BSD--3--Clause-blue)

---

## 📋 Descripción

El proyecto automatiza un flujo funcional completo en DuckDuckGo:
1. Abrir el navegador Chrome
2. Navegar a `duckduckgo.com`
3. Ingresar un término de búsqueda
4. Esperar los resultados con `WebDriverWait`
5. Validar que la página retorna resultados

Esto demuestra el uso de **Explicit Waits**, **CSS Selectors** y manejo de estados dinámicos del DOM.

---

## 🏗️ Estructura del proyecto

```
selenium_test_funcional/
├── test_busqueda.py          # Script principal de prueba funcional
├── run_tests.sh              # Script de ejecución en Linux
├── chromedriver              # Binario ChromeDriver (Linux)
├── chromedriver-linux64/     # ChromeDriver descomprimido
├── requirements.txt          # Dependencias Python
└── .github/                  # Configuración de CI/CD
```

---

## 🛠️ Tecnologías

| Herramienta | Versión | Rol |
|---|---|---|
| Python | 3.x | Lenguaje principal |
| Selenium | 4.33.0 | Automatización de navegador |
| ChromeDriver | Linux64 | Driver para Google Chrome |
| Trio | 0.30.0 | Soporte async para Selenium |

---

## 🚀 Cómo ejecutar

### Prerrequisitos
- Python 3.8+
- Google Chrome instalado en el sistema
- Linux (el ChromeDriver incluido es para Linux x64)

### Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Carl0gonzalez/selenium_test_funcional.git
cd selenium_test_funcional

# 2. Crear entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Dar permisos al ChromeDriver
chmod +x chromedriver

# 4. Ejecutar el test
python test_busqueda.py
```

### Ejecución headless (sin ventana visible)

Descomenta esta línea en `test_busqueda.py`:

```python
# options.add_argument("--headless")
```

### Salida esperada

```
✅ Prueba completada con éxito: se encontraron 10 resultados.
```

---

## 🤖 Flujo del test automatizado

```
Abrir Chrome → Navegar a DuckDuckGo → Ingresar búsqueda
    → WebDriverWait (10s) → Localizar resultados (CSS Selector)
    → assert resultados > 0 → ✅ PASS
```

---

## 💡 Aprendizajes clave

- Manejo de waits explícitos (`WebDriverWait` + `expected_conditions`) para elementos dinámicos
- Uso de CSS Selectors para localizar elementos del DOM en aplicaciones reales
- Gestión del ciclo de vida del navegador con context manager (`with webdriver.Chrome(...) as driver`)
- Diferencia entre pruebas funcionales (flujo de usuario) vs. pruebas unitarias (lógica aislada)

---

## 👤 Autor

**Carlo González** — [GitHub](https://github.com/Carl0gonzalez)
