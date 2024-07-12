const url2 = './assets/benefits_2plat.csv';

sankeyfier(url2)
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
      title: "My Card Benefits",
      font: {
        size: 10
      }
    }

    Plotly.react('benefits_2plat_sankey', data, layout)
  });

