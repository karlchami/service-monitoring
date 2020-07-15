import Vue from 'vue'
import Router from 'vue-router'
import BrowseView from '@/views/BrowseView'
import Client from '@/components/ClientComponent'
import Technology from '@/components/TechnologyComponent'
import Workflow from '@/components/WorkflowComponent'
import Test from '@/components/TestComponent'
import TestDetails from '@/components/TestDetailsComponent'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '',
      component: BrowseView,
      // BrowseView is the main container for all the other sub views
      children: [
        {
          path: '/',
          name: 'client',
          component: Client
        },
        {
          path: '/client/:client/technology',
          name: 'technology',
          component: Technology
        },
        {
          path: 'client/:client/technology/:technology/workflow',
          name: 'workflow',
          component: Workflow
        },
        {
          path:
            'client/:client/technology/:technology?/workflow/:workflow?/test/:state?',
          name: 'test',
          component: Test
        },
        {
          path:
            'client/:client/technology/:technology?/workflow/:workflow?/test/:test_id/:test/details',
          name: 'details',
          component: TestDetails
        }
      ]
    }
  ]
})
