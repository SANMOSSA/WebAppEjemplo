import subprocess
from datetime import datetime, timedelta

def obtener_commits(repo_path):
    commandDate = "git log --pretty=%ad"
    comandName = "git log --pretty=%s"
    resultDate = subprocess.run(commandDate, shell=True, capture_output=True, text=True).stdout.strip().split('\n')
    resultName = subprocess.run(comandName, shell=True, capture_output=True, text=True).stdout.strip().split('\n')
    resultName.reverse()
    UltimoPago = resultName.index("Pago")
    resultName = resultName[UltimoPago:]
    resultDate.reverse()

    return [commit.split('|') for commit in commits]

def main(repo_path, commit_referencia):
    commits = obtener_commits(repo_path)
    print(commits)
    
if __name__ == "__main__":
    repo_path = __file__.replace("Tester.py", "")
    commit_referencia = "hash_del_commit_Pago"
    main(repo_path, commit_referencia)
