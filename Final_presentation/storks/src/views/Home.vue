<template>
  <div class="about">
    <div class="position-absolute top-50 start-50 translate-middle" style="width: 110rem">
      <div class="row justify-content-center">
        <div class="row justify-content-center mb-5" style="width: 110rem; height: rem">
          <div class="card border-4" style="width: 110rem; height: 25rem">
            <v-chart class="chart row justify-content-center rounded" :option="option" />
          </div>
        </div>
        <div class="row justify-content-center">
          <div class="row justify-content-between" style="width: 110rem; height: 20rem">
            <div class="card border-4" style="width: 15rem; height: 23rem">
              <div class="card-body">
                <h3 class="titleinfo card-title text-center">28 March</h3><br>
                <h5 class="info1 card-title text-center">Prediction of the day</h5>
                <h2 class="card-title text-center">1576</h2>
                <h5 class="info2 card-title text-center">Birth of the day</h5>
                <h2 class="card-title text-center">1666</h2>
                <h5 class="info3 card-title text-center">Number of births in 2020</h5>
                <h2 class="card-title text-center">2073</h2>
              </div>
            </div>
            <div class="card mb-3 border border-4" style="width: 26rem; height: 23rem">
                <v-chart class="gauge row justify-content-center rounded" :option="gauge" />
            </div>
            <div class="card mb-3 border border-4" style="width: 61rem; height: 23rem">
                <v-chart class="chart2 row justify-content-center rounded" :option="test" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import { TitleComponent, TooltipComponent, LegendComponent } from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";

use([CanvasRenderer, PieChart, TitleComponent, TooltipComponent, LegendComponent]);

