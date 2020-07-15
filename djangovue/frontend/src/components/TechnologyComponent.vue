<template>
  <div>
    <!--Search Bar-->
    <v-card-title class="search-section">
      <v-text-field
        data-cy='technology-search'
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      />
    </v-card-title>
    <!--Table containing technology information-->
    <v-data-table
      data-cy='technology-table'
      :loading="loading"
      :headers="headers"
      :items="technology"
      :search="search"
      class="elevation-1 custom"
      @click:row="handleClick"
      @page-count="pageCount = $event"
      hide-default-footer
    >
      <v-spacer/>
      <!--
        State counts
        Disabled if count is 0.
        On click: Routes to Test Technology using a state parameter.
      -->
      <template v-slot:item.Success="{ item }">
        <v-chip
          disabled
          v-if="item.Success == 0"
          dark>{{ item.Success }}</v-chip>
        <v-chip
          v-else
          color="green"
          :data-cy="ChipCounter('green', item.id)"
          @click="quick_test_view(item, 'Success')"
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
          color="orange"
          :data-cy="ChipCounter('orange', item.id)"
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
          color="red"
          :data-cy="ChipCounter('red', item.id)"
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
  name: 'Technology',
  data () {
    return {
      search: '',
      loading: null,
      // Define table column names and their references.
      headers: [
        {
          text: 'Technology',
          align: 'start',
          sortable: true,
          value: 'technology'
        },
        { text: 'Passed', value: 'Success' },
        { text: 'Warning', value: 'Warning' },
        { text: 'Failed', value: 'Failed' }
      ],
      technology: []
    }
  },
  components: {},
  created () {
    // Api call to retrieve technology and state count list.
    this.fetch_technology_state(this.$route.params.client)
  },
  methods: {
    // Fetch data from rest api and save to local component variable.
    fetch_technology_state (client) {
      this.loading = true
      api
        .get_technology_state(client)
        .then(response => {
          this.technology = response.data
          // console.log(this.technology)
          this.loading = false
        })
        .catch(error => {
          console.log(error)
        })
    },
    // Pushing to sibling router Workflow.
    handleClick (value) {
      this.$router.push({
        name: 'workflow',
        params: {
          client: this.$route.params.client,
          technology: value.technology
        }
      })
    },
    // Pushing sibling router Test.
    quick_test_view (item, state) {
      this.$router.push({
        name: 'test',
        params: {
          client: this.$route.params.client,
          technology: item.technology,
          state: state
        }
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
