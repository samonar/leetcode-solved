import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    cols, row= players.shape
    return ([cols,row])
    # return [players.shape[0], players.shape[1]]