export default {
  name: "HelloWorld",
  components: {
    VChart,
  },
  provide: {
    [THEME_KEY]: "light",
  },
  data() {
    var colors = ["#5470C6", "#EE6666", "#007A04"];
    var colors2 = ["#5470C6", "#91CC75", "#EE6666"];
    return {
      option: {
        color: colors,

        tooltip: {
          trigger: "none",
          axisPointer: {
            type: "cross",
          },
        },
        title: {
          text: "Tracking of births during the year",
          left: "center",
          top: 10,
        },
        legend: {
          data: ["Prediction", "Current year", "Births in 2020"],
          top: 45,
        },
        grid: {
          top: 105,
          bottom: 50,
        },
        xAxis: [
          {
            type: "category",
            axisTick: {
              alignWithLabel: true,
            },
            axisLine: {
              onZero: false,
              lineStyle: {
                color: colors[1],
              },
            },
            axisPointer: {
              label: {
                formatter: function (params) {
                  return "Current year " + params.value + (params.seriesData.length ? "：" + params.seriesData[0].data : "");
                },
              },
            },
            data: [
              "January",
              "Febuary",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December",
            ],
          },
          {
            type: "category",
            axisTick: {
              alignWithLabel: true,
            },
            axisLine: {
              onZero: false,
              lineStyle: {
                color: colors[0],
              },
            },
            axisPointer: {
              label: {
                formatter: function (params) {
                  return (
                    "Prediction " + params.value + (params.seriesData.length ? "：" + params.seriesData[0].data : "")
                  );
                },
              },
            },
            data: [
              "January",
              "Febuary",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December",
            ],
          },
          {
            type: "category",
            axisTick: {
              alignWithLabel: true,
            },
            axisLine: {
              onZero: false,
              lineStyle: {
                color: colors[0],
              },
            },
            axisPointer: {
              label: {},
            },
            data: [],
          },
        ],
        yAxis: [
          {
            type: "value",
            min: 45000,
          },
        ],
        series: [
          {
            name: "Prediction",
            type: "line",
            xAxisIndex: 1,
            smooth: true,
            emphasis: {
              focus: "series",
            },
            data: [53925, 50278, 54889, 52427, 56888, 55214, 58596, 57107, 57060, 58230, 54837, 53896],
          },
          {
            name: "Current year",
            type: "line",
            smooth: true,
            emphasis: {
              focus: "series",
            },
            data: [53760, 51660],
          },
          {
            name: "Births in 2020",
            type: "line",
            smooth: true,
            emphasis: {
              focus: "series",
            },
            data: [62341, 56492, 60450, 57360, 62969, 61830, 66061, 63736, 63120, 64201, 60660, 58583],
          },
        ],
      },
      test: {
        color: colors2,

        tooltip: {
          trigger: "none",
          axisPointer: {
            type: "cross",
          },
        },
        title: {
          text: "Number of births in the last 15 days",
          left: "center",
          top: 10,
        },
        legend: {
          data: ["Tracking curve"],
          top: 45,
        },
        grid: {
          top: 105,
          bottom: 50,
        },
        xAxis: [
          {
            type: "category",
            axisTick: {
              alignWithLabel: true,
            },
            axisLine: {
              onZero: false,
              lineStyle: {
                color: colors[2],
              },
            },
            axisPointer: {
              label: {
                formatter: function (params) {
                  return "Number of births " + params.value + (params.seriesData.length ? "：" + params.seriesData[0].data : "");
                },
              },
            },
            data: [
              "13/03",
              "14/03",
              "15/03",
              "16/03",
              "17/03",
              "18/03",
              "19/03",
              "20/03",
              "21/03",
              "22/03",
              "23/03",
              "24/03",
              "25/03",
              "26/03",
              "27/03",
            ],
          },
          
          {
            type: "category",
            axisTick: {
              alignWithLabel: true,
            },
            
            axisPointer: {
              label: {},
            },
            data: [],
          },
        ],
        yAxis: [
          {
            type: "value",
            min: 1000,
          },
        ],
        series: [
          {
            name: "Tracking curve",
            type: "line",
            xAxisIndex: 1,
            smooth: true,
            emphasis: {
              focus: "series",
            },
            data: [1567, 1794, 1865, 1946, 1647, 1349, 1792, 1934, 1273, 1372, 1893, 1835, 1924, 1769, 2006],
          },
          {
            name: "",
            type: "bar",
            smooth: true,
            emphasis: {
              focus: "series",
            },
            data: [1567, 1794, 1865, 1946, 1647, 1349, 1792, 1934, 1273, 1372, 1893, 1835, 1924, 1769, 2006],
          },
        ],
      },
      gauge: {
        title: {
            show: true,
            text: "Birth rate compared to last month",
            left: "center",
            top: 10,
        },
    series: [{
        type: 'gauge',
        progress: {
          show: true,
            width: 18,
        },
        axisLine: {
          lineStyle: {
            width: 18
            }
        },
        axisTick: {
          show: true
        },
        splitLine: {
          length: 4,
            lineStyle: {
              width: 2,
                color: '#111',
            }
        },
        axisLabel: {
            distance: 25,
            color: '#999',
            fontSize: 15
        },
        anchor: {
            show: true,
            showAbove: true,
            size: 15,
            itemStyle: {
                borderWidth: 5,
            }
        },
        detail: {
            valueAnimation: true,
            fontSize: 30,
            offsetCenter: [0, '70%'],
            formatter: "{value}%"
        },
        data: [{
            value: 6.3
        }],
        min: -10,
        max: 10,
        center: ["50%", "60%"]
    }]
}
    };
  },
};
</script>

<style scoped>
.chart {
  height: 25rem;
  width: 108rem;
  border-radius: 30rem;
}
.chart2 {
  height: 23rem;
  width: 60.5rem;
  border-radius: 30rem;
}
.gauge {
  height: 23rem;
  width: 25.5rem;
  border-radius: 30rem;
}
.titleinfo {
  font-weight: bold;
  text-decoration : underline;
}
.info1 {
  color: rgb(84, 112, 198);
}
.info2 {
  color: rgb(238, 102, 102);
}
.info3 {
  color: rgb(0, 122, 4);
}
</style>
