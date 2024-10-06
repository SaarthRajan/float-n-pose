
def percent_to_score(percent) :
    high_percent = 97
    low_percent = 70
    high_score = 100
    low_score = 0
    
    if percent < low_percent :
        return low_score
    if percent > high_percent :
        return high_score
    
    score = low_score + (percent - low_percent)*(high_score - low_score)/(high_percent - low_percent)

    return round(score)