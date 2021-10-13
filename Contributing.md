# 🚀CONTRIBUTING GUIDLINES

Developers are welcome to contribute to this project
<br>Initial Step: Comment under the issue you want to work on and get the issue assigned to yourself.
<br>
# Steps for contributing 
## Fork this repository
Fork the repo by clicking on the Fork option<br>
## Clone the repository 
Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the _copy to clipboard_ icon.

Open a terminal and run the following git command:

```
git clone "url you just copied"
```

where "url you just copied" (without the quotation marks) is the url to this repository (your fork of this project). See the previous steps to obtain the url.

For example:

```
git clone https://github.com/YOUR-USERNAME/DesktopAssistant.git 
```

where `YOUR-USERNAME` is your GitHub username. Here you're copying the contents of the first-contributions repository on GitHub to your computer.

## Create a branch

Change to the repository directory on your computer (if you are not already there):

```
Run `cd DesktopAssitant`
```

Now create a branch using the `git branch` command:

```
Run `git branch <new_branch_name>`
```
Here, you can try and keep branch name as the number of issue you are trying to solve i.e ```issue_1``` <br>

Checkout to the new branch so you can push onto the new branch of the forked repository 

```
git checkout <new_branch_name>
```


## Make necessary changes and commit those changes

If you go to the project directory and execute the command `git status`, you'll see there are changes.

Add those changes to the branch you just created using the `git add` command:

```
git add .
```

Now commit those changes using the `git commit` command:

```
git commit -m "anything that expresses whatever changes you have made"
```

## Push changes to GitHub

Push your changes using the command `git push`:

```
git push origin <new_branch_name>
```

replacing `<new_branch_name>` with the name of the branch you created earlier.

## Submit your changes for review

Now you are ready to make a pull request. Go to the forked repo on Github under your profile and a click on the ```Compare & pull request```button. You will be taken to a page where you can create a pull request.
When creating a PR, add the linked issue in the description. For example : "Closes #1" if the issue you have resolved is issue #1
<br>
