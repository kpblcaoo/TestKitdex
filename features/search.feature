@search
Feature: Advanced Search
  As a developer
  I want to search TestKit methods
  So that I can find relevant utilities quickly

  Background:
    Given I have a clean database
    And I have indexed TestKit methods
    And the search index is built
    And I have test data with various tags and methods

  Scenario: Search by tags
    When I search for tags "message" and "factory"
    Then I should get methods tagged with both
    And results should be sorted by relevance_score DESC
    And the first result should have relevance_score >= 0.8
    And I should see method details

  Scenario: Semantic search
    When I search for "create user message"
    Then I should get methods for creating user messages
    And results should include semantic matches
    And results should be sorted by semantic_score DESC
    And the first result should have semantic_score >= 0.7
    And confidence scores should be shown

  Scenario: Filter by return type
    When I search for methods returning "Message"
    Then I should get only methods with Message return type
    And results should be sorted by relevance

  Scenario: Search with pagination
    When I search with limit 5 and offset 10
    Then I should get at most 5 results
    And results should start from the 11th item
    And total count should be provided

  Scenario: Search with pagination edge cases
    When I search with limit 0
    Then I should get an error with code 400
    And the error message should be "Limit must be greater than 0"

    When I search with negative limit
    Then I should get an error with code 400
    And the error message should be "Limit must be positive"

    When I search with offset equal to total count
    Then I should get an empty result set
    And total count should be provided

    When I search with limit greater than maximum allowed
    Then I should get an error with code 400
    And the error message should be "Limit exceeds maximum of 100"

  Scenario: Full-text search
    When I search for "telegram bot"
    Then I should get methods with "telegram" in description
    And I should get methods with "bot" in description
    And results should be ranked by relevance

  Scenario: Search by component category
    When I search for methods in "messaging" category
    Then I should get only methods from messaging components
    And results should include component information

  Scenario: Search with tag inheritance
    Given I have a tag hierarchy with "moderation" as parent
    And "ban" and "warn" are child tags of "moderation"
    When I search for methods with tag "moderation"
    Then I should get methods tagged with "moderation"
    And I should get methods tagged with "ban"
    And I should get methods tagged with "warn"

  Scenario: Search with multiple criteria
    When I search for methods with tags "user,factory" returning "User"
    Then I should get methods matching all criteria
    And results should be ranked by relevance
    And I should see detailed method information

  Scenario: Search performance
    Given I have 10000 indexed methods
    When I search for "message"
    Then I should get results within 100ms
    And results should be relevant
    And search should use indexes efficiently

  Scenario: Search suggestions
    When I type "mess" in the search box
    Then I should see suggestions for "message"
    And I should see suggestions for "messaging"
    And suggestions should be ranked by popularity

  Scenario: Search history
    When I perform multiple searches
    Then my search history should be saved
    And I should see recent searches
    And I should be able to repeat previous searches 