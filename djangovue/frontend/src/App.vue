
<template>
  <v-app id="main">
    <!--Left Drawer-->
    <v-navigation-drawer
      v-model="drawer"
      color="#004f8f"
      app
      clipped
      dark>
      <!--All main pages and their routes.-->
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content @click="router_push('/')">
            <v-list-item-title>Service Monitoring</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-cog</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Settings</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <!--Navigation Bar-->
    <v-app-bar
      app
      clipped-left
      color="#00549a"
      dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"/>
      <img
        class="bell-logo"
        src="./img/bell-logo.png" >
      <v-toolbar-title class="logo-text">USCI</v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container
        class="fill-height"
        fluid>
        <v-row
          align="center"
          justify="center">
          <!--Any active route content will show withing these tags.-->
          <router-view/>
        </v-row>
      </v-container>
    </v-content>

    <!--<v-footer app>
      <span>Last update on {{last_update}}</span>
    </v-footer>-->
  </v-app>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-polyfill/7.8.7/polyfill.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
<script>
import moment from "moment";
moment().format();
export default {
  props: {
    source: String
  },
  data: () => ({
    drawer: null,
    last_update: ""
  }),
  created() {
    // Fetching the last update from api response.
    this.get_last_update();
  },
  methods: {
    // The alternative way of using <router-link>
    router_push(path) {
      this.$router.push(path);
    },
    // TODO: Obtain REST api for last update.
    get_last_update() {
      let response_date = "2020-05-29 00:35:53+00:00";
      var formatted_date = this.format_date(response_date);
      this.last_update = formatted_date;
    },
    // Splits date using regex and creates a readable date object
    format_date(datetime) {
      datetime = datetime.substring(0, datetime.indexOf("+"));
      var regex = /(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})/;
      var dateArray = regex.exec(datetime);
      var dateObject = new Date(
        +dateArray[1],
        +dateArray[2] - 1, // Careful, month starts at 0!
        +dateArray[3],
        +dateArray[4],
        +dateArray[5],
        +dateArray[6]
      );
      var formatted = moment(dateObject).format("dddd D MMMM YYYY hh:mm A");
      return formatted;
    }
  },
  computed: {}
};
</script>

<style>
@import url("./css/global_custom.css");
</style>

<style scoped>
.bell-logo {
  width: 80px;
  margin-left: 8px;
}
.logo-text {
  margin-top: 15px;
  margin-left: 8px;
  font-size: 100%;
  font-weight: 300;
}
span {
  font-size: 15px;
}
</style>
