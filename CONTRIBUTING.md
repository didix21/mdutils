# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct, please follow it in all your interactions with the project.

## Pull Request Process

1. Squash all your commits before opening the PR.
2. Ensure you're pull-request contains a unique commit referencing the issue that solves in the commit message. Example: `Implement new features #7`.
3. You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

## Deployment

1. The versioning scheme we use is [SemVer](http://semver.org/).
2. Increase the version number in the `mdutils/doc/source/config.py` file.
3. Increase the version number in the `mdutils/setup.py` file.
3. Increase the version number in the `mdutils/pyproject.toml` file.
4. Increase the version number in the `.github_changelog_generator` file.
5. Run `github_changelog_generator -u didix21 -p mdutils`.
6. Run `python -m build`.
7. Upload package to pypi: `twine upload dist/*`.
