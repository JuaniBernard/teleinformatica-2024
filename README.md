# Caso 1 - Enunciado

Una organización con alcance nacional ha contratado enlaces para sus 6 sucursales con la idea de armar una red Wan Nacional. En el armado de esta red Wan se ha dispuesto utilizar para el direccionamiento IP la red 192.168.100.0/24 dividida en subredes con máscara /29.

Cada una de las sucursales utilizará para su direccionamiento IP interno una red /24 completa, del tipo 10.0.n.0/24.

De este modo cada sucursal poseerá un enlace Wan (red 192.168.100.n/29) y una red interna (10.0.n.0/24).

La Dirección IP del enlace wan del router de la sucursal será la primera dirección utilizable de la red /29 su contraparte en la casa matríz será la última dirección utilizable de la red /29.

La dirección IP privada del router de la sucursal será la primer dirección utilizable de la red 10.0.n.0/24.



La correspondencia de direcciones de enlaces y redes estará dada por la siguiente regla:

Sucursal 1-> Enlace Wan: Primer red 192.168.100.n/29 -> Direccionamiento privado: 10.0.1.0/24

Sucursal 2-> Enlace Wan: Segunda red 192.168.100.n/29 -> Direccionamiento privado: 10.0.2.0/24

Sucursal 3-> Enlace Wan: Tercer red 192.168.100.n/29 -> Direccionamiento privado: 10.0.3.0/24

Sucursal 4-> Enlace Wan: Cuarta red 192.168.100.n/29 -> Direccionamiento privado: 10.0.4.0/24

Sucursal 5-> Enlace Wan: Quinta red 192.168.100.n/29 -> Direccionamiento privado: 10.0.5.0/24

Sucursal 6-> Enlace Wan: Sexta red 192.168.100.n/29 -> Direccionamiento privado: 10.0.6.0/24



Resolución:

Deberá desarrollar todo el direccionamiento IP de las redes conjuntamente con un esquema de la misma.

Implementar con mininet el router de casa matriz, dos sucursales con: el router [primer IP] y un puesto de trabajo de la sucursal [última IP].

## Esquema en MiniEdit

![Esquema del Caso 1: Router de la casa matriz y dos sucursales](/caso1/caso1.png "Caso 1")

##
###### Estos trabajos fueron desarrollados durante el cursado de Teleinformática (Universidad de Mendoza) por Juan Ignacio Bernard.
