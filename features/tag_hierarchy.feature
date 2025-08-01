@tag_hierarchy
Feature: Tag Hierarchy
  As a developer
  I want to use hierarchical tags
  So that I can find related methods easily

  Background:
    Given I have a clean database
    And I have a tag hierarchy configured
    And "moderation" is a parent tag
    And "ban" and "warn" are child tags of "moderation"

  Scenario: Search with tag inheritance
    When I search for methods with tag "moderation"
    Then I should get methods tagged with "moderation"
    And I should get methods tagged with "ban"
    And I should get methods tagged with "warn"
    And results should be sorted by relevance_score DESC
    And the first result should have relevance_score >= 0.8

  Scenario: Navigate tag hierarchy
    When I explore the tag hierarchy
    Then I should see parent-child relationships
    And I should see sibling relationships
    And I should see related tags
    And I should be able to drill down

  Scenario: Search with complex hierarchies
    Given I have a deep tag hierarchy
    When I search for a top-level tag
    Then I should get methods from all child levels
    And results should be properly ranked
    And I should see hierarchy information

  Scenario: Suggest tag improvements
    When I run "tkx tags suggest"
    Then I should get suggestions for new tags
    And I should get suggestions for tag relationships
    And I should get suggestions for tag consolidation

  Scenario: Validate tag hierarchy
    When I run "tkx tags validate"
    Then I should see validation results
    And I should see circular dependency warnings
    And I should see orphaned tag warnings
    And I should see optimization suggestions

  Scenario: Export tag hierarchy
    When I run "tkx tags export --format graphviz"
    Then I should get a Graphviz file
    And the file should represent the hierarchy
    And I should be able to visualize the graph

  Scenario: Import tag hierarchy
    Given I have a tag hierarchy in JSON format
    When I run "tkx tags import hierarchy.json"
    Then the hierarchy should be imported
    And all relationships should be preserved
    And the system should validate the import

  Scenario: Merge tag hierarchies
    Given I have two different tag hierarchies
    When I run "tkx tags merge hierarchy1.json hierarchy2.json"
    Then the hierarchies should be merged
    And conflicts should be resolved
    And the result should be consistent

  Scenario: Analyze tag usage patterns
    When I run "tkx tags analyze --usage"
    Then I should see tag usage patterns
    And I should see tag co-occurrence patterns
    And I should see tag evolution trends
    And I should see optimization opportunities

  Scenario: Handle tag conflicts
    Given I have conflicting tag definitions
    When I run "tkx tags resolve"
    Then I should see conflict resolution options
    And I should be able to choose resolution strategy
    And the system should apply the resolution

  Scenario: Performance with large hierarchies
    Given I have a hierarchy with 1000+ tags
    When I search using the hierarchy
    Then the search should complete within 50ms
    And the hierarchy should be efficiently traversed
    And memory usage should be optimized 