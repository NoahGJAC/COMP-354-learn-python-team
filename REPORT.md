# Software Configuration Management with Git and GitHub

## Team Information

Include:
- Names and student IDs of all four team members.
- GitHub usernames.
- Assigned responsibilities.

| Name | ID | Github Username | Assigned Responsibilities |
|------|----|-----------------|---------------------------|
| Noah Groleau | 40312953 | NoahGJAC | Repository Maintainer (Student A) and Student D due to team of 3 |
---

### GitHub Repositories

- Original Repo: `https://github.com/NoahGJAC/COMP-354-learn-python-team`
- The URLs of forked repos for
  - Student B: `https://github.com/DanielHaselock/COMP-354-learn-python-team`
  - Student C: `https://github.com/vonAdlee/COMP-354-learn-python-team`

---

## Generative AI Use Disclosure

**GenAI Level 1 — Limited AI Use**

TODO

---

## Part A — Repository Setup and Forking

### Step 1 — Create the Original Repository

![Initial Git Repository](./docs/screenshots/InitialRepo.png)
*Creation of the original repository and its initial commits.*

### Step 2 — Fork and Clone
TODO: Each student must understand the difference between the `origin` and `upstream` remotes.

### Step 3 — Synchronize the Forks
TODO: In your report, briefly explain the difference between `origin` and `upstream` and describe how the synchronization was performed.

---

## 5. Part B — Collaborative Development and Pull Requests

Each team member must improve a different part of the existing Python learning project. The assigned responsibilities are:

| Student | Project Area | Assigned Responsibility |
|---------|--------------|-------------------------|
| A | `src/data_types/test_lists.py` | Add at least two new examples or test cases demonstrating Python list operations, such as sorting, filtering, slicing, or list comprehensions. |
| B | `src/data_types/test_dictionaries.py` | Add at least two new examples or test cases demonstrating dictionary operations, such as adding, updating, removing, or retrieving entries. |
| C | `src/control_flow/test_if.py` | Add at least two new examples or test cases demonstrating conditional statements, including nested conditions or multiple `elif` branches. |
| A | `src/functions/test_function_definition.py` | Add at least two new examples or test cases demonstrating function definitions, parameters, return values, or simple input validation. |

### Development Requirements

Each student must:

1. Create a separate development branch for the assigned task.
2. Examine the existing code and follow its general structure and conventions.
3. Implement the assigned improvements.
4. Add appropriate assertions or tests to demonstrate the expected behavior.
5. Execute the relevant tests and verify that the changes work correctly.
6. Create at least two meaningful commits describing the development work.

> The modifications should be relatively small but meaningful. The objective is to demonstrate a professional collaborative workflow, not to rewrite the existing project.

### Pull Request Workflow

**Students B, and C must:**

1. Push their development branches to their respective GitHub forks.
2. Open pull requests targeting Student A's original repository.

**Student A must also:**

1. Implement the assigned changes in a separate development branch.
2. Open a pull request from that branch into the `main` branch of the original repository.

### Code Review Requirements

For all four pull requests:

1. Another team member must review the proposed changes.
2. The reviewer must inspect the modified files.
3. The reviewer must provide at least one meaningful review comment.
4. Any identified issues should be addressed before merging.
5. The team must merge the contributions into the original repository.

Each pull request must contain:

- A meaningful title.
- A brief description of the modifications.
- An explanation of how the changes were tested.

> **Important:** Simply pushing changes directly to the `main` branch does not satisfy the pull request requirements.

---

## 6. Part C — Merge Conflict Challenge (30%)

After completing Part B, the team must deliberately create and resolve two merge conflicts using the existing Python project. The conflicts must involve overlapping modifications to the same lines of code.

### Conflict 1 — Command-Line Resolution

**Participants:** Students A and B  
**Use the existing file:** `src/data_types/test_lists.py`

Students A and B must:

