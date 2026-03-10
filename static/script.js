let chart;

async function refreshPrediction() {
    try {
        // Update prediction
        const pred = await fetch('/api/predict');
        const data = await pred.json();
        
        document.getElementById('tomorrow').textContent = data.tomorrow;
        document.getElementById('current').textContent = data.current;
        document.getElementById('signal').textContent = data.signal;
        document.getElementById('signal').style.color = data.change > 0 ? '#00ff88' : data.change < 0 ? '#ff4444' : '#ffaa00';
        
        // Update chart
        updateChart();
    } catch(e) {
        console.error('Prediction failed:', e);
    }
}

async function updateChart() {
    try {
        const chartData = await fetch('/api/chart');
        const data = await chartData.json();
        
        const trace1 = {
            x: data.dates.slice(0, -1),
            y: data.actual,
            type: 'scatter', mode: 'lines+markers',
            name: 'Actual',
            line: {color: '#00ff88', width: 3}
        };
        
        const trace2 = {
            x: data.dates.slice(1),
            y: data.predicted,
            type: 'scatter', mode: 'lines+markers',
            name: 'AI Prediction (95%)',
            line: {color: '#FFD700', width: 3}
        };
        
        const layout = {
            title: 'RELIANCE Next 30 Days - AI Forecast',
            font: {family: 'Poppins, sans-serif', size: 14},
            plot_bgcolor: 'rgba(0,0,0,0)',
            paper_bgcolor: 'rgba(0,0,0,0)',
            height: 450
        };
        
        Plotly.newPlot('priceChart', [trace1, trace2], layout, {responsive: true});
    } catch(e) {
        console.error('Chart failed:', e);
    }
}

// Load on start
refreshPrediction();
setInterval(refreshPrediction, 30000); // Update every 30s
