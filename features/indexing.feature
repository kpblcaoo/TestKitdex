@indexing
Feature: TestKit Indexing
  As a developer
  I want to index TestKit components
  So that I can search and discover test utilities

  Background:
    Given I have a clean database
    And I have a TestKit directory

  Scenario: Index C# files with tags
    Given I have C# files with tagged methods
    When I run the indexer
    Then it should parse all .cs files
    And extract methods with their tags
    And store them in the database
    And create indexes for fast search

  Scenario: Handle complex tag hierarchies
    Given I have methods with multiple tags
    When I index the methods
    Then it should normalize tag names
    And create tag relationships
    And support tag inheritance

  Scenario: Handle parsing errors gracefully
    Given I have malformed C# files
    When I run the indexer
    Then it should log errors
    And continue processing other files
    And report summary statistics

  Scenario: Extract method signatures correctly
    Given I have a C# method with complex signature
    When I run the indexer
    Then it should extract the full signature
    And preserve parameter types
    And handle generic methods correctly

  Scenario: Process XML documentation
    Given I have methods with XML documentation
    When I run the indexer
    Then it should extract summary descriptions
    And parse custom tags
    And store documentation in the database

  Scenario: Handle different method types
    Given I have static and instance methods
    And I have generic and non-generic methods
    When I run the indexer
    Then it should categorize method types correctly
    And store method metadata
    And create appropriate indexes

  Scenario: Index large TestKit efficiently
    Given I have a TestKit with 1000+ methods
    When I run the indexer
    Then it should complete within 30 seconds
    And use efficient database operations
    And provide progress feedback

  Scenario: Update existing index
    Given I have an existing indexed TestKit
    And I have new or modified files
    When I run the indexer again
    Then it should detect changes
    And update only modified components
    And preserve existing data 