1. Create separate branches from the same starting commit.
2. Independently modify overlapping lines in an existing test function.
3. Commit their changes separately.
4. Integrate the first branch.
5. Attempt to integrate the second branch to produce a Git merge conflict.
6. Resolve the conflict using the Git command-line interface (CLI).
7. Ensure that the final version preserves the intended changes from both students.
8. Commit the resolved version.

> For example, the two students may modify the same list example by adding different operations or assertions. The final resolution should preserve both intended improvements rather than simply discarding one student's work.

### Conflict 2 — GUI Resolution

**Participants:** Students C and A
**Use the existing file:** `src/control_flow/test_if.py`

Students C and A must:

1. Create separate branches from the same starting commit.
2. Independently modify overlapping lines in an existing conditional statement example.
3. Commit their changes separately.
4. Integrate the first branch.
5. Attempt to integrate the second branch to produce another merge conflict.
6. Resolve the conflict using the graphical merge editor in **VS Code or PyCharm**.
7. Preserve the intended functionality of both modifications.
8. Commit the resolved version.

### Required Evidence for Both Conflicts

Your team must:

- Demonstrate the conflicting changes before resolution.
- Capture the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
- Explain why Git could not automatically merge the changes.
- Document the resolution process.
- Show the final resolved code.
- Demonstrate that the modified tests execute successfully.

> **Important:** The team must actually create and resolve both conflicts. Screenshots or explanations of hypothetical conflicts are insufficient. The two conflicts must be distinct, and one must be resolved using the CLI while the other must be resolved using a GUI merge editor.

---

## 7. Part D — Final Verification and SCM Report (15%)

After all contributions and conflict resolutions have been integrated, the team must perform a final verification.

### Step 1 — Verify the Integrated Project

The team must:

1. Confirm that all four students' improvements are present in the original repository.
2. Verify that the two conflict resolutions did not remove any required functionality.
3. Confirm that the final version is available on the `main` branch of Student A's repository.

### Step 2 — Examine the Git History

Use the following command:

```bash
git log --oneline --decorate --graph --all
```

Examine the resulting commit history and identify the major contributions and merges.

### Step 3 — Create a Release Tag

Create a Git release tag named:

```
v1.0.0
```

Push the tag to the original GitHub repository.

### Step 4 — Prepare the SCM Report

Prepare a short report documenting the team's practical work, GitHub collaboration, conflict resolution, and final verification.

---

## 8. Submission Requirements

Each team must submit one PDF report to Moodle. The report must contain the following sections.

### C. Practical Evidence — Screenshots

A comprehensive set of screenshots demonstrating the actual execution of the assignment is mandatory. Screenshots must clearly demonstrate:

- [x] Creation of the original repository and its initial commits.
- [ ] The three GitHub forks and local clones.
-  [ ] `origin` and `upstream` remote configurations.
-  [ ] Successful synchronization of the forks.
-  [ ] Individual development branches.
-  [ ] At least two meaningful commits per student.
-  [ ] The four pull requests.
-  [ ] Code review comments and successful merges.
-  [ ] Both merge conflicts before and after resolution.
-  [ ] Conflict markers and the CLI resolution process.
-  [ ] The GUI merge editor and the second conflict resolution.
-  [ ] Successful execution of the modified Python tests.
-  [ ] The final Git history and release tag.

Screenshots must be readable, appropriately labeled, and accompanied by brief explanations.

### D. Conflict Resolution Discussion

Briefly explain:

1. What caused each merge conflict.
2. Why Git could not merge the changes automatically.
3. How the conflict was resolved.
4. How the team verified that the required functionality was preserved.

### E. Final Results

Summarize:

- The improvements made to the existing Python project.
- The testing results.
- Each student's contributions.
- Any significant challenges encountered during the Git/GitHub workflow.

---

## 9. Important Submission and Grading Instructions

### Moodle Submission

Submit the complete **PDF** report.