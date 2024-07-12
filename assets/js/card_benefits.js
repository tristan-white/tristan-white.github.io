const url = './assets/benefits.csv';

sankeyfier(url)
  .then(jsonData => {
    var data = {
      type: "sankey",
      orientation: "h",
      node: {
        pad: 15,
        thickness: 30,
        line: {
          color: "black",
          width: 0.5
        },
      label: jsonData.label,
      color: "blue"
      },

      link: {
        source: jsonData.source,
        target: jsonData.target,
        value: jsonData.value,
      }
    }

    var data = [data]

    var layout = {
      title: "Overview of Flagship Credit Card Benefits",
      font: {
        size: 10
      }
    }

    Plotly.react('benefits_sankey', data, layout)
  });

