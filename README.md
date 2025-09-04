# Coin-Game

A simple arcade-style coin collecting game built with Pygame where players collect coins while avoiding enemies.

## Game Description
- Control a character to collect coins and earn points
- Avoid enemies that move around the screen
- Time-limited gameplay with score tracking
- Shoot enemies to clear your path

## How to Play
1. Use arrow keys to move your character
2. Collect coins for points
3. Avoid enemies or shoot them
4. Try to get the highest score before time runs out

## Development Setup
1. Ensure Python and Pygame are installed
2. Clone the repository
3. Run `python main.py` to start the game

## Agile Development with GitHub Projects

This project follows Scrum methodology using GitHub Projects for backlog management. Below is a guide on how we manage our development process:

### Project Views

We use four main views in GitHub Projects:

1. **New Item**
   - New PBI (Product Backlog Item) candidates
   - Items without size estimation
   - Query: `no:size -ready:"Drop"`

2. **Product Backlog**
   - Prioritized list of PBIs
   - Items with size estimation but not dropped
   - Query: `is:open -no:size -ready:"Drop"`

3. **Sprint Backlog**
   - Current sprint items
   - Organized by status (TODO, In Progress, In Review, DONE)
   - Query: `sprint:this`

4. **Completed**
   - Finished PBIs sorted by sprint
   - Query: `is:closed -no:size -ready:"Drop"`

### Issue Fields

Each PBI (issue) contains these custom fields:
- **System**: Which system component the issue affects
- **Title**: User story format (e.g., "As a player, I can collect coins to increase my score")
- **Ready**: Status (Ready, NotReady, Draft, Drop)
- **Ready Condition/Notes**: Required conditions or notes
- **Size**: Fibonacci number (1, 2, 3, 5, 8...)
- **Labels**: Issue type labels
- **Sprint**: Sprint number or "this" for current sprint
- **Status**: For Sprint Backlog organization (TODO, In Progress, In Review, DONE)

### PBI Template

```
## Overview
<!-- Briefly explain the main feature or issue and expected outcomes -->

### What to do

### Why do it

## Acceptance Criteria
<!-- List conditions for completing this PBI. Write as states. -->
- [ ] Criterion 1
- [ ] Criterion 2

## Tasks
<!-- List specific tasks needed to complete this PBI -->
- [ ] Task 1
- [ ] Task 2

## Other
<!-- Related documents, similar PBIs, notes or remarks -->
```

### Workflow

#### Daily Meeting (Refinement + Daily Scrum)
- Check New Items (refine and size if any)
- Confirm Product Backlog priorities
- Review Sprint Backlog for any blockers

#### Sprint Planning
- Select PBIs from Product Backlog by priority
- Add "this" label to selected items for Sprint Backlog
- Plan according to team capacity

#### Completing PBIs
- Update Sprint column to sprint number (e.g., "S1")
- Close the issue after completion
- Item moves to Completed view

For detailed information, see the reference article: [GitHub Projects を使ったバックログ管理](https://dev.classmethod.jp/articles/scrum-backlog-github-projects/)