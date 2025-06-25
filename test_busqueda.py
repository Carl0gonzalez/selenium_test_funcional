from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # Configuración de ChromeDriver
    service = Service(executable_path="./chromedriver")
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Descomenta si no necesitas ver el navegador
    
    # Arranca el navegador
    with webdriver.Chrome(service=service, options=options) as driver:
        wait = WebDriverWait(driver, 10)
        
        # 1) Abre DuckDuckGo
        driver.get("https://duckduckgo.com/")
        
        # 2) Espera a que el input esté clickable y realiza búsqueda
        search_input = wait.until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )
        search_input.send_keys("inmuebles en Bogotá", Keys.RETURN)
        
        # 3) Espera a que aparezcan los enlaces de resultado
        results = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[data-testid="result-title-a"]'))
        )
        
        # 4) Validación
        assert results, "No se encontraron resultados."
        print(f"✅ Prueba completada con éxito: se encontraron {len(results)} resultados.")

if __name__ == "__main__":
    main()

