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
        <material-card
          color="green"
          title="Cryptocurrency Table"
          text="Real-time exchange status of world cryptocurrencies"
        >
          <v-data-table
            :headers="headers"
            :items="items"
            hide-actions
          >
            <template
              slot="headerCell"
              slot-scope="{ header }"
            >
              <span
                class="subheading font-weight-light text-success text--darken-3"
                v-text="header.text"
              />
            </template>
            <template
              slot="items"
              slot-scope="{ item }"
            >
              <td>{{ item.name }}</td>
              <td>{{ item.price }}</td>
              <td>{{ item.change }}</td>
              <td class="text-xs-right"> {{ item.percentChange }} </td>
            </template>
          </v-data-table>
        </material-card>
      </v-flex>
<!--      <v-flex
        md12
      >
        <material-card
          color="green"
          flat
          full-width
          title="Table on Plain Background"
          text="Here is a subtitle for this table"
        >
          <v-data-table
            :headers="headers"
            :items="items.slice(0, 7)"
            hide-actions
          >
            <template
              slot="headerCell"
              slot-scope="{ header }"
            >
              <span
                class="subheading font-weight-light text--darken-3"
                v-text="header.text"
              />
            </template>
            <template
              slot="items"
              slot-scope="{ item }"
            >
              <td>{{ item.name }}</td>
              <td>{{ item.price }}</td>
              <td>{{ item.change }}</td>
              <td class="text-xs-right"> {{ item.percentChange }} </td>
            </template>
          </v-data-table>
        </material-card>
      </v-flex> -->
    </v-layout>
  </v-container>
</template>

<script src="https://unpkg.com/vuetify/dist/vuetify.js"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
import axios from 'axios'

export default {
  mounted: function () {
    this.getCrypto()
    console.log('Mounted Got Here')
  },
  data: () => ({
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
        value: 'change'
      },
      {
        sortable: false,
        text: 'Percent Change',
        value: 'percentChange',
        align: 'right'
      }
    ],
    items: [],
  }),
  methods: {
    getCrypto: function () {
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
      self.items = response.data
    })
    .catch(error => {
      console.log(error)
    })
    }
  }
}
</script>
