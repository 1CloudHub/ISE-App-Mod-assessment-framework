# Session 7: Data & DB Assessment

## Overview

Session 7 focuses on the data layer of the legacy application, including database schemas, data models, and data access patterns. This session is critical for understanding data dependencies, identifying data quality issues, and planning data migration strategies.

## Pre-Session Activities

### Assessment Team Preparation

- Reverse engineer DB schemas from shared dumps
- Analyze data access patterns in the codebase
- Identify data volume and growth patterns
- Prepare data model visualization tools

### Customer Team Preparation

- Validate current data model and business critical entities
- Identify data owners and subject matter experts
- Document known data quality issues
- Prepare examples of critical data queries and reports

## Session Activities

### Data Model Analysis

- Document entity relationships and cardinality
- Identify primary and foreign key constraints
- Analyze data normalization/denormalization patterns
- Map business entities to database tables

### Data Access Pattern Review

- Analyze SQL queries and stored procedures
- Identify data access patterns (CRUD operations)
- Document transaction boundaries
- Assess performance of critical queries

### Data Migration Considerations

- Identify data migration challenges
- Document data transformation requirements
- Assess data quality and cleansing needs
- Define data governance requirements

## Deliverables

### Data Design Document

The Data Design Document includes:
- Current data model documentation
- Data access patterns and anti-patterns
- Data quality assessment
- Data volume and growth projections
- Data migration strategy recommendations
- Data governance recommendations

### ERD Diagrams

The Entity Relationship Diagrams visualize:
- Database tables and views
- Entity relationships and cardinality
- Key constraints and indexes
- Data domains and types

## Modernization Considerations

The session also addresses specific data modernization considerations:

- Relational to NoSQL migration opportunities
- Polyglot persistence strategies
- Data partitioning and sharding approaches
- Caching strategies
- Data access layer modernization

## Next Steps

- Prepare for external integrations review in Session 8
- Identify data entities that could benefit from different storage technologies
- Document data migration test cases
- Distribute data design documentation for stakeholder review