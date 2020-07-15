<template>
  <v-card
    width="60%"
    height="80vh"
    class="media-height borderless"
    outlined>
    <v-card-title
      color="#00549a"
      class="sticky-head header">
      <!--Previous browser navigation button-->
      <div data-cy="back-arrow">
        <v-btn
          v-if="this.$route.name == 'Client'"
          disabled
          dark
          icon
          class="mr-10">
          <v-icon class="navigation-arrow">keyboard_arrow_left</v-icon>
        </v-btn>
        <v-btn
          v-else
          @click="route_back()"
          dark
          icon
          class="mr-10">
          <v-icon class="navigation-arrow">keyboard_arrow_left</v-icon>
        </v-btn>
      </div>
      <!--
        Display all current route parameters representing user selections in each section.
        Clicking on a route parameter redirects to the parameter's corresponding section.
        "index" represents the route parameter's name.
        Does not show links for Test id or state.
      -->
      <div
        @click="route_to(index)"
        v-for="(link, index) in this.$route.params"
        :key="index">
        <div
          data-cy="workflow-header"
          v-if="index == 'workflow' && link">
          <a class="link">{{ string_formatter(link, 'workflow') }}</a> /&nbsp;
        </div>
        <div
          data-cy="idkyet-header"
          v-else-if="!(link == undefined) && index !='test_id' && index !='state'"
        >
          <a class="link">{{ link }}</a> /&nbsp;
        </div>
      </div>
      <!--
        Display section name when in its matching route with no chosen parameters.
        Clicking is disabled on this link.
        Formats the name of the Workflow to cleanup from repeated text.
        Does not display navigation links for test ids nor states.
        Hierarchical conditioning.
      -->
      <div
        data-cy="detail-header"
        class="disabled-link"
      >{{ this.$route.name.charAt(0).toUpperCase() + this.$route.name.slice(1) }} &nbsp;</div>
      <v-spacer />
      <!--Next browser navigation button-->
      <v-btn
        data-cy="forward-arrow"
        @click="route_forward()"
        dark
        icon>
        <v-icon class="navigation-arrow">keyboard_arrow_right</v-icon>
      </v-btn>
    </v-card-title>
    <!--Any selected routes will display within the router view-->
    <router-view />
  </v-card>
</template>

<script>
export default {
  name: 'BrowseView',
  data () {
    return {}
  },
  components: {},
  created () {},
  methods: {
    // The following 2 methods navigate routes by 1 step forward or backward.
    route_forward () {
      this.$router.go(1)
    },
    route_back () {
      this.$router.go(-1)
    },
    // Calling the proper route based on the router parameter clicked, to bring the user back to the parameter's section
    route_to (index) {
      this.$router.push({
        name: index,
        params: this.defined_parameters(index)
      })
    },
    // Returns defined route parameters based on route name.
    defined_parameters (route) {
      var DefinedParameters = [
        {
          client: {},
          technology: { client: this.$route.params.client },
          workflow: {
            client: this.$route.params.client,
            technology: this.$route.params.technology
          },
          test: {
            client: this.$route.params.client,
            technology: this.$route.params.technology,
            workflow: this.$route.params.workflow,
            state: this.$route.params.state
          }
        }
      ]
      return DefinedParameters[0][route]
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
.header {
  width: 100%;
  background: #00549a;
  color: white;
}
.link,
.disabled-link {
  color: white;
  font-weight: 300;
  text-decoration: none;
  cursor: pointer;
}
.disabled-link {
  font-weight: 500;
}
.link:hover {
  text-decoration: underline;
}
.link:active {
  transform: scale(1.1);
}
.borderless {
  border: none !important;
}
.navigation-arrow {
  color: white !important;
}
.sticky-head {
  position: -webkit-sticky !important; /* Safari */
  position: sticky;
  top: 0;
  z-index: 1;
}
.media-height {
  top: 50% !important;
  transform: translateY(-50) !important;
}
</style>
