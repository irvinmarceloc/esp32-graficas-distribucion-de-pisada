// static/script.js
function updateGraphs() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const time = Array.from({length: 100}, (_, i) => i);
            
            // Left foot
            const leftData = [
                {
                    x: time,
                    y: data.left.talon,
                    name: 'Talón',
                    type: 'scatter'
                },
                {
                    x: time,
                    y: data.left.medio,
                    name: 'Medio',
                    type: 'scatter'
                },
                {
                    x: time,
                    y: data.left.punta,
                    name: 'Punta',
                    type: 'scatter'
                }
            ];
            
            Plotly.newPlot('leftFoot', leftData, {
                title: 'Pie Izquierdo',
                xaxis: {title: 'Tiempo'},
                yaxis: {title: 'Presión'}
            });

            // Right foot
            const rightData = [
                {
                    x: time,
                    y: data.right.talon,
                    name: 'Talón',
                    type: 'scatter'
                },
                {
                    x: time,
                    y: data.right.medio,
                    name: 'Medio',
                    type: 'scatter'
                },
                {
                    x: time,
                    y: data.right.punta,
                    name: 'Punta',
                    type: 'scatter'
                }
            ];
            
            Plotly.newPlot('rightFoot', rightData, {
                title: 'Pie Derecho',
                xaxis: {title: 'Tiempo'},
                yaxis: {title: 'Presión'}
            });
        });
}

// Actualizar cada segundo
setInterval(updateGraphs, 1000);
// Primera actualización
updateGraphs();
