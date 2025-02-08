// static/script.js
function updateGraphs() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const time = Array.from({length: 100}, (_, i) => i);
            // Left foot
            const leftDataCircle = [{
                values: [
                    Math.max(...data.left.talon),
                    Math.max(...data.left.medio),
                    Math.max(...data.left.punta)
                ],
                    labels: ['Talón', 'Medio', 'Punta'],
                    type: 'pie',
                    hole: .4,
                    marker: {
                        colors: ['#8884d8', '#82ca9d', '#ffc658']
                    }
            }];

            Plotly.newPlot('leftFootCircle', leftDataCircle, {
                title: 'Distribución de Presión - Pie Izquierdo',
                height: 400,
                showlegend: true
            });

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
