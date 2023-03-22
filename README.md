# Prixz Developer
Este README.md tiene como objetivo proporcionar una guía para la implementación de nuevas funcionalidades en Odoo, con el objetivo de seguir las mejores prácticas y asegurar la calidad del código. En este documento se aborda el contexto específico del examen técnico para entrar como desarrollador Odoo.

## Requerimiento visualizar productos en vista de lista

Se requiere que en la vista de lista de los pedidos de venta se puedan visualizar los productos en formato many2many widgets para poder saber qué productos se vendieron sin abrir la vista de formulario.

### Solución propuesta

Para cumplir con este requerimiento, es necesario crear una vista personalizada para la lista de pedidos de venta. En esta vista, se debe agregar un campo many2many que permita visualizar los productos vendidos. Este campo debe estar oculto por defecto y sólo se debe mostrar cuando el usuario haga clic en un botón desplegable o en una pestaña. Es importante tener en cuenta que la adición de nuevos campos a las vistas de Odoo puede afectar el rendimiento, por lo que se debe hacer una evaluación cuidadosa antes de agregar nuevos campos.

## Creación de un cron para enviar correos electrónicos

Se requiere crear un cron que ejecute la siguiente acción cada 12 hrs:
a. Que busque todas las órdenes de venta que se crearon en el día en curso y que se encuentran en cotización
b. Agrupar las órdenes de venta por vendedor
c. Mandar un correo al vendedor diciendo que tiene tantas ordenes de venta en cotización.

### Solución propuesta

Para crear un cron que ejecute esta acción, se debe crear un archivo Python en el directorio de la aplicación correspondiente. En este archivo, se debe definir una función que realice las tres acciones mencionadas. La función debe buscar todas las órdenes de venta que se crearon en el día actual y que se encuentran en cotización. Luego, debe agrupar las órdenes de venta por vendedor y enviar un correo electrónico al vendedor con la cantidad de órdenes de venta en cotización. Finalmente, se debe programar un cron que ejecute la función cada 12 horas.


## Visualización del RFC del cliente en la vista de formulario de las órdenes de venta

Se necesita ver el RFC del cliente directamente en la vista de formulario de las órdenes de venta, este deberá estar ligado al RFC del cliente principal, es decir, si se cambia el RFC del cliente en la vista de formulario, el nuevo campo se deberá actualizar de manera automática en la vista de formulario de la orden de venta.

### Solución propuesta

Para visualizar el RFC del cliente en la vista de formulario de las órdenes de venta, se debe agregar un nuevo campo a la vista que esté vinculado al RFC del cliente principal.