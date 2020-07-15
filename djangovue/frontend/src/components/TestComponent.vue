<template>
  <div>
    <v-card-title class="search-section">
      <!--Test Counts-->
      <v-chip
        v-if="count == 1"
        color="#00549a"
        class="mt-5 extend-chip-width"
        dark
      >{{ count }} {{ this.$route.params.state }}</v-chip>
      <v-chip
        v-else-if="this.$route.params.state == undefined"
        color="#00549a"
        class="mt-5 extend-chip-width"
        dark
      >{{ count }} tests</v-chip>
      <v-chip
        v-else
        color="#00549a"
        class="mt-5 extend-chip-width"
        dark
      >{{ count }} {{ this.$route.params.state }}</v-chip>
      <v-spacer />
      <!--Search Bar-->
      <v-text-field
        data-cy='test-search'
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      />
    </v-card-title>
    <!--Table containing test information-->
    <v-data-table
      data-cy='test-table'
      :loading="loading"
      :headers="headers"
      :items="test.results"
      :items-per-page="items_per_page"
      :search="search"
      class="elevation-1 custom"
      @click:row="handleClick"
      hide-default-footer
    >
      <v-spacer />
      <!--Success, Warning, or Failed tag based on value.-->
      <template v-slot:item.state="{ item }">
        <v-chip
          class="extend-chip-width-icon"
          v-if="item.state == 'Success'"
          color="green"
          dark>
          <v-avatar left>
            <v-icon>mdi-checkbox-marked-circle</v-icon>
          </v-avatar>
          {{ item.state }}
        </v-chip>
        <v-chip
          class="extend-chip-width-icon"
          v-else-if="item.state == 'Warning'"
          color="orange"
          dark
        >
          <v-avatar left>
            <span class="material-icons">warning</span>
          </v-avatar>
          {{ item.state }}
        </v-chip>
        <v-chip
          class="extend-chip-width-icon"
          v-else-if="item.state == 'Failed'"
          color="red"
          dark>
          <v-avatar left>
            <span class="material-icons">error</span>
          </v-avatar>
          {{ item.state }}
        </v-chip>
      </template>
    </v-data-table>
    <br >
    <!--
      Pagination only if response returns more than 1 page.
      On pagination left or right click, call next/previous page api.
    -->
    <v-pagination
      data-cy='test-table-pagination'
      v-if="pageCount != 1"
      color="#00549a"
      v-model="page"
      :length="pageCount"
      @input="navigate_pagination"
      :total-visible="5"
    />
  </div>
</template>

<script>
import api from '../api'

export default {
  name: 'Test',
  data () {
    return {
      // Test result count.
      count: 0,
      page: 1,
      pageCount: 0,
      // Matching with backend defined pagination number.
      items_per_page: 5,
      search: '',
      loading: false,
      // Define table column names and their references.
      headers: [
        {
          text: 'Test',
          align: 'start',
          sortable: true,
          value: 'test_name'
        },
        { text: 'State', value: 'state' }
      ],
      test: []
    }
  },
  components: {},
  created () {
    // Get test of pagination 0 aka page 0.
    this.get_test(0)
  },
  methods: {
    // Uses the self-building api function by passing a specific pagination number.
    get_test (pagination) {
      let client = this.$route.params.client
      let technology = this.$route.params.technology
      let workflow = this.$route.params.workflow
      let state = this.$route.params.state
      this.loading = true
      api
        .get_test(client, technology, workflow, state, pagination)
        .then(response => {
          this.test = response.data
          this.pageCount = Math.ceil(this.test.count / this.items_per_page)
          this.count = this.test.count
          this.loading = false
        })
        .catch(error => {
          console.log(error)
        })
    },
    // Routing to Test Details based on quick view route.
    handleClick (value) {
      this.$router.push({
        name: 'details',
        params: {
          client: this.$route.params.client,
          technology: this.$route.params.technology,
          workflow: this.$route.params.workflow,
          state: this.$route.params.state,
          test: value.test_name,
          test_id: value.test_id
        }
      })
    },
    // Calls api function with pagination as multiple of 5 (agreed pagination number).
    // Page is decremented by 1 as the default pagination for the api is 0 and lowest page value in this component is 1.
    navigate_pagination (page) {
      this.get_test((page - 1) * 5)
    }
  },
  watch: {}
}
</script>
<style scoped>
.extend-chip-width {
  width: 100px !important;
}
.extend-chip-width:hover {
  transform: scale(1);
}
</style>
