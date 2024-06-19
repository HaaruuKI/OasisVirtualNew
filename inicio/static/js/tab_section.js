function navegarASeccion(idSeccion) {
    // Obtiene el elemento de la sección con el ID especificado
    const seccion = document.getElementById(idSeccion)

    // Si la sección existe, se navega a ella
    if (seccion) {
        seccion.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        })
    } else {
        console.error(`No se encontró la sección con ID: ${idSeccion}`)
    }
}