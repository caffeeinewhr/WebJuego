const cartas = document.querySelectorAll('.carta');

cartas.forEach($carta => {
    let limites;

    // Función que se ejecuta cuando el ratón entra en la carta
    $carta.addEventListener('mouseenter', () => {
        limites = $carta.getBoundingClientRect();
        document.addEventListener('mousemove', rotarCarta);
    });

    $carta.addEventListener('mouseleave', () => {
        document.removeEventListener('mousemove', rotarCarta);
        $carta.style.transform = '';
    });

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
