@diff
Feature: TestKit Diff
  As a developer
  I want to see changes in TestKit
  So that I can track evolution and impact

  Background:
    Given I have a clean database
    And I have two TestKit databases: old.db and new.db
    And the databases contain indexed methods
    And I have test data with various changes

  Scenario: Compare TestKit states
    When I compare two databases
    Then I should see added methods
    And I should see removed methods
    And I should see modified method signatures
    And I should see new tags
    And the output should be in markdown format

  Scenario: Generate diff for CI
    When I compare two databases and save to file
    Then a diff.md file should be created
    And it should contain change summary
    And it should be suitable for PR comments

  Scenario: Handle empty changes
    Given both databases are identical
    When I compare two databases
    Then I should see "No changes detected"
    And the exit code should be 0

  Scenario: Detect method signature changes
    Given a method signature has changed
    When I run "tkx diff old.db new.db"
    Then I should see the old signature
    And I should see the new signature
    And I should see what changed

  Scenario: Track tag evolution
    Given new tags have been added
    And some tags have been removed
    When I run "tkx diff old.db new.db"
    Then I should see added tags
    And I should see removed tags
    And I should see tag usage statistics

  Scenario: Detect line number changes
    Given method line numbers have changed due to refactoring
    When I run "tkx diff old.db new.db"
    Then I should see line number changes
    And I should identify refactoring patterns
    And I should show impact analysis

  Scenario: Compare large TestKit efficiently
    Given I have TestKit with 10000+ methods
    When I run "tkx diff old.db new.db"
    Then the comparison should complete within 5 seconds
    And memory usage should be efficient
    And progress should be shown

  Scenario: Generate detailed diff report
    When I run "tkx diff old.db new.db --detailed"
    Then I should see detailed change information
    And I should see before/after comparisons
    And I should see impact analysis
    And I should see recommendations

  Scenario: Handle corrupted databases gracefully
    Given one of the databases is corrupted
    When I run "tkx diff old.db new.db"
    Then I should get a clear error message
    And the exit code should be non-zero
    And the system should not crash

  Scenario: Diff with specific filters
    When I run "tkx diff old.db new.db --tags message,user"
    Then I should see only changes related to message and user tags
    And other changes should be filtered out
    And the output should be focused

  Scenario: Generate diff statistics
    When I run "tkx diff old.db new.db --stats"
    Then I should see summary statistics
    And I should see change percentages
    And I should see trend analysis
    And I should see recommendations 