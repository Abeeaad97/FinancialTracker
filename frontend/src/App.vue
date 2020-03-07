<template>
  <div>
    <button
      type="button"
      name="button"
      @click="getUsers()"
    >
      get users
    </button>
    <table>
      <th>ticker</th>
      <th>price</th>
      <th>change</th>
      <tbody>
        <tr
          v-for="elem in users" :key="elem.key">
          <td> {{ elem.ticker }} </td>
          <td> {{ elem.price }} </td>
          <td> {{ elem.change }} </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      users: []
    }
  },
  methods: {
    getUsers () {
      axios.get('http://localhost:8000/stocks/')
        .then(response => {
          console.log(response.json())
        })
        .catch(error => console.log(error))
    }
  }
}
</script>

<style lang="scss">
@import '@/styles/index.scss';

/* Remove in 1.2 */
.v-datatable thead th.column.sortable i {
  vertical-align: unset;
}
</style>
