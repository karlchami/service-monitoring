import axios from 'axios'

// @ts-ignore
const client = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  headers: { 'Content-Type': 'application/json' }
  // json: true,
})

// TODO change base url before hosting
// const baseUrl = 'http://127.0.0.1:8000/'

// All API calls go here
export default {
  execute (method, resource, data) {
    return client({
      method,
      url: resource,
      data,

      headers: {}
    })
  },
  get_all_client_state () {
    return this.execute('get', 'get_client_state_counts')
  },
  get_technology_state (client) {
    return this.execute('get', `get_technology_state_counts/?client=${client}`)
  },
  get_workflow_state (client, technology) {
    return this.execute(
      'get',
      `get_workflow_state_counts/?client=${client}&technology=${technology}`
    )
  },
  get_test_details (TestId) {
    return this.execute('get', `get_test_by_id/?testid=${TestId}`)
  },
  get_test (client, technology, workflow, state, pagination) {
    // Building a rest api call starting with empty parameters
    let ClientUrl = ''
    let TechnologyUrl = ''
    let WorkflowUrl = ''
    let StateUrl = ''
    let PaginationUrl = ''
    // Create an api parameter from defined method paratemers
    if (client) {
      ClientUrl = '&client=' + client
    }
    if (technology) {
      TechnologyUrl = '&technology=' + technology
    }
    if (workflow) {
      WorkflowUrl = '&workflow=' + workflow
    }
    if (state) {
      StateUrl = '&state=' + state
    }
    // Defines which page of the rest api to show as response.
    // Pagination is set to 5 elements per page so this number should be a multiple of 5.
    if (pagination !== 0) {
      PaginationUrl = '&offset=' + pagination
    }
    // Concat all api parameters
    return this.execute(
      'get',
      `get_test_list/?` +
        ClientUrl +
        TechnologyUrl +
        WorkflowUrl +
        StateUrl +
        PaginationUrl
    )
  }
}
