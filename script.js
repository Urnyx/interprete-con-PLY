
function enviarContenido(){
    var contenido = document.getElementById("codigo").value;
        fetch('/procesar_contenido', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ content: contenido })
        })
        .then(response => response.text())
        .then(resultado => {
          // Manejar el resultado devuelto por Flask
          console.log(resultado);
        })
        .catch(error => {
          console.error('Error:', error);
        });
}