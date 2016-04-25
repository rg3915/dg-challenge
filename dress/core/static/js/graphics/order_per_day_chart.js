$(function () {
    var url = "/orders/order_per_day_json/";

    $.getJSON(url, function(res){
        console.log(res);
        /* Transformando o dicionário em lista.
           Com o comando map eu coloco uma lista dentro da outra,
           necessário para este tipo de gráfico. */
        var data = res.map(function (v) {
            return [v.dia, v.quant]
        });

        console.log(data);

        $('#order_per_day_chart').highcharts({
            chart: {
                type: 'column'
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
                    y: 25, // 25 pixels down from the top
                    style: {
                        fontSize: '15px'
                    }
                }
            }],
        });
    });
});