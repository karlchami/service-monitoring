<template>
  <div>
    <!--Search Bar-->
    <v-card-title class="search-section">
      <v-text-field
        data-cy='client-search'
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      />
    </v-card-title>
    <!--Table containing client information-->
    <v-data-table
      data-cy='client-table'
      :loading="loading"
      :headers="headers"
      :items="client"
      :search="search"
      class="elevation-1 custom"
      @click:row="handleClick"
      @page-count="pageCount = $event"
      hide-default-footer
    >
      <v-spacer />
      <!--
        State counts
        Disabled if count is 0.
        On click: Routes to Test Client using a state parameter.
      -->
      <template
        :data-cy="ChipCounter('green', item.id)"
        v-slot:item.Success="{ item }">
        <v-chip
          disabled
          v-if="item.Success == 0"
          dark>{{ item.Success }}</v-chip>
        <v-chip

          v-else
          color="green"
          @click="quick_test_view(item, 'Success' )"
          dark
        >{{ item.Success }}</v-chip>
      </template>
      <template v-slot:item.Warning="{ item }">
        <v-chip
          disabled
          v-if="item.Warning == 0"
          dark>{{ item.Warning }}</v-chip>
        <v-chip
          v-else
          :data-cy="ChipCounter('orange', item.id)"
          color="orange"
          @click="quick_test_view(item, 'Warning')"
          dark
        >{{ item.Warning }}</v-chip>
      </template>
      <template v-slot:item.Failed="{ item }">
        <v-chip
          disabled
          v-if="item.Failed == 0"
          dark>{{ item.Failed }}</v-chip>
        <v-chip
          v-else
          :data-cy="ChipCounter('red', item.id)"
          color="red"
          @click="quick_test_view(item, 'Failed')"
          dark
        >{{ item.Failed }}</v-chip>
      </template>
    </v-data-table>
  </div>
</template>
<script>
import api from '../api'

export default {
  name: 'Client',
  data () {
    return {
      search: '',
      loading: false,
      // Define table column names and their references.
      headers: [
        {
          text: 'Client',
          align: 'start',
          sortable: true,
          value: 'client'
        },
        { text: 'Passed', value: 'Success' },
        { text: 'Warning', value: 'Warning' },
        { text: 'Failed', value: 'Failed' }
      ],
      client: []
    }
  },
  components: {},
  created () {
    // Api call to retrieve client and state count list.
    this.fetch_all_client_state()
  },
  methods: {
    // Fetch data from rest api and save to local component variable.
    fetch_all_client_state () {
      this.loading = true
      api
        .get_all_client_state()
        .then(response => {
          this.client = response.data
          // console.log(this.client)
          this.loading = false
        })
        .catch(error => {
          console.log(error)
        })
    },
    // Pushing to sibling router Technology.
    handleClick (value) {
      this.$router.push({
        name: 'technology',
        params: { client: value.client }
      })
    },
    // Pushing to sibling router Test.
    quick_test_view (item, state) {
      this.$router.push({
        name: 'test',
        params: { client: item.client, state: state }
      })
    },
    ChipCounter (color, id) {
      return color + '-chip-' + id
    }
  },
  watch: {}
}
</script>
<style scoped>
</style>
