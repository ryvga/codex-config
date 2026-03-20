# Git And GitHub Workflow

## Local Commit Flow

```bash
cd ~/codex-config
git status --short
git add .
git commit -m "chore: scaffold codex-config repo and portable sync tooling"
git add .
git commit -m "feat: add global codex config, registry, and production agent cluster"
git add .
git commit -m "docs: add install, override, contribution, and source documentation"
```

## Remote Creation With `gh`

`gh` must be authenticated first:

```bash
gh auth login
```

Then create and push the private repo:

```bash
cd ~/codex-config
gh repo create codex-config --private --source=. --remote=origin --push
```

For a public template instead:

```bash
gh repo create codex-config --public --source=. --remote=origin --push
```

## Current Local Constraint

At implementation time on this machine, `gh auth status` reported no logged-in GitHub host, so the repository was prepared locally and committed, but remote creation and push were not attempted.

