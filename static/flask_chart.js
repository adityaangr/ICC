function showChart(dataJSONFZ,canvas) {
  var chartJSONFZ = dataJSONFZ;
  var datasetchartFZ = [];
  var mergedData = [].concat.apply([], chartJSONFZ.data);
  for (var i = 0; i < chartJSONFZ.columns.length; i++) {
    var dataFZ = {
      label: [chartJSONFZ.columns[i]],
      data: mergedData[i],
      backgroundColor: getRandomColor(),
    };
    datasetchartFZ.push(dataFZ);
  }
  var areachartFZ = {
    labels: chartJSONFZ.index[0],
    datasets: datasetchartFZ,
  };
  console.log(areachartFZ,'areachartFZ')
  //-------------
  //- BAR CHART -
  //-------------
  getConfig(canvas, areachartFZ);
}
///

///

// RANDOM COLOR FOR BACKGROUND COLOUR
function getRandomColor() {
  var letters = "0123456789ABCDEF".split("");
  var color = "#";
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

//    func config for all chart
function getConfig(getCanvas, datasetBarChart) {
  //---------------------
  //- CONFIG STACKED BAR CHART
  //---------------------
  var barChartData = jQuery.extend(true, {}, datasetBarChart);
  var temp0 = datasetBarChart.datasets[0];
  var temp1 = datasetBarChart.datasets[1];
  console.log(temp0, "temp0");
  barChartData.datasets[0] = temp1;
  barChartData.datasets[1] = temp0;
  var barChartOptions = {
    plugins: {
      title: {
        display: true,
        text: "Chart.js Bar Chart - Stacked",
      },
    },
    responsive: true,
    interaction: {
      intersect: true,
    },
    scales: {
      x: {
        stacked: true,
      },
    },
  };
  var stackedBarChartData = jQuery.extend(true, {}, datasetBarChart);
  var stackedBarChartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      xAxes: [
        {
          stacked: true,
        },
      ],
      yAxes: [
        {
          stacked: true,
        },
      ],
    },
  };
  var stackedBarChart = new Chart(getCanvas, {
    type: "bar",
    data: stackedBarChartData,
    options: stackedBarChartOptions,
  });
}
