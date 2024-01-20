# AUTOMATIZACIÓN DE PRUEBAS A SERVICIOS WEB - RESTFUL - BOOKER

### 📄 Contexto:

RestFul Booker, es una API que puede utilizar para obtener más información sobre API Testing o probar herramientas de API Testing. 
RestFul-Booker contiene end-points que permiten Crear, Leer, Actualizar y Eliminar reservas. 
El API REST viene con funciones de autenticación y errores para que pueda explorar. 
La API viene precargada con 10 registros para que pueda trabajar y se restablece cada 10 minutos a ese estado predeterminado.
### ☠ Problemática:

Actualmente en la aplicación de reservas RESTFUL - BOOKER se están detectando diferentes errores funcionales a nivel de la GUI, 
pero al detectarlos en este nivel no se puede dar feedback temprano a los desarrolladores. 
Por lo que se requiere que se automaticen pruebas a nivel de integración, 
por eso se requiere implementar pruebas automatizadas a los servicios web.

### 💡 Solución:

Para abordar la problemática de la detección tardía de errores funcionales 
en la interfaz de usuario de Restful-Booker, se propone implementar un enfoque 
integral de pruebas automatizadas a nivel de integración, utilizando el framework de 
pruebas Test Junkie. Este enfoque permitirá la ejecución sistemática y eficiente de 
casos de prueba que cubren operaciones CRUD y escenarios críticos de la API REST. 
La automatización se llevará a cabo mediante el uso de scripts desarrollados en Python, 
haciendo uso de la biblioteca requests para interactuar con los servicios web.

***

# 🤖 PLAN DE PRUEBAS FUNCIONAL



### 🎯 OBJETIVO

El objetivo principal es asegurar la calidad y confiabilidad de la API Restful-Booker 
mediante la implementación de pruebas automatizadas a nivel de integración. 
Esto incluye la validación de operaciones CRUD, autenticación y gestión de errores.

### ALCANCE
El alcance de este plan de pruebas abarca las operaciones principales de la API Restful Booker, 
centrándose en las funcionalidades críticas que incluyen la autenticación, 
la gestión de reservas y la salud general del sistema. A continuación, se detalla el alcance específico:


    Pruebas de Autenticación
    Pruebas de Reservas
    Pruebas de Datos
    Informes y Registro
    Escenarios de Excepción

### RIESGOS

| Riesgo                                                                                                           | Mitigación                                                                                                             |
|:-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Cambios inesperados en la API Restful Booker pueden causar fallos en las pruebas automatizadas.                  |  Establecer una comunicación constante con el equipo de desarrollo para anticipar cambios. Monitorizar la documentación de la API y ajustar scripts de prueba en consecuencia. |
| Interrupciones en el entorno de pruebas pueden impedir la ejecución de pruebas en los plazos previstos.         | Establecer un calendario de mantenimiento regular y coordinar con los equipos de operaciones para garantizar la disponibilidad del entorno.                                     |
| Modificaciones en los requisitos de autenticación pueden afectar la ejecución de pruebas que dependen de tokens. | Mantener una comprensión clara de los requisitos de autenticación y adaptar los scripts de prueba cuando sea necesario. Actualizar los tokens de acceso según las políticas de seguridad.|
| La variabilidad en la respuesta de la API podría causar fallos intermitentes en las pruebas.                     | Implementar mecanismos de espera y validaciones flexibles en los scripts para manejar variaciones en la respuesta. Establecer criterios claros para considerar una prueba exitosa.|

***

### 👨‍💻 Herramientas y Tecnologías:

Framework de Pruebas: Test Junkie
Lenguaje de Programación: Python
Bibliotecas: requests para realizar llamadas HTTP

### Fuera del Alcance:

El presente plan de pruebas de automatización se enfoca específicamente en las operaciones fundamentales de la API Restful Booker. 
Sin embargo, existen aspectos que se consideran fuera del alcance de este plan:

1) Pruebas de Interfaz de Usuario (UI):

    Las pruebas relacionadas con la interfaz de usuario no están incluidas en este plan, ya que se centra exclusivamente en la capa de servicios web.
    
2) Pruebas de Rendimiento:
   La evaluación del rendimiento, como pruebas de carga y estrés, no forma parte de este plan. 
      Estas pruebas pueden requerir un enfoque y herramientas específicas.

3) Pruebas de Seguridad:
   La seguridad de la API, más allá de las pruebas básicas de autenticación, no está dentro del alcance. 

### 📋 Casos de Prueba:

✏️GetHealthCheck [BOOKING_001]
    
    Verificar la respuesta del servicio.
    Validar el código de estado y el contenido de la respuesta.

✏️Auth_CreateToken [BOOKING_002]

    Obtener un token de acceso válido.
    Verificar el código de estado y la presencia del token en la respuesta.

✏️GetBookingIds

    Obtener la lista de IDs de reservas.
    Validar el código de estado y la estructura de la respuesta.

✏️CreateBooking:

    Crear una reserva.
    Validar el código de estado y la existencia del ID de reserva en la respuesta.

✏️GetBookingById:

    Obtener detalles de una reserva por ID.
    Validar el código de estado y la coherencia de la información obtenida.

✏️PutUpdateBooking:

    Actualizar los detalles de una reserva.
    Validar el código de estado y la correcta actualización de la información.

✏️PatchPartialUpdateBooking:

    Actualizar parcialmente una reserva.
    Validar el código de estado y la actualización adecuada de la información.

✏️DeleteBooking:

    Eliminar una reserva.
    Validar el código de estado y la confirmación de eliminación en la respuesta.

### 📨 ENTEGRABLES DE PRUEBAS

> ☑️ El plan de pruebas actual, la ruta de su ubicación es: `TestDeliverables/PLAN_DE_PRUEBAS.markdown`  
> ☑️ El informe del resultado de pruebas, la ruta de su ubicación es: `API_TestSuite_Yape/reports/report_yape.html`   
> ☑️ El repositorio en GitHub con los scripts
> desarrollados: (https://github.com/osborrero/Api_automation_desafio_tecnico)
***

### ❗ INFORMACIÓN ADICIONAL

> *Toda la información relacionada a la estructura del proyecto se especifica en el archivo README.md*

***