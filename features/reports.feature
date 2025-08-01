@reports
Feature: TestKit Reports
  As a team lead
  I want to see TestKit usage reports
  So that I can optimize test utilities

  Background:
    Given I have indexed TestKit with usage data
    And the database contains usage metrics

  Scenario: Generate usage report
    When I generate a usage report
    Then I should see top 10 used tags
    And I should see unused methods
    And I should see coverage by domain
    And the report should be in markdown format

  Scenario: Generate coverage report
    When I generate a coverage report
    Then I should see coverage percentages by domain
    And I should see methods with low coverage
    And I should see recommendations for improvement

  Scenario: Generate trends report
    When I generate a trends report
    Then I should see usage trends over time
    And I should see emerging patterns
    And I should see declining patterns
    And the report should include an SVG heat-map

  Scenario: Identify unused methods
    Given I have methods that are never used
    When I run "tkx report unused"
    Then I should see a list of unused methods
    And I should see last usage dates
    And I should see recommendations for cleanup

  Scenario: Analyze tag quality
    When I run "tkx report tags"
    Then I should see tag usage statistics
    And I should see tag quality metrics
    And I should see suggestions for tag improvements

  Scenario: Generate performance report
    When I run "tkx report performance"
    Then I should see search performance metrics
    And I should see indexing performance metrics
    And I should see API response times
    And I should see optimization recommendations

  Scenario: Export report data
    When I run "tkx report usage --export json"
    Then I should get a JSON file with report data
    And the data should be structured
    And the data should be machine-readable

  Scenario: Generate custom reports
    Given I want to focus on messaging domain
    When I run "tkx report usage --domain messaging"
    Then I should see usage statistics for messaging only
    And I should see messaging-specific insights
    And I should see domain-specific recommendations

  Scenario: Track method complexity
    When I run "tkx report complexity"
    Then I should see complexity metrics for methods
    And I should see methods that are too complex
    And I should see refactoring suggestions

  Scenario: Analyze test coverage patterns
    When I run "tkx report coverage --detailed"
    Then I should see detailed coverage analysis
    And I should see coverage gaps
    And I should see suggestions for improving coverage

  Scenario: Generate team usage report
    When I run "tkx report team"
    Then I should see usage patterns by team members
    And I should see collaboration metrics
    And I should see knowledge sharing opportunities

  Scenario: Handle large datasets efficiently
    Given I have 100000+ usage records
    When I run "tkx report usage"
    Then the report should generate within 10 seconds
    And memory usage should be efficient
    And the report should be accurate

  Scenario: Generate actionable insights
    When I run "tkx report insights"
    Then I should see actionable recommendations
    And I should see priority suggestions
    And I should see impact analysis
    And I should see implementation guidance 