<template>
  <div>
    <!--Search Bar-->
    <v-card-title class="search-section">
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      />
    </v-card-title>
    <!--Table containing workflow information-->
    <v-data-table
      data-cy='workflow-table'
      :loading="loading"
      :headers="headers"
      :items="workflow"
      :search="search"
      class="elevation-1 custom"
      @click:row="handleClick"
      @page-count="pageCount = $event"
      hide-default-footer
    >
      <v-spacer/>
      <!--
        Evnironment tag.
        State counts.
        Disabled if count is 0.
        On click: Routes to a test list using a state parameter.
      -->
      <template v-slot:item.workflow="{ item }">{{ string_formatter(item.workflow, 'workflow') }}</template>
      <template
        v-slot:item.environment="{ item }"
        class="extend-chip-width"
        color="#00549a">
        <v-chip
          class="extend-chip-width"
          color="#00549a"
          dark
        >{{ string_formatter(item.workflow, 'environment') }}</v-chip>
      </template>
      <template v-slot:item.Success="{ item }">
        <v-chip
          disabled
          v-if="item.Success == 0"
          dark>{{ item.Success }}</v-chip>
        <v-chip
          v-else
          @click="quick_test_view(item, 'Success')"
          color="green"
          :data-cy="ChipCounter('green', item.id)"
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
          @click="quick_test_view(item, 'Warning')"
          color="orange"
          :data-cy="ChipCounter('orange', item.id)"
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
          @click="quick_test_view(item, 'Failed')"
          color="red"
          :data-cy="ChipCounter('red', item.id)"
          dark
        >{{ item.Failed }}</v-chip>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import api from '../api'

export default {
  name: 'Workflow',
  data () {
    return {
      search: '',
      loading: false,
      // Define table column names and their references.
      headers: [
        {
          text: 'Workflow',
          align: 'start',
          sortable: true,
          value: 'workflow'
        },
        { text: 'Environment', value: 'environment' },
        { text: 'Passed', value: 'Success' },
        { text: 'Warning', value: 'Warning' },
        { text: 'Failed', value: 'Failed' }
      ],
      workflow: []
    }
  },
  components: {},
  created () {
    // Api call to retrieve workflow and state count list.
    this.fetch_workflow_state(
      this.$route.params.client,
      this.$route.params.technology
    )
  },
  methods: {
    // Fetch data from rest api and save to local component variable.
    fetch_workflow_state (client, technology) {
      this.loading = true
      api
        .get_workflow_state(client, technology)
        .then(response => {
          this.workflow = response.data
          this.loading = false
        })
        .catch(error => {
          console.log(error)
        })
    },
    // Pushing to sibling router Test
    handleClick (value) {
      this.$router.push({
        name: 'test',
        params: {
          client: this.$route.params.client,
          technology: this.$route.params.technology,
          workflow: value.workflow
        }
      })
    },
    // Formatting workflow name (containing client, technology, and environment in the same string).
    string_formatter (name, field) {
      // Split workflow name and environment
      var x = name.split(':')
      // Split environment and technology/workflow
      var y = x[1].split('-')

      if (field === 'environment') {
        return y[0]
      } else if (field === 'workflow');
      return y[2]
    },
    // Pushing sibling router Test.
    quick_test_view (item, state) {
      this.$router.push({
        name: 'test',
        params: {
          client: this.$route.params.client,
          technology: this.$route.params.technology,
          workflow: item.workflow,
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
.extend-chip-width:hover {
  transform: scale(1);
}
</style>
