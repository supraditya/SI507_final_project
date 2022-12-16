# **Welcome to the Repository Visualizer!**
**Please note that the attempt-2 branch is the latest branch and is intended to the final submission, and not the 'master' branch. Thank you!**

## SETUP (with preexisting .env file)
1. Clone the repository
2. copy the .env file into the root directory of the repo
3. Install the following python libraries:
	- requests
	- dotenv
	- flask
	- flask_dance
4. Run app.py
5. Open your browser, go to http://127.0.0.1:5000
6. You should be redirected to a GitHub Login window. Login with your GitHub credentials.
**Note: This application requests access to all public and private repositories with the users GitHub account.**
7. Enter the name of the repository that you wish to visualize.
**Note: This field is case-sensitive**
8. Click on the 'Calibrate' button before moving onto the graph.
9. Hover on the graph's commits to render the edges, and view the commit information!


## Data Structures Used
### Directed Graph
- Repository used for example:
https://github.com/supradtya/test-repo3

[IMAGE from git graph]

`branch_graph={'fdfea8ae454de76f6ae17bc8c882c4833f67681e': [['branch-2', 'branch-3', 'branch-4', 'main', 'something']], 'd8fdb3b1a0300958242d84052dcd256979aa4d61': [['branch-2', 'branch-3', 'branch-4', 'main', 'something']], '6e6f6ee948be9b4b9e60d6028fd3eec5e89447c7': [['branch-2', 'branch-3']], '527b8e45dc34c7678a0a374888907aaeb2e6c2a8': [['branch-4', 'main', 'something']], '8b9bcdcc77b648cffa09cd7d24d1d489b6794902': [['something']], '95d89962953ee8f3806a764587a39b7470428406': [['main']]}`

`message_graph={'fdfea8ae454de76f6ae17bc8c882c4833f67681e': ['Create README.md'], 'd8fdb3b1a0300958242d84052dcd256979aa4d61': ['Update README.md'], '6e6f6ee948be9b4b9e60d6028fd3eec5e89447c7': ['Update README.md'], '527b8e45dc34c7678a0a374888907aaeb2e6c2a8': ['Update README.md'], '8b9bcdcc77b648cffa09cd7d24d1d489b6794902': ['Update README.md'], '95d89962953ee8f3806a764587a39b7470428406': ['Update README.md']}
`

`children_graph={'fdfea8ae454de76f6ae17bc8c882c4833f67681e': ['d8fdb3b1a0300958242d84052dcd256979aa4d61'], 'd8fdb3b1a0300958242d84052dcd256979aa4d61': ['6e6f6ee948be9b4b9e60d6028fd3eec5e89447c7', '527b8e45dc34c7678a0a374888907aaeb2e6c2a8'], '6e6f6ee948be9b4b9e60d6028fd3eec5e89447c7': [], '527b8e45dc34c7678a0a374888907aaeb2e6c2a8': ['95d89962953ee8f3806a764587a39b7470428406', '8b9bcdcc77b648cffa09cd7d24d1d489b6794902'], '8b9bcdcc77b648cffa09cd7d24d1d489b6794902': [], '95d89962953ee8f3806a764587a39b7470428406': []}`

[Screenshots for data structures within application]

## Features
- Ability to visualize all your repositories, both public and private!
- Allows for easy traversal and viewing of your Github commit history.
- Dynamic edge rendering for even the most complicated repository structures!
- Hover over commit nodes to view individual commit data.





