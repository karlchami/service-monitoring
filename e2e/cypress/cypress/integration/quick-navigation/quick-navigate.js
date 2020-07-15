describe("Navigate to Details Section", () => {
  it("Navigates through all sections.", () => {
    const generateUrl = (p) => {
      var UrlCondition = "";
      var state = "";
      for (var i = 0; i < p.length; i++) {
        if ([i]) {
          UrlCondition = UrlCondition + "&" + p[i].name + "=" + p[i].value;
          if (p[i].name == "state") state = p[i].value;
        }
      }
      return {
        method: "GET",
        url: `**/get_test_list/?${UrlCondition}`,
        response: `fixture:component_test/get_specific_data/test.${state}.json`,
      };
    };

    // Let cypress know we are using stubs
    cy.server();

    let params_client_technology_pass = [
      { name: "client", value: "CIBC" },
      { name: "technology", value: "Genesys" },
      { name: "state", value: "Success" },
    ];
    let params_client_fail = [
      { name: "client", value: "CIBC" },
      { name: "state", value: "Failed" },
    ];
    let params_client_technology_workflow_pass = [
      { name: "client", value: "CIBC" },
      { name: "technology", value: "Genesys" },
      { name: "workflow", value: "CIBC : PROD - Genesys - Sanity Check" },
      { name: "state", value: "Success" },
    ];
    cy.route(generateUrl(params_client_technology_pass)).as(
      "params_client_technology_pass"
    );
    cy.route(generateUrl(params_client_fail)).as("params_client_fail");
    cy.route(generateUrl(params_client_technology_workflow_pass)).as(
      "params_client_technology_workflow_pass"
    );
    cy.route(
      "**/get_client_state_counts",
      "fixture:component_test/get_name_filter/client.json"
    ).as("getClient");

    // TODO: Should make this into an env variable eventually
    cy.visit("localhost:8080");
    cy.wait("@getClient");

    // Route to quick view Failed Client Tests
    cy.visit("localhost:8080/client/CIBC/technology/workflow/test/Failed");
    // Link api call to fixture
    cy.wait("@params_client_fail");
    // Verify presence of elements first row
    cy.get("tbody > tr > :nth-child(1)").contains("GI2Servers");
    cy.get(".extend-chip-width-icon > .v-chip__content").contains("Failed");

    // Route to quick view Success Technology Tests
    cy.visit(
      "http://localhost:8080/client/CIBC/technology/Genesys/workflow/test/Success"
    );
    // Link api call to fixture
    cy.wait("@params_client_technology_pass");
    // Verify presence of elements first row
    cy.get("tbody > tr > :nth-child(1)").contains("GA - Alarms");
    cy.get(":nth-child(1) > :nth-child(2) > .extend-chip-width-icon").contains(
      "Success"
    );

    // Route to quick view Success Workflow Tests
    cy.visit(
      "http://localhost:8080/client/CIBC/technology/Genesys/workflow/CIBC%20:%20PROD%20-%20Genesys%20-%20Sanity%20Check/test/Success"
    );
    // Link api call to fixture
    cy.wait("@params_client_technology_workflow_pass");
    // Verify presence of elements first row
    cy.get("tbody > tr > :nth-child(1)").contains("GA - Alarms");
    cy.get(":nth-child(1) > :nth-child(2) > .extend-chip-width-icon").contains(
      "Success"
    );
  });
});
