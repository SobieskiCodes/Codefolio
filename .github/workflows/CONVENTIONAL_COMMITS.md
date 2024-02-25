
# Conventional Commits Quick Reference Guide

Conventional commits are a specification for adding human and machine-readable meaning to commit messages. This document serves as a quick reference guide for creating conventional commits and includes examples specific to the `pre_release` and `main`/`develop` branch workflow.

## Commit Structure

Each commit message consists of a header, a body, and a footer. The header has a special format that includes a type, an optional scope, and a subject:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

## Commit Types

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `build`: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
- `ci`: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
- `chore`: Other changes that don't modify `src` or `test` files
- `revert`: Reverts a previous commit

## Pre-release Commits

When working in the `pre_release` branch and you want to denote a commit that should be part of a pre-release version:

```
<type>(<scope>): <subject> (pre-release)
```

Example:

- `feat(auth): add OAuth2 support (pre-release)`
- `fix(server): correct memory leak in image processing (pre-release)`

## Standard Release Commits

When working in the `main` or `develop` branches and you are ready for a standard release version:

```
<type>(<scope>): <subject>
```

Example:

- `feat(auth): add OAuth2 support`
- `fix(server): correct memory leak in image processing`

## Examples

Here are some examples of conventional commit messages:

- `feat(blog): add comment section to posts`
  - Indicates a new feature for the blog section, specifically a new comment section for posts.

- `fix(auth): prevent security breach when user logs out`
  - Fixes a bug in the auth module that could lead to a security breach.

- `docs(readme): update installation instructions`
  - Documentation update for the project's README file.

- `perf(api): optimize query performance by adding indexes`
  - Performance improvements in the API by adding database indexes.

- `style(formatter): run prettier on all js files`
  - Code style update by running prettier on all JavaScript files.

- `refactor(core): simplify async flow with async/await`
  - Refactoring the core module to simplify the asynchronous flow.

- `test(auth): add tests for password reset flow`
  - Adding missing tests for the password reset flow in the auth module.

- `build(deps): update axios to v0.21.1`
  - Build-related update for bumping the axios dependency to a specific version.

- `ci(circleci): update config file for improved caching`
  - Continuous integration change to improve caching in CircleCI configuration.

Remember to keep your commit messages clear and descriptive, and to group changes logically for readability and easier automation with tools like Release Please.
