@suggestions @ai
Feature: AI Suggestions
  As a developer
  I want to get intelligent suggestions for TestKit methods
  So that I can discover relevant utilities quickly

  Background:
    Given I have indexed TestKit with AI capabilities
    And the suggestion engine is trained

  Scenario: Get tag suggestions for context
    Given I have context "I need to create a test user with a message"
    When I request tag suggestions for this context
    Then I should get suggestions including "user"
    And I should get suggestions including "message"
    And suggestions should have confidence scores above 0.8

  Scenario: Get method suggestions for task
    Given I have a task description "create telegram bot test"
    When I request method suggestions for this task
    Then I should get methods related to telegram
    And I should get methods related to bot functionality
    And suggestions should be ranked by relevance

  Scenario: Context-aware method recommendations
    Given I am working on user registration tests
    When I request method suggestions
    Then I should get user-related methods
    And I should get registration-related methods
    And suggestions should include relevant tags

  Scenario: Semantic search with embeddings
    When I search for "send notification to user"
    Then I should get methods for sending messages
    And I should get methods for user notifications
    And results should include semantic matches

  Scenario: Learn from usage patterns
    Given I frequently use methods with "message" tag
    When I request suggestions for a new context
    Then I should get message-related methods prioritized
    And suggestions should reflect my preferences

  Scenario: Suggest related methods
    Given I am looking at a specific method
    When I request related method suggestions
    Then I should get methods with similar functionality
    And I should get methods with related tags
    And suggestions should be contextually relevant

  Scenario: Handle ambiguous queries
    Given I search for "create"
    When I request suggestions for this ambiguous query
    Then I should get suggestions for different creation contexts
    And I should see clarification options
    And suggestions should cover multiple domains

  Scenario: Suggest method combinations
    Given I need to create a complex test scenario
    When I request method combination suggestions
    Then I should get sequences of related methods
    And I should get workflow suggestions
    And combinations should be logically sound

  Scenario: Improve suggestions over time
    Given I provide feedback on suggestions
    When I request suggestions again
    Then the suggestions should be improved
    And the system should learn from my feedback
    And suggestions should be more relevant

  Scenario: Handle edge cases gracefully
    Given I request suggestions for an unknown context
    When I get suggestions
    Then I should get general-purpose suggestions
    And I should see confidence scores
    And the system should not crash

  Scenario: Performance of AI suggestions
    Given I have a complex context
    When I request AI suggestions
    Then I should get suggestions within 500ms
    And the suggestions should be relevant
    And the system should use efficient algorithms 