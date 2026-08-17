# Library Management System — Team Project

A small team project used to demonstrate **version control with Git and GitHub**:
a shared repository, one branch per module, pull requests with code review,
and merge conflict resolution.

---

## Team & Module Ownership

Each member owns one module and develops it on a dedicated branch.

| Module | Branch | Owner | Status |
|---|---|---|---|
| `core` | `main` | Team | Merged |
| `auth` | `feature/auth-module` | Member 1 | Merged |
| `catalog` | `feature/catalog-module` | Member 2 | In review |

---

## Repository Structure

```
team-project-library-management/
├── app.py              # entry point; MODULES registry activates each module
├── modules/
│   └── core.py         # shared helpers
└── README.md           # this file - the team workflow
```

A module is activated by adding its name to the `MODULES` list in `app.py`.
Because every member edits that same list, it is the file where merge
conflicts are most likely — which is exactly what this experiment demonstrates.

---

## Branching Strategy

```
main                 protected; always in a working state
 │
 ├── feature/auth-module        member 1
 ├── feature/catalog-module     member 2
 └── feature/borrowing-module   member 3
```

Rules the team follows:

1. **Never commit directly to `main`.** All work arrives through a pull request.
2. **One branch per module**, named `feature/<module>-module`.
3. **Pull `main` before merging** so conflicts surface locally, not on GitHub.
4. **At least one reviewer approves** before a pull request is merged.
5. **Delete the branch after merge** to keep the branch list readable.

---

## Workflow

### 1. Clone the shared repository

```bash
git clone https://github.com/tharuncoder676/team-project-library-management.git
cd team-project-library-management
```

### 2. Create your module branch

```bash
git checkout -b feature/auth-module
```

### 3. Build the module and commit

```bash
git add modules/auth.py app.py README.md
git commit -m "Add authentication module"
```

### 4. Push and open a pull request

```bash
git push -u origin feature/auth-module
gh pr create --base main --head feature/auth-module
```

### 5. Code review

A teammate reviews the pull request on GitHub and either requests changes or
approves it. Review comments are left inline on the diff.

### 6. Sync with `main` and resolve conflicts

Once someone else's pull request is merged first, `main` has moved on. Before
merging, bring those changes into your branch:

```bash
git checkout main
git pull origin main
git checkout feature/catalog-module
git merge main
```

If Git reports `CONFLICT`, edit the affected files, remove the conflict
markers, then:

```bash
git add <resolved files>
git commit
git push origin feature/catalog-module
```

### 7. Merge the pull request

After approval and a clean merge, the pull request is merged into `main`.

---

## Conflict Log

Conflicts encountered during this project and how they were settled.

| # | Files | Cause | Resolution |
|---|---|---|---|
| 1 | `app.py`, `README.md` | PR #1 (auth) merged first. `feature/catalog-module` was cut from the same baseline, so both branches added a new entry at the **same position** in the `MODULES` list and the **same row** in the ownership table. | Kept **both** entries. The two modules are independent additions that only collided by line position, so nothing had to be discarded — `auth` and `catalog` were both listed, in registration order. |

---

## Running the Project

```bash
python app.py
```
