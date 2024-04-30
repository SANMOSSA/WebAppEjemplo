import subprocess
from datetime import datetime, timedelta

def obtener_commits(repo_path):
    commandDate = "git log --pretty=%ad"
    comandName = "git log --pretty=%s"
    resultDate = subprocess.run(commandDate, shell=True, capture_output=True, text=True).stdout.strip().split('\n')
    resultName = subprocess.run(comandName, shell=True, capture_output=True, text=True).stdout.strip().split('\n')
    UltimoPago = resultName.index("Pago")
    resultName = resultName[:UltimoPago]
    resultDate = resultDate[:UltimoPago]
    resultDate.reverse()
    resultName.reverse()
    Tiempos = [[]]
    for i, Name, Date in zip(range(len(resultName)), resultName, resultDate):
        print(i, Name, Date)
        if Name.lower() in ["inicio", "fin"]:
            if Name.lower() == "inicio":
                Tiempos[-1].append(Date)
            else:
                Tiempos[-1].append(Date)
                Tiempos.append([])
        else:
            resultDate.pop(i)
            resultName.pop(i)
    
    if Tiempos[-1] == []:
        Tiempos.pop(-1)
        
    return Tiempos

def main(repo_path, commit_referencia):
    commits = obtener_commits(repo_path)
    print(commits)
    
if __name__ == "__main__":
    repo_path = __file__.replace("Tester.py", "")
    commit_referencia = "hash_del_commit_Pago"
    main(repo_path, commit_referencia)
