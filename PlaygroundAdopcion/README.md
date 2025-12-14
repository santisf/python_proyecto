## Cómo probar (orden)
1. Clonar repo y crear entorno virtual.
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py runserver`
5. Abrir `http://127.0.0.1:8000/` (inicio).
6. Ir a "Animales" y crear animales (o usar "Nuevo Animal").
7. Ir a "Adoptantes" y crear adoptantes.
8. Desde la ficha de un animal o desde "Solicitudes" crear una solicitud de adopción.
9. Probar búsqueda en `/buscar/?q=nombre`.