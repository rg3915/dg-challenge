$(function () {
    var url = "/dresses/dress_per_color_json/";

    $.getJSON(url, function(res){
        console.log(res);
        /* Transformando o dicionário em lista.
           Com o comando map eu coloco uma lista dentro da outra,
           necessário para este tipo de gráfico. */
        var data = res.map(function (v) {
            return [v.cor, v.quant]
        });

        console.log(data);

        $('#dress_color_chart').highcharts({
            chart: {
                type: 'bar'
            },
            title: {
                text: ''
            },
            xAxis: {
                type: 'category'
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Quantidade'
                }
            },
            legend: {
                enabled: false
            },
            // colors: ['#44AD41', '#DE2121'],
            series: [{
                data: data,
                colorByPoint: true,
                dataLabels: {
                    enabled: true,
                    align: 'center',
                    color: '#FFFFFF',
                    x: -25, // 25 pixels down from the top
                    style: {
                        fontSize: '15px'
                    }
                }
            }],
        });
    });
});