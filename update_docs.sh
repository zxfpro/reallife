rm -rf docs/
project=实践级别
github_repo=$(basename "$(pwd)")
cp -r ../obsidian/工作/工程系统级设计/$project/$github_repo/docs ~/GitHub/$github_repo/
cp ../obsidian/工作/工程系统级设计/$project/$github_repo/README.md ~/GitHub/$github_repo/
