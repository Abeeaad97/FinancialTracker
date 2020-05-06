<template>
  <v-container
    fill-height
    fluid
    grid-list-xl
  >
    <v-layout wrap>
       <v-flex
        md12
        lg6
      >
      <v-tooltip top>
        <material-card
          color="green"
          slot="activator"
          title="Top Stocks"
          text="Your Top Stocks"
        >
          <v-data-table
            :headers="headers"
            :items="items"
            :items-per-page="5"
            item-key="name"
            class="elevation-1"
            :footer-props="{
              showFirstLastPage: true,
            }"
          >
            <template
              slot="headerCell"
              slot-scope="{ header }"
            >
              <span
                class="font-weight-light text-warning text--darken-3"
                v-text="header.text"
              />
            </template>
            <template
              slot="items"
              slot-scope="{ index, item }"
            >
              <td>{{ item.name }}</td>
              <td>{{ item.price }}</td>
              <td>{{ item.change }}</td>
              <td class="text-xs-right"> {{ item.volume }} </td>
            </template>
          </v-data-table>
        </material-card>
        <span>5 most active stocks immediately shown</span>
        </v-tooltip>
      </v-flex>
      <v-flex
        md12
        lg6
      >
      <v-tooltip top>
        <material-card
          color="red"
          slot="activator"
          title="Cryptocurrency"
          text="Current Crypto Values"
        >
          <v-data-table
            :headers="cryptoHeaders"
            :items="cryptoItems"
            :items-per-page="5"
            item-key="name"
            class="elevation-1"
            :footer-props="{
              showFirstLastPage: true,
            }"
          >
            <template
              slot="headerCell"
              slot-scope="{ header }"
            >
              <span
                class="font-weight-light text-warning text--darken-3"
                v-text="header.text"
              />
            </template>
            <template
              slot="items"
              slot-scope="{ index, item }"
            >
              <td>{{ item.name }}</td>
              <td>{{ item.price }}</td>
              <td>{{ item.change }}</td>
              <td class="text-xs-right"> {{ item.percentChange }} </td>
            </template>
          </v-data-table>
        </material-card>
        <span>5 most active cryptocurrencies immediately shown</span>
        </v-tooltip>
      </v-flex>
      <v-flex
        sm6
        xs12
        md6
        lg3
      >
        <material-stats-card
          color="green"
          icon="mdi-store"
          title="Revenue"
          value="$34,245"
       
        />
      </v-flex>
      <v-flex
        sm6
        xs12
        md6
        lg3
      >
        <material-stats-card
          color="orange"
          icon="mdi-bank"
          title="Avaiable Stocks"
          value="200/500"
        />
      </v-flex>
      <v-flex
        sm6
        xs12
        md6
        lg3
      >
        <material-stats-card
          color="red"
          icon="mdi-coin"
          title="Crypto Trackers"
          value="111/200"
        />
      </v-flex>
      <v-flex
        sm6
        xs12
        md6
        lg3
      >
        <material-stats-card
          color="info"
          icon="mdi-earth"
          title="Indices Increase"
          value="+150"
        />
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
      this.getCrypto()
      console.log('Mounted Got Here')
    },
  data() {
    return {
       dailySalesChart: {
        data: {
          labels: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
          series: [
            [12, 17, 7, 17, 23, 18, 38]
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
      cryptoItems:[
        {
          name: "Bitcoin USD",
          price: "9037.66",
          change: "+38.54",
          percentChange: "+0.43%"
        },
        {
            name: "Ethereum USD",
            price: "209.59",
            change: "+2.90",
            percentChange: "+1.40%"
        },
        {
            name: "XRP USD",
            price: "0.2201",
            change: "+0.0037",
            percentChange: "+1.69%"
        },
        {
            name: "Tether USD",
            price: "1.0043",
            change: "+0.0030",
            percentChange: "+0.30%"
        },
        {
            name: "Bitcoin Cash USD",
            price: "249.44",
            change: "+4.79",
            percentChange: "+1.96%"
        },
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
    getCrypto: function() {
    var self = this
    const url = 'http://localhost:8000/crypto/'
    axios.get(url, {
      dataType: 'json',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
    })
    .then(response => {
      console.log(response.data)
      self.cryptoItems = response.data
    })
    .catch(error => {
      console.log(error)
    })
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
