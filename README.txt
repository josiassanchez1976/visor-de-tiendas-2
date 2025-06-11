INSTRUCCIONES DE USO LOCAL

1. Instalar dependencias:
   pip install -r requirements.txt

2. Copiar el archivo `.env.example` a `.env` y colocar tu clave de Google:
   cp .env.example .env
   # Edita `.env` y asigna tu API key

3. Ejecutar interfaz Streamlit:
   streamlit run app_refactor.py

4. Ejecutar API REST:
   uvicorn api_busqueda:app --reload

5. Probar API en:
   http://127.0.0.1:8000/docs

6. Ejecutar pruebas:
   pytest
