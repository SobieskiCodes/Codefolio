## https://github.com/SobieskiCodes/Codefolio/tree/

When using the Release Please Action for automated versioning and you want to add a new feature while following the Conventional Commits specification, the typical workflow would be as follows:

1. **Start from the `pre_release` Branch**:
   Make sure the `pre_release` branch is up to date with the latest changes.

2. **Create a New Feature Branch**:
   From `pre_release`, create a new branch for your feature, let's call it `new_feature`.

   ```bash
   git checkout pre_release
   git pull
   git checkout -b new_feature
   ```

3. **Develop Your Feature**:
   Make changes for the new feature in the `new_feature` branch. Commit these changes using the Conventional Commits format, for example:

   ```bash
   git commit -m "feat(new-component): add new component to the app"
   ```

4. **Make Additional Commits**:
   If you make a bug fix or documentation update, commit these with appropriate messages, such as:

   ```bash
   git commit -m "fix(new-component): fix alignment issue"
   git commit -m "docs(new-component): add usage documentation"
   ```

5. **Push the Feature Branch**:
   Push the `new_feature` branch to the remote repository.

   ```bash
   git push -u origin new_feature
   ```

6. **Open a Pull Request (PR)**:
   Go to the GitHub repository and open a pull request from your `new_feature` branch to the `pre_release` branch. The PR should have a clear title summarizing the feature, and the description can contain details about the feature, fix, and documentation you added.

7. **Merge the Pull Request**:
   Once the PR is reviewed and approved, you can merge it into the `pre_release` branch. With the Release Please Action configured, it should recognize the Conventional Commits in the `new_feature` branch and propose a new release PR with the appropriate version bump and generated changelog.

8. **Release PR**:
   The Release Please Action will create a release PR against your `pre_release` branch. This PR will contain the version bump and changelog updates. Once you merge this PR, the action will tag the commit with the new version number.

By following these steps, you're making sure that each commit in your `new_feature` branch is scoped and described correctly according to the type of change it introduces. This practice allows the Release Please Action to accurately generate release notes and version numbers based on the changes included when these commits are merged back into your `pre_release` branch.