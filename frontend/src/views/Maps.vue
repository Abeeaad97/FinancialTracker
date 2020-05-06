<template>
  <v-container
    fill-height
    fluid
    grid-list-xl
  >
    <v-layout
      justify-center
      wrap
      >
      <v-flex
        md12
      >
        <material-chart-card
          :data="dataCompletedTasksChart.data"
          :options="dataCompletedTasksChart.options"
          color="green"
          type="Line"
        >
          <h3 class="title font-weight-light">Hourly Trends</h3>
          <p class="category d-inline-flex font-weight-light"></p>

        </material-chart-card>
      </v-flex>
      <v-flex
        md

      >
        <material-chart-card
          :data="dailySalesChart.data"
          :options="dailySalesChart.options"
          color="info"
          type="Line"
        >
          <h4 class="title font-weight-light">Weekly Trends</h4>
        </material-chart-card>
      </v-flex>
      
      <v-flex
        md12
      >
        <material-chart-card
          :data="emailsSubscriptionChart.data"
          :options="emailsSubscriptionChart.options"
          :responsive-options="emailsSubscriptionChart.responsiveOptions"
          color="red"
          type="Line"
        >
          <h4 class="title font-weight-light">Annual Trends</h4>
        </material-chart-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script src="https://unpkg.com/vuetify/dist/vuetify.js"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
import axios from 'axios'
export default {
  mounted: function (){
      this.getStocks()
      console.log('Mounted Got Here')
    },
  data() {
    return {
       dailySalesChart: {
        data: {
          labels: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
          series: [
            [12,17,7,17,23,18,38]
          ]
        },
        options: {
          lineSmooth: this.$chartist.Interpolation.cardinal({
            tension: 0
          }),
          low: 0,
          high: 50, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 0
          }
        }
      },
      dataCompletedTasksChart: {
        data: {
          labels: ['12am', '3pm', '6pm', '9pm', '12pm', '3am', '6am', '9am'],
          series: [
            [230, 750, 450, 300, 280, 240, 200, 190]
          ]
        },
        options: {
          lineSmooth: this.$chartist.Interpolation.cardinal({
            tension: 0
          }),
          low: 0,
          high: 1000, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 0
          }
        }
      },
      emailsSubscriptionChart: {
        data: {
          labels: ['Ja', 'Fe', 'Ma', 'Ap', 'Mai', 'Ju', 'Jul', 'Au', 'Se', 'Oc', 'No', 'De'],
          series: [
            [542, 443, 320, 780, 553, 453, 326, 434, 568, 610, 756, 895]

          ]
        },
        options: {
          axisX: {
            showGrid: false
          },
          low: 0,
          high: 1000,
          chartPadding: {
            top: 0,
            right: 5,
            bottom: 0,
            left: 0
          }
        },
        responsiveOptions: [
          ['screen and (max-width: 640px)', {
            seriesBarDistance: 5,
            axisX: {
              labelInterpolationFnc: function (value) {
                return value[0]
              }
            }
          }]
        ]
      },
      cryptoHeaders: [
        {
          sortable: false,
          text: 'Name',
          value: 'name'
        },
        {
          sortable: false,
          text: 'Price',
          value: 'price'
        },
        {
          sortable: false,
          text: 'Change',
          value: 'change',
        },
        {
          sortable: false,
          text: 'Percent Change',
          value: 'percentChange',
          align: 'right'
        }
      ],
      cryptoItems: [
        {
          name: 'Exchange Union USD',
          price: '0.6026',
          change: '0.0512',
          percentChange: '9.29'
        }
      ],
      headers: [
        {
          sortable: false,
          text: 'Name',
          value: 'name'
        },
        {
          sortable: false,
          text: 'Price',
          value: 'price'
        },
        {
          sortable: false,
          text: 'Change',
          value: 'change',
        },
        {
          sortable: false,
          text: 'Volume',
          value: 'volume',
          align: 'right'
        }
      ],
      items: [],
      tabs: 0,
      list: {
        0: false,
        1: false,
        2: false
      }
    }
  },
  methods: {
    complete (index) {
      this.list[index] = !this.list[index]
    },
    getStocks: function () {
    var self = this
    const url = 'http://localhost:8000/stocks/'
    axios.get(url, {
      dataType: 'json',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
    })
    .then(response => {
       
      console.log(response.data)
      self.items = response.data

      
    })
    .catch(error => {
      console.log(error)
    })
    }
  }
}
</script>
