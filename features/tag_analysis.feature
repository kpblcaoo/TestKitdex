@tag_analysis
Feature: Tag Analysis and AI Suggestions
  As a developer
  I want to get AI-powered tag analysis
  So that I can improve tag organization

  Background:
    Given I have a clean database
    And I have indexed TestKit with various tags
    And the AI analysis engine is trained

  Scenario: AI tag suggestions with hierarchy
    When I request tag suggestions for "user management"
    Then I should get suggestions including "user"
    And I should get suggestions including "registration"
    And I should get suggestions including "profile"
    And suggestions should respect hierarchy

  Scenario: Build tag hierarchy automatically
    When I run tag analysis
    Then the system should suggest tag relationships
    And I should see confidence scores for suggestions
    And I should be able to accept or reject suggestions

  Scenario: Suggest tag improvements
    When I run tag analysis
    Then I should get suggestions for new tags
    And I should get suggestions for tag relationships
    And I should get suggestions for tag consolidation

  Scenario: Analyze tag usage patterns
    When I run tag analysis with usage data
    Then I should see tag usage patterns
    And I should see tag co-occurrence patterns
    And I should see tag evolution trends
    And I should see optimization opportunities

  Scenario: Handle tag conflicts
    Given I have conflicting tag definitions
    When I run tag conflict resolution
    Then I should see conflict resolution options
    And I should be able to choose resolution strategy
    And the system should apply the resolution

  Scenario: AI tag clustering
    When I request tag clustering
    Then I should get semantically similar tag groups
    And each group should have a confidence score
    And I should be able to merge or split groups

  Scenario: Tag quality assessment
    When I run tag quality analysis
    Then I should see quality metrics for each tag
    And I should see suggestions for improvement
    And I should see tags that need attention

  Scenario: Predict tag usage
    When I request tag usage prediction
    Then I should get predictions for tag popularity
    And I should see confidence intervals
    And I should see factors influencing predictions

  Scenario: Handle edge cases gracefully
    Given I request analysis for unknown context
    When I get tag suggestions
    Then I should get general-purpose suggestions
    And I should see confidence scores
    And the system should not crash

  Scenario: Performance of AI analysis
    Given I have 1000+ tags to analyze
    When I run comprehensive tag analysis
    Then the analysis should complete within 30 seconds
    And the suggestions should be relevant
    And the system should use efficient algorithms 