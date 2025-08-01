@mcp_api
Feature: MCP API Integration
  As an AI assistant
  I want to query TestKit through MCP
  So that I can suggest relevant methods

  Background:
    Given the MCP server is running
    And I have indexed TestKit data

  Scenario: Get method details via MCP
    When I request method details for ID 123
    Then I should get complete method information
    And it should include all related tags
    And it should include component information

  Scenario: Search methods via MCP
    When I search for methods with tags "message,factory"
    Then I should get a list of matching methods
    And each method should have basic information
    And results should be ranked by relevance

  Scenario: Get tag suggestions via MCP
    When I request tag suggestions for "create user"
    Then I should get relevant tag recommendations
    And each suggestion should have confidence score
    And suggestions should be ranked by relevance

  Scenario: Handle MCP errors gracefully
    When I make an invalid MCP request
    Then I should get an error with code 400
    And the error message should be "Invalid request format"
    And the server should continue working

  Scenario: Context-aware method suggestions
    Given I have context about user management
    When I request method suggestions for this context
    Then I should get methods related to user management
    And suggestions should include relevant tags
    And confidence scores should be provided

  Scenario: Batch MCP operations
    When I request multiple method details at once
    Then I should get all requested method details
    And the response should be efficient
    And error handling should be graceful

  Scenario: MCP server performance
    Given I have 10000 indexed methods
    When I make multiple concurrent MCP requests
    Then all requests should complete within 200ms
    And the server should handle load efficiently
    And no requests should fail due to overload

  Scenario: MCP authentication
    When I make an authenticated MCP request
    Then the request should be processed
    And user context should be preserved
    And access control should be enforced

  Scenario: MCP caching
    When I make the same MCP request multiple times
    Then subsequent requests should be served from cache
    And response times should be faster
    And cache should be invalidated when data changes

  Scenario: MCP streaming responses
    When I request a large dataset via MCP
    Then the response should be streamed
    And memory usage should be efficient
    And the client should receive data incrementally

  Scenario: MCP protocol compliance
    When I use standard MCP protocol methods
    Then the server should respond correctly
    And the response should follow MCP specifications
    And error handling should be protocol-compliant 