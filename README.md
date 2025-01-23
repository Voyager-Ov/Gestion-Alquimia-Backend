# Gestion-Alquimia - Backend

**Gestion-Alquimia Backend** es la parte encargada de gestionar todos los aspectos del lado del servidor para la aplicación web de lavandería. Está desarrollado con **Node.js** y utiliza **Express** para construir una API RESTful robusta y escalable que facilita la gestión de pedidos, usuarios, suscripciones y finanzas.

## Propósito

El propósito principal del backend de **Gestion-Alquimia** es proporcionar la lógica de negocio y una API RESTful que permita a los administradores gestionar los pedidos, usuarios y suscripciones, así como supervisar las finanzas de la lavandería de manera eficiente.

## Tecnologías utilizadas

- **Node.js**: Entorno de ejecución para JavaScript en el servidor.
- **Express.js**: Framework minimalista para la creación de aplicaciones web y APIs.
- **MongoDB** o **PostgreSQL**: Base de datos para gestionar la información del sistema.
- **JWT**: Para la autenticación segura de usuarios.
- **Sequelize** o **Mongoose**: ORM/ODM para la gestión de datos según la base elegida.

## Funcionalidades principales

### Para Administradores
- **Gestión de pedidos**: Ver todos los pedidos con detalles como tipo de servicio, cliente, estado del pedido, entre otros.
- **Gestión de usuarios**: Acceso a información detallada de clientes registrados, suscripciones activas y actividad reciente.
- **Finanzas**: Consultar estadísticas, reportes y el estado de los pagos de la lavandería.
- **Panel de administración**: Consola personalizable para administrar todos los aspectos del negocio.

### Autenticación y seguridad
- Implementación de **autenticación JWT** para asegurar el acceso a la API.
- Futuro soporte para autenticación mediante **Google**, **Apple ID** y métodos **biométricos** (huella dactilar o reconocimiento facial).

## Despliegue

El backend será desplegado en un servidor cloud (como **AWS**, **Heroku**, o **Railway**) y se comunicará con el frontend desarrollado en Angular a través de la API RESTful.

## Contribuciones

Si deseas contribuir al backend del proyecto, abre un **issue** o envía un **pull request**. La colaboración es bienvenida.
