<template>
  <v-card>
    <v-card-title>{{ current_test_name }}</v-card-title>
    <!--Loading circle-->
    <div
      class="loading-circle-custom"
      v-if="test_details.count == null">
      <v-progress-circular
        class="mb-6"
        :size="70"
        :width="7"
        color="#00549a"
        indeterminate/>
    </div>
    <div v-else>
      <v-card-text>
        <v-row
          align="center"
          class="mx-0">
          <!--Status-->
          <v-chip
            class="extend-chip-width-icon"
            v-if="test_details.results[0].stateid.name == 'Success'"
            color="green"
            dark
          >
            <v-avatar left>
              <v-icon>mdi-checkbox-marked-circle</v-icon>
            </v-avatar>
            {{ test_details.results[0].stateid.name }}
          </v-chip>
          <v-chip
            class="extend-chip-width-icon"
            v-else-if="test_details.results[0].stateid.name == 'Warning'"
            color="orange"
            dark
          >
            <v-avatar left>
              <span class="material-icons">warning</span>
            </v-avatar>
            {{ test_details.results[0].stateid.name }}
          </v-chip>
          <v-chip
            class="extend-chip-width-icon"
            v-else-if="test_details.results[0].stateid.name == 'Failed'"
            color="red"
            dark
          >
            <v-avatar left>
              <span class="material-icons">error</span>
            </v-avatar>
            {{ test_details.results[0].stateid.name }}
          </v-chip>
          <v-spacer/>
        </v-row>
        <v-divider class="mt-2 mb-2 ml-2 mx-4"/>
        <!--AgentHostName-->
        <div
          data-cy='host-name'
          class="my-5 subtitle-1">
          <strong
          >Host Name:</strong>
          {{ test_details.results[0].resultid.agentid.name }}
        </div>
        <div
          data-cy='trigger'
          class="my-5 subtitle-1">
          <strong
          >Trigger:</strong>
          {{ test_details.results[0].triggerid.name }}
        </div>
        <!--Formatted date-->
        <div
          data-cy='start-time'
          class="my-5 subtitle-1">
          <strong>Start:</strong>
          {{ this.format_date_string(test_details.results[0].starttime) }}
        </div>
        <div
          data-cy='end-time'
          class="my-5 subtitle-1">
          <strong >End:</strong>
          {{ this.format_date_string(test_details.results[0].endtime) }}
        </div>
        <!--Calculated duration-->
        <div
          data-cy='duration'
          class="my-5 subtitle-1">
          <strong >Duration:</strong>
          {{ this.get_date_duration(test_details.results[0].starttime,test_details.results[0].endtime) }} seconds
        </div>
      </v-card-text>
      <!-- Client name and Environment-->
      <div class="mb-4 ml-4">
        <v-chip
          class="extend-chip-width"
          color="#00549a"
          dark
        >{{ test_details.results[0].resultid.clientid.name }}</v-chip>&nbsp;
        <v-icon class="right-arrow">keyboard_arrow_right</v-icon>
        <v-chip
          class="extend-chip-width"
          color="#00549a"
          dark
        >{{ test_details.results[0].resultid.technologyid.name }}</v-chip>&nbsp;
        <v-icon class="right-arrow">keyboard_arrow_right</v-icon>
        <v-chip
          class="extend-chip-width"
          color="#00549a"
          dark
        >{{ this.string_formatter(test_details.results[0].resultid.workflowid.name, 'workflow') }}</v-chip>&nbsp;
        <v-icon class="right-arrow">keyboard_arrow_right</v-icon>
        <v-chip
          class="extend-chip-width"
          color="#00549a"
          dark
        >{{ test_details.results[0].resultid.environmentid.name }}</v-chip>
      </div>
      <v-divider class="mx-4"/>
      <v-card-title>Details</v-card-title>
      <!--Conditional view of details based on value.-->
      <v-card-text
        data-cy='detail-none'
        v-if="test_details.results[0].result_detail == ''">No details to show.</v-card-text>
      <v-card-text
        data-cy='detail-not-none'
        v-else>{{ test_details.results[0].result_detail[0].details }}</v-card-text>
    </div>
  </v-card>
</template>

<script>
import moment from 'moment'
import api from '../api'
moment().format()

export default {
  name: 'TestDetails',
  data () {
    return {
      current_test_name: this.$route.params.test,
      test_duration: 0,
      test_details: []
    }
  },
  components: {},
  created () {
    // Initial rest api call to fetch data.
    this.get_test_details()
  },
  methods: {
    // Calls rest api function and saves response to data.
    get_test_details () {
      let id = this.$route.params.test_id
      api
        .get_test_details(id)
        .then(response => {
          this.test_details = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    // Splits date using regex and creates a readable date object
    format_date (datetime) {
      datetime = datetime.replace(/[a-z]/gi, ' ')
      var regex = /(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})/
      var dateArray = regex.exec(datetime)
      var dateObject = new Date(
        +dateArray[1],
        +dateArray[2] - 1, // Careful, month starts at 0!
        +dateArray[3],
        +dateArray[4],
        +dateArray[5],
        +dateArray[6]
      )
      return dateObject
    },
    // Formats a date time into a display string.
    format_date_string (datetime) {
      var dateObject = this.format_date(datetime)
      var formatted = moment(dateObject).format('llll')
      var FromNow = moment(dateObject).fromNow()
      return formatted + ' (' + FromNow + ')'
    },
    // Get duration between 2 formatted datetimes.
    get_date_duration (start, end) {
      var DateObjectStart = this.format_date(start)
      var DateObjectEnd = this.format_date(end)
      var FormattedStart = moment(DateObjectStart)
      var FormattedEnd = moment(DateObjectEnd)
      var duration = moment.duration(FormattedEnd.diff(FormattedStart))
      return Math.round(duration.asSeconds())
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
    }
  },
  watch: {}
}
</script>
<style scoped>
.loading-circle-custom {
  margin-bottom: 10% !important;
  text-align: center !important;
}
.extend-chip-width{
  width: auto !important;
}
.extend-chip-width:hover {
  transform: scale(1) !important;
}
.right-arrow{
  margin-left: -8px !important;
  margin-right: -4px !important;
}
</style>
