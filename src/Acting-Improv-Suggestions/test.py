from git import Repo

PATH_OF_GIT_REPO = r"C:/Users/Rent\Documents/GitHub/Python-Acting-Improv-Suggestions/.git"  # make sure .git folder is properly configured
COMMIT_MESSAGE = "comment from python script"


def git_push():
    file1 = open("testOutput.py", "a")
    file1.write("Test")
    file1.close()
    # repo = Repo(PATH_OF_GIT_REPO)
    # repo.git.add(update=True)
    # repo.index.commit(COMMIT_MESSAGE)
    # origin = repo.remote(name="origin")
    # origin.push()


git_push()
