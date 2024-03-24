// Seleccionar todos los elementos con la clase 'carta' en el documento HTML
const cartas = document.querySelectorAll('.carta');

// Iterar sobre cada elemento 'carta'
cartas.forEach($carta => {
    let limites;

    // Función que se ejecuta cuando el ratón entra en la carta
    $carta.addEventListener('mouseenter', () => {
        // Obtener los límites (posición y tamaño) del elemento 'carta'
        limites = $carta.getBoundingClientRect();
        // Agregar un evento para detectar el movimiento del ratón y llamar a la función rotarCarta
        document.addEventListener('mousemove', rotarCarta);
    });

    // Función que se ejecuta cuando el ratón sale de la carta
    $carta.addEventListener('mouseleave', () => {
        // Remover el evento que detecta el movimiento del ratón y llama a la función rotarCarta
        document.removeEventListener('mousemove', rotarCarta);
        // Restaurar la transformación CSS del elemento 'carta' a su estado original
        $carta.style.transform = '';
    });

    // Función que rota la carta en respuesta al movimiento del ratón
    function rotarCarta(e) {
        // Obtener las coordenadas del ratón en la pantalla
        const mouseX = e.clientX;
        const mouseY = e.clientY;
        // Calcular la distancia desde el centro de la carta hasta el ratón
        const leftX = mouseX - limites.x;
        const topY = mouseY - limites.y;
        const center = {
            x: leftX - limites.width / 2,
            y: topY - limites.height / 2
        }
        // Calcular la distancia basada en una potencia cuártica (x^4 + y^4)
        const distancia = Math.sqrt(center.x ** 4 + center.y ** 4);

        // Aplicar transformaciones CSS al elemento 'carta'
        $carta.style.transform = `
            scale3d(1.10, 1.10, 1.10)
            rotate3d(          
                ${-center.y / 100},  
                ${center.x / 100},    
                0,              
                ${Math.log(distancia) * 2}deg 
            )
        `;
    }
});
