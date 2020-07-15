describe("Navigate to Details Section", () => {
  it("Navigates through all sections.", () => {
    // Let cypress know we are using stubs
    cy.server();

    //Dynamic parameters for routes and fixtures
    const genTest = (id) => {
      return {
        method: "GET",
        url: `**/get_test_by_id/?testid=${id}`,
        response: `fixture:component_test/get_test_by_id/${id}.json`,
      };
    };

    const genGen = (lastPage) => {
      return {
        method: "GET",
        url: `**/get_test_list/?&client=CIBC&technology=Genesys&workflow=CIBC : PROD - Genesys - Sanity Check${
          lastPage ? "&offset=10" : ""
        }`,
        response: `fixture:component_test/get_specific_data/client.technology.workflow.genesys${
          lastPage ? "2" : "1"
        }.json`,
      };
    };

    cy.route(
      "**/get_client_state_counts",
      "fixture:component_test/get_name_filter/client.json"
    ).as("getClient");
    cy.route(
      "**/get_technology_state_counts/?client=CIBC",
      "fixture:component_test/get_name_filter/client.technology.json"
    ).as("getCIBC");
    cy.route(
      "**/get_workflow_state_counts/?client=CIBC&technology=Genesys",
      "fixture:component_test/get_name_filter/client.technology.workflow.json"
    ).as("getWorkflow");
    cy.route(genGen(false)).as("getGen1");
    cy.route(genTest(115)).as("getTest115");
    cy.route(genTest(117)).as("getTest117");
    cy.route(genGen(true)).as("getGen2");

    // TODO: Should make this into an env variable eventually
    cy.visit("localhost:8080");

    cy.wait("@getClient");
    // Clicks 1st row of client table
    cy.get("[data-cy=client-table]").get("tr").eq(1).click();

    cy.wait("@getCIBC");
    // Clicks 1st row of technology table
    cy.get("[data-cy=technology-table]").get("tr").eq(1).click();

    cy.wait("@getWorkflow");
    // Clicks first row of workflow table
    cy.get("[data-cy=workflow-table]").get("tr").eq(1).click();

    cy.wait("@getGen1");

    // Clicks first row of workflow table
    cy.get("[data-cy=test-table]").get("tr").eq(1).click();

    cy.wait("@getTest117");

    // Verify is data is present and correct
    cy.get("[data-cy=host-name]").contains("PCBEVDAPRGTLS01");
    cy.get("[data-cy=trigger]").contains("Manual");
    cy.get("[data-cy=start-time]").contains("Tue, Jul 7, 2020 6:45 AM");
    cy.get("[data-cy=end-time]").contains("Tue, Jul 7, 2020 6:47 AM");
    cy.get("[data-cy=duration]").contains("72 seconds");
    cy.get("[data-cy=detail-not-none]").contains(
      "PCBELEPPRGII01.ConnectionServer: Initializing - Disabled <br/>PCBEVDAPRGII01.ConnectionServer32: Initializing - Disabled <br/>"
    );


    cy.go("back");
    cy.wait("@getGen1");
    cy.get(".v-pagination__item").last().click();
    cy.wait("@getGen2");
    cy.get("[data-cy=test-table]").get("tr").eq(1).click();
    
    // Verify is data is present on last page click
    cy.get("[data-cy=host-name]").contains("PCBEVDAPRGTLS01");
    cy.get("[data-cy=trigger]").contains("Manual");
    cy.get("[data-cy=start-time]").contains("Tue, Jul 7, 2020 6:35 AM");
    cy.get("[data-cy=end-time]").contains("Tue, Jul 7, 2020 6:38 AM");
    cy.get("[data-cy=duration]").contains("153 seconds");
    cy.get("[data-cy=detail-none]").contains("No details to show.");


  });
});
