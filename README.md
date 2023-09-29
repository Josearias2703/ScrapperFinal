# ScrapperFinal
Este es un proyecto para realizar web scrapping de camisetas de futbol en este caso en específico de camisetas de la primera equipacion del Manchester City, la data se extrajo de esta pagina de España https://www.camisetasfutboleses.com/ que ofrece camisetas de futbol de muchos equipos importantes.

## Índice
- Herramientas
- Funcionamiento
- Conclusiones
- Recomendaciones

# Herramientas

En este proyecto se utilizaron herramientas como:
- Python
  -   Selenium
  -   Pymongo
- Mongo DB Atlas

# Funcionamiento

Este proyecto se basa en código Python en conjunto con la libreria Selenium para la extracción de la data de las camisetas, el precio normal, el precio con descuento y el descuento. Adicional se usa la libreria Pymongo para la conexión con la base de datos. Esta data se almacena en una base de datos MongoDB Atlas.

![image](https://github.com/Josearias2703/ScrapperFinal/assets/32946598/4656fac0-aef0-4a91-97a3-d9cd69ad0185)

# Conclusiones

Se obtiene una búsqueda y recolección de datos automatizada.

# Recomendaciones

Se recomienda en páginas donde existan mas resultados pero aparecen unicamente hasta 16 resultados como este fue el caso, encontrar el campo donde se puede aumentar el límite de objetos por cada página